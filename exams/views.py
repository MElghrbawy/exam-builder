from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course


@login_required
def home(request):
    courses = Course.objects.filter(teacher_id=request.user.id)
    return render(request, 'home.html', {'courses': courses})