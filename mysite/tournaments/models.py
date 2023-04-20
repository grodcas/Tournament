from django.db import models

class tournament(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    dates=models.CharField(max_length=100)  
    pools=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class team(models.Model):
    name=models.CharField(max_length=100)
    trainer=models.CharField(max_length=100)
    players=models.CharField(max_length=1000) 
    def __str__(self):
        return self.name

class pool(models.Model):
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE) 
    number=models.IntegerField()
    numberStr=models.CharField(max_length=100, default=None)
    teams=models.ManyToManyField(team)
    def __str__(self):
        return self.numberStr

class match(models.Model):
    date=models.DateTimeField('date published')
    place=models.CharField(max_length=100)
    teams=models.ManyToManyField(team)
    score=models.CharField(max_length=100)
    score_Team1=models.IntegerField(default=0)
    score_Team2=models.IntegerField(default=0)
    pool=models.ForeignKey(pool,on_delete=models.CASCADE)
