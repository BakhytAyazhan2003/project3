from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name + ' ' + self.phone_number + ' ' + self.student_id + ' ' + self.login + ' ' + self.password + ' ' + self.city

    #def get_integer(self):
        #return 6

    def get_true(self):
        return True