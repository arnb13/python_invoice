from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField

class InvoiceModel (models.Model):
    id = models.AutoField(auto_created= True, primary_key= True, unique= True, editable= False)
    company_name = models.CharField (max_length= 250, default= '-1')
    file_location = models.FileField ()
    invoice_info = models.TextField (default= '-1')

    def __str__ (self) :
        return self.company_name

