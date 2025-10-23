from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    path('', RedirectView.as_view(url='tasks/'), name='home'),
    path('tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
