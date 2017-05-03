from django.db import models


"""
	管理作家信息
	作家姓名、生平信息、作品集等
"""
class Author(models.Model):
	
	name = models.CharField(default=" ",max_length=100)

	"""
		作家简介
	"""
	intro = models.TextField(default=" ")

	def __str__(self):
		return self.name

"""
	管理出版社信息 
	出版社简要信息
"""
class Publisher(models.Model):
	"""
		出版社名称
	"""
	name = models.CharField(default=" ",max_length=100)

	def __str__(self):
		return self.name

# """
# 	管理图书上榜理由
# """
# class ReasonForListing(models.Model):

# 	reason = models.TextField(default=" ")

"""
	管理图书信息类
	包括出版社、作家、ISBN书号信息
"""
class Book(models.Model):
	
	"""
		书名
	"""
	name = models.CharField(default=" ",max_length=100)

	"""
		一本书可能有好几个作者
	"""
	anthors = models.ManyToManyField('Author')

	"""
		一本书对应一个出版社
	"""
	publisher = models.ForeignKey('Publisher',null=True)

	"""
		每本书都对应一个上榜的理由
	"""
	reasonForListing = models.TextField(default=" ",null=True)



	def __str__(self):
		return self.name


"""
	管理书单信息
	由一本本的书构成
"""
class Booklist(models.Model):

	"""
		书单的名称
	"""
	name = models.CharField(default=" ",max_length=100)

	"""
		一个书单包含若干本书
	"""
	books = models.ManyToManyField('Book')


	def __str__(self):
		return self.name
