package book_management;

public class Book {
    private int accessionNumber;
    private String title;
    private String author;

    public Book(int accessionNumber, String title, String author) {
    if (accessionNumber <= 0) {
        throw new IllegalArgumentException("Book ID must be positive");
    }

    if (title == null || title.trim().isEmpty()) {
        throw new IllegalArgumentException("Book title cannot be empty");
    }

    if (author == null || author.trim().isEmpty()) {
        throw new IllegalArgumentException("Book author cannot be empty");
    }

    this.accessionNumber = accessionNumber;
    this.title = title;
    this.author = author;
}

    public int getAccessionNumber() {
    return accessionNumber;
}

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }
}