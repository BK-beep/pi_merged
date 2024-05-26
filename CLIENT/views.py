from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import  UserRegisterForm
from django.contrib import messages
from .models import Conversation, Message
from .serene import Serene
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm


#import application blogs views
from blogs.views import *
from django.contrib.auth import logout

# instantiate the chatbot
chatbot = Serene()


def client_logout(request):
    logout(request)
    return redirect('client-login')
# Create your views here.
def client_index(request):
    return render(request, "index.html")



@csrf_protect
def client_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('client-index')
        else :
            print(form.errors)
            messages.error(request, f'Account not created! Please try again.')
            return redirect('client-signup')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/signup.html', {'form': form})

def client_login(request):
    if request.method == 'POST':
        print('login')
        form = UserLoginForm(request.POST)
        print('login')
        if form.is_valid():
            print('form is valid')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                print('created succ')
                return redirect('client-chat')  # Redirect to home or any other desired page
            else:
                # Authentication failed
                print('user authentication failed')
                messages.error(request, 'Invalid email or password.')
        else:
            print('form not valid')
            print(form.errors)  # Print form errors to identify validation issues
    else:
        print('not login')
        form = UserLoginForm()

    return render(request, 'auth/login.html', {'form': form})

@login_required
def client_chat(request):
    if request.method == 'POST':
        Conversation.objects.create(
            user=request.user ,
            name = request.POST.get('name')
            )
        return redirect('client-chat')
    conversations = Conversation.objects.filter(user=request.user)
    
    return render(request , "app/client_chat.html", {'conversations': conversations})

# Chat view
@login_required
def client_send_message(request):
    conversation = Conversation.objects.get(id=request.POST.get('conversation_id'))
    Message.objects.create(
        content = request.POST.get('content'),
        conversation = conversation
    )
    predict = chatbot.make_prediction(request.POST.get('content'))
    message = Message.objects.create(
        content = predict,
        conversation = conversation
    )
    data = serializers.serialize('json', [message,])
    return JsonResponse(data, safe=False)

def client_get_message(request):
    conversation_id = request.GET.get('conversation_id')
    conversation = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    data = serializers.serialize('json', messages)
    return JsonResponse(data, safe=False)

@login_required
def client_delete_conversation(request ,pk):
    conversation = Conversation.objects.get(id=pk)
    conversation.delete()
    return redirect('client-chat')

# Error 404
def error_404(request, exception):
    return render(request,'error/404.html')

# Error 500
def error_500(request):
    return render(request,'error/500.html')