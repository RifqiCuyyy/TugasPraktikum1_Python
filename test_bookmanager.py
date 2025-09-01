import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)
        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    # [TUGAS 1] Melengkapi tes yang kosong
    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada (Harus Passed)"""
        self.book_manager.add_book(Book("Buku Ada", "Penulis Ada", 2021))
        removed = self.book_manager.remove_book("Buku Tidak Ada")
        # Ekspektasi: method harus mengembalikan False
        self.assertFalse(removed)
        # Ekspektasi: jumlah buku tetap 1
        self.assertEqual(1, self.book_manager.get_book_count())

    # [TUGAS 1] Melengkapi tes yang kosong
    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author (Harus Passed)"""
        self.book_manager.add_book(Book("Buku A", "Andi", 2020))
        self.book_manager.add_book(Book("Buku B", "Budi", 2021))
        self.book_manager.add_book(Book("Buku C", "Andi", 2022))
        found_books = self.book_manager.find_books_by_author("Andi")
        # Ekspektasi: harus menemukan 2 buku
        self.assertEqual(2, len(found_books))

    # [TUGAS 1] Melengkapi tes yang kosong
    def test_get_all_books(self):
        """Test mendapatkan semua buku (Harus Passed)"""
        self.book_manager.add_book(Book("Buku A", "Andi", 2020))
        self.book_manager.add_book(Book("Buku B", "Budi", 2021))
        all_books = self.book_manager.get_all_books()
        # Ekspektasi: harus mengembalikan 2 buku
        self.assertEqual(2, len(all_books))

    # [TUGAS 3] Membuat test case yang gagal
    def test_get_book_count_should_fail(self):
        """Test mendapatkan jumlah buku (Sengaja Dibuat Fail)"""
        self.book_manager.add_book(Book("Buku A", "Andi", 2020))
        # Ekspektasi salah: kita mengharapkan 5, padahal seharusnya 1.
        # Ini akan membuat tes gagal.
        self.assertEqual(5, self.book_manager.get_book_count())

if __name__ == '__main__':
    unittest.main()