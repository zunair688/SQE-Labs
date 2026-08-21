package book_management;

public class Book {
    private int bookId;
    private String title;
    private String author;

    public Book(int bookId, String title, String author) {
    if (bookId <= 0) {
        throw new IllegalArgumentException("Book id must be positive");
    }

    if (title == null || title.trim().isEmpty()) {
        throw new IllegalArgumentException("Book title cannot be empty");
    }

    if (author == null || author.trim().isEmpty()) {
        throw new IllegalArgumentException("Book author cannot be empty");
    }

    this.bookId = bookId;
    this.title = title;
    this.author = author;
}

  
    public int getBookId() {
    return bookId;
}

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }
}