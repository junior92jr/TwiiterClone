from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from twitterclone.models import Tweet
from twitterclone.forms import TweetForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
	tweet_list = Tweet.objects.order_by('-pub_date')
	context_dict = {'tweets': tweet_list}

	return render(request, 'twitterclone/index.html', context_dict)

@login_required
def add_tweet(request):
	if request.method == 'POST':
		form = TweetForm(request.POST)
		form.nickname = request.user

		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print form.errors 

	else: 
		form = TweetForm()

	return render(request, 'twitterclone/add_tweet.html', {'form': form})

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		#profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid(): #and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			#profile = profile_form.save(commit=False)
			#profile.user = user

			#profile.save()

			registered = True
		else:
			print user_form.errors#, profile_form.errors

	else:
		user_form = UserForm()
		#profile_form = UserProfileForm()

	return render(request, 'twitterclone/register.html',
		{'user_form': user_form,
		'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/twitterclone/')
			else:
				return HttpResponse("Your Twitter Account is disabled.")

		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'twitterclone/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/twitterclone/')