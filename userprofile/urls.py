from django.urls import path
from django.contrib.auth.views import login, logout

from .views import signup
from userprofile.views import activate
urlpatterns = [
    path('login/', login,{'template_name': 'login.html'}, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout,{'next_page': '/'}, name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
