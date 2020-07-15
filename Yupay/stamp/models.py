from django.db import models

# Create your models here.
class Person(models.Model):
    DNI = models.IntegerField(primary_key=True) 
    base_trxid = models.CharField(max_length=50) 
    def getDNI(self):
        return self.DNI
    
    def getTrx(self):
        return self.base_trxid