from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm): #모델 폼 사용 

    class Meta:
        model = Jasoseol 
        fields = ('title','content',) #모델 안에서 타이틀, 컨텐츠 폼 사용

    def __init__(self, *args, **kwargs): #init 이용해서 커스텀
        super().__init__(*args,**kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder':'제목',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'jss_content_form',
        })

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)