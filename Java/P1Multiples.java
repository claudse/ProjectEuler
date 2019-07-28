/*
 * Project Euler Problem 1: Multiples of 3 and 5
 */

public class P1Multiples {

	public static void main(String[] args) {
		
		int sum = 0;
		
		for (int i = 0; i < 1000; i++) {
			if ((i % 3 == 0) || (i % 5 == 0)) {
				sum += i;
			}
		}
		
		System.out.println("The sum of integer divisible by 3 or 5 below 1000 is: " + sum);

	}

}
