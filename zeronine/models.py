from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# 회원
class Member(AbstractUser):
    username = models.CharField(primary_key=True, max_length=20, verbose_name='아이디')
    name = models.CharField(max_length=20, verbose_name='이름', default='')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    phone = models.CharField(max_length=64, verbose_name='전화번호')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ('Member')
        verbose_name_plural = ('Members')

# 카테고리
class Category(models.Model):
    category_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True)

    class Meta:
        ordering =['category_code']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zeronine:product_in_category', args=[self.slug])

# 상품
class Product(models.Model):
    product_code = models.AutoField(primary_key=True)
    username = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='username')
    category_code = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=False, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    benefit = models.TextField()
    detail = models.TextField()
    target_price = models.IntegerField()
    start_date = models.DateField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    kakao_link = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ['product_code']
        index_together = [['product_code', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zeronine:product_detail', args=[self.product_code, self.slug])

    def get_total(self):
        join_list = list(JoinDetail.objects.filter(join_code__product_code_id=self.product_code).values_list('price', flat=True))
        total_price = sum(list(filter(None, join_list)))
        return total_price

    def option_exists(self):
        options = self.option.all()
        if options.exists():
            return True
        else:
            return False

# 게시글
class Post(models.Model):
    post_code = models.AutoField(primary_key=True)
    username = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='username')
    title = models.CharField(max_length=64)
    content = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['post_code']

# 댓글(댓글코드, 게시글코드(fk), 아이디(fk), 내용, 등록날짜)
class Comment(models.Model):
    comment_code = models.AutoField(primary_key=True)
    post_code = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_code')
    username = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='username')
    content = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['register_date']

# 찜하기(찜코드, 아이디(fk), 상품코드(fk))
class Zzim(models.Model):
    zzim_code = models.AutoField(primary_key=True)
    username = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='username')
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_code')

    def __str__(self):
        return str(self.zzim_code)

    class Meta:
        ordering = ['zzim_code']

# 상품이미지(이미지코드, 상품코드(fk), 이미지경로)
class Photo(models.Model):
    photo_code = models.AutoField(primary_key=True)
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_code')
    photo = models.ImageField(upload_to="photos/%Y%m%d")

    def __str__(self):
        return str(self.photo_code)

    class Meta:
        ordering = ['photo_code']


# 옵션(옵션코드, 옵션명, 상품코드(fk))
class Option(models.Model):
    option_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_code', related_name='option')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['option_code']

# 옵션값(옵션값코드, 옵션값명, 옵션코드(fk), 상품코드(fk))
class Value(models.Model):
    value_code = models.AutoField(primary_key=True)
    option_code = models.ForeignKey(Option, on_delete=models.CASCADE, db_column='option_code', null=True, blank=True)
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_code', null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    extra_cost = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['value_code']

# 옵션지정상품(옵션지정상품코드, 상품코드(fk), 가격, 참여수량)
class Designated(models.Model):
    designated_code = models.AutoField(primary_key=True)
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_code')
    price = models.IntegerField()
    rep_price = models.BooleanField(default=True)

    class Meta:
        ordering = ['designated_code']

    def __str__(self):
        return str(self.designated_code)

# 상품옵션구성(상품옵션구성코드, 옵션지정상품코드, 옵션값코드)
class Element(models.Model):
    element_code = models.AutoField(primary_key=True)
    designated_code = models.ForeignKey(Designated, on_delete=models.CASCADE, db_column='designated_code')
    value_code = models.ForeignKey(Value, on_delete=models.CASCADE, db_column='value_code', null=True, blank=True)

    class Meta:
        ordering = ['element_code']

    def __str__(self):
        return str(self.element_code)

# 참여(참여코드, 아이디(fk), 상품코드(fk), 수량)
class Join(models.Model):
    join_code = models.AutoField(primary_key=True)
    username = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='username')
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_code')
    part_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.join_code)

    class Meta:
        ordering = ['join_code']

#참여상세(참여상세코드, 수량, 가격, 참여코드, 옵션지정상품코드)
class JoinDetail(models.Model):
    joindetail_code = models.AutoField(primary_key=True)
    join_code = models.ForeignKey(Join, on_delete=models.CASCADE, db_column='join_code')
    value_code = models.ForeignKey(Value, on_delete=models.CASCADE, db_column='value_code', null=True, blank=True)
    designated_code = models.ForeignKey(Designated, on_delete=models.CASCADE, null=True, blank=True, db_column='designated_code')
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=64, db_column='name')
    phone = models.CharField(max_length=64, db_column='phone')
    address = models.CharField(max_length=300, db_column='address')

    def __str__(self):
        return str(self.joindetail_code)

    class Meta:
        ordering = ['joindetail_code']
