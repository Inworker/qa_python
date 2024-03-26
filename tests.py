from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_init_all_genre(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_add_two_books(self):
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

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] ==  'Ужасы'




    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        listok = list(collector.books_genre.keys())
        assert listok == ['Гордость и предубеждение и зомби']


    def test_get_books_with_specific_genre_two_book_detective(self):
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Ониме')
        collector.add_new_book('Шерлок')
        collector.set_book_genre('Шерлок', 'Детективы')
        collector.add_new_book('Майор Гром')
        collector.set_book_genre('Майор Гром', 'Детективы')
        assert collector.get_books_with_specific_genre("Детективы") == ['Шерлок', 'Майор Гром']


    def test_get_books_genre_33(self):
         collector = BooksCollector()
         collector.add_new_book('Смешарики')
         collector.set_book_genre('Смешарики', 'Фантастика')
         collector.add_new_book('Шерлок')
         collector.set_book_genre('Шерлок', 'Детективы')
         collector.add_new_book('Майор Гром')
         collector.set_book_genre('Майор Гром', 'Детективы')
         assert collector.get_books_genre() == {'Смешарики': 'Фантастика', 'Шерлок': 'Детективы', 'Майор Гром': 'Детективы'}


    def test_get_books_for_children_for_children_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.add_new_book('Машенька')
        collector.set_book_genre('Машенька', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Смешарики', 'Машенька']


    def test_add_book_in_favorites(self):#Добавил в избранные 1 книгу - 1 книга в списке
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Фантастика')
        collector.add_book_in_favorites('Смешарики')
        assert collector.get_list_of_favorites_books() == ['Смешарики']
        # print(collector.get_list_of_favorites_books())


    def test_delete_book_from_favorites(self):# добавил и удалил 1 книгу из избранного = список избранных пустой
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Фантастика')
        collector.add_book_in_favorites('Смешарики')
        collector.delete_book_from_favorites('Смешарики')

        assert collector.get_list_of_favorites_books() == []
        # print(collector.get_list_of_favorites_books())

    def test_get_list_of_favorites_books(self): #добавить одинаковые избранные книги
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.add_new_book('Смешарики')
        collector.add_new_book('Смешарики')
        collector.add_book_in_favorites('Смешарики')
        collector.add_book_in_favorites('Смешарики')
        assert collector.get_list_of_favorites_books() == ['Смешарики']
