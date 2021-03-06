from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test

from .models import Document
from .forms import DocumentForm
import glob, os


def index(request):
    return render(request, 'blog/index.html',{})


@user_passes_test(lambda u: u.is_superuser)
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect(reverse('blog.views.list'))

    else:
        form = DocumentForm() 
    return render_to_response('blog/list.html',{ 'form': form},context_instance=RequestContext(request))


def photo(request):
    documents = Document.objects.all()
    return render_to_response('blog/photo.html',{'documents': documents})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')





