Sprint_4
# qa_python
test_add_new_book_add_two_books тест был изменен. Вызывался несуществующий метод, заменен на get_books_genre, Тест проверяет метод add_new_book на возможность добавления двух книг, количество элементов в словаре
test_add_new_book_duplicate Проверка того, что методв не дублирует записи в соварь. При вводе одинаковых имен, запись не дублируется
test_add_new_book_invalid_length Тест, проверяющий, что при вводе в качеств имени пустого значения или названия, количество символов в котором превышает 41, запись в словарь не происходит

test_set_book_genre проверка метода на возможность добавления жанра в запись
test_set_book_genre_invalid_genre При попытке записи несуществующего жанра, значение остается пустым

test_get_book_genre проверяет возможность получения записи о жанре 
test_get_book_genre_nonexistent_book проверка отсутствия несуществующей записи

test_get_books_with_specific_genre_success Тест добавления нескольких записей в один жанр
test_get_books_with_specific_genre_empty_books_genre тест на проверку отсутствия записей в жанре

test_get_books_genry проверка кореектности записи жанра

test_get_books_for_children Проверка возвращения методом списка детских книг
test_get_books_for_children_with_age_restricted_genre проверка, что книги с жанрами не подходящими для детей не возвращаются методом

test_add_book_in_favorites Проверка, что метод не добавляет книгу в список избранных
test_add_book_in_favorites_duplicate Проверка, что метод не добавляет дубликаты
test_add_book_in_favorites_nonexistent_book Проверка, что метод не добавляет несуществующую в списке книгу

test_delete_book_from_favorites Проверка что метод удаляет книгу из списка избранных
test_delete_book_from_favorites_nonexistent_book Проверка обработки удаления несуществующей книги

test_get_list_of_favorites_books Проверка, что метод возвращает список избранных книг
