package member_management;

import book_management.Book;
import java.util.ArrayList;
import java.util.List;

public class Member {
    private int id;
    private String name;
    private List<Book> borrowedBooks;

    public Member(int id, String name) {
        this.id = id;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void addBook(Book book) {
        // Validate the book before modifying the member's collection.
        if (book == null) {
            throw new IllegalArgumentException("Book cannot be null");
        }

        if (borrowedBooks.contains(book)) {
            throw new IllegalArgumentException("Book is already assigned to this member");
        }

        borrowedBooks.add(book);
    }

    public void removeBook(Book book) {
        if (book == null) {
            throw new IllegalArgumentException("Book cannot be null");
        }

        borrowedBooks.remove(book);
    }

    public List<Book> getBooks() {
        return borrowedBooks;
    }
}