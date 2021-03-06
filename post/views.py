from django.shortcuts import render, redirect
from .models import *
from .forms import EditPost, AddPost
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    post = Post.objects.last()
    if request.method == "POST":
        form = AddPost(request.POST)
        user=request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = user
            post.save()
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # category = request.POST.get('category')
        # user = request.user
        # if content is not None:
        #     Post.objects.create(title=title, content=content, category=category, created_by=user)
            return redirect("/")
    else:
        form = AddPost()
    data={'posts':posts,
          'last_post':post,
          'form':form
          
    } 
    return render(request, 'post/home.html', data)
    
@login_required()
def new_post(request):
    
    if request.method =="POST":
        form = AddPost(request.POST)
        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.created_by=user
            post.save()
            return redirect("/")
    else:
        form=AddPost()
    data = {
        "form":form        
    } 
    return render(request, 'post/new_post.html', data)

def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    form = EditPost(instance=post)
    if request.method == "POST":
        form = EditPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detail", post.id)
        # user = request.user
        # content = request.POST.get('content')
        # post = Post.objects.update(content=content, created_by=user)

    data={
        'post':post,
        'form':form
    }
    return render(request, 'post/post_edit.html', data)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        comment = Comment.objects.create(created_by=user, comment=comment, post=Post.objects.get(id=post_id))
        return redirect('detail', post_id)
    comment = Comment.objects.filter(post=Post.objects.get(id=post_id), active=True)

    data={'post':post,
          "comment":comment
    }
    return render(request, 'post/post_detail.html', data)

def post_delete(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('/')
    data={
        'post':post
    }
    
    return render(request, "post/delete.html", data)