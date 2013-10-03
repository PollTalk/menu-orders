# Create your models here.

from django.db import models

class CategorizeItem(models.Model):
	"""categories definition"""
	category_name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.category_name

class Item(models.Model):
	""" This class defines the items listed in the menu list"""	
	item = models.CharField(max_length=50, unique=True)
	category = models.ForeignKey(CategorizeItem)
	price_per_item = models.IntegerField(db_index=True)
	date_created = models.DateField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.item

class Order(models.Model):
	""" A definition of the Orders dependent on the Menu Items"""
	items = models.ManyToManyField(Item, through='TakeOrder')
	cost_of_order = models.IntegerField(default=0, db_index=True)
	ordering_time = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return u"Order made on %s" % self.ordering_time.strftime('%a, %d - %b - %Y, %H:%M:%S GMT')

	class Meta:
		verbose_name = u'Menu Order'

class TakeOrder(models.Model):
	""" This model class is an intermediary between Item and Order """
	item = models.ForeignKey(Item)
	order = models.ForeignKey(Order)
	number_of_items = models.IntegerField(default=1)

	def __unicode__(self):
		return "%s, %s" % (self.item, self.order)
	