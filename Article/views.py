from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from Article.forms import AddArticle
from Article.models import Article


# Create your views here.
def index(request):
    return HttpResponse("Bonjour,voici la page index")

def index_id(request,id):
    result="bonjour id  %s"
    return HttpResponse(result %id)

def index_template(request):
    return render(request,'Article/index.html')

def list_Article(request):
    articles=Article.objects.all()
    contexte={'a':articles}
    return render(request,'Article/list.html',contexte)

def detail_article(request,id):
    article=Article.objects.get(pk=id)
    context={'a':article}
    return render(request,'Article/detail.html',context)

def add_article(request):
    if request.method=='GET':
        form=AddArticle()
        return render(request,'Article/AddArticle.html',{'f':form})
    if request.method=='POST':
        form=AddArticle(request.POST)
        if form.is_valid():
            Article=form.save(commit=True)
            Article.save()
            return HttpResponseRedirect(reverse('affichage'))
        else:
            return render(request,'Article/AddArticle.html',{'f':form,'msg_error':'Error lors de lajou'})

def Delete(request,id):
    #article=Article.objects.get(pk=id)
    article=get_object_or_404(Article,pk=id)
    article.delete()
    return HttpResponseRedirect(reverse('afiche_view'))

def update_Article(request,id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'GET':
        form = AddArticle(instance=article)
        return render(request, 'Article/EditArticle.html', {'form': form,'id':id})
    if request.method == 'POST':
        form = AddArticle(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('afiche_view'))
        else:
            return render(request, 'Article/AddArticle.html', {'form': form, 'msg_error': 'Error lors de lajou'})

# les classes de vue generiques:
class article_listView(ListView):
    model = Article
    template_name = 'liste_view.html'
    context_object_name = 'a'
    ordering = ['-pub_date'] # - desc

class detail_view(DetailView):
    model = Article
    context_object_name = 'aa'
    template_name = 'article_detail.html'

class Add_Article_View(CreateView):
    model = Article
    fields=['headline','pub_date','est_valide','reporter']
    success_url = reverse_lazy('afiche_view')
    template_name = 'add_article_view.html'

class Delete_view(DeleteView):
    model = Article
    success_url = reverse_lazy('afiche_view')
    template_name = 'article_confirm_delete.html'

class Update_view(UpdateView):
    model = Article
    template_name = 'Article/EditArticle.html'
    fields = ['headline', 'pub_date', 'est_valide', 'reporter']
    success_url = reverse_lazy('afiche_view')