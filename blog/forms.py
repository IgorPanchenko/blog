from django import forms

from blog.models import Comment


class EmailFormPost(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=25)
    email = forms.EmailField(label='Ваша почта')
    to = forms.EmailField(label='Адрес получателя')
    comment = forms.CharField(required=False, widget=forms.Textarea, label='Комментарий', max_length=100)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
        self.fields['email'].label = 'Почта'
        self.fields['body'].label = 'Коментарий'


class SearchForm(forms.Form):
    query = forms.CharField()
