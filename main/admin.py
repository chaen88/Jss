from django.contrib import admin
from .models import Jasoseol, Comment
# Register your models here.

admin.site.register(Jasoseol) #admin 페이지에 자소설 모델 등록
admin.site.register(Comment)

