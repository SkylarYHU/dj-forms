from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  message = models.TextField(max_length=500)
  uploaded_at = models.DateTimeField(auto_now_add=True) # 自动记录上传时间，注意不可编辑

  def __str__(self):
      return f"{self.name}: '{self.uploaded_at}'"
  
class UploadFile(models.Model):
  file = models.FileField(upload_to="upload/")
  message = models.TextField()
  uploaded_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"{self.file.name} - {self.uploaded_at}"
  
