from django import forms
from .models import Contact, UploadFile

# ModelForm从模型派生表单，通过 Meta 类指定了对应的模型，快速创建与模型字段对应的表单，减少了重复的代码，并且更容易保持表单与模型之间的数据一致性
class ContactModelForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name','email','message']

  # 自定义字段验证
  def clean_name(self):
    name = self.cleaned_data.get('name')
    if "test" in name:
      raise forms.ValidationError("Name cannot include 'test'")
    return name

  # 表单级验证
  def clean(self):
    cleaned_data = super().clean()
    name = cleaned_data.get('name')
    email = cleaned_data.get('email')

    if name and email and name in email:
      raise forms.ValidationError("Name cannot be included in email.")
    
class UploadFileModelForm(forms.ModelForm):
  class Meta:
    model = UploadFile
    fields = ['file', 'message']