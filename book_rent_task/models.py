from datetime import *
import traceback
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TimestampDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

    def get_creation_time(self):
        return self.created_at

class Book(TimestampDate):
    title = models.CharField(max_length=60, default="")
    pages = models.CharField(max_length=40, default="")
    author = models.CharField(max_length=60, default="",blank=True, null=True)
    is_free = models.BooleanField(default=False)
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rented_books", db_column="user_renter", default=None, blank=True, null=True)
    total_renters = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    # pdf = models.FileField(upload_to='books/pdfs/', default = None,null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.pages} {self.author} {self.is_free} {self.renter} {self.total_renters}"

class rental_books_user(TimestampDate):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rental", db_column="rental_user", default=None, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_rental", db_column="book_for_rent", default=None, blank=True, null=True)
    renter_duration = models.IntegerField(default=timedelta(days=30))
    renter_page_book = models.IntegerField(default=0)
    rent_of_book = models.FloatField(default=0)
    payment_signature = models.CharField(max_length=100,null=True,blank=True)
    payment_id = models.CharField(max_length=100,null=True,blank=True)

    def access_expired(self):
        rental_period = timedelta(days=self.renter_duration)
        return timezone.now() > self.created_at + rental_period

    def __str__(self) -> str:
        try:
            return f"{self.user} {self.book}  {self.renter_duration} {self.renter_page_book} {self.rent_of_book}"
        except:
            print(traceback.print_exc)
