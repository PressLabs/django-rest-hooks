# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.CharField(db_index=True, max_length=64, verbose_name=b'Event', choices=[(b'customer.created', b'customer.created'), (b'customer.deleted', b'customer.deleted'), (b'customer.updated', b'customer.updated'), (b'invoice.created', b'invoice.created'), (b'invoice.deleted', b'invoice.deleted'), (b'invoice.updated', b'invoice.updated'), (b'plan.created', b'plan.created'), (b'plan.deleted', b'plan.deleted'), (b'plan.updated', b'plan.updated'), (b'proforma.created', b'proforma.created'), (b'proforma.deleted', b'proforma.deleted'), (b'proforma.updated', b'proforma.updated'), (b'provider.created', b'provider.created'), (b'provider.deleted', b'provider.deleted'), (b'provider.updated', b'provider.updated'), (b'subscription.created', b'subscription.created'), (b'subscription.deleted', b'subscription.deleted'), (b'subscription.updated', b'subscription.updated')])),
                ('target', models.URLField(max_length=255, verbose_name=b'Target URL')),
                ('global_hook', models.BooleanField(default=False, help_text=b'Fire the hook, regardless of user owning the object.', verbose_name=b'Global hook')),
                ('user', models.ForeignKey(related_name='hooks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hook',
            unique_together=set([('user', 'event', 'target', 'global_hook')]),
        ),
    ]
