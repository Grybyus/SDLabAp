# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Region(models.Model):
    r_regionkey = models.IntegerField(primary_key=True)
    r_name = models.CharField(max_length=25, blank=True, null=True)
    r_comment = models.CharField(max_length=152, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Nation(models.Model):
    n_nationkey = models.IntegerField(primary_key=True)
    n_name = models.CharField(max_length=25, blank=True, null=True)
    n_regionkey = models.ForeignKey('Region', models.DO_NOTHING, db_column='n_regionkey', blank=True, null=True)
    n_comment = models.CharField(max_length=152, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nation'

class Customer(models.Model):
    c_custkey = models.BigIntegerField(primary_key=True)
    c_mktsegment = models.CharField(max_length=10, blank=True, null=True)
    c_nationkey = models.ForeignKey('Nation', models.DO_NOTHING, db_column='c_nationkey', blank=True, null=True)
    c_name = models.CharField(max_length=25, blank=True, null=True)
    c_address = models.CharField(max_length=40, blank=True, null=True)
    c_phone = models.CharField(max_length=15, blank=True, null=True)
    c_acctbal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    c_comment = models.CharField(max_length=118, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Orders(models.Model):
    o_orderdate = models.DateField(blank=True, null=True)
    o_orderkey = models.BigIntegerField(primary_key=True)
    o_custkey = models.ForeignKey(Customer, models.DO_NOTHING, db_column='o_custkey')
    o_orderpriority = models.CharField(max_length=15, blank=True, null=True)
    o_shippriority = models.IntegerField(blank=True, null=True)
    o_clerk = models.CharField(max_length=15, blank=True, null=True)
    o_orderstatus = models.CharField(max_length=1, blank=True, null=True)
    o_totalprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    o_comment = models.CharField(max_length=79, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Part(models.Model):
    p_partkey = models.BigIntegerField(primary_key=True)
    p_type = models.CharField(max_length=25, blank=True, null=True)
    p_size = models.IntegerField(blank=True, null=True)
    p_brand = models.CharField(max_length=10, blank=True, null=True)
    p_name = models.CharField(max_length=55, blank=True, null=True)
    p_container = models.CharField(max_length=10, blank=True, null=True)
    p_mfgr = models.CharField(max_length=25, blank=True, null=True)
    p_retailprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    p_comment = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class Supplier(models.Model):
    s_suppkey = models.IntegerField(primary_key=True)
    s_nationkey = models.ForeignKey(Nation, models.DO_NOTHING, db_column='s_nationkey', blank=True, null=True)
    s_comment = models.CharField(max_length=102, blank=True, null=True)
    s_name = models.CharField(max_length=25, blank=True, null=True)
    s_address = models.CharField(max_length=40, blank=True, null=True)
    s_phone = models.CharField(max_length=15, blank=True, null=True)
    s_acctbal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Partsupp(models.Model):
    ps_partkey = models.ForeignKey(Part, models.DO_NOTHING, db_column='ps_partkey', primary_key=True)
    ps_suppkey = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='ps_suppkey')
    ps_supplycost = models.DecimalField(max_digits=19, decimal_places=4)
    ps_availqty = models.IntegerField(blank=True, null=True)
    ps_comment = models.CharField(max_length=199, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partsupp'
        unique_together = (('ps_partkey', 'ps_suppkey'),)


class Lineitem(models.Model):
    l_shipdate = models.DateField(blank=True, null=True)
    l_orderkey = models.ForeignKey('Orders', models.DO_NOTHING, db_column='l_orderkey', primary_key=True)
    l_discount = models.DecimalField(max_digits=19, decimal_places=4)
    l_extendedprice = models.DecimalField(max_digits=19, decimal_places=4)
    l_suppkey = models.IntegerField()
    l_quantity = models.BigIntegerField()
    l_returnflag = models.CharField(max_length=1, blank=True, null=True)
    l_partkey = models.ForeignKey('Partsupp', models.DO_NOTHING, db_column='l_partkey')
    l_linestatus = models.CharField(max_length=1, blank=True, null=True)
    l_tax = models.DecimalField(max_digits=19, decimal_places=4)
    l_commitdate = models.DateField(blank=True, null=True)
    l_receiptdate = models.DateField(blank=True, null=True)
    l_shipmode = models.CharField(max_length=10, blank=True, null=True)
    l_linenumber = models.BigIntegerField()
    l_shipinstruct = models.CharField(max_length=25, blank=True, null=True)
    l_comment = models.CharField(max_length=44, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineitem'
        unique_together = (('l_orderkey', 'l_linenumber'),)
