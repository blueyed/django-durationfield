# encoding: utf8
from django.db import models, migrations
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithDuration',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('runtime', durationfield.db.models.fields.duration.DurationField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
