from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('secret', views.secret),
    path('manager-view', views.manager_view),
    path('api-token-auth', obtain_auth_token),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check),
    path('api/token/', TokenObtainPairView.as_view(), name='token_ontain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(),
         name='token_blacklist'),
]
