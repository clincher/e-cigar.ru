# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Manufacturer'
        db.create_table('myshop_manufacturer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('service_center', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('myshop', ['Manufacturer'])

        # Adding model 'Flavour'
        db.create_table('myshop_flavour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('myshop', ['Flavour'])

        # Adding model 'Cartridge'
        db.create_table('myshop_cartridge', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('myshop', ['Cartridge'])

        # Adding M2M table for field flavours on 'Cartridge'
        db.create_table('myshop_cartridge_flavours', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartridge', models.ForeignKey(orm['myshop.cartridge'], null=False)),
            ('flavour', models.ForeignKey(orm['myshop.flavour'], null=False))
        ))
        db.create_unique('myshop_cartridge_flavours', ['cartridge_id', 'flavour_id'])

        # Adding model 'CartridgeImage'
        db.create_table('myshop_cartridgeimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('src', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cartridge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['myshop.Cartridge'])),
        ))
        db.send_create_signal('myshop', ['CartridgeImage'])

        # Adding model 'Cigarette'
        db.create_table('myshop_cigarette', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myshop.Manufacturer'])),
            ('default_flavour', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myshop.Flavour'])),
            ('cartridge', self.gf('django.db.models.fields.related.OneToOneField')(related_name='cigarette', unique=True, to=orm['myshop.Cartridge'])),
            ('length', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('diameter', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('conditional_number', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('battery_capacity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('full_recharge', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('myshop', ['Cigarette'])

        # Adding model 'CigaretteImage'
        db.create_table('myshop_cigaretteimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('src', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cigarette', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['myshop.Cigarette'])),
        ))
        db.send_create_signal('myshop', ['CigaretteImage'])

        # Adding model 'Accessory'
        db.create_table('myshop_accessory', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('myshop', ['Accessory'])

        # Adding M2M table for field related_cigarettes on 'Accessory'
        db.create_table('myshop_accessory_related_cigarettes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accessory', models.ForeignKey(orm['myshop.accessory'], null=False)),
            ('cigarette', models.ForeignKey(orm['myshop.cigarette'], null=False))
        ))
        db.create_unique('myshop_accessory_related_cigarettes', ['accessory_id', 'cigarette_id'])

        # Adding model 'AccessoryImage'
        db.create_table('myshop_accessoryimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('src', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('accessory', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['myshop.Accessory'])),
        ))
        db.send_create_signal('myshop', ['AccessoryImage'])


    def backwards(self, orm):
        
        # Deleting model 'Manufacturer'
        db.delete_table('myshop_manufacturer')

        # Deleting model 'Flavour'
        db.delete_table('myshop_flavour')

        # Deleting model 'Cartridge'
        db.delete_table('myshop_cartridge')

        # Removing M2M table for field flavours on 'Cartridge'
        db.delete_table('myshop_cartridge_flavours')

        # Deleting model 'CartridgeImage'
        db.delete_table('myshop_cartridgeimage')

        # Deleting model 'Cigarette'
        db.delete_table('myshop_cigarette')

        # Deleting model 'CigaretteImage'
        db.delete_table('myshop_cigaretteimage')

        # Deleting model 'Accessory'
        db.delete_table('myshop_accessory')

        # Removing M2M table for field related_cigarettes on 'Accessory'
        db.delete_table('myshop_accessory_related_cigarettes')

        # Deleting model 'AccessoryImage'
        db.delete_table('myshop_accessoryimage')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myshop.accessory': {
            'Meta': {'object_name': 'Accessory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'related_cigarettes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'accessories'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['myshop.Cigarette']"})
        },
        'myshop.accessoryimage': {
            'Meta': {'object_name': 'AccessoryImage'},
            'accessory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['myshop.Accessory']"}),
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'myshop.cartridge': {
            'Meta': {'object_name': 'Cartridge'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flavours': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myshop.Flavour']", 'symmetrical': 'False'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        'myshop.cartridgeimage': {
            'Meta': {'object_name': 'CartridgeImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cartridge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['myshop.Cartridge']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'myshop.cigarette': {
            'Meta': {'object_name': 'Cigarette'},
            'battery_capacity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cartridge': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'cigarette'", 'unique': 'True', 'to': "orm['myshop.Cartridge']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conditional_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'default_flavour': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myshop.Flavour']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diameter': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'full_recharge': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myshop.Manufacturer']"}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'myshop.cigaretteimage': {
            'Meta': {'object_name': 'CigaretteImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cigarette': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['myshop.Cigarette']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'myshop.flavour': {
            'Meta': {'object_name': 'Flavour'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'myshop.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'service_center': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['myshop']
