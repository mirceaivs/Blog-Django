from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

all_posts = [
{
    "slug": "playing-games",
    "image": "World_of_Warcraft.jpg",
    "author": "Mircea",
    "date": date(2023, 7, 21),
    "title": "Playing games",
    "excerpt": "There's nothing like the lorem ipsum",
    "content": """
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
    """
},
{
    "slug": "coding",
    "image": "coding.jpg",
    "author": "Mircea",
    "date": date(2023, 7, 22),
    "title": "Coding",
    "excerpt": "There's nothing like the lorem ipsum",
    "content": """
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
    """
},
{
    "slug": "nature-at-its-best",
    "image": "woods.jpg",
    "author": "Mircea",
    "date": date(2023, 7, 11),
    "title": "Nature at its best",
    "excerpt": "There's nothing like the lorem ipsum",
    "content": """
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
    """
},
{
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Mircea",
    "date": date(2023, 7, 1),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the lorem ipsum",
    "content": """
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
     Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae distinctio iure consequuntur vel nesciunt accusamus itaque sunt et consectetur unde. Dolorem deleniti 
            adipisci consequatur at inventore 
            soluta fugit. Eligendi, earum.
    """
}
]

def get_date(all_post):
    return all_post["date"]

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    # for i in latest_posts:
    #     print(i["date"])
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):   
    return render(request, "blog/all-posts.html",{
    "posts":all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']== slug)
    return render(request, "blog/post-detail.html", {
        "post":identified_post
                  })
