from django import forms


class AddTodoForm(forms.Form):
    text = forms.CharField(label="Название")
    deadline = forms.DateField(label="Дедлайн",widget=forms.SelectDateWidget)
class AddCommentForm(forms.Form):
    text = forms.CharField(label="Комментарий",widget=forms.Textarea)
