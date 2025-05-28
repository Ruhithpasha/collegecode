import java.util.Scanner;
public class ExceptionHandlingExample {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 int num1, num2;

 try {
 System.out.print("Enter first number: ");
 num1 = sc.nextInt();
 System.out.print("Enter second number: ");
 num2 = sc.nextInt();
 int result = num1 / num2;
 System.out.println("Result: " + result);
 } catch (ArithmeticException e) {
 System.out.println("Error: Division by zero is not allowed.");
 } catch (Exception e) {
 System.out.println("An error occurred: " + e.getMessage());
 } finally {
 System.out.println("This block always executes.");
 }
 }
}