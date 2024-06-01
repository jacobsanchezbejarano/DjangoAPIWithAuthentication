from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('secret', views.secret),
    path('manager-view', views.manager_view),
    path('api-token-auth', obtain_auth_token),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check),
    path('me', views.me),
    path('groups/manager/users', views.managers),
]
