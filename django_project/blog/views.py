from django.shortcuts import render,redirect
from .models import Post,Comment
# from django.http import 404
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    print([post.author for post in Post.objects.all()])
    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context=context)

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date_posted')
    template_name="blog/index.html"
    context_object_name = 'posts'
    # ordering = 

def about(request):
    return render(request,'blog/about.html')

class PostDetailView(DetailView):
    model = Post
    template_name='blog/post_detail.html'

@login_required
def post_detail_view(request,pk):
    data = Post.objects.get(id=pk)
    user = request.user
    print(user)
    print(pk)
    comments = Comment.objects.filter(blog = data)
    if request.method =="POST":
        print(request.POST.values)
        form = CommentForm(request.POST,instance=user)
        # print(form)
        if form.is_valid():
            comment = Comment(your_name= request.user,
            comment=form.cleaned_data['comment'],
            blog=data)
            comment.save()
            return redirect(f'/post/{pk}')
        else:
            print("fuck world")

    else:
        form = CommentForm()

    context = {
            'data':data,
            'form':form,
            'comments':comments.order_by('-date_posted'),
        }
    return render(request,'blog/post_detail_2.html',context)

class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment']

    def form_valid(self,form):
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form): # add author before the form is created..
        # form is valid only if ..

        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form): # add author before the form is created..
        # form is valid only if ..

        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    # template_name='blog/post_detail.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False
