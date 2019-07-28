/*
 * Project Euler Problem 2: Even Fibonacci numbers
 */

public class P2EvenFibonacciNumbers {

	public static void main(String[] args) {
		int maxFib = 4000000;
		int lenSeq = 100000000;
		int fiboSum = sumEvenValues(lenSeq, maxFib); 
		System.out.println("The fibonacci sum is " + fiboSum);
		
	}
	
	public static int fibonacci(int len_seq) {
		int fibOld = 1;
		int fibNew = 2;
		int result = 1;
		
		for (int i=1; i<=len_seq; i++) {
			result = fibOld + fibNew;
			
			fibOld = fibNew;
			fibNew = result;
			
		}
		
		return fibNew;
	}
		
	public static int sumEvenValues(int lenSeq, int maxFib) {
		int evenSum = 2;
		int i = 1;
		while (i <= lenSeq) {
			int fib = fibonacci(i);
			if (fib >= maxFib) {
				System.out.println("Reached max number ");
				break;
			}
			else if (fib % 2 == 0) {
				evenSum += fib;
			}
			i++;
		}
		return evenSum;
		
	}
		
}
