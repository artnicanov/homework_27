from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=200, unique=True)

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self):
		return self.name

class Ad(models.Model):
	name = models.CharField(max_length=200)
	author = models.ForeignKey('users.User', on_delete=models.CASCADE)
	price = models.PositiveIntegerField()
	description = models.TextField()
	address = models.CharField(max_length=300)
	is_published = models.BooleanField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='ads/images/', null=True, blank=True )

	class Meta:
		verbose_name = "Объявление"
		verbose_name_plural = "Объявления"

	def __str__(self):
		return self.name
