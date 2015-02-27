from datetime import datetime
from django.contrib.admin.forms import AdminAuthenticationForm
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponseForbidden
import django.contrib.auth
from trips.models import Post, Message
from .forms import PostForm
from django.shortcuts import render_to_response
from django.template import RequestContext


def hello_world(request):
    return render(request,
                  'hello_world.html',
                 {'current_time': datetime.now()})

def home(request):
    # get all the posts
    post_list = Post.objects.all()
    username = None
    if "username" in request.session:
        username = request.session['username']
    return render(request,
                  'home.html',
                 {'post_list': post_list,
                  'username': username})

def post_detail(request, id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.name = request.user
            obj.post =  Post.objects.get(id=id)
            obj.save()
    else:
        form = PostForm()
    post = Post.objects.get(id=id)
    msg_list = Message.objects.filter(post=post)
    print(msg_list)
    return render_to_response('post.html',
            {'post': post,
             'form': form,
             'msg_list': msg_list},
            context_instance=RequestContext(request))

def sign_up(request):
    return render(request,
                  'sign_up.html')

def sign_up_user(request):
    username = request.POST['username']
    familyname = request.POST['familyname']
    email = request.POST['email']
    pwd = request.POST['password']

def login(request):
    if request.method == 'GET':
        form = AdminAuthenticationForm(request)
        return render(request,
                      'login.html',
                     {'app_path': "/login",
                      'form':form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                django.contrib.auth.login(request, user)
                request.session['username'] = username
                # Redirect to a success page.
                index_path = "/"
                # from django.shortcuts import redirect
                # return redirect(index_path)
                return HttpResponseRedirect(index_path)
            else:
                # Return a 'disabled account' error message
                return HttpResponseForbidden()
        else:
            # Return an 'invalid login' error message.
            return HttpResponseForbidden()

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    index_path = "/"
    return HttpResponseRedirect(index_path)
