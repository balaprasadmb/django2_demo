from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils import timezone

from restra.models import RestaurantReview, Restaurant, Dish
from restra.forms import RestaurantForm, DishForm

class RestaurantIndexView(generic.ListView):
    template_name = 'restra/restaurant_list.html'
    context_object_name = 'latest_restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5]

class RestaurantDetail(generic.DetailView):
    model = Restaurant
    template_name = 'restra/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

class RestaurantCreate(generic.CreateView):
    model = Restaurant
    template_name = 'restra/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class RestaurantUpdate(generic.UpdateView):
    model = Restaurant
    template_name = 'restra/form.html'
    form_class = RestaurantForm

class DishCreate(generic.CreateView):
    model = Dish
    template_name = 'restra/form.html'
    form_class = DishForm
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)

class DishUpdate(generic.UpdateView):
    model = Dish
    template_name = 'restra/form.html'
    form_class = DishForm

class DishDetail(generic.DetailView):
    model = Dish
    template_name = 'restra/dish_detail.html'

def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('restra:restaurant_detail', args=(restaurant.id,)))
