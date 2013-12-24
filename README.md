Simple project for demonstration https://github.com/jeffknupp/sandman/issues/20 bug.


We have existinbg django project with models:

```python
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class Custmer(models.Model):
    name = models.CharField(max_length=100)

    billing_address = models.ForeignKey(
        Address,
        related_name='billing_customer_set')
    shipping_address = models.ForeignKey(
        Address,
        related_name='shipping_customer_set')
```

When you run sandman
```
python sandman_server.py
```
you got the error
```
sqlalchemy.exc.AmbiguousForeignKeysError: Could not determine join condition between parent/child tables on relationship customer_address.__customer_custmer - there are multiple foreign key paths linking the tables.  Specify the 'foreign_keys' argument, providing a list of those columns which should be counted as containing a foreign key reference to the parent table.
```


Sqlite database included.
