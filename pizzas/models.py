from django.db import models

class Pizza(models.Model):
    """A model representing a pizza."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """A specific topping added to a pizza."""
    pizza = models.ForeignKey(Pizza)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
