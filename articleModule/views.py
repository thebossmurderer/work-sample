from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from articleModule.models import article, articleCategories, articleComment
from jalali_date import datetime2jalali, date2jalali


# Create your views here.


class articlesListView(ListView):
    model = article
    template_name = 'articleModule/articlePage.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super(articlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(articlesListView, self).get_queryset()
        query = query.filter(isActive=True)
        categotyName = self.kwargs.get('category')
        if categotyName is not None:
            query = query.filter(selectedCategories__urlTitle__iexact=categotyName)
        return query


def articelCategoriesPartial(request: HttpRequest):
    articleMainCategories = articleCategories.objects.prefetch_related('articlecategories_set').filter(isActive=True, parent_id=None)
    context = {
        'mainCategories': articleMainCategories
    }
    return render(request, 'articleModule/includes/articleCategoriesPartial.html', context)


class articleDetailView(DetailView):
    model = article
    template_name = 'articleModule/articleDetailPage.html'

    def get_queryset(self):
        query = super(articleDetailView, self).get_queryset()
        query = query.filter(isActive=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(articleDetailView, self).get_context_data()
        articles: article = kwargs.get('object')
        context['comments'] = articleComment.objects.filter(article_id=articles.id, parent=None).order_by('-createDate').prefetch_related('articlecomment_set')
        context['commentsCount'] = articleComment.objects.filter(article_id=articles.id).count()
        return context


def addArticleComment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        newComment = articleComment(article_id=article_id, text=article_comment, user_id=request.user.id,
                                    parent_id=parent_id)
        newComment.save()
        context = {
            'comments': articleComment.objects.filter(article_id=article_id, parent=None).order_by('-createDate').prefetch_related('articlecomment_set'),
            'commentsCount':articleComment.objects.filter(article_id=article_id).count()
        }
        return render(request, 'articleModule/includes/articleCommentPartial.html',context)
    return HttpResponse('hello')
