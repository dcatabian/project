from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=31)
    lname = models.CharField(max_length=31)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.fname

class LoginInfo(models.Model):
    member_id = models.OneToOneField(Member,
        null = True, blank = True,
        on_delete = models.SET_NULL)
    username = models.CharField(max_length=31)
    password = models.CharField(max_length=31)

    def __str__(self):
        return self.username

class PurchaseRequest(models.Model):
    p_id = models.AutoField(primary_key=True)
    sub_id = models.ForeignKey('Member',
        null = True, blank = True,
        on_delete = models.SET_NULL,
        related_name = 'Submitter_ID')
    app_id = models.ForeignKey('Member',
        null = True, blank = True,
        on_delete = models.SET_NULL,
        related_name = 'Approver_ID')
    iname = models.CharField(max_length=31)
    quant = models.IntegerField()
    cost = models.IntegerField()
    arg = models.CharField(max_length=255)

    def __str__(self):
        return self.iname

class Invoice(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Purchased', 'Purchased'),
        ('Fulfilled', 'Fulfulled'),
    )

    in_id = models.AutoField(primary_key=True)
    approved_pr = models.OneToOneField(PurchaseRequest,
        null = True, blank = True,
        on_delete = models.SET_NULL)
    app_date = models.DateField()
    ful_Status = models.CharField(max_length = 255, choices = STATUS)
    ful_date = models.DateField()

    def __str__(self):
        return self.in_id

class Item(models.Model):
    POSSESION = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    it_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    possessed = models.CharField(max_length=255, choices = POSSESION)
    p_by = models.CharField(max_length=255)

    def __str__(self):
        return self.it_id




    