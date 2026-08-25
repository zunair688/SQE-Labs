import member_management.Member;

public class testCase {

    public static void main(String[] args) {

        // Test duplicate member ID
        Member member1 = new Member(101, "Ali");

        try {
            Member member2 = new Member(101, "Ahmed");
            System.out.println("FAIL: Duplicate member ID was accepted.");
        } catch (IllegalArgumentException e) {
            System.out.println("PASS: Duplicate member ID was rejected.");
        }

        // Test case-insensitive name matching
        if (member1.matchesName("ali")) {
            System.out.println("PASS: Lowercase name search works.");
        } else {
            System.out.println("FAIL: Lowercase name search failed.");
        }

        if (member1.matchesName("ALI")) {
            System.out.println("PASS: Uppercase name search works.");
        } else {
            System.out.println("FAIL: Uppercase name search failed.");
        }

        // Test borrowing limit
        try {
            member1.addBook(new book_management.Book(1, "Book One", "Author"));
            member1.addBook(new book_management.Book(2, "Book Two", "Author"));
            member1.addBook(new book_management.Book(3, "Book Three", "Author"));
            member1.addBook(new book_management.Book(4, "Book Four", "Author"));

            System.out.println("FAIL: Fourth book was accepted.");
        } catch (IllegalArgumentException e) {
            System.out.println("PASS: Fourth book was rejected.");
        }
    }
}
