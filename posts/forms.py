from django import forms
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field,HTML


class CreateCommentForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CreateCommentForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field("content", css_class="single-input", rows="3")
        )

        self.helper.add_input(Submit('submit', 'Yorum Ekle', css_class="nw-btn primary-btn mt-10"))


    class Meta:
        model = Comment
        fields = ('content',)




