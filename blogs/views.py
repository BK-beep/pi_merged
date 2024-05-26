from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
from users.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import SubscriberForm, NewsletterForm,PostForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post

def profile(request):
    user=request.user
    posts = Post.objects.filter(author=user).order_by('-created_at')

    for post in posts:
        print(f"Post author is {post.author.first_name}")
    context={
        'user': user,
        'posts': posts
    }
    
    return render(request, 'profile.html',context)



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Get the currently logged in user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Post creation failed. Please try again.')
            return redirect('add_post')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def blog_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    context={
        'authenticated_user' : request.user,
        'posts': posts
    }
    for post in posts:
        if post.author == context['authenticated_user']:
            print("post author is authenticated user")
        post.image.name=post.image.name.replace('/static','/')
        print("image url--->"+post.image.name) 

    return render(request, 'blog.html', context)
@login_required

def blog_home(request):
    context={
        #get the currently auth user,
        'authenticated_user' : User.objects.get(first_name='khaoula'),
        }
    return render(request, '_base.html', context)


def blog_category(request, category):
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(categories=category)
    context={
        'category': category,
        'posts': posts
    }
    return render(request, 'category.html', context)

def blog_details(request,blog_id):
    post = Post.objects.get(id=blog_id)
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog_details.html', context)

def comments(request):
    return render(request, 'commentSection.html')

def add_comment(request, slug):
    if request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)
        content = request.POST.get('content')
        
        if content:
            # Create a new comment associated with the post
            new_comment = Comment.objects.create(
                post=post,
                content=content
            )
            print("New comment created:", new_comment.content)
            return redirect('blog_details', blog_id=post.id)  # Redirect to the post detail page
        else:
            # Handle invalid form submission (e.g., empty comment)
            return HttpResponse('Invalid comment data', status=400)
    else:
        # Handle non-POST requests (if any)
        return HttpResponse('Method Not Allowed', status=405)
    

def reply(request, comment_id):
    if request.method == 'POST':
        parent = get_object_or_404(Comment, id=comment_id)
        content = request.POST.get('content')
        
        if content:
            new_reply = Comment.objects.create(
                post=parent.post,
                content=content,
                author=None,
                parent_comment=parent
            )
            print("New reply created for comment:", parent.content)
            return redirect('blog_details', blog_id=parent.post.id)
        else:
            return HttpResponse('Invalid reply data', status=400)
    else:
        return HttpResponse('Method Not Allowed', status=405)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Thanks for subscribing!"
            body = "Welcome to our newsletter! You'll receive updates on our latest blog posts and more."
            html_content = render_to_string('newsletter_email.html', {'subject': subject, 'body': body})

            try:
                # Create the email
                email = EmailMultiAlternatives(
                    subject=subject,
                    body=body,  # Plain text content
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=['berkaouikhawla2002@gmail.com']  # Replace with the recipient's email address
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                print(f'Email send result: {email}')  # Debugging: print the result
                messages.success(request, 'Subscription successful! A confirmation email has been sent.')
            except Exception as e:
                print(f'Error sending email: {e}')  # Debugging: print any exceptions
                messages.error(request, 'Subscription successful, but there was an error sending the confirmation email.')
            return redirect('thank_you')
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})

def send_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            subscribers = Subscriber.objects.all()
            for subscriber in subscribers:
                send_mail(
                    newsletter.subject,
                    newsletter.body,
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email]
                )
            return redirect('newsletter_sent')
    else:
        form = NewsletterForm()
    return render(request, 'send_newsletter.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def newsletter_sent(request):
    return render(request, 'newsletter_sent.html')