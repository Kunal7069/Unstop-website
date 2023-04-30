from django.shortcuts import render
from .models import Mentor
from accounts.views import ShowProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mentors(request):
    mentors = Mentor.objects.all()
    id = request.GET.get('id')
    if id == '1':
        mentors = Mentor.objects.filter(mentor_type='technology')
    elif id == '2':
        mentors = Mentor.objects.filter(mentor_type='management')
    elif id == '3':
        mentors = Mentor.objects.all()
    else:
        mentors = Mentor.objects.all()

    # technology_mentors = Mentor.objects.filter(mentor_type='Technology').all()
    # management_mentors = Mentor.objects.filter(mentor_type='Management').all()
    context = {
        'mentors': mentors,
        # 'technology_mentors': technology_mentors,
        # 'management_mentors': management_mentors,

    }
    return render(request, 'mentors.html', context)