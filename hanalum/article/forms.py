from django import forms
from .models import Article
from .models import Comment
from ckeditor.widgets import CKEditorWidget


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'file_1', 'file_2', 'file_3']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목'}),
            'content': CKEditorWidget(),
            'file_1': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'file_2': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'file_3': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }

    def save(self, **kwargs):
        # 비밀번호를 해시 상태로 저장
        article = super().save(commit=False)
        article.pub_user = kwargs.get('pub_user')
        article.board_type = kwargs.get('board_type')
        article.save()
        return article.pk


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 입력하십시오', 'class': 'form-control mb-2',})
        }
        labels = {
            'content': '댓글 작성'
        }

    def save(self, **kwargs):
        # 비밀번호를 해시 상태로 저장
        comment = super().save(commit=False)
        comment.article_type = kwargs.get('article_type')
        comment.pub_user = kwargs.get('pub_user')
        comment.save()
        return comment.pk
