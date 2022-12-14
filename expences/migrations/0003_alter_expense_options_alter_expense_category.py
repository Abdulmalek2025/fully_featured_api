# Generated by Django 4.1 on 2022-08-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expences', '0002_rename_data_expense_date_alter_expense_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('RENT', 'RENT'), ('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('TRAVEL', 'TRAVEL'), ('OTHERS', 'OTHERS'), ('FOOD', 'FOOD')], max_length=255),
        ),
    ]
