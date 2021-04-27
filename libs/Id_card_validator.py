from django.core.exceptions import ValidationError


# 自定义身份证字段验证器
def id_validator(value):
    # 身份证号码验证
    wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ti = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    sum_num = 0
    value = value.upper()
    if len(value) != 18:
        # raise serializers.ValidationError('请输入18位身份证号码,您只输入了%s位' % len(value))
        raise ValidationError('请输入18位身份证号码,您只输入了%s位' % len(value))
    for i in range(17):
        sum_num += int(value[i]) * wi[i]
    if ti[sum_num % 11] != value[17]:
        # raise serializers.ValidationError('请输入正确的身份证号码')
        raise ValidationError('请输入正确的身份证号码')
