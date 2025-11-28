from django.contrib import admin
from django.urls import path,include
from shortener.views import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/url/', include('shortener.urls')),
    path('<str:short_code>',RedirectView.as_view(),name='redirect')

]
