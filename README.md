#  QA  Python (Sprint 4)

* `setUp`: создаёт новый экземпляр BooksCollector перед каждым тестом.
* `test_add_new_book_add_two_books`: проверяет добавление двух новых книг.
* `test_set_book_genre_book_exists_genre_exists`: проверяет, что к книге добавился жанр.
* `test_set_book_genre_book_exists_genre_not_exists`: проверяет что к существующей книге не добавился жанр.
* `test_set_book_genre_book_not_exists_genre_exists`: проверяет, что не добавлся жанр к несуществующей книге.
* `test_get_book_genre_book_exists`: проверяет, что функция `get_books_genre` возвращает список добавленных книг.
* `test_get_books_with_specific_genre_add_three_books`: проверяет, что возвращаются книги указанного жанра.
* `test_get_books_genre`: проверяет что возвращается книга которая находиться в списке книг.
* `test_get_books_for_children`: проверяет, что возвращаются книги только для детей.
* `test_add_book_in_favorites`: проверяет добавление книги в избранное.
* `test_delete_book_from_favorites`: проверяет, удаление книги из избранного.
* `test_get_list_of_favorites_books`: проверяет возвращаемый список избранных книг.
