from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class AMC(models.Model):
    name = models.CharField(max_length=255, unique=True)

# actual schemes class
class Scheme(models.Model):
    amc = models.ForeignKey(
        'AMC',
        on_delete=models.CASCADE,
    )
    scheme_category = models.CharField(max_length=255, null=False)
    scheme_type = models.CharField(max_length=255, null=False)
    scheme_sub_type = models.CharField(max_length=255, null=False)
    fund_code = models.CharField(max_length=255, null=False, unique=True)
    fund_name = models.CharField(max_length=255, null=False)
    fund_option = models.CharField(max_length=255, null=False)
    fund_type = models.CharField(max_length=255, null=False)

    class meta:
        unique_together = ("amc", "fund_code")

class Nav(models.Model):
    scheme = models.ForeignKey(
        'Scheme',
        on_delete=models.CASCADE,
    )
    nav = models.FloatField(null=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("scheme", "date")