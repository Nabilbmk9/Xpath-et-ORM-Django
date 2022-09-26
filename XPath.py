import bs4

# 1) Retourner tous les éléments book
def get_books():
    with open('books.xml', 'r') as f:
        xml = f.read()
        soup = bs4.BeautifulSoup(xml, 'xml')
        books = soup.find_all('book')
        return books

# 2) Retourner tous les éléments title ayant comme parent un élément book avec un attribut type égal à roman
def get_books_title():
    books = get_books()
    return [book.find('title').text for book in books if book['type'] == 'roman']

# 3) Retourner le nombre d'éléments book ayant un attribut type égal à bd
def get_books_bd():
    books = get_books()
    return len([book for book in books if book['type'] == 'bd'])

# 4) Que renvoie la requête XPath suivante :  /library/library/ancestor-or-self::library
La requête renvoie
<book type="roman">
	<title>toto5</title>
	<author>titi</author>
</book>

