from django.shortcuts import render
# from django.http import HttpResponse
from appTwo.models import Site
from appTwo.forms import NewSiteForm
from appTwo.models import Document
from appTwo.forms import DocumentForm
# Create your views here.

def index(request):
    site_list = Site.objects.order_by('site_name')
    site_dict = {'sites': site_list}
    return render(request,'appTwo/index.html', context = site_dict)

def site(request):

    form = NewSiteForm()

    if request.method == "POST":
        form = NewSiteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'appTwo/site.html',{'form':form})


def model_form_upload(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'appTwo/upload.html', {
        'form': form
    })


def sales_estimate(request):
    return render(request,'appTwo/sales_estimate.html')
