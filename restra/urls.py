from django.urls import path
from restra import views

app_name = 'restras'

urlpatterns = [

# List latest 5 restaurants: /myrestaurants/
    path('', views.RestaurantIndexView.as_view(), name='index'),
#     url('', 
#         ListView.as_view(
#             queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
#             context_object_name='latest_restaurant_list',
#             template_name='restra/restaurant_list.html'),
#         name='restaurant_list'),

# Restaurant details, ex.: /myrestaurants/restaurants/1/
    path('<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),
#     url(r'\^restaurants/(?P<pk>\d+)/\$',
#         RestaurantDetail.as_view(),
#         name='restaurant_detail'),

# Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    path('dishes/<int:pk>',views.DishDetail.as_view(), name='dish_detail'),
#     url(r'\^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/\$',
#         DetailView.as_view(
#             model=Dish,
#             template_name='restra/dish_detail.html'),
#         name='dish_detail'),

# Create a restaurant, /myrestaurants/restaurants/create/
    path('create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
#     url(r'\^restaurants/create/\$',
#         RestaurantCreate.as_view(),
#         name='restaurant_create'),

# Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    path('<int:pk>/edit/', views.RestaurantUpdate.as_view(), name='restaurant_edit'),
#     url(r'\^restaurants/(?P<pk>\d+)/edit/\$',
#         UpdateView.as_view(
#             model = Restaurant,
#             template_name = 'restra/form.html',
#             form_class = RestaurantForm),
#         name='restaurant_edit'),

# Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    path('<int:pk>/dishes/create/', views.DishCreate.as_view(), name='dish_create'),
#     url(r'\^restaurants/(?P<pk>\\d+)/dishes/create/\$',
#         DishCreate.as_view(),
#         name='dish_create'),

# Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    path('dishes/<int:pk>/edit', views.DishUpdate.as_view(), name='dish_edit'),
#     url(r'\^restaurants/(?P<pkr>\\d+)/dishes/(?P<pk>\\d+)/edit/\$',
#         UpdateView.as_view(
#             model = Dish,
#             template_name = 'restras/form.html',
#             form_class = DishForm),
#         name='dish_edit'),

# Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    path('<int:pk>/reviews/create/', views.review, name='review_create'),
#     url(r'\^restaurants/(?P<pk>\\d+)/reviews/create/\$',
#         review,
#         name='review_create'),
]
