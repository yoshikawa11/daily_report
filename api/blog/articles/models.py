import uuid
from django.db import models

# Create your models here.
class Todo(models.Model):
    uuid = models.UUIDField('uuid', primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(verbose_name="todo", max_length=100)
    priority = models.CharField(verbose_name="優先度", max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
