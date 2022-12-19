from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def main(request):
    return render(request, 'index4.html', context={'text': 'hello world', 'pagelist': [('main', 'Main'), ('writers', 'Writers'), ('books', 'Top of books')]})


main_page = f'<ul><li><a href="http://127.0.0.1:8000">Main</a></li></ul>'
writers_page = f'<ul><li><a href="http://127.0.0.1:8000/writers">Writers</a></li></ul>'
top_page = f'<ul><li><a href="http://127.0.0.1:8000/books">Top of books</a></li></ul>'


def books(request):
    return HttpResponse(f"{main_page}{writers_page}<br>Choose book place")


def book_top(request, place):
    if place == 1:
        return HttpResponse(f"{main_page}{writers_page}<br>Honey and Spice by Bolu Babalola")
    elif place == 2:
        return HttpResponse(f"{main_page}{writers_page}<br>An Immense World by Ed Yong")
    elif place == 3:
        return HttpResponse(f"{main_page}{writers_page}<br>In Love by Amy Bloom")
    elif place == 4:
        return HttpResponse(f"{main_page}{writers_page}<br>Lolo's Light by Liz Garton Scanlon")
    elif place == 5:
        return HttpResponse(f"{main_page}{writers_page}<br>Man o' War by Cory McCarthy")
    else:
        return HttpResponse(f"{main_page}{writers_page}<br>No number in this top of books - {place}")


def writers(request):
    writers_list = "<ul><li>Scott Fitzgerald</li><li>Marcel Proust</li><li>Lille</li><li>James Joyce</li></ul>"
    return HttpResponse(f"{main_page}{top_page}<br>Some of the most famous writers:<br>{writers_list}")


def writer(request, name_writer):
    if name_writer.lower() == "scott_fitzgerald":
        return HttpResponse(f"{main_page}{top_page}<br>Scott Fitzgerald was a 20th-century American short-story "
                            f"writer and novelist. Although he completed four novels and more than 150 short stories "
                            f"in his lifetime, he is perhaps best remembered for his third novel, The Great Gatsby")
    elif name_writer.lower() == "marcel_proust":
        return HttpResponse(f"{main_page}{top_page}<br>Marcel Proust was an early 20th-century French writer "
                            f"responsible for what is officially the longest novel in the world: À la recherche du "
                            f"temps perdu – which has 1,267,069 words in it; double those in War and Peace.")
    else:
        return HttpResponse(f"{main_page}{top_page}<br>Nothing haven`t found about this writer - {name_writer}<br"
                            f">Return to the list of writers:<br>{writers_page}")


def writers_book(request, book, name):
    if name.lower() == "scott_fitzgerald" and book == "the_great_gatsby":
        return HttpResponse(f"{main_page}{top_page}<br>Founded,but no information")
    elif name.lower() == "marcel_proust" and book == "a_la_recherche_du_temps_perdu":
        return HttpResponse(f"{main_page}{top_page}<br>Founded,it is the longest novel in the world")
    else:
        return HttpResponse(f"{main_page}{top_page}<br>Nothing haven`t found about {book} of {name}"
                            f"<br>Return to the list of writers:<br>{writers_page}")

