
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
    id = models.BigAutoField(primary_key=True)
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
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    phone_num = models.CharField(max_length=20)
    real_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    id_card = models.CharField(max_length=18)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.SmallIntegerField()
    status = models.IntegerField()
    avatar = models.ForeignKey('UploadAvatarImage', models.DO_NOTHING, blank=True, null=True)

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


class CrmAreas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', models.DO_NOTHING)
    code = models.CharField(max_length=20)
    level = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'crm_areas'


class CrmCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    qq = models.CharField(max_length=255)
    wechat = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    tel = models.CharField(max_length=255)
    address = models.ForeignKey(CrmAreas, models.DO_NOTHING)
    create_account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop = models.ForeignKey('CrmShop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_customer'


class CrmFollowup(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    follow_way = models.SmallIntegerField()
    follow_time = models.DateTimeField(blank=True, null=True)
    follow_next_time = models.DateTimeField(blank=True, null=True)
    chat_record = models.TextField(blank=True, null=True)
    follow_description = models.CharField(max_length=255, blank=True, null=True)
    marking = models.SmallIntegerField()
    intentional = models.IntegerField()
    estimated_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estimated_date = models.DateField(blank=True, null=True)
    sales_stage = models.SmallIntegerField()
    cooperative_business_type = models.ForeignKey('CrmProductType', models.DO_NOTHING)
    follow_account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    order = models.ForeignKey('CrmOrder', models.DO_NOTHING)
    shop = models.ForeignKey('CrmShop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_followup'


class CrmFollowupChatDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    followupmodel = models.ForeignKey(CrmFollowup, models.DO_NOTHING)
    followupdocumentmodel = models.ForeignKey('UploadFollowupDocument', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_followup_chat_document'
        unique_together = (('followupmodel', 'followupdocumentmodel'),)


class CrmFollowupChatRecording(models.Model):
    id = models.BigAutoField(primary_key=True)
    followupmodel = models.ForeignKey(CrmFollowup, models.DO_NOTHING)
    recordingmodel = models.ForeignKey('UploadFollowupRecording', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_followup_chat_recording'
        unique_together = (('followupmodel', 'recordingmodel'),)


class CrmFollowupChatScreenshot(models.Model):
    id = models.BigAutoField(primary_key=True)
    followupmodel = models.ForeignKey(CrmFollowup, models.DO_NOTHING)
    screenshotmodel = models.ForeignKey('UploadFollowupImage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_followup_chat_screenshot'
        unique_together = (('followupmodel', 'screenshotmodel'),)


class CrmFollowupComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    reason = models.CharField(max_length=255)
    account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop = models.ForeignKey(CrmFollowup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_followup_comment'


class CrmFollowupReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.SmallIntegerField()
    reason = models.CharField(max_length=255)
    account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop = models.ForeignKey(CrmFollowup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_followup_review'


class CrmOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    transaction_type = models.IntegerField()
    order_num = models.CharField(max_length=255)
    settlement_order_num = models.CharField(max_length=255)
    invoice_num = models.CharField(max_length=255)
    invoice_top_num = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    des_effect = models.TextField()
    cooperation_cycle = models.IntegerField(blank=True, null=True)
    founder = models.ForeignKey(AuthUser, models.DO_NOTHING)
    order_contract = models.ForeignKey('UploadOrderDocument', models.DO_NOTHING, blank=True, null=True)
    order_pic = models.ForeignKey('UploadOrderImage', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('CrmPayment', models.DO_NOTHING)
    product = models.ForeignKey('CrmProductProduct', models.DO_NOTHING)
    shop = models.ForeignKey('CrmShop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_order'


class CrmOrderCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordermodel = models.ForeignKey(CrmOrder, models.DO_NOTHING)
    customermodel = models.ForeignKey(CrmCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_order_customer'
        unique_together = (('ordermodel', 'customermodel'),)


class CrmOrderGiveaway(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordermodel = models.ForeignKey(CrmOrder, models.DO_NOTHING)
    giveawaymodel = models.ForeignKey('CrmProductGiveaway', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_order_giveaway'
        unique_together = (('ordermodel', 'giveawaymodel'),)


class CrmOrderReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.SmallIntegerField()
    reason = models.CharField(max_length=255)
    account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop = models.ForeignKey(CrmOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_order_review'


class CrmPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    channel = models.CharField(max_length=255)
    name = models.TextField()
    method = models.CharField(max_length=255)
    remark = models.TextField()
    hide = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crm_payment'


class CrmProductGiveaway(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crm_product_giveaway'


class CrmProductPlatform(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crm_product_platform'


class CrmProductProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    charging_type = models.IntegerField()
    unified_price_year = models.DecimalField(max_digits=20, decimal_places=2)
    minimum_price_year = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unified_price_half_year = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    minimum_price_half_year = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unified_price_quarter = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    minimum_price_quarter = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unified_price_month = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    minimum_price_month = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    hide = models.IntegerField()
    contract_file = models.ForeignKey('UploadProductDocument', models.DO_NOTHING)
    platform = models.ForeignKey(CrmProductPlatform, models.DO_NOTHING)
    type = models.ForeignKey('CrmProductType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_product_product'


class CrmProductProductGiveaway(models.Model):
    id = models.BigAutoField(primary_key=True)
    productmodel = models.ForeignKey(CrmProductProduct, models.DO_NOTHING)
    giveawaymodel = models.ForeignKey(CrmProductGiveaway, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_product_product_giveaway'
        unique_together = (('productmodel', 'giveawaymodel'),)


class CrmProductProductServiceTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    productmodel = models.ForeignKey(CrmProductProduct, models.DO_NOTHING)
    servicetimemodel = models.ForeignKey('CrmProductServiceTime', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_product_product_service_time'
        unique_together = (('productmodel', 'servicetimemodel'),)


class CrmProductServiceTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    service_price = models.DecimalField(max_digits=20, decimal_places=2)
    service_minimum_price = models.DecimalField(max_digits=20, decimal_places=2)
    service_times = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_product_service_time'


class CrmProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crm_product_type'


class CrmSalesStage(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stage_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crm_sales_stage'


class CrmShop(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(unique=True, max_length=255)
    url = models.CharField(max_length=1024)
    product_quantity = models.IntegerField(blank=True, null=True)
    cumulative_sales = models.IntegerField(blank=True, null=True)
    sales = models.DecimalField(max_digits=15, decimal_places=2)
    shop_opening_time = models.DateField(blank=True, null=True)
    locked = models.IntegerField()
    lock_time = models.DateTimeField(blank=True, null=True)
    followup_method = models.SmallIntegerField()
    platform = models.SmallIntegerField()
    is_close = models.IntegerField()
    category = models.ForeignKey('CrmShopStoreCategory', models.DO_NOTHING)
    create_person = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop_own = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_shop'


class CrmShopComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    reason = models.CharField(max_length=255)
    account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop = models.ForeignKey(CrmShop, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_shop_comment'


class CrmShopReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.SmallIntegerField()
    reason = models.CharField(max_length=255)
    account = models.ForeignKey(AuthUser, models.DO_NOTHING)
    shop = models.ForeignKey(CrmShop, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_shop_review'


class CrmShopStoreCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_shop_store_category'


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


class SoftdeleteChangeset(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField()
    object_id = models.CharField(max_length=100)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'softdelete_changeset'


class SoftdeleteSoftdeleterecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField()
    object_id = models.CharField(max_length=100)
    changeset = models.ForeignKey(SoftdeleteChangeset, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'softdelete_softdeleterecord'
        unique_together = (('changeset', 'content_type', 'object_id'),)


class SysRegion(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.CharField(max_length=10, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_region'


class UploadAvatarImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_avatar_image'


class UploadFollowupDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_followup_document'


class UploadFollowupImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_followup_image'


class UploadFollowupRecording(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_followup_recording'


class UploadOrderDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_order_document'


class UploadOrderImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_order_image'


class UploadProductDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_product_document'
