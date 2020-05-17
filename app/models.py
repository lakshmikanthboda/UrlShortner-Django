from django.db import models

# Create your models here.
class short(models.Model):
    lurl= models.URLField()
    surl=models.URLField()
    views=models.IntegerField()
    def __str__(self):
        return str(self.lurl+' | '+str(self.views)+' | '+str(self.surl))

    class Meta:
        db_table=''
        managed=True
        verbose_name='url'
        verbose_name_plural='urls'

