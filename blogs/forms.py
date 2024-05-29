from django import forms
from .models import Subscriber, Newsletter, Post

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'pl-2 w-full text-base font-medium leading-none text-gray-600 placeholder-gray-600 focus:outline-none bg-gray-100',
                'placeholder':'Enter your email address here',
                'id':'id_email'
            })
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'body']

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content','slug', 'image']
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class':'pl-2 w-full text-base font-medium leading-none text-gray-600 placeholder-gray-600 focus:outline-none bg-gray-100',
#                 'placeholder':'Enter the title of your post here',
#                 'id':'id_title'
#             }),
#             'content': forms.Textarea(attrs={
#                 'class':'pl-2 w-full text-base font-medium leading-none text-gray-600 placeholder-gray-600 focus:outline-none bg-gray-100',
#                 'placeholder':'Enter the content of your post here',
#                 'id':'id_content'
#             })
#         }



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','slug', 'image']  # Include all the fields you want to include in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title bg-gray-100 border border-gray-300 p-2 mb-4 outline-none', 'spellcheck': 'false', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'description bg-gray-100 sec p-3 h-60 border mb-4 border-gray-300 outline-none', 'spellcheck': 'false', 'placeholder': 'Describe everything about this post here'}),
            'slug': forms.TextInput(attrs={'class': 'title bg-gray-100 border border-gray-300 p-2 mb-4 outline-none', 'spellcheck': 'false', 'placeholder': 'Slug'}),
            'image': forms.FileInput(attrs={'class':'block w-full mb-5 text-sm text-gray-900 border border-gray-300 cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400' ,'id':"default_size",'type':'file'}),
        }
    
 