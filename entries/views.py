from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry, Comment
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def like_post(request, id):
    entry = Entry.objects.get(id=id)
    entry.likes.add(request.user.id)
    #return HttpResponseRedirect('/detail/{% entry.id %}')
    url = '/detail/' + str(entry.id)
    print(url)
    return HttpResponseRedirect(url)


def index(request):
    entries = Entry.objects.all().order_by("-id")
    paginator = Paginator(entries, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def detail(request, id):
    entry = Entry.objects.get(id=id)
    entry_likes = entry.likes.count()
    comments = Comment.objects.filter(comment_entry_id=id)
    context = {}
    context['entry'] = entry
    context['entry_likes'] = entry_likes
    context['comments'] = comments
    return render(request, 'detail.html', {"context": context})

@login_required
def add_post(request):
    if request.POST:
        form = EntryForm(request.POST, request.FILES)#这样接收关联文件
    else:
        form = EntryForm()# 有格式有数据的form
    if form.is_valid():# 校验 调用form的clean函数
        obj = form.save(commit=False)
        obj.entry_author = request.user
        obj.save()# 有格式有数据的form save 就把数据保存到数据库
        return redirect('/')
    form = EntryForm()  # 有格式没数据的form
    return render(request, 'add.html', {'form': form})