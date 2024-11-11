from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from datetime import datetime
#from django.http import Http404

from comments.forms import CommentForm
from .models import Comment

from django.core.paginator import Paginator
# Create your views here.

# def add(request):
    
#     if request.method == 'POST':
#         if request.POST.get('text') != '':
#             print('Adding')
#             comment = Comment()
#             comment.text = request.POST.get('text')
#             comment.save()
            
#         else: 
#             print('No data')
    
#     data = {'year': datetime.now().year,
#             'month': datetime.now().month,
#             'day': datetime.now().day,
#             'hour': datetime.now().hour,
#             'minute': datetime.now().minute,
#             'second': datetime.now().second,
#             'autor' : 'Ernesto Marquez'}
#     return render(request, 'comments/add.html', {'data': data})

def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save()
        return redirect('comments:index')
    else: 
        form = CommentForm()  
    return render(request, 'comments/add.html',{'form': form})

def index(request):
    comment = Comment.objects.all()
    paginator = Paginator(comment,2) 
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number) 
    return render(request, 'comments/index.html', {'comments': comments_page})


def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # try:
    #     comment = Comment.objects.get(pk=pk)
    # except Comment.DoesNotExist :
    #     raise Http404
        
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()
            return redirect('comments:index')
    else:      
        form = CommentForm(instance=comment)
    return render(request, 'comments/add.html', {'form': form})

def delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments:index')
        #return render(request, 'comments/index.html', {'comments': comment})