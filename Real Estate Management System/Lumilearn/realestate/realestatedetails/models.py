from django.db import models

class RealEstate(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    confirm_password = models.CharField(max_length=8)  # Changed to 'confirm_password' to follow naming conventions
    contact_no = models.PositiveBigIntegerField()  # Changed to snake_case for consistency
    email = models.CharField(max_length=30)
    role = models.CharField(max_length=20, default='10')  # Assuming a max length for the role field



class details(models.Model):
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200,default=0)
    qualification = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    account_no = models.PositiveBigIntegerField(default=0)
    ifsc_code = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=20)
    plots_purchased = models.CharField(max_length=10)

class sellers(models.Model):
    company_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200,default=0)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)

class plotsDetails(models.Model):
    area_name = models.CharField(max_length=20)
    No_of_plots= models.PositiveBigIntegerField()
    square_feet_rate= models.PositiveBigIntegerField()
    amenities = models.CharField(max_length=200)

class bi(models.Model):
    client_name = models.CharField(max_length=20)
    contact_no = models.PositiveBigIntegerField()
    area_name = models.CharField(max_length=20)
    booked_amount = models.PositiveBigIntegerField()
    reg_amt = models.PositiveBigIntegerField()
    reg_date = models.DateField()

class plotinfo(models.Model):
    area_name = models.CharField(max_length=20)
    No_of_plots = models.PositiveBigIntegerField()
    square_feet_rate = models.PositiveBigIntegerField()
    Amenities = models.CharField(max_length=200)

class client_req(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    plot_seen= models.PositiveBigIntegerField()
    amount_Details = models.PositiveBigIntegerField()
    requirements = models.CharField(max_length=200)

