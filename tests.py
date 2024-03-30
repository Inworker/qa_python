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
        assert collector.get_list_of_favorites_books() == []

    def test_null_books_genre(self): #Пустой словарь книга/жанр
        collector = BooksCollector()
        assert collector.get_books_genre() == {}


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
    def test_add_new_book_add_one_book_42_symbol_null(self):# Добавление 1 книги в пустой список с кол-ом символов = 42
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби и зомби..'
        ganre = "Ужасы"
        collector.add_new_book(book)
        collector.set_book_genre(book,ganre)
        assert collector.get_books_genre() == {}


    def test_get_book_genre_one_book(self): # Жанр 1 добавленной книги по названию
        collector = BooksCollector()
        one_book = 'Гордость и предубеждение и зомби'
        book_ganre = "Ужасы"
        collector.add_new_book(one_book)
        collector.set_book_genre(one_book, book_ganre)
        assert collector.get_book_genre(one_book) == book_ganre

    def test_get_books_with_specific_genre_add_two_book_different_ganre_one_specific(self): # Добавление 1 книги с определенным жанром, которого нет в списке жанров
        collector = BooksCollector()
        books_with_specific_genre = []
        first_book = 'Шерлок'
        first_ganre = 'Детективы'
        second_book = 'Майор Гром'
        second_ganre = 'Jyloo'
        collector.add_new_book(first_book)
        collector.set_book_genre(first_book, first_ganre)
        collector.add_new_book(second_book)
        collector.set_book_genre(second_book, second_ganre)
        assert collector.get_books_with_specific_genre(first_ganre) != [first_book,second_book]

    def test_add_book_in_favorites_book_not_in_genre(self):  # Добавление 1 книги в избранное, которой нет в списке жанров
        collector = BooksCollector()
        first_ganre = 'Ониме'
        collector.add_book_in_favorites(first_ganre)
        assert collector.get_list_of_favorites_books not in collector.favorites

    def test_get_books_genre_add_3_different_books_ganre(self):# Список книг с 3 разными жанрами
        collector = BooksCollector()
        book_list =['Смешарики', 'Майор Гром','Чужой']
        book_ganre = ['Мультфильмы', 'Детективы','Ужасы']
        collector.add_new_book(book_list[0])
        collector.set_book_genre(book_list[0], book_ganre[0])
        collector.add_new_book(book_list[1])
        collector.set_book_genre(book_list[1], book_ganre[1])
        collector.add_new_book(book_list[2])
        collector.set_book_genre(book_list[2], book_ganre[2])
        assert collector.get_books_genre() == {book_list[0]: book_ganre[0], book_list[1]: book_ganre[1], book_list[2]: book_ganre[2]}


    def test_get_books_for_children_add_2_children_book(self): # Список книг с детскими жанрами
        collector = BooksCollector()
        first_book = 'Смешарики'
        first_ganre = 'Мультфильмы'
        second_book = 'Машенька'
        second_ganre = 'Мультфильмы'
        collector.add_new_book(first_book)
        collector.set_book_genre(first_book, first_ganre)
        collector.add_new_book(second_book)
        collector.set_book_genre(second_book, second_ganre)
        assert collector.get_books_for_children() == [first_book, second_book]

    def test_get_books_for_children_add_book_age_rating_in_list_children_books(self): # Добавление книги с взрослым жанром в список с детскими жанрами
        collector = BooksCollector()
        first_book = 'Смешарики'
        first_ganre = 'Мультфильмы'
        second_book = 'Машенька'
        second_ganre = 'Ужасы'
        collector.add_new_book(first_book)
        collector.set_book_genre(first_book, first_ganre)
        collector.add_new_book(second_book)
        collector.set_book_genre(second_book, second_ganre)
        assert collector.get_books_for_children() == [first_book]

    def test_add_book_in_favorites_add_one_favorites_book(self):#Добавление 1 книги в избранное
        collector = BooksCollector()
        first_book = 'Смешарики'
        collector.add_new_book(first_book)
        collector.add_book_in_favorites(first_book)
        assert collector.get_list_of_favorites_books() == [first_book]

    def test_add_book_in_favorites_add_two_same_books_in_favorites(self):#Повторное добавление 1 книги в избранное
        collector = BooksCollector()
        book_name = 'Book1'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]

    def test_delete_book_from_favorites_add_and_remove_same_favorite_book(self):# Очистить список избранных книг
        collector = BooksCollector()
        first_book = 'Смешарики'
        collector.add_new_book(first_book)
        collector.add_book_in_favorites(first_book)
        collector.delete_book_from_favorites(first_book)
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_remove_book_not_favorite(self):# Удалить книгу, которой нет в избранных
        collector = BooksCollector()
        collector.add_book_in_favorites('Harry Potter')
        collector.add_book_in_favorites('Lord of the Rings')
        collector.delete_book_from_favorites('Game of Thrones')
        assert 'Game of Thrones' not in collector.get_list_of_favorites_books()

