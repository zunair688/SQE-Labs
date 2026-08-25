package member_management;

import book_management.Book;
import java.util.ArrayList;
import java.util.List;

public class Member {
    private int id;
    private String name;
    private List<Book> borrowedBooks;

    // Store IDs of already registered members
    private static List<Integer> memberIds = new ArrayList<>();

    public Member(int id, String name) {

        // Prevent duplicate member IDs
        if (memberIds.contains(id)) {
            throw new IllegalArgumentException(
                "Member ID already exists: " + id
            );
        }

        this.id = id;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();

        // Register the new member ID
        memberIds.add(id);
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public boolean matchesName(String searchName) {
    if (searchName == null) {
        return false;
    }

    return name.equalsIgnoreCase(searchName.trim());
}

    

    public void addBook(Book book) {
    if (book == null) {
        throw new IllegalArgumentException("Book cannot be null");
    }

    if (borrowedBooks.contains(book)) {
        throw new IllegalArgumentException(
            "Book is already assigned to this member"
        );
    }

    // A student can borrow a maximum of 3 books.
    if (borrowedBooks.size() >= 3) {
        throw new IllegalArgumentException(
            "Student cannot borrow more than 3 books"
        );
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
