from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator #Paginator 페이지 나누게 해 줄수 있는거

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all() #모든 objects all_jss에 첨부
    return render(request, 'index.html',{'all_jss':all_jss})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user) #filter: 특정 object만 filtering해서 가져옴 (원하는 필드,조건)
    return render(request, 'index.html',{'all_jss':my_jss})

@login_required(login_url='/login/') #login_required 기능 적용
def create(request):
    if request.method == "POST": # method 가 POST 방식이면
        filled_form = JssForm(request.POST) #POST 방식으로 들어온 데이터가 자소서 폼에 적용
        if filled_form.is_valid(): #is_valid: 내장된 함수 모델폼에서 함수, 유효성 검증
            temp_form = filled_form.save(commit=False) # 임시 form으로 유효성 검증 후 저장,commit=False :저장 지연 
            temp_form.author = request.user
            temp_form.save() #유효성 검증 통과하면 저장
            return redirect('index')
    jss_form = JssForm()
    return render(request,'create.html',{'jss_form':jss_form})

@login_required(login_url='/login/')
def detail(request, jss_id): #함수 옆 인자로써 jss_id 받기
 #오류 시   
    #try:
    #    my_jss = Jasoseol.objects.get(pk=jss_id) #pk=jss_id(index.html있움) 값 정하기
    #except:
    #    raise Http404
    my_jss = get_object_or_404 (Jasoseol,pk=jss_id) 
    comment_form = CommentForm()

    return render(request,'detail.html', {'my_jss':my_jss,'comment_form':comment_form})

def delete(request, jss_id):
    
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author: #object와 author 동일 시 my_jss삭제
        my_jss.delete() #delete 함수로 단순 삭제
        return redirect('index')

    raise PermissionDenied #타인이 삭제하려 할 때 오류 표시

#모델 폼 이용한 update
def update(request, jss_id):
    jss_form=JssForm()
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss) #instance로 추가되는 object rendering
    if request.method == "POST": #확인 버튼으로 POST 방식 요청
        updated_form = JssForm(request.POST, instance=my_jss) #수정시, 원래 있던 모델폼에 씌우기
        if updated_form.is_valid(): # updated form 유효성 검증
            updated_form.save()
            return redirect('index')
    return render(request,'create.html',{'jss_form':jss_form}) #create.html jss form 활용

def create_comment(request,jss_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id) #detail.html에 있는 자소서에 넣어줘야함
        temp_form.save()
        return redirect('detail',jss_id) 

def delete_comment(request,jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail',jss_id)

    else:
        raise PermissionDenied

def index(request):
    all_jss = Jasoseol.objects.all() #자소서 전체목록 불러오기
    paginator = Paginator(all_jss, 5) #한페이지에 자소설 5개만 보임
    page = request.GET.get('page') #요청받은 페이지 알아내기
    jss_page = paginator.get_page(page) #자른 페이지 중에서 요청받은ㄴ 페이지에 들어가는 자소서 목록들
    return render(request,'index.html',{'all_jss' : jss_page}) #모든 페이지 한 페이지로 보이게