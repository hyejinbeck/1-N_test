from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.

def index(request): 
    articles = Article.objects.all()

    context = {
        'articles' : articles, 
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()


    context = {
        'article': article, 
        'comment_form': comment_form,
    }
    return render(request,'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            article=form.save()
            return redirect('articles:index')
            
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request, 'create.html', context)

def comment_create(request,article_id):
    comment_form = CommentForm(request.POST) # comment_form 변수에 CommentForm 클래스로 받은 댓글 content를 받은 것을 저장
    if comment_form.is_valid():
        comment=comment_form.save(commit=False) # DB에 저장하기 전에 잠깐 멈춰! 
        article=Article.objects.get(id=article_id)
        comment.article=article
        comment.save()
        
        return redirect('articles:detail', id=article_id)

def delete_comment(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()

    return redirect('articles:detail', id=article_id)
    
    
    
    
    

    

