import datetime
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField 

class Article(models.Model):
	article_title = models.CharField('Заголовок', max_length = 200)
	article_alias = models.CharField('Псевдоним', max_length = 50, unique=True)
	article_shorttext = models.TextField('Краткое описание')
	article_text = RichTextUploadingField ('Описание')
	article_date = models.DateTimeField('Дата публикации новости')
	article_status = models.BooleanField('Статус')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.article_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'