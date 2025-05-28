 import java.util.Scanner;
public class ArrayExample {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 int n;
 System.out.print("Enter the size of the array: ");
 n = sc.nextInt();

 if (n == 0) {
 System.out.println("Array is empty!");
 return;
 }

 int[] arr = new int[n];
 System.out.println("Enter the elements of the array:");
 for (int i = 0; i < n; i++) {
 arr[i] = sc.nextInt();
 }int max = arr[0];
 for (int i = 1; i < n; i++) {
 if (arr[i] > max) {
 max = arr[i];
 }
 }

 System.out.println("Largest number in the array: " + max);
 }
}
