from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm,PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseForbidden



def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def board_topics(request, board_id):

    board = get_object_or_404(Board,pk=board_id)
    topics = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
    
    return render(request,'topics.html',{'board':board, 'topics':topics})


@login_required
def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)

    if request.method == "POST":
        form = NewTopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()
            print(form.cleaned_data.get('pic'))

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                pic=form.cleaned_data.get('pic'),
                created_by=request.user,
                topic=topic
            )

            return redirect('board_topics', board_id=board.pk)
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})


@login_required
def topic_posts(request, board_id, topic_id):
    board = get_object_or_404(Board, pk=board_id)
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    topic.views += 1
    topic.save()

    posts = Post.objects.filter(topic=topic).order_by('-created_dt')
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Pass both request.POST and request.FILES to the form
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            form.save_m2m()  # Save the many-to-many relationships, such as the 'likes' field
            return redirect('topic_posts', board_id=board.pk, topic_id=topic.pk)
    else:
        form = PostForm()

    if request.method == "POST" and 'like_post_id' in request.POST:
        post_id = int(request.POST.get('like_post_id'))
        post = get_object_or_404(Post, pk=post_id)

        if request.user in post.likes.all():
            # User has already liked the post, remove the like
            post.likes.remove(request.user)
        else:
            # User has not liked the post, add the like
            post.likes.add(request.user)

    return render(request, 'topic_posts.html', {'topic': topic, 'form': form, 'posts' : posts})

    # return render(request,'topic_posts.html',{'topic':topic,'form':form})



@login_required
def delete_post(request, board_id, topic_id, post_id):
    board = get_object_or_404(Board, pk=board_id)
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    post = get_object_or_404(Post, pk=post_id)
    
    # Check if the user has the necessary permission to delete the post
    if request.user == post.created_by:
        post.delete()
        # Assuming `topic_post` is the URL name for the view displaying the topic and its posts
        return redirect('topic_posts', board_id=board.pk, topic_id=topic.pk)
    else:
        return HttpResponseForbidden('You do not have permission to delete this post.')


    


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model =Post
    fields = ('message', 'pic')
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


    def form_valid(self,form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_dt = timezone.now()
        post.save()

        return redirect('topic_posts', board_id = post.topic.board.pk, topic_id = post.topic.pk)