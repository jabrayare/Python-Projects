from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


from post.models import Post


from .form import PostForm, RawProductForm


# This let's users post form to the database.


# def post_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         # Validates data
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # Now the data is clearn.
#             print(my_form.cleaned_data)
#             Post.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)

#     my_context = {
#         "form": my_form
#     }
#     return render(request, "posts/post_form.html", my_context)


# def post_create_view(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = PostForm()
#     my_context = {
#         "form": form
#     }
#     return render(request, "posts/post_form.html", my_context)

# It looks up the data in the database. It renders a new page everytime the id changes.
def dynamic_lookup_view(request, my_id):
    #obj = Post.objects.get(id=my_id)
    # It raised page not found error if the url is not found.
    obj = get_object_or_404(Post, id=my_id)
    # This try and except block all raised page not found
    # try:
    #     obj = Post.objects.get(id=my_id)
    # except Post.DoesNotExist:
    #     raise Http404
    my_context = {
        "obj": obj
    }
    return render(request, "posts/post_form.html", my_context)


def post_delete_view(request, my_id):
    obj = get_object_or_404(Post, id=my_id)
    # confirming delete mthod
    if request.method == "POST":
        obj.delete()
        # redirecting to another url when an Item is deleted from the database
        return redirect('../../../')
    my_context = {
        "obj": obj
    }
    return render(request, "posts/post_delete.html", my_context)


def post_listItem_view(request):
    queryset = Post.objects.all()
    my_context = {
        "items": queryset
    }
    return render(request, "posts/detail.html", my_context)
# def post_details_view(request):
#     obj = Post.objects.get(id=1)
#     # my_context = {
#     #     "name": obj.Name,
#     #     "email": obj.Email,
#     #     "message": obj.Message,

#     # }
#     my_context = {
#         "object": obj

#     }
#     return render(request, "Posts/detail.html", my_context)

# Form validations.
