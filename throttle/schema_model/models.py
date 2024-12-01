from django.db import models

class SchemaSharedModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shared_collection'

    def __str__(self):
        return self.name
