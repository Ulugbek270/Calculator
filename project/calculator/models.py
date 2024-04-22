from django.db import models


class Calculator(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    history = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return str(self.history)
        # return str(self.value2)


