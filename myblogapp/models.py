from django.db import models

PRIORITY=(
    (1,'Health'),
    (2,'Magazine'),
    (3,'Food'),
    (4,'Book'),
    (5,'Movies')
)


class Post(models.Model):
    category=models.IntegerField(choices=PRIORITY)
    title=models.CharField(max_length=32)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category+' '+self.title+' '+self.created_date
