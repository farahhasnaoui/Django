from django import forms
from users.models import Person

CHOIX= (
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport', 'Sport')
    )

class EventForm(forms.Form):

    title = forms.CharField(label="Title",max_length=8)
    description =forms.CharField(label="Title",widget=forms.Textarea(attrs = { 'class':'form-control'})) #attrs je peux metrre le css ici
    image = forms.ImageField()
    category = forms.ChoiceField(label="category" , choices=CHOIX , widget=forms.RadioSelect)
    nbe_participant =forms.IntegerField(size_step=1 ,min_value=0)
    evt_date =forms.DateField(
label="Event date",widget=forms.DateInput(attrs={
        
        'type':'date',
        'class' : 'form-control date input'
})

    )
    organizer =forms.ModelChoiceField(label="orgonayzer",queryset=Person.objects.all())


