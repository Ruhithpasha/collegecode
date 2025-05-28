public class StringmanipulationExample {
    public static void main(String[] args) {
    String str = "Hello, Java Programming!";
   
    // Concatenation
    String concatenated = str + " Welcome to Java!";
   
    // Length of the string
    int length = str.length();
   
    // Uppercase and Lowercase
    String upperCase = str.toUpperCase();
    String lowerCase = str.toLowerCase();
   
    // Substring
    String subString = str.substring(7, 12); // Extracting "Java"
   
    System.out.println("Concatenated String: " + concatenated);
    System.out.println("Length of the string: " + length);
    System.out.println("Uppercase: " + upperCase);
    System.out.println("Lowercase: " + lowerCase);
    System.out.println("Substring (7, 12): " + subString);
    }
   }