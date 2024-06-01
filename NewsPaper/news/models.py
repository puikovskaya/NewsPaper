from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # Суммарный рейтинг статей
        post_ratings = sum([post.rating * 3 for post in self.post_set.all()])

        # Суммарный рейтинг комментариев автора
        author_comment_ratings = sum([comment.rating for comment in self.user.comment_set.all()])

        # Суммарный рейтинг комментариев к статьям автора
        post_comment_ratings = sum([comment.rating for comment in Comment.objects.filter(post__author=self)])

        # Общий рейтинг
        self.rating = post_ratings + author_comment_ratings + post_comment_ratings
        self.save()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category.title()

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10, choices=[('article', 'Статья'), ('news', 'Новость')])
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        preview_text = self.text[:124]
        if len(preview_text) < 124:
            return preview_text
        return preview_text + '...'

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.post.title()}: {self.text[:20]}'
