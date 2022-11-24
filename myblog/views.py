import imp
from django.shortcuts import get_object_or_404, render
from myblog.models import Post, Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from django.core.mail import send_mail
from myblog.forms import EmailSendForm, CommentForm
from django.conf import settings
import socket

# Create your views here.
def post_list_view(request):
    post_list = Post.objects.all()
    post = Post.objects.all()
    paginator=Paginator(post_list,1)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)

    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
        
    return render(request,'post_list.html',{'post_list':post_list,'post':post})

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publish',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active = True)
    csubmit = False
    if request.method== 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.post = post
            new.save()
            csubmit=True
    else:
        form = CommentForm()
    return render(request,'post_detail.html',{'post': post,'form':form,'comments':comments, 'csubmit':csubmit})




def mail_send_view(request,id):
    post = get_object_or_404(Post, id = id, status='publish')
    sent=False
    if request.method =='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}({})recommand you to read "{}"'.format(post_url,cd['name'],cd['email'],post.title)
            message='Read Post at: \n{}\n{}\'Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'swappathak1997@gmail.com',[cd['to']])
            sent = True
    else:
        form=EmailSendForm()
    return render(request, 'share.html',{'post':post,'form':form,'sent':sent})




def listview(request):
    post = Post.objects.all()   
    return render(request,'sidebar.html',{'post' : post})