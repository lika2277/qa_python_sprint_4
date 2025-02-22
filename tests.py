from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_book_exists_genre_exists(self):
        book_name = 'Вольт'
        book_genre = 'Мультфильмы'

        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_set_book_genre_book_exists_genre_not_exists(self):
        book_name = 'Вольт'

        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Классика')
        assert collector.get_book_genre(book_name) == ''

    def test_set_book_genre_book_not_exists_genre_exists(self):
        book_name = 'Вольт'

        collector = BooksCollector()
        collector.set_book_genre(book_name, 'Классика')
        assert not collector.get_book_genre(book_name)

    def test_get_book_genre_book_exists(self):
        book_name = 'Вольт'

        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in list(collector.get_books_genre())

    def test_get_book_genre_books_not_exists(self):
        collector = BooksCollector()
        assert len(list(collector.get_books_genre())) == 0

    def test_get_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Вольт')
        assert 'Мулан' not in list(collector.get_books_genre())



    def test_get_books_with_specific_genre_add_three_books(self):
        books = [
            'Вольт',
            'Мулан',
            'Рататуй'
        ]
        collector = BooksCollector()
        for name in books:
            collector.add_new_book(name)
        for name in books:
            collector.set_book_genre(name, 'Мультфильмы')
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == len(books)

    def test_get_books_genre(self):
        collector = BooksCollector()
        assert len(collector.get_books_genre()) == 0

        book_name = 'Вольт'
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1
        assert book_name in collector.get_books_genre()

    def test_get_books_for_children(self):
        books = {
            'Хроники Нарнии': 'Фантастика',
            'Лес': 'Ужасы',
            'Отель убийц': 'Детективы',
            'Мулан': 'Мультфильмы',
            'Кешка в центре внимания': 'Комедии'
        }
        books_for_children = []
        for name, genre in books.items():
            if genre in ['Фантастика', 'Мультфильмы', 'Комедии']:
                books_for_children.append(name)

        collector = BooksCollector()
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name,genre)
        assert len(collector.get_books_genre()) == len(books)
        assert len(collector.get_books_for_children()) == len(books_for_children)
        for name in list(collector.get_books_for_children()):
            assert name in books_for_children

    def test_add_book_in_favorites(self):
        book_name = 'Вольт'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        book_name = 'Вольт'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites('Мулан')
        assert len(collector.get_list_of_favorites_books()) == 1

        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books(self):
        book_name = 'Вольт'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()