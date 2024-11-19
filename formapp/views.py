from django.shortcuts import render, redirect
from .forms import ContactModelForm, UploadFileModelForm
from .models import Contact, UploadFile
import os
# Create your views here.

def home_view(request):
  return render(request, "formapp/home.html")

def contact_view(request):
  if request.method == "POST":
    form = ContactModelForm(request.POST) # 将提交的数据绑定到表单
    if form.is_valid(): # 验证表单数据
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      Contact.objects.create(
        name = name,
        email = email,
        message = message,
      )
      print(f"Name: {name}, Email: {email}, Message: {message}")
      
      return redirect('success') # 显示成功页面
  else:
    form = ContactModelForm() # 创建一个空表单
  return render(request, 'formapp/contact.html', {"form": form})

def upload_view(request):
  if request.method == "POST":
    form = UploadFileModelForm(request.POST, request.FILES)
    if form.is_valid():
      uploaded_file = form.cleaned_data['file']
      message = request.POST.get('message')
      UploadFile.objects.create(
        file = uploaded_file,
        message = message,
      )
      return redirect('success')
  else:
    form = UploadFileModelForm()

  return render(request, 'formapp/upload.html', {"form": form})

def upload_success_view(request):
    files = UploadFile.objects.all()
    for file in files:
        # 提取文件名
        file.display_name = os.path.basename(file.file.name)

        extension = file.file.name.split('.')[-1].lower()
        if extension == "pdf":
            file.icon_class = "fas fa-file-pdf"
        elif extension in ["doc", "docx"]:
            file.icon_class = "fas fa-file-word"
        elif extension in ["jpg", "jpeg", "png"]:
            file.icon_class = "fas fa-file-image"
        else:
            file.icon_class = "fas fa-file"
    return render(request, 'formapp/success.html', {"files": files})
