import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("name", ["", "b" * 41])
    def test_add_new_book_invalid_length(self, name):
        collector = BooksCollector()
        assert collector.add_new_book(name) is not True

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Dune")
        collector.set_book_genre("Dune", "Фантастика")
        assert collector.books_genre["Dune"] == "Фантастика"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Dune")
        collector.set_book_genre("Dune", "Научная фантастика")
        assert collector.books_genre["Dune"] == ""
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        assert collector.get_book_genre("Властелин колец") == "Фантастика"

    @pytest.mark.parametrize("not_existing_name", ["", "Рандомная книга"])
    def test_get_book_genre_nonexistent_book(self,not_existing_name):
        collector = BooksCollector()
        assert collector.get_book_genre(not_existing_name) is None

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.add_new_book("Властелин колец")
        collector.add_new_book("Dune")
        collector.set_book_genre("Dune", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Властелин колец","Dune"]

    def test_get_books_with_specific_genre_empty_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre("Фантастика") == []

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Dune")
        collector.set_book_genre("Dune", "Фантастика")
        assert collector.get_books_genre() == {"Dune": "Фантастика"}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Winnie the Pooh")
        collector.set_book_genre("Winnie the Pooh", "Мультфильмы")
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")
        assert collector.get_books_for_children() == ["Winnie the Pooh","Властелин колец"]

    def test_get_books_for_children_with_age_restricted_genre(self):
        collector = BooksCollector()
        collector.add_new_book("The Shining")
        collector.set_book_genre("The Shining", "Ужасы")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Pride and Prejudice")
        collector.add_book_in_favorites("Pride and Prejudice")
        assert collector.get_list_of_favorites_books() == ["Pride and Prejudice"]

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        collector.add_book_in_favorites("1984")
        assert collector.get_list_of_favorites_books() == ["1984"]

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.add_book_in_favorites("Рандомная книга") is None

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Pride and Prejudice")
        collector.add_book_in_favorites("Pride and Prejudice")
        collector.delete_book_from_favorites("Pride and Prejudice")
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book("Pride and Prejudice")
        collector.add_book_in_favorites("Pride and Prejudice")
        collector.delete_book_from_favorites("Nonexistent Book")
        assert collector.get_list_of_favorites_books() == ["Pride and Prejudice"]

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Jane Eyre")
        collector.add_book_in_favorites("Jane Eyre")
        assert collector.get_list_of_favorites_books() == ["Jane Eyre"]