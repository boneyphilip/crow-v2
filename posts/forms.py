from django import forms

from .models import Category, Comment, Post


class PostForm(forms.ModelForm):
    """Form used for creating and editing posts."""

    class Meta:
        model = Post
        fields = ["title", "content", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a clear post title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Write your post content here",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
        labels = {
            "title": "Title",
            "content": "Content",
            "category": "Category",
        }

    def __init__(self, *args, **kwargs):
        """Order categories cleanly and keep category optional."""
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.order_by("name")
        self.fields["category"].required = False

    def clean_title(self):
        """Validate and normalise the title field."""
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Title is required.")
        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long."
            )
        return title

    def clean_content(self):
        """Validate and normalise the content field."""
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise forms.ValidationError("Content is required.")
        if len(content) < 3:
            raise forms.ValidationError(
                "Content must be at least 3 characters long."
            )
        return content


class CommentForm(forms.ModelForm):
    """Form used for editing comments."""

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Edit your comment",
                }
            ),
        }
        labels = {
            "content": "Comment",
        }

    def clean_content(self):
        """Validate and normalise the comment content."""
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise forms.ValidationError("Comment content is required.")
        if len(content) < 2:
            raise forms.ValidationError(
                "Comment must be at least 2 characters long."
            )
        return content
