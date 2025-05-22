import pytest
import library

from class_Library import Library


def test_library_initialization():
    lib = Library()
    assert lib.books == []

def test_add_book():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    assert len(lib.books) == 1
    book = lib.books[0]
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"
    assert book.available is True

def test_check_availability_exists():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    assert lib.is_available("Dune") is True

def test_check_availability_not_exists():
    lib = Library()
    assert lib.is_available("Nonexistent") is False

def test_borrow_book_available():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.borrow_book("Dune")
    assert result is True
    assert lib.is_available("Dune") is False

def test_borrow_book_already_borrowed():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    lib.borrow_book("Dune")
    result = lib.borrow_book("Dune")
    assert result is False

def test_borrow_book_not_in_library():
    lib = Library()
    result = lib.borrow_book("Unknown Book")
    assert result is False

def test_return_book_valid():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    lib.borrow_book("Dune")
    result = lib.return_book("Dune")
    assert result is True
    assert lib.is_available("Dune") is True

def test_return_book_does_not_exist():
    lib = Library()
    result = lib.return_book("Nonexistent Book")
    assert result is False

def test_return_book_already_available():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.return_book("Dune")
    assert result is True
    assert lib.is_available("Dune") is True
