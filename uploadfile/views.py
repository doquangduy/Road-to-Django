from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from uploadfile.forms import DocumentForm
from uploadfile.models import Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'uploadFile/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploadFile/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploadFile/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'uploadFile/model_form_upload.html', {
        'form': form
    })
