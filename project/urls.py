
from django.contrib import admin
from django.urls import path

from marketing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.send_campaign_emails)
]
