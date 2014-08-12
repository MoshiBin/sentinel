from django.db import models

class Repo(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=200)


class File(models.Model):
    path = models.CharField(max_length=300)
    repo = models.ForeignKey(Repo)


class FileScore(models.Model):
    src_file = models.ForeignKey(File)
    test_date = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField()
