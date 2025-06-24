from django.shortcuts import render, redirect, get_object_or_404

from .models import TodoItem


def todo_list(request):
    items = TodoItem.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/todo_list.html', {'items': items})


def toggle_complete(request, item_id):
    item = get_object_or_404(TodoItem, pk=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('todo_list')
