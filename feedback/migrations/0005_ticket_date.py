# Generated by Django 5.0.6 on 2024-06-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_ticket_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
