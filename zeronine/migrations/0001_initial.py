# Generated by Django 3.1.5 on 2021-11-16 23:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='아이디')),
                ('name', models.CharField(default='', max_length=20, verbose_name='이름')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('phone', models.CharField(max_length=64, verbose_name='전화번호')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['category_code'],
            },
        ),
        migrations.CreateModel(
            name='Designated',
            fields=[
                ('designated_code', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('rep_price', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['designated_code'],
            },
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('join_code', models.AutoField(primary_key=True, serialize=False)),
                ('part_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['join_code'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['option_code'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('benefit', models.TextField()),
                ('detail', models.TextField()),
                ('target_price', models.IntegerField()),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kakao_link', models.CharField(default='', max_length=200)),
                ('category_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='zeronine.category')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['product_code'],
                'index_together': {('product_code', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Zzim',
            fields=[
                ('zzim_code', models.AutoField(primary_key=True, serialize=False)),
                ('product_code', models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.product')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['zzim_code'],
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('value_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('extra_cost', models.CharField(blank=True, max_length=32, null=True)),
                ('option_code', models.ForeignKey(blank=True, db_column='option_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='zeronine.option')),
                ('product_code', models.ForeignKey(blank=True, db_column='product_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='zeronine.product')),
            ],
            options={
                'ordering': ['value_code'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_code', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['post_code'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_code', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='photos/%Y%m%d')),
                ('product_code', models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.product')),
            ],
            options={
                'ordering': ['photo_code'],
            },
        ),
        migrations.AddField(
            model_name='option',
            name='product_code',
            field=models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.CASCADE, related_name='option', to='zeronine.product'),
        ),
        migrations.CreateModel(
            name='JoinDetail',
            fields=[
                ('joindetail_code', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=300)),
                ('designated_code', models.ForeignKey(blank=True, db_column='designated_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='zeronine.designated')),
                ('join_code', models.ForeignKey(db_column='join_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.join')),
                ('value_code', models.ForeignKey(blank=True, db_column='value_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='zeronine.value')),
            ],
            options={
                'ordering': ['joindetail_code'],
            },
        ),
        migrations.AddField(
            model_name='join',
            name='product_code',
            field=models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.product'),
        ),
        migrations.AddField(
            model_name='join',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('element_code', models.AutoField(primary_key=True, serialize=False)),
                ('designated_code', models.ForeignKey(db_column='designated_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.designated')),
                ('value_code', models.ForeignKey(blank=True, db_column='value_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='zeronine.value')),
            ],
            options={
                'ordering': ['element_code'],
            },
        ),
        migrations.AddField(
            model_name='designated',
            name='product_code',
            field=models.ForeignKey(db_column='product_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.product'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_code', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('post_code', models.ForeignKey(db_column='post_code', on_delete=django.db.models.deletion.CASCADE, to='zeronine.post')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['register_date'],
            },
        ),
    ]
