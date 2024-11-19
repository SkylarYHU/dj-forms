from django.contrib import admin
from .models import Contact, UploadFile
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from mimetypes import guess_type

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'message', 'uploaded_at')

  # 用于控制模型对象在 编辑页面（添加或修改模型对象） 中的字段组织和布局
  fieldsets = (
    ('Info', {'fields':('name', 'email')}),
    ('Message', {'fields':('message',)}),
  )

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
  list_display = ('file', 'preview', 'uploaded_at')
  readonly_fields = ('uploaded_at',)

  def preview(self, obj):
    if obj.file and guess_type(obj.file.url)[0].startswith('image/'):
      return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.file.url)
    return 'Not an image'
  preview.short_description = 'Preview of images'


