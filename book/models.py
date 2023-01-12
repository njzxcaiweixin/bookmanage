# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bookinfo(models.Model):
    bname = models.CharField(max_length=255, blank=True, null=True, verbose_name='书名')
    author = models.CharField(max_length=255, blank=True, null=True, verbose_name='作者')
    pub = models.CharField(max_length=255, blank=True, null=True, verbose_name='出版社')
    pubdate = models.DateTimeField(blank=True, null=True, verbose_name='出版日期')
    bread = models.IntegerField(blank=True, null=True, verbose_name='阅读量')
    isdelete = models.IntegerField(blank=True, null=True, verbose_name='删除标识')
    bsid = models.ForeignKey('Bookshop', models.DO_NOTHING, db_column='bsid', blank=True, null=True,
                             verbose_name='所在书店')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='价格')

    class Meta:
        # managed = False
        #改表名
        db_table = 'bookinfo'
        #修改后admin后台显示信息配置
        verbose_name = '书名'
        verbose_name_plural = '书名'

    def __str__(self) -> str:
        return self.bname


class Bookshop(models.Model):
    bsname = models.CharField(max_length=255, blank=True, null=True, verbose_name='书店名称')
    bookid = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'bookshop'
        verbose_name = '书店'
        verbose_name_plural = '书店'

    def __str__(self) -> str:
        return self.bsname


class District(models.Model):
    name = models.CharField(max_length=32, verbose_name='地区名')
    level = models.IntegerField(verbose_name='层级')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='所属地区')

    class Meta:
        # managed = False
        db_table = 'district'
        verbose_name = '地区'
        verbose_name_plural = '地区'

        def __str__(self) -> str:
            return self.name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Figure(models.Model):
    fname = models.CharField(max_length=255, blank=True, null=True, verbose_name='姓名')
    gender = models.CharField(max_length=10, blank=True, null=True, verbose_name='性别')
    zhiye = models.CharField(max_length=255, blank=True, null=True, verbose_name='zhiye ')
    age = models.IntegerField(blank=True, null=True, verbose_name='年龄')
    wenhua = models.CharField(max_length=255, blank=True, null=True, verbose_name='文化程度')
    bid = models.ForeignKey(Bookinfo, models.DO_NOTHING, db_column='bid', blank=True, null=True, verbose_name='所属书籍')

    def __str__(self) -> str:
        return self.fname

    class Meta:
        # managed = False
        db_table = 'figure'
        verbose_name = '人物'
        verbose_name_plural = '人物'
