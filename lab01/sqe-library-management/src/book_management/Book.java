package book_management;

public class Book {
    private int id;
    private String title;
    private String author;

    public Book(int id, String title, String author) {
    if (id <= 0) {
        throw new IllegalArgumentException("Book ID must be positive");
    }

    if (title == null || title.trim().isEmpty()) {
        throw new IllegalArgumentException("Book title cannot be empty");
    }

    if (author == null || author.trim().isEmpty()) {
        throw new IllegalArgumentException("Book author cannot be empty");
    }

    this.id = id;
    this.title = title;
    this.author = author;
}

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }
}