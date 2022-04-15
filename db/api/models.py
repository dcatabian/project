from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=31)
    lname = models.CharField(max_length=31)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    leave_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.fname

class LoginInfo(models.Model):
    M_TYPE = (
        (1, 1),
        (2, 2),
    )
    member_id = models.OneToOneField(Member,
        null = True, blank = True,
        on_delete = models.SET_NULL)
    username = models.CharField(max_length=31, unique=True)
    password = models.CharField(max_length=31)
    memType = models.IntegerField(choices = M_TYPE, default = 1)
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
    app_date = models.DateField(auto_now_add=True, null=True)
    ful_Status = models.CharField(max_length = 255, choices = STATUS)
    ful_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return str(self.in_id)

class Item(models.Model):
    POSSESION = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    it_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    possessed = models.CharField(max_length=255, choices = POSSESION)
    p_by = models.CharField(max_length=255)
    inv = models.ForeignKey('Invoice',
        null = True, blank = True,
        on_delete = models.SET_NULL,
        related_name = 'linked_invoice')

    def __str__(self):
        return self.name




    