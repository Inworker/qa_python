from main import BooksCollector
import pytest
#тут
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.parametrize('ganre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_get_all_genre(self, ganre): #  Список всех жанров
        collector = BooksCollector()
        assert ganre in collector.genre

    @pytest.mark.parametrize('age_ganre', ['Ужасы', 'Детективы']) #Список взрослых жанров
    def test_init_get_age_rating(self,age_ganre):
        collector = BooksCollector()
        assert age_ganre in collector.genre_age_rating

    def test_null_favotites_list(self):# Пустой список в избранном
        collector = BooksCollector()
        assert collector.favorites == []

    def test_null_books_genre(self): #Пустой словарь книга/жанр
        collector = BooksCollector()
        assert collector.books_genre == {}


    def test_add_new_book_add_two_books(self):# Добавление 2 книг в пустой список
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_one_book(self): #Добавление жанра "Ужасы" "для книги Гордость и предубеждение и зомби"
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] ==  'Ужасы'


    def test_get_book_genre_one_book(self):# Жанр 1 добавленной книги по названию
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'


    def test_get_books_with_specific_genre_add_two_book_same_ganre(self):# Добавление 2 книг с жанром "Детектив"
        collector = BooksCollector()
        books_with_specific_genre = []
        collector.add_new_book('Шерлок')
        collector.set_book_genre('Шерлок', 'Детективы')
        collector.add_new_book('Майор Гром')
        collector.set_book_genre('Майор Гром', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок','Майор Гром']


    def test_get_books_genre_add_3_different_book_ganre(self):# Список книг с разными жанрами
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.add_new_book('Шерлок')
        collector.set_book_genre('Шерлок', 'Детективы')
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        assert collector.get_books_genre() == {'Смешарики': 'Мультфильмы', 'Шерлок': 'Детективы', 'Чужой': 'Ужасы'}


    def test_get_books_for_children_add_2_children_book(self): # Список книг с детскими жанрами
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.add_new_book('Машенька')
        collector.set_book_genre('Машенька', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Смешарики', 'Машенька']

    def test_add_book_in_favorites_add_one_favorites_book(self):#Добавление 1 книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Фантастика')
        collector.add_book_in_favorites('Смешарики')
        assert collector.get_list_of_favorites_books() == ['Смешарики']

    def test_delete_book_from_favorites_add_and_remove_same_favorite_book(self):# Очистить список избранных книг
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.add_book_in_favorites('Смешарики')
        collector.delete_book_from_favorites('Смешарики')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_add_2_same_favorite_book_(self): #Добавление 2 одинаковых книги в избранные
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.add_new_book('Смешарики')
        collector.add_book_in_favorites('Смешарики')
        assert collector.get_list_of_favorites_books() == ['Смешарики']