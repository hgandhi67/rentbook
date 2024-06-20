from datetime import *
from django.urls import reverse
import requests


from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from urllib.parse import quote
from book_rent_task.models import *
from django.db.models import Count
from django.utils import timezone

# Create your views here.
def create_user(request):
  if request.method =='POST':
    print("asjhdbajkhsn",request.POST.get('fname'))
    print("in post")
    first_name_ui = request.POST.get('fname')
    last_name_ui = request.POST.get('lname')
    username_ui = request.POST.get('uname')
    email_ui = request.POST.get('email')
    password_ui = request.POST.get('pwd')
    con_password_ui = request.POST.get('conpwd')
    print(first_name_ui,last_name_ui,email_ui,username_ui,con_password_ui)
    
    if not first_name_ui or not last_name_ui or not username_ui or not email_ui or not password_ui or not con_password_ui:
      return render(request, 'signup.html', {'error': 'Please fill all the fields'})
    
    if con_password_ui != password_ui:
      return render(request, 'signup.html', {'error': 'conform password is not matching'})
    
    print("in post")
    User.objects.create_user(first_name = first_name_ui,last_name = last_name_ui  ,email = email_ui ,username = username_ui , password = password_ui)
    # return render(request, "signup.html",{"data":"hello"})


  return render(request, "signup.html",{"data":"hello"})



def open_signin(request):
  return render(request, "login.html")


def singin(request):
  if request.method =='POST':
    print("asjhdbajkhsn",request.POST.get('fname'))
    print("in post")
    username_ui = request.POST.get('uname')
    password_ui = request.POST.get('pwd')
    print(username_ui,password_ui)
    try:
      user_super = User.objects.get(username = username_ui)
    except:
      return render(request, 'login.html', {'error': 'User does not exist'})
    
      
    
    if not password_ui or not password_ui:
      
      return render(request, 'login.html', {'error': 'Please fill all the fields'})
    
    user = authenticate(request , username = username_ui, password = password_ui)
    
    if not user:
      print("user",user)
      return render(request, "login.html",{"error":"user name or password is not valid"})
    
    else:
      if user_super.is_superuser==True:
        login(request, user)
        return redirect("dashboard")
      else:
        login(request, user)
        return redirect("load_view")
    # print("in post")
    # return render(request, "signup.html",{"data":"hello"})
  else:
    return redirect('load_view')


def load_page(request):
  user = User.objects.get(username = request.user)
  user_books = rental_books_user.objects.filter(user=user.id)

  available_books = [ub.book for ub in user_books if not ub.access_expired()]
  print("available_books",available_books)

  return render(request,'show_rental_books.html',{"bookdata": available_books})

# def search_book(request):
#     print("Request method:", request.method)
#     if request.method == 'POST':
#         return render(request, "show_book.html", {"message": "success"})
#     return render(request, "show_book.html", {"message": "success"})

def openAPIdemo(request):
    data_json = {}
    book_dtl =[]


    if request.method == 'POST':
        print("POST request received")
        book_title = request.POST.get('book_title')

        if not book_title:
          return redirect("load_view")
        
        data = requests.get(f"https://openlibrary.org/search.json?title={book_title}")
        data_json = data.json()['docs']

        if not data_json:
          return render(request, "show_book.html",{"error":"no book found"})
        

        for i in data_json:
            book_details = {
                'title': i.get('title_suggest', 'N/A'),
                'author': ", ".join(i.get('author_name', ['N/A'])),
                'cover_id': i.get('cover_i', None),
                'key': i.get('key',['N/A']),
                'subject': ", ".join(i.get('subject', ['N/A'])),
                'publish_year': i.get('first_publish_year', 'N/A'),
                'total_pages':i.get('number_of_pages_median',0)
            }
            book_dtl.append(book_details)

        user = User.objects.get(username = request.user)
        user_books = rental_books_user.objects.filter(user=user.id)

        available_books = [ub.book for ub in user_books if not ub.access_expired()]
        print("available_books",available_books)
    
    return render(request, "show_rental_books.html", {'data': book_dtl ,"bookdata":available_books })


def load_book_details(request, key, pages):
    data = requests.get(f"https://openlibrary.org{key}.json")
    book_details = data.json()

    rent_prise = abs(pages/100)
    print("rent_prise",rent_prise)
    return render(request, 'book_details.html', {'data': book_details,"key":key,'pages':pages})

def signout(request):
  print("ins ign out",request.user)

  your_data = request.session.get('your_key', None)
  print("your_data",your_data)
  logout(request)
  return redirect(reverse('load_login'))

def rent_book(request,key,pages):
  print("request.user",request.user)
  data = requests.get(f"https://openlibrary.org{key}.json")
  book_details = data.json()
  print("book_details",book_details,pages)
  author = str(book_details.get("authors")[0].get('author').get('key'))
  book_title= book_details.get('title')
  # author = author.split('/')
  print("author",book_title)
  rent_prise = abs(pages/100)
  return render(request, 'rent_book.html',{"data":book_title,"pages":pages,"total_rent":rent_prise,"author":author})

def rent_conform_book(request):
    renter_duration = timezone.now().strftime("%d")
    title = request.POST.get("title")
    pages = request.POST.get("pages")
    rent_price = request.POST.get("rent_price")
    payment_mode = request.POST.get("payment_mode")
    author = request.POST.get("author")
    
    print( "author", author)
    user = User.objects.get(username=request.user)
    books_count = Book.objects.filter(author=author, title=title).count()
    # books_data = Book.objects.filter(title = title)
    book_data= Book.objects.create(title = title,pages = pages,author=author ,is_free = True, renter =  user, total_renters= books_count)
    book_duration = rental_books_user.objects.create(user = user, book = book_data,renter_duration =renter_duration,renter_page_book = pages, rent_of_book = float(rent_price))
      
    if books_count>=1 :
      books_count +=1
      book_data.save()
      current_time = timezone.now()

      print( "ajhsgdvjahsdbkjasndkj,n",type(rent_price))

      for book in rental_books_user.objects.all():
        if isinstance(book.renter_duration, datetime):
          # Calculate the difference in days between now and the datetime value
          time_difference = book.renter_duration - book.created_at
          book.renter_duration = time_difference.days
          book.save()
      
      renter_duration = int(renter_duration)
      
      
      book= Book.objects.create(title = title,pages = pages,author=author ,is_free = True, renter =  user, total_renters= books_count)
      book_duration = rental_books_user.objects.create(user = user, book = book,renter_duration =renter_duration,renter_page_book = pages, rent_of_book = float(rent_price))

      
      print("book_duration",book_duration)
     
   
    return redirect('load_view')


def dashboard(request):
  books_details = rental_books_user.objects.all()
  return render(request,'admin_dashboard.html',{"data":books_details})


def admin_add_new_book(request):
  # if request.method == 'POST':
  #   title = request.POST.get("title")
  #   pages = request.POST.get("pages")
  #   author = request.POST.get("pages")

  #   user = request.user
  #   user_data = Book.objects.get(title = title,pages = pages,author =author,is_free = False,renter = None,is_admin = True)

   return render(request,'admin_add_book.html')

  # else:
  #   redirect("dashboard" , ke)
