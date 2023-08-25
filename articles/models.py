from django.db import models

# Create your models here.

class Article(models.Model):          # 게시판 
    title = models.CharField(max_length=50)  # 제목 
    content = models.TextField()            # 내용 


class Comment(models.Model):       # 댓글 
    content = models.TextField()    # 작성칸 
    article = models.ForeignKey(Article,on_delete=models.CASCADE) # 
