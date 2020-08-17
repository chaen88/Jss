#데이터 형식, 어떤 식으로 담을지 세부사항 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model): #첫 글자 대문자, 첫 줄 import models 상속
    title = models.CharField(max_length=50) 
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) #auto_now=True: 자기소개서 업데이트 될 때 자기소개서 자동으로 관리
    author = models.ForeignKey(User,on_delete=models.CASCADE) #ForeignKey(연결해주고 싶은 모델,on_delete=models.CASCADE)
    #on_delete=models.CASCADE: ForeignKey로 연걸된 object 삭제 시, 연결된 자소서 object도 삭제
    # *null=True 빈 값도 허용 (작성자 없어도 괜찮다)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol,on_delete=models.CASCADE)
