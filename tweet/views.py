from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.forms import TweetPost
from tweet.models import Tweet
from twitteruser.models import TwitterUser
# from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html",{})

def tweetadd(request):
    if request.method == "POST":
        form = TweetPost(request.POST)
        if form.is_valid():
            tweetpost = form.cleaned_data
            twitteruser = TwitterUser.objects.get(id=request.user.id)
            Tweet.objects.create(
                tweet = tweetpost["tweet"],
                twitteruser = twitteruser
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = TweetPost()
    return render(request, "tweetpost.html" , {"form": form})


