from django.db import models
import uuid


class Wallet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Пользователь')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Баланс')

    def __str__(self):
        return f"Баланс пользователя {self.uuid} составляет {self.balance}"


