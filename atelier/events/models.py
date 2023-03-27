from django.db import models
from users.models import Person

# Create your models here.

class Event(models.Model):
    title = models.CharField('TITLE' ,max_length=255,blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    CHOIX= (
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport', 'Sport')
    )
    category = models.CharField(choices=CHOIX,max_length=15)
    state = models.BooleanField(default=False)
    nbe_participant = models.IntegerField(default=0)
    evt_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(Person,on_delete=models.CASCADE)
    subscription = models.ManyToManyField(
        Person,
        related_name='Participation',
        through='Participation',
    
        )

class Participation(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_participation = models.DateTimeField(auto_now_add=True)

