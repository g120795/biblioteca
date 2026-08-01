from decimal import Decimal

from django.contrib.auth.models import User
from django.test import Client, TestCase

from books.models import Author, Book, Editorial


class ApiTestBook(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='test', password='test123')
        self.user2 = User.objects.create_user(username='test1', password='test321',is_staff=True)
        self.navegador1 = Client()
        self.navegador2 = Client()
        self.navegador1.force_login(self.user1)
        self.navegador2.force_login(self.user2)


        self.editorial = Editorial.objects.create(
            name = 'los felices',
            adress = 'av.perdicion 180',
            city = 'new jersy',
            region = 'los angeles',
            country = 'Estados Unidos',
            postal_code = '20005',
            email = 'los_felices@gmail.com',
            year_foundation = '2026-07-30',
            create_by = self.user1
        )

        self.author = Author.objects.create(
            name = 'dead',
            lastname = 'pool',
            born = '2000-07-12',
            nationality = 'peruvian',
            biograpy = 'sin biografia',
            email = 'deadp@gmail.com',
            phone = '931953033',
            web_site = 'www.google.com',
            awards = 'premio fields',
        )


        self.libro = Book.objects.create(
                    title = 'el talisman',
                    isbn = '1111111111111',
                    publication_date = '2026-01-30',
                    pages_number = '35',
                    language = 'ES',
                    description = 'no es una prueba',
                    gender = 'sabor',
                    unit_price = Decimal('222.00'),
                    is_out_of_stock = False,
                )


    def test_create_read_book(self):
        response = self.navegador2.get('/books/read_books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['form'].object_list), 1)
        libro = response.context['form'].object_list
        self.assertEqual(libro[0].title, 'el talisman')


        book = {
            'title' : 'el brujo',
            'isbn' :'23343123432',
            'publication_date' : '2026-07-30',
            'pages_number' : '333',
            'language' : 'ES',
            'description' : 'este libro fue publicado ayer y es una prueba',
            'editorial' : 1,
            'gender' : 'sabor',
            'unit_price' : Decimal('222.00'),
            'is_out_of_stock' : False,
            'authores' : 1,
        }
        response = self.navegador2.post('/books/create_book/', book)
        self.assertEqual(response.status_code, 200)
        response1 = self.navegador2.get('/books/read_books/')
        self.assertEqual(len(response1.context['form'].object_list), 2)
        libros = response1.context['form'].object_list
        self.assertEqual(libros[1].title, 'el brujo')

        
    def test_edit_book(self):
        data = {   'title': self.libro.title,
                        'isbn': '2222222222222',
                        'publication_date': self.libro.publication_date,
                        'pages_number': self.libro.pages_number,
                        'language': self.libro.language,
                        'editorial': self.editorial.id,
                        'description': self.libro.description,
                        'gender': self.libro.gender,
                        'unit_price': self.libro.unit_price,
                        'authores': self.author.id,
                        'is_out_of_stock': self.libro.is_out_of_stock,                         
                    }
        
        response = self.navegador2.post(f'/books/{self.libro.id}/edit_book/',data
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/books/read_books/')
        update_book = Book.objects.get(id=self.libro.id)
        self.assertEqual(update_book.isbn, '2222222222222')
        




class ApiTestAuthor(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='test1',password='test123')
        self.user2 = User.objects.create_user(username='test2', password='test321', is_staff=True)
        self.navegador1 = Client()
        self.navegador2 = Client()
        self.navegador1.force_login(self.user1)
        self.navegador2.force_login(self.user2)

    def test_create_author(self):
        pass








class ApiTestEditorial(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='test1', password='test123')
        self.user2 = User.objects.create_user(username='test2', password='test321', is_staff=True)
        self.navegador1 = Client()
        self.navegador2 = Client()
        self.navegador1.force_login(self.user1)
        self.navegador2.force_login(self.user2)

    def test_create_editorial(self):
        pass



