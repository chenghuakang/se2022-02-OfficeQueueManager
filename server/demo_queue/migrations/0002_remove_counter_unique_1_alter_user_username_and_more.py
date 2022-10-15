# Generated by Django 4.1.2 on 2022-10-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_queue', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='counter',
            name='unique_1',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AddConstraint(
            model_name='counter',
            constraint=models.UniqueConstraint(fields=('_id', 'service'), name='unique_1'),
        ),
    ]