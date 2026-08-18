package member_management;

import book_management.Book;
import java.util.ArrayList;
import java.util.List;

public class Member {
    private int id;
    private String name;
    private List<Book> books;

    public Member(int id, String name) {
        this.id = id;
        this.name = name;
        this.books = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void addBook(Book book) {
        if (book == null) {
            throw new IllegalArgumentException("Book cannot be null");
        }

        books.add(book);
    }

    public void removeBook(Book book) {
    if (book == null) {
        throw new IllegalArgumentException("Book cannot be null");
    }

    books.remove(book);
}

    public List<Book> getBooks() {
        return books;
    }
}