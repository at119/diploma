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
    # You can add a Captcha field if required

class AminaForm(forms.ModelForm):
    class Meta:
        model = Amina
        fields = ("first_name", "last_name", "biography", "image")



class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))
    class Meta:
        model = Review
        fields = ['author', 'content', 'rating']
    
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Please rate this site from 1 to 5')
        return rating
    

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ("author", "content", "source")