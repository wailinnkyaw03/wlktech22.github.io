from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def comment(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('comment.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

  
def add(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = request.POST['name']
  y = request.POST['email']
  z = request.POST['comment']
  if (x=="" or y=="" or z==""):
    messages.info(request, "All fields are required!")
    return HttpResponseRedirect(reverse('index'))
  else:
    member = Members(username =x, email=y, comment = z)
    member.save()
    messages.info(request, "Thank you so much for your feedbacks!")
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('comment'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  name = request.POST['name']
  email = request.POST['email']
  comment = request.POST['comment']
  member = Members.objects.get(id=id)
  member.username = name
  member.email = email
  member.comment = comment
  member.save()
  return HttpResponseRedirect(reverse('comment'))