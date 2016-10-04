from __future__ import unicode_literals

from django.db import models

# Create your models here.

track = (('python','python'),
	('android','android'),
	('web','web')
	)

class project(models.Model):
	p_name = models.CharField(max_length=500)
	p_description = models.TextField()
	deadline = models.DateTimeField()
	track = models.CharField(choices=track,max_length=500)

	def __str__(self):
		return self.p_name

class users(models.Model):
	g_uname = models.CharField(max_length=100)
	s_uname = models.CharField(max_length=100)
	p_submitted = models.ManyToManyField(project)
	f_name  = models.CharField(max_length=100)
	track= models.CharField(choices=track,max_length=500)

	def __str__(self):
		return self.f_name

class s_project(models.Model):
	user=models.ForeignKey(users)
	project=models.ForeignKey(project)
	repo_link =models.CharField(max_length=500)
	hosted_url = models.CharField(max_length=500)

	def __str__(self):
		return self.user.f_name + " : " +self.project.p_name