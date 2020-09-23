from django.db import models
from django.contrib.auth.models import User

# 데이타베이스 테이블 생성 정보 및 dto(vo) 역할 
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # 객체 표현 양식 
    def __str__(self):
        return self.title
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()