from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

def home(request):
    User = get_user_model()
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'home.html', context)