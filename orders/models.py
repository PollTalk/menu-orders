# Create your models here.

from django.db import models

class Item(models.Model):
	""" This class defines the items listed in the menu list"""

	MENU_CATEGORIES = (
		('BF', 'BreakFast'),
		('LU', 'Lunch'),
		('SN', 'Snacks'),
		)
	
	item = models.CharField(max_length=50, unique=True)
	category = models.CharField(max_length=2, choices=MENU_CATEGORIES)
	price_per_item = models.IntegerField(db_index=True)
	date_created = models.DateField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.item

class Order(models.Model):
	""" A definition of the Orders dependent on the Menu Items"""
	items = models.ManyToManyField(Item)
	ordering_time = models.DateTimeField(auto_now_add=True)
	cost_of_order = models.IntegerField(default=0, db_index=True)

	def __unicode__(self):
		return u"Order made at %s" % self.ordering_time

	class Meta:
		verbose_name = u'Menu Order'