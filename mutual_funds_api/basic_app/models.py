from django.db import models

# Create your models here.
class MutualFundsCode(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.code

class MutualFundsScheme(models.Model):
    fund_house = models.CharField(max_length=255)
    scheme_type = models.CharField(max_length=255)
    scheme_category = models.CharField(max_length=255)
    scheme_code = models.ForeignKey(MutualFundsCode,on_delete=models.CASCADE,
                                    related_name='mutual_funds_schemes')
    scheme_name = models.TextField()
    scheme_start_date = models.DateField()

    def __str__(self):
        return str(self.scheme_code)
    