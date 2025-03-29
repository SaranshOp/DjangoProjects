from django.shortcuts import render

from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, 'tweet/index.html')

def tweet_list(request):
    tweets  =  Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/tweet_list.html', {'tweets':tweets})

def tweet_create(request):
    # form = TweetForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES) # create a form instance and populate it with data from the request
        if form.is_valid(): # check if the form is valid, security measure, csrf validation, etc.
            tweet = form.save(commit=False) # commit= False means that we don't want to save the form to the database yet
            tweet.user = request.user 
            tweet.save()
            return redirect('tweet:tweet_list')
    
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet) # instance=tweet means that we want to edit the tweet object
        if form.is_valid():
            form.save()
            return redirect('tweet:tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet_form.html', {'form':form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet:tweet_list')
    

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweet/tweet_detail.html', {'tweet':tweet})

        
    
    