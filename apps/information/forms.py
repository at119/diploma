from django import forms


from apps.information.models import University, Amina, Major, News

from localflavor.us.forms import USStateSelect

from .models import Review, About



class UniCreateForm(forms.ModelForm):
    location = USStateSelect()


    class Meta:
        model = University
        fields = "__all__"


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('name', 'role', 'content')



class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', required=True)
    email = forms.EmailField(label='Your Email Address', required=True)
    phone = forms.CharField(label='Your Phone', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(label='Type Message', widget=forms.Textarea, required=True)
    location = forms.CharField(label='Location', required=True )
    # Можете добавить Captcha поле, если требуется

class AminaForm(forms.ModelForm):
    class Meta:
        model = Amina
        fields = ("first_name", "last_name", "biography", "image")



class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5, min_value=1, widget=forms.NumberInput())
    class Meta:
        model = Review
        fields = ['author', 'content']
    
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Оцените этот сайт от 1 до 5')
        return rating
    

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ("author", "content", "source")