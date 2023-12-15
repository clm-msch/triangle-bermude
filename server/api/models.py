from django.db import models


class Price_type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Access_type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Adresse(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_name = models.CharField(max_length=255, null=True)
    address_street = models.CharField(max_length=255, null=True)
    address_zipcode = models.CharField(max_length=255, null=True)
    address_city = models.CharField(max_length=255, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    
    def __str__(self):
        return self.address_name
    
class Audience(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.TextField(max_length=255, null=True)
    title = models.TextField(max_length=255, null=True)
    lead_text = models.TextField(null=True)
    description = models.TextField(null=True)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)
    date_description = models.TextField(max_length=255, null=True)
    cover_url = models.TextField(max_length=255, null=True)
    cover_alt = models.TextField(max_length=255, null=True)
    cover_credit = models.TextField(max_length=255, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    pmr = models.BooleanField(null=True)
    blind = models.BooleanField(null=True)
    deaf = models.BooleanField(null=True)
    transport = models.TextField(null=True)
    contact_url = models.TextField(max_length=255, null=True)
    contact_phone = models.TextField(max_length=255, null=True)
    contact_mail = models.TextField(max_length=255, null=True)
    contact_facebook = models.TextField(max_length=255, null=True)
    contact_twitter = models.TextField(max_length=255, null=True)
    price_id = models.ForeignKey(Price_type, on_delete=models.SET_NULL, null=True)
    price_detail = models.TextField(max_length=255, null=True)
    access_id = models.ForeignKey(Access_type, on_delete=models.SET_NULL, null=True)
    access_link = models.TextField(max_length=255, null=True)
    access_link_text = models.TextField(max_length=255, null=True)
    updated_at = models.DateTimeField(null=True)
    programs = models.TextField(null=True)
    address_url = models.TextField(max_length=255, null=True)
    address_url_text = models.TextField(max_length=255, null=True)
    address_text = models.TextField(max_length=255, null=True)
    title_event = models.TextField(max_length=255, null=True)
    audience_id = models.ForeignKey(Audience, on_delete=models.SET_NULL, null=True)
    childrens = models.TextField(null=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    adress_id = models.ForeignKey(Adresse, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    

class Occurrence(models.Model):
    id = models.BigAutoField(primary_key=True)
    occurrence_start = models.DateTimeField(null=True)
    occurrence_end = models.DateTimeField(null=True)
    occurence_id = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)