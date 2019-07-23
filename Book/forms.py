from django import forms

class borrowbook(forms.Form):
    b_name = forms.CharField(label='书名', max_length=30)
    stu_id = forms.CharField(label='学号', max_length=10)
    stu_name = forms.CharField(label='姓名', max_length=15)
    stu_phone = forms.CharField(label='联系电话', max_length=11)
    stu_qq = forms.CharField(label='QQ', max_length=15)

class retuenbook(forms.Form):
    b_name = forms.CharField(label='书名', max_length=30)
    stu_id = forms.CharField(label='学号', max_length=10)