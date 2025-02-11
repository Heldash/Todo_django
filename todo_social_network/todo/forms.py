from django import forms
class AddTodoForm(forms.Form):
    text_class="border-2 bg-neutral-300 transition rounded-sm p-2 pl-2 hover:bg-neutral-200 focus:bg-neutral-100 hover:border-blue-950 focus:scale-103 hover:scale-103"
    text = forms.CharField(label="Название",widget=forms.TextInput(attrs={"class":text_class}))
    deadline = forms.DateField(label="Дедлайн",widget=forms.SelectDateWidget)
class AddCommentForm(forms.Form):
    text_class="border-2 h-13 bg-neutral-300 transition rounded-sm p-2 pl-2 hover:bg-neutral-200 focus:bg-neutral-100 hover:border-blue-950 focus:border-3 hover:border-3"
    text = forms.CharField(label="Комментарий",widget=forms.Textarea(attrs={"class":text_class}))
