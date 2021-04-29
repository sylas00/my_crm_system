#存在问题
索引设置 单条索引和联合索引

#笔记
on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
on_delete=models.SET,         # 删除关联数据,
 a. 与之关联的值设置为指定值,设置：models.SET(值)
 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)

模型字段类型：
models.CharField() # 字符串类型
models.TextField() # 文本类型
models.IntegerField() # int类型
models.BooleanField() # bool类型
models.NullBooleanField() # 允许为空的bool类型
models.DateField() # 日期类型 年月日
models.DecimalField() # 金额类型 可以指定ForeignKey长度和小数位数 max_digits=15, decimal_places=2, 总长度15位，小数位为2
models.EmailField() # 邮箱类型
models.FloatField() # 浮点数类型
models.TimeField() # 时间类型
models.ForeignKey(OtherModel, on_delete=models.PROTECT, verbose_name='label', related_name='related_name') # 外键类型
models.OneToOneField(OtherModel, on_delete=models.PROTECT, verbose_name='label', related_name='related_name') # 一对一的外键类型

模型常用options：
null = True # 允许值为空
blank = True # 允许键为空，指定的字段可以不传
choices = ((0,'男'),('1','女'),) # 选项类型
default = 1 # 指定默认值
verbose_name = '描述' # 指定label 或字段描述
auto_now_add = True # 在创建的时候插入时间
auto_now = True # 每次修改都会更新时间
max_length = 255 # 指定字段容量长度，CharField必须要指定

mixins.CreateModelMixin	    create   POST	  创建数据
mixins.RetrieveModelMixin	retrieve GET	  检索数据
mixins.UpdateModelMixin	    update   PUT	  更新数据
                            perform_update PATCH 更新数据
mixins.DestroyModelMixin	destroy  DELETE	  删除数据


django-softdelete
delete() 标记
undelete 恢复
再delete 硬删除
