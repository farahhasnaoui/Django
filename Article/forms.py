from django.forms import ModelForm, Textarea

from Article.models import Article


class AddArticle(ModelForm):
    class Meta:
        model=Article
        fields=('headline','pub_date','est_valide','reporter')
        widgets={'headline':Textarea(attrs={'col':20,'rows':20})}