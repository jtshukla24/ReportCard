# Generated by Django 4.2.17 on 2024-12-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
