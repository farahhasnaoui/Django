from django.db import models

from Reporter.models import Reporter


# Create your models here.
class Article(models.Model):
    headline=models.CharField(max_length=30)
    pub_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    est_valide=models.BooleanField(default=True)
    reporter=models.ForeignKey(
        Reporter,on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.headline
