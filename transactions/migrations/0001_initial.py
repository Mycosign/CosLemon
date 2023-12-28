# Generated by Django 4.2.3 on 2023-09-26 19:58

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal_internationa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('recipient_bank_name', models.CharField(default='', max_length=200)),
                ('account_number', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals_international', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Transfer_international',
                'verbose_name_plural': 'Manage Transfers_international',
            },
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('bank_sort_code', models.CharField(default='', max_length=200)),
                ('swift_code', models.CharField(default='', max_length=200)),
                ('recipient_bank_name', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=80)),
                ('account_number', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Transfer',
                'verbose_name_plural': 'Manage Transfers',
            },
        ),
        migrations.CreateModel(
            name='SUPPORT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.CharField(choices=[('Please Select Customer Service Department', 'Please Select Customer Service Department'), ('Request For Transaction Files', 'Request For Transaction Files'), ('Customer Services Department', 'Customer Services Department'), ('Account Department', 'Account Department'), ('Transfer Department', 'Transfer Department'), ('Card Services Department', 'Card Services Department'), ('Loan Department', 'Loan Department'), ('Bank Deposit Department', 'Bank Deposit Department')], max_length=255)),
                ('message', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SUPPORT',
                'verbose_name_plural': 'SUPPORTs',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('ETHEREUM', 'Ethereum'), ('BITCOIN', 'Bitcoin')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete')], default='PENDING', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Deposit/Payment',
                'verbose_name_plural': 'Manage Deposit/Payment',
            },
        ),
        migrations.CreateModel(
            name='PayBills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=512)),
                ('address2', models.CharField(default='', max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('state', models.CharField(max_length=512)),
                ('zipcode', models.CharField(max_length=512)),
                ('nickname', models.CharField(max_length=512)),
                ('delivery_method', models.CharField(choices=[('Paper Check', 'Paper Check'), ('Digital Receipt', 'Digital Receipt')], default='', max_length=200)),
                ('memo', models.CharField(default='', max_length=80)),
                ('account_number', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('day', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_bills', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Bills',
                'verbose_name_plural': 'Manage Bills',
            },
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_facility', models.CharField(choices=[('Personal Home Loans', 'Personal Home Loans'), ('Joint Mortgage', 'Joint Mortgage'), ('Automobile Loans', 'Automobile Loans'), ('Salary loans', 'Salary loans'), ('Secured Overdraft', 'Secured Overdraft'), ('Contract Finance', 'Contract Finance'), ('Secured Term Loans', 'Secured Term Loans'), ('StartUp/Products Financing', 'StartUp/Products Financing'), ('Local Purchase Orders Finance', 'Local Purchase Orders Finance'), ('Operational Vehicles', 'Operational Vehicles'), ('Revenue Loans and Overdraft', 'Revenue Loans and Overdraft'), ('Retail TOD', 'Retail TOD'), ('Commercial Mortgage', 'Commercial Mortgage'), ('Office Equipment', 'Office Equipment'), ('Health Finance Product Guideline', 'Health Finance Product Guideline'), ('Health Finance', 'Health Finance')], default='', max_length=40)),
                ('payment_tenure', models.CharField(choices=[('6 Months', '6 Months'), ('12 Months', '12 Months'), ('2 Years', '2 Years'), ('3 Years', '3 Years'), ('4 Years', '4 Years'), ('5 Years', '5 Years')], default='', max_length=40)),
                ('reason', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoWITHDRAW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('ETHEREUM', 'Ethereum'), ('BITCOIN', 'Bitcoin')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('recipient_address', models.CharField(default='', max_length=512)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete')], default='PENDING', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Crypto Withdrawal',
                'verbose_name_plural': 'Crypto Withdrawals',
            },
        ),
        migrations.CreateModel(
            name='CHECK_DEPOSIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='deposits/')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to='deposits/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Check Deposit',
                'verbose_name_plural': 'Check Deposits',
            },
        ),
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('V', 'Visa'), ('M', 'Mastercard'), ('D', 'Discover'), ('A', 'American Express'), ('CUP', 'China Union Pay'), ('DC', 'Dollar Card'), ('MC', 'Master Card'), ('VC', 'Visa Card'), ('JC', 'JCB Card'), ('AE', 'American Express'), ('UB', 'Union Bank Card'), ('BC', 'Bank Card'), ('EB', 'Eurocard'), ('NC', 'Nordic Card'), ('AC', 'Asian Card'), ('IC', 'International Card'), ('MC', 'Maestro Card'), ('EC', 'Eurocheque Card'), ('GC', 'Global Card'), ('UC', 'Uba Card'), ('FC', 'First Bank Card'), ('ZC', 'Zenith Bank Card'), ('AC', 'Access Bank Card'), ('GC', 'GTBank Card'), ('KC', 'Keystone Bank Card'), ('EC', 'Ecobank Card'), ('IC', 'UBA International Card'), ('OC', 'Other Card')], max_length=255)),
                ('card_number', models.CharField(max_length=255)),
                ('expiry_month', models.PositiveIntegerField()),
                ('expiry_year', models.PositiveIntegerField()),
                ('cvv', models.CharField(max_length=3)),
                ('card_owner', models.CharField(blank=True, max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card Detail',
                'verbose_name_plural': 'Card Details',
            },
        ),
    ]
