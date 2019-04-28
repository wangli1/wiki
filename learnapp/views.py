from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.forms import forms
from DjangoUeditor.forms import UEditorModelForm, UEditorField
from learnapp.models import articles, Blog

#自己生成form类型
class TestUEditorForm(UEditorModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class TestForm(forms.Form):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="updates/imgs", filePath="updates/files/",
                           upload_settings={"imageMaxSize": 1204000}, settings={})

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('收到')
        form = TestUEditorForm(request.POST)
        if form.is_valid():
          form.save()
        return HttpResponse('成功')
    else:
        form = TestUEditorForm()
        return render(request, 'home.html', {'value': 'lss', 'form': form})


def send(request):

    return HttpResponse('f')
