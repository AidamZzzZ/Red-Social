from django.urls import path
from .views import index, sign_up, sign_in, sign_out, ProfileListView, follow, ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('', index, name="home"),
    path('login/', sign_in, name="login"),
    path('logout', sign_out, name="logout"),
    path('register/', sign_up, name="register"),
    path('<int:pk>/profile/', follow, name="profile"),
    path('profile_list/', ProfileListView.as_view(), name="list"),
    path("<int:pk>profile/update", ProfileUpdateView.as_view(), name="update"),
    path('<int:pk>/principal/profile', ProfileDetailView.as_view(), name="principal"),
]


