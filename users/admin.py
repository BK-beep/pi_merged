from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('first_name', 'email')
    list_filter = ('first_name', 'email')
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()
    
    # # Customizing the fieldsets without duplicating 'email'
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # bio = models.CharField(max_length=250, blank=True, null=True)
    # Occupation = models.CharField(max_length=50, blank=True, null=True)
    # institution = models.CharField(max_length=50, blank=True, null=True)
    # email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=20)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # date_of_birth = models.DateField(auto_now=True, blank=True, null=True)
    # address = models.TextField()
    # image = models.ImageField(upload_to='./static/users', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='./static/users', blank=True, null=True)
    # friends = models.ManyToManyField('self', blank=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','thumbnail','image','bio','Occupation','institution','phone_number','gender','date_of_birth','address','friends')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    # Adding add_fieldsets for the add user form in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
