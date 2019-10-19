from django.shortcuts import render
from .models import Article,Category,Tag

# Create your views here.
def index(request):
    # 对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all()
    allcategory = Category.objects.all()
    # 把查询到的对象，封装到上下文
    context = {
        'allarticle': allarticle,
        'allcategory': allcategory,
    }
    # 把上传文传到模板页面index.html里
    return render(request, 'index.html', context)

def blog(request):
    # 对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all()
    allcategory = Category.objects.all()
    # 把查询到的对象，封装到上下文
    context = {
        'allarticle': allarticle,
        'allcategory': allcategory,
    }
    # 把上传文传到模板页面index.html里
    return render(request, 'blog.html', context)
#文章列表
def list(request,lid):
    # list = Article.objects.filter(filter=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    # cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    # remen = Article.objects.filter(tui__id=2)[:6]#右侧的热门推荐
    # allcategory = Category.objects.all()#导航所有分类
    # tags = Tag.objects.all()#右侧所有文章标签
    # return render(request, 'list.html', locals())
    # 把查询到的对象，封装到上下文
    cname = Category.objects.get(id=lid)
    lists = Article.objects.filter(id=lid)
    articles = Article.objects.filter(category_id=lid)
    context = {
        'lid': lid,
        'lists':lists,
        'cname':cname,
        'articles':articles
    }
    # 把上传文传到模板页面index.html里
    # return render(request, 'list.html', context)
    return render(request, 'list.html', locals())

def show(request,sid):
    # show = Article.objects.get(id=sid)#查询指定ID的文章
    allcategory = Category.objects.all()#导航上的分类
    # tags = Tag.objects.all()#右侧所有标签
    # remen = Article.objects.filter(tui__id=2)[:6]#右侧热门推荐
    # hot = Article.objects.all().order_by('?')[:10]#内容下面的您可能感兴趣的文章，随机推荐
    # previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    # netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    # show.views = show.views + 1
    # show.save()
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    context = {
        'sid': sid,
        'show':show,
        'allcategory':'allcategory',
    }
    return render(request, 'show.html', locals())