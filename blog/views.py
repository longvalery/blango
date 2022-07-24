from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import CommentForm
import logging
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.vary import vary_on_headers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create your views here.
# cache  5 minute

#@cache_page(300)
## @vary_on_headers("Cookie")
#@vary_on_cookie
def index(request):

    #return HttpResponse(str(request.user).encode("ascii"))
    logger.log(logging.DEBUG, "datetime.now() : %s", datetime.now())
    #posts = Post.objects.filter(created_at__lte=datetime.now())
    posts = Post.objects.filter(created_at__lte=timezone.now()).select_related("author") \
    #   .only("title", "summary", "content", "author", "published_at", "slug")
    #    .defer("created_at", "modified_at")

    ##posts = Post.objects.all
    cnt = posts.count()
    ## cnt = Post.objects.all().count()
    ## print("posts",type(posts),"", cnt)

    logger.debug("Got %d posts", cnt)
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
)
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )    
    
def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])