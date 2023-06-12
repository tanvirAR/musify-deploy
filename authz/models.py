from django.db import models
import uuid
import hashlib
import time


# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


def generate_id():
    new_uuid = uuid.uuid4().hex[:10]
    unique_value = str(time.time()).encode('utf-8')
    hashed_id = hashlib.sha256(
        unique_value + new_uuid.encode('utf-8')).hexdigest()

    return hashed_id[:20]

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(null=True, max_length=200, default="null")
    password = models.CharField(max_length=100)
    id = models.CharField(max_length=50, primary_key=True, unique=True, default=generate_id)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    # def get_name(self):
    #     return self.name

    def clean(self):
        if self.email is None or self.email.strip() == '':
            raise ValidationError('Email is required!')

        # if self.name is None or self.name.strip() == '':
        #     raise ValidationError('Name is required!')
        
        if self.password is None or self.password.strip() == '':
            raise ValidationError('Password is required!')
        

        if len(self.password) < 4:
            raise ValidationError(
                'Password must be at least 4 characters long')
        if len(self.password) > 100:
            raise ValidationError(
                'Please use a shorter password!')


    def save(self, *args, **kwargs):
        # if not self.pk:
        self.id = generate_id()
        super().save(*args, **kwargs)