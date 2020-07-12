import uuid

from django.db import models


class IdMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class MoneyMixin(models.Model):
    amount = models.FloatField()
    type = models.CharField(max_length=7, choices=(('income', 'income'), ('expense', 'expense')))

    class Meta:
        abstract = True


class Budget(IdMixin):
    start_date = models.DateField()
    end_date = models.DateField()


class LineItem(IdMixin, MoneyMixin):
    budget = models.ForeignKey(Budget, null=True, on_delete=models.SET_NULL)


class Transaction(IdMixin, MoneyMixin):
    line_item = models.ForeignKey(LineItem, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
