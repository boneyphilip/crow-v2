import json

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from cloudinary.exceptions import BadRequest

from .forms import CommentForm, PostForm
from .models import Category, Comment, Post, PostMedia, Vote


def home(request):
    """Render the home feed and optionally handle post creation."""
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            if request.user.is_authenticated:
                post.author = request.user
            else:
                post.author = User.objects.first()

            post.created_at = timezone.now()

            category_name = request.POST.get("category", "").strip()
            if category_name:
                category, _ = Category.objects.get_or_create(
                    name=category_name
                )
                post.category = category

            post.save()
            messages.success(
                request,
                "Your post has been shared successfully!",
            )
            return redirect("home")

        messages.error(request, "Please correct the errors in the form.")

    query = request.GET.get("q", "").strip()
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by(
            "-created_at"
        )
    else:
        posts = Post.objects.all().order_by("-created_at")

    for post in posts:
        post.user_vote_value = post.user_vote(request.user)

    return render(
        request,
        "posts/home.html",
        {
            "form": form,
            "posts": posts,
        },
    )


@login_required
def create_post(request):
    """Create a new post with optional media uploads."""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        category_name = request.POST.get("category", "").strip()

        if not title or not content:
            messages.error(request, "Title and content are required.")
            return redirect("create_post")

        category = None
        if category_name:
            category, _ = Category.objects.get_or_create(
                name=category_name
            )

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            category=category,
        )

        try:
            for image_file in request.FILES.getlist("images"):
                if image_file and getattr(image_file, "size", 0) > 0:
                    PostMedia.objects.create(post=post, file=image_file)

            video_file = request.FILES.get("video")
            if video_file and getattr(video_file, "size", 0) > 0:
                PostMedia.objects.create(post=post, file=video_file)

            for source_file in request.FILES.getlist("sources"):
                if source_file and getattr(source_file, "size", 0) > 0:
                    PostMedia.objects.create(post=post, file=source_file)

        except BadRequest:
            post.delete()
            messages.error(
                request,
                (
                    "One of the uploaded files was empty or invalid. "
                    "Please try again."
                ),
            )
            return redirect("create_post")

        messages.success(request, "Post created successfully.")
        return redirect("create_post")

    return render(request, "posts/create_post.html")


def post_detail(request, post_id):
    """Display a single post."""
    post = get_object_or_404(Post, id=post_id)
    post.user_vote_value = post.user_vote(request.user)
    return render(request, "posts/post_detail.html", {"post": post})


@login_required
def vote_post(request, post_id):
    """Handle vote toggle and switching through AJAX."""
    if request.method != "POST":
        return JsonResponse(
            {"success": False, "error": "Invalid method"},
            status=405,
        )

    post = get_object_or_404(Post, id=post_id)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse(
            {"success": False, "error": "Bad JSON"},
            status=400,
        )

    action = data.get("action")
    if action not in ("upvote", "downvote"):
        return JsonResponse(
            {"success": False, "error": "Invalid action"},
            status=400,
        )

    value = 1 if action == "upvote" else -1

    vote, created = Vote.objects.get_or_create(
        user=request.user,
        post=post,
        defaults={"value": value},
    )

    if not created:
        if vote.value == value:
            vote.delete()
        else:
            vote.value = value
            vote.save()

    return JsonResponse(
        {
            "success": True,
            "score": post.get_score(),
            "user_vote": post.user_vote(request.user),
        }
    )


@login_required
def add_comment(request, post_id):
    """Add a comment to a post."""
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()

        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content,
            )
            messages.success(request, "Comment added successfully.")
        else:
            messages.error(request, "Comment content cannot be empty.")

    return redirect("post_detail", post_id=post_id)


@login_required
def reply_comment(request, comment_id):
    """Reply to an existing comment."""
    parent = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()

        if content:
            Comment.objects.create(
                post=parent.post,
                author=request.user,
                content=content,
                parent=parent,
            )
            messages.success(request, "Reply added successfully.")
        else:
            messages.error(request, "Reply content cannot be empty.")

    return redirect("post_detail", post_id=parent.post.id)


@login_required
def delete_comment(request, comment_id):
    """Delete a comment if the current user is the author."""
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return HttpResponseForbidden()

    post_id = comment.post.id
    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect("post_detail", post_id=post_id)


@login_required
def edit_comment(request, comment_id):
    """Edit a comment using a Django ModelForm."""
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect("post_detail", post_id=comment.post.id)

        messages.error(request, "Please correct the errors below.")
    else:
        form = CommentForm(instance=comment)

    return render(
        request,
        "posts/edit_comment.html",
        {
            "comment": comment,
            "form": form,
        },
    )


@login_required
def edit_post(request, post_id):
    """Edit a post using a Django ModelForm."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect("post_detail", post_id=post.id)

        messages.error(request, "Please correct the errors below.")
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/edit_post.html",
        {
            "post": post,
            "form": form,
        },
    )


@login_required
def delete_post(request, post_id):
    """Delete a post if the current user is the author."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("home")

    return render(request, "posts/delete_post.html", {"post": post})


def register_user(request):
    """Register a new user."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "posts/register.html", {"form": form})


def ajax_search(request):
    """Return matching posts/authors as JSON for live search."""
    query = request.GET.get("q", "").strip()
    if not query:
        return JsonResponse({"results": []})

    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query)
    ).select_related("author")

    results = []
    for post in posts:
        thumbnail = None
        if post.media.exists() and post.media.first().is_image():
            thumbnail = post.media.first().file.url

        results.append(
            {
                "id": post.id,
                "title": post.title,
                "author": post.author.username,
                "thumb": thumbnail,
            }
        )

    return JsonResponse({"results": results})


def profile_page(request, username):
    """Display a user's profile page."""
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=profile_user).order_by("-created_at")

    return render(
        request,
        "posts/profile.html",
        {
            "profile_user": profile_user,
            "posts": posts,
        },
    )


def category_search(request):
    """Return matching categories as JSON."""
    query = request.GET.get("q", "").strip()
    if not query:
        return JsonResponse({"results": []})

    categories = Category.objects.filter(name__icontains=query)[:6]
    return JsonResponse(
        {"results": [category.name for category in categories]}
    )
