from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from expenses.models import Expense
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class ExpenseAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.user1 = User.objects.create_user(username='testuser1', password='testpass321')
        self.client=APIClient()
        self.client1=APIClient()
        self.client.force_authenticate(user=self.user)#simula login
        self.client1.force_authenticate(user=self.user1)

        self.expense = Expense.objects.create(
            category = 'test',
            amount = Decimal('100.00'),
            date = '2026-06-09',
            description = 'gasto de prueba',
            user = self.user
        )
        self.expense1 = Expense.objects.create(
            category = 'test2',
            amount = Decimal('100.00'),
            date = '2026-07-15',
            description = 'gasto de prueba 2',
            user = self.user
        )
        self.expense4 = Expense.objects.create(
            category = 'test4',
            amount = Decimal('500.00'),
            date = '2026-07-15',
            description = 'gasto de prueba 4',
            user = self.user1
        )

    def test_list_expenses(self):
        #GET  /expenses/expenses/
        response = self.client.get('/api_expenses/expenses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_expense(self):
        # POST /expenses/expenses/
        data = {
            'category': 'nuevo',
            'amount' : 50.00,
            'date' : '2026-06-03',
            'description': 'creado desde test',

        }
        response = self.client.post('/api_expenses/expenses/',data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_idor(self):# IDOR : Insecure Direct Object Reference O Referencia Directa a Objecto Inseguro
        url = reverse('expense-detail', kwargs={'pk':self.expense.id})
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unaunthenticated(self):
        #Usuario no autenticado deberia recibir 401

        self.client.force_authenticate(user=None) #USUARIO NONE forzado
        response = self.client.get('/api_expenses/expenses/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_summary(self):
        url = reverse('expense-summary')
        response = self.client.get(url)# para probar con una fecha hardcodeada la url completa seria: response = self.client.get(f'{url}?datefrom=2026-01-01&date_to=2026-07-20')
        self.assertEqual(response.status_code, status.HTTP_200_OK )

    def test_category_summary(self):
        response = self.client.get('/api_expenses/expenses/category_summary/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_greater(self):
        response = self.client.get('/api_expenses/expenses/category_greater/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comparative_summary(self):
        url = '/api_expenses/expenses/comparative_summary/'
        response = self.client.get(f'{url}?date_from=2026-06-01&date_to=2026-06-30&date_from1=2026-07-01&date_to1=2026-07-31')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_expense_by_day(self):
        self.expense3 = Expense.objects.create(
            category = 'test',
            amount = Decimal('10.00'),
            date = '2026-06-09',
            description = 'gasto de prueba',
            user = self.user
        )

        response = self.client.get('/api_expenses/expenses/expense_by_day/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['expense']), 2)
        self.assertEqual(self.expense.date,str(response.data['expense'][1]['date']))
        precio = self.expense.amount+self.expense3.amount
        self.assertEqual(precio, response.data['expense'][1]['total'])

        response1 = self.client1.get('/api_expenses/expenses/expense_by_day/')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response1.data['expense']),1)
        self.assertEqual(response1.data['expense'][0]['cantidad'],1)
        self.assertEqual(self.expense4.amount, response1.data['expense'][0]['total'])
        self.assertEqual(self.expense4.date, str(response1.data['expense'][0]['date']))


    def test_recent(self):
        self.expense5 = Expense.objects.create(
                    category = 'test5',
                    amount = Decimal('20.00'),
                    date = '2026-05-09',
                    description = 'gasto de prueba 5',
                    user = self.user
                )
        response = self.client.get('/api_expenses/expenses/recent/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.expense1.date, response.data[0]['date'])
        self.assertEqual(self.expense.date, response.data[1]['date'])
        self.assertEqual(len(response.data),2)

        response1 = self.client1.get('/api_expenses/expenses/recent/')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response1.data), 1)
        self.assertEqual(response1.data[0]['id'], self.expense4.id)
        
    def test_exp_evol_success_aggregation(self):
        self.expense6 = Expense.objects.create(
                    category = 'test6',
                    amount = Decimal('101.00'),
                    date = '2026-06-10',
                    description = 'gasto de prueba 6',
                    user = self.user
                )

        self.expense7 = Expense.objects.create(
                    category = 'test7',
                    amount = Decimal('900.00'),
                    date = '2026-06-10',
                    description = 'gasto de prueba 7',
                    user = self.user
                )
        
        response1 = self.client.get('/api_expenses/expenses/expenses_evolution/?date_from=2026-06-01&date_to=2026-06-30')
        self.assertEqual(response1.status_code, status.HTTP_200_OK )
        self.assertEqual(len(response1.data['data']), 2)
        self.assertEqual(self.expense6.date, str(response1.data['data'][1]['date']))
        self.assertEqual(self.expense.date, str(response1.data['data'][0]['date']))
        self.assertEqual((self.expense6.amount + self.expense7.amount), response1.data['data'][1]['amount'])
        self.assertEqual(self.expense.amount, response1.data['data'][0]['amount'])

    def test_exp_evol_aislamiento(self):

        self.expense6 = Expense.objects.create(
                    category = 'test6',
                    amount = Decimal('101.00'),
                    date = '2026-06-10',
                    description = 'gasto de prueba 6',
                    user = self.user
        )

        self.expense7 = Expense.objects.create(
                    category = 'test7',
                    amount = Decimal('900.00'),
                    date = '2026-06-10',
                    description = 'gasto de prueba 7',
                    user = self.user1
                )
        self.expense8 = Expense.objects.create(
                            category = 'test8',
                            amount = Decimal('300.00'),
                            date = '2026-06-10',
                            description = 'gasto de prueba 8',
                            user = self.user1
                        )

        response1 = self.client.get('/api_expenses/expenses/expenses_evolution/?date_from=2026-06-01&date_to=2026-06-30')
        self.assertEqual(response1.status_code, status.HTTP_200_OK )
        self.assertEqual(len(response1.data['data']), 2)
        self.assertEqual(self.expense6.date, str(response1.data['data'][1]['date']))
        self.assertEqual(self.expense.date, str(response1.data['data'][0]['date']))
        self.assertEqual(self.expense6.amount, response1.data['data'][1]['amount'])
        self.assertEqual(self.expense.amount, response1.data['data'][0]['amount'])

        response2 = self.client1.get('/api_expenses/expenses/expenses_evolution/?date_from=2026-06-01&date_to=2026-06-30')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response2.data['data']), 1)# un indice en la lista
        self.assertEqual(str(response2.data['data'][0]['date']), self.expense7.date)# misma fecha
        self.assertEqual((self.expense7.amount + self.expense8.amount), response2.data['data'][0]['amount'])#suma de montos en la misma fecha


    def test_exp_evol_missing_one_date_params(self):
        response1 = self.client1.get('/api_expenses/expenses/expenses_evolution/?date_from=&date_to=2026-06-01')
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response1.data['detail'],'bad request')
        response2 = self.client1.get('/api_expenses/expenses/expenses_evolution/?date_from=2026-06-01&date_to=')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.data['detail'],'bad request')

    def test_exp_evol_invert_range(self):
        response = self.client1.get('/api_expenses/expenses/expenses_evolution/?date_from=2026-06-30&date_to=2026-06-01')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'],'bad request')


    def test_exp_evol_invalid_format(self):
        response = self.client1.get('/api_expenses/expenses/expenses_evolution/?date_from=HOLA&date_to=2026-06-01')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'],'bad request')

    def test_exp_evol_inexist_date(self):
        response = self.client1.get('/api_expenses/expenses/expenses_evolution/?date_from=2026-02-50&date_to=2026-06-01')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'],'bad request')

    def test_exp_evol_ausent_params(self):
        response = self.client.get('/api_expenses/expenses/expenses_evolution/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'],'bad request')
