from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from comment.models import Comment
from django.template.loader import render_to_string


class Link(models.Model):
    STATUS_NORMAL = 1  # 状态正常
    STATUS_DELETE = 0  # 删除状态
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )
    title = models.CharField(max_length=255, verbose_name='标题', default='')
    href = models.URLField(verbose_name="链接", default='')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name='权重',
                                         help_text="权重高展示顺序靠前")

    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING,related_name='config_Tag_owner')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '友链'

class SideBar(models.Model):   #侧边栏
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )
    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4
    SIDE_TYPE = (
        (DISPLAY_HTML, 'HTML'),
        (DISPLAY_LATEST, '最新文章'),
        (DISPLAY_HOT, '最热文章'),
        (DISPLAY_COMMENT, '最新评论')
    )

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        result = ''
        if self.display_type ==self.DISPLAY_HTML:
            result = self.content
        elif self.display_type == self.DISPLAY_LATEST:
            context = {
                'posts': Post.latest_post()
            }
            result = render_to_string('config/block/sidebar_posts.html', context=context)
        elif self.display_type == self.DISPLAY_HOT:
            context = {
                'posts': Post.hot_post()
            }
            result = render_to_string('config/block/sidebar_posts.html', context=context)
        elif self.display_type == self.DISPLAY_COMMENT:
            context = {
                'comments': Comment.objects.filter(status=Comment.STATUS_NORMAL)
            }
            result = render_to_string('config/block/sidebar_comments.html', context=context)
        return result

    title = models.CharField(max_length=50, verbose_name='标题')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='展示类型')
    content = models.TextField(verbose_name='正文', blank=True, help_text='如果设置的不是HTML类型，可为空')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING, related_name='config_Post_owner')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')



    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'