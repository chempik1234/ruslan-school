# Generated by Django 5.0.6 on 2024-06-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_ticket_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]