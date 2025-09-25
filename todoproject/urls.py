from django.contrib import admin
from django.urls import path, include  # 👈 include যোগ করো

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # app urls include
]

