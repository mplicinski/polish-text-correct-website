from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        text_data = {
            "rows":30,
            "class":"form-control md-textarea"
        }
        self.fields['text'].widget.attrs.update(text_data)
    
