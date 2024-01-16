from django.urls import path
from .views import index, sign_up, sign_in, sign_out, ProfileListView, ProfileDetailView

urlpatterns = [
    path('', index, name="home"),
    path('login/', sign_in, name="login"),
    path('logout', sign_out, name="logout"),
    path('register/', sign_up, name="register"),
    path('profile_list/', ProfileListView.as_view(), name="list"),
    path('<int:pk>/profile/', ProfileDetailView.as_view(), name="profile")
]


