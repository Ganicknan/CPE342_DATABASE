# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customernumber = models.TextField(db_column='customerNumber', primary_key=True)  # Field name made lowercase.
    customername = models.TextField(db_column='customerName', blank=True, null=True)  # Field name made lowercase.
    contactlastname = models.TextField(db_column='contactLastName', blank=True, null=True)  # Field name made lowercase.
    contactfirstname = models.TextField(db_column='contactFirstName', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(blank=True, null=True)
    addressline1 = models.TextField(db_column='addressLine1', blank=True, null=True)  # Field name made lowercase.
    addressline2 = models.TextField(db_column='addressLine2', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    postalcode = models.TextField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(blank=True, null=True)
    salesrepemployeenumber = models.TextField(db_column='salesRepEmployeeNumber', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.TextField(db_column='creditLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeenumber = models.TextField(db_column='employeeNumber', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    extension = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    officecode = models.TextField(db_column='officeCode', blank=True, null=True)  # Field name made lowercase.
    reportsto = models.TextField(db_column='reportsTo', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.TextField(db_column='jobTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class Offices(models.Model):
    officecode = models.TextField(db_column='officeCode', primary_key=True)  # Field name made lowercase.
    city = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    addressline1 = models.TextField(db_column='addressLine1', blank=True, null=True)  # Field name made lowercase.
    addressline2 = models.TextField(db_column='addressLine2', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    postalcode = models.TextField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase.
    territory = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offices'


class Orderdetails(models.Model):
    ordernumber = models.TextField(db_column='orderNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    productcode = models.TextField(db_column='productCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quantityordered = models.TextField(db_column='quantityOrdered', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    priceeach = models.TextField(db_column='priceEach', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    orderlinenumber = models.TextField(db_column='orderLineNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Orders(models.Model):
    ordernumber = models.TextField(db_column='orderNumber', primary_key=True)  # Field name made lowercase.
    orderdate = models.TextField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    requireddate = models.TextField(db_column='requiredDate', blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.TextField(db_column='shippedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    customernumber = models.TextField(db_column='customerNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Payments(models.Model):
    customernumber = models.TextField(db_column='customerNumber', blank=True, null=True)  # Field name made lowercase.
    checknumber = models.TextField(db_column='checkNumber', primary_key=True)  # Field name made lowercase.
    paymentdate = models.TextField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class Productlines(models.Model):
    productline = models.TextField(db_column='productLine', primary_key=True)  # Field name made lowercase.
    textdescription = models.TextField(db_column='textDescription', blank=True, null=True)  # Field name made lowercase.
    htmldescription = models.TextField(db_column='htmlDescription', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productlines'


class Products(models.Model):
    productcode = models.TextField(db_column='productCode', primary_key=True)  # Field name made lowercase.
    productname = models.TextField(db_column='productName', blank=True, null=True)  # Field name made lowercase.
    productline = models.TextField(db_column='productLine', blank=True, null=True)  # Field name made lowercase.
    productscale = models.TextField(db_column='productScale', blank=True, null=True)  # Field name made lowercase.
    productvendor = models.TextField(db_column='productVendor', blank=True, null=True)  # Field name made lowercase.
    productdescription = models.TextField(db_column='productDescription', blank=True, null=True)  # Field name made lowercase.
    quantityinstock = models.TextField(db_column='quantityInStock', blank=True, null=True)  # Field name made lowercase.
    buyprice = models.TextField(db_column='buyPrice', blank=True, null=True)  # Field name made lowercase.
    msrp = models.TextField(db_column='MSRP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'
