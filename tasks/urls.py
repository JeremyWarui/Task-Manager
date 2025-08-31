from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_list, name="task_list"),
    path("<int:pk>/", views.task_detail, name="task_detail"),
    path("new/", views.task_create, name="task_create"),
    path("<int:pk>/edit", views.task_edit, name="task_edit"),
    path("<int:pk>/delete", views.task_delete, name="task_delete"),
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]