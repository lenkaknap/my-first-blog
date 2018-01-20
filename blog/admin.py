from django.contrib import admin
from .models import Post # dot means the same directory where I am in

admin.site.register(Post)