import pytest

from class_Book import Book  # adjust import if needed

def test_initialization():
    book = Book("1984", "George Orwell")
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.available is True

def test_borrow_when_available():
    book = Book("1984", "George Orwell")
    result = book.borrow()
    assert result is True
    assert book.available is False

def test_borrow_when_not_available():
    book = Book("1984", "George Orwell")
    book.borrow()
    result = book.borrow()
    assert result is False
    assert book.available is False

def test_return_book():
    book = Book("1984", "George Orwell")
    book.borrow()
    book.return_book()
    assert book.available is True
