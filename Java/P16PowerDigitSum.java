/*
 * Project Euler Problem 16: Power digit sum
 */

import java.math.BigInteger;

public class P16PowerDigitSum {

	public static void main(String[] args) {
		int a = 2;
		BigInteger bi2 = new BigInteger(String.valueOf(a));
		BigInteger number = bi2.pow(1000);
		int sum = digitSum(number);
		System.out.println("The Power digit sum is: " + sum);
		
	}
		
	static int digitSum(BigInteger num) {
		BigInteger bi0 = new BigInteger("0");
		BigInteger sum = new BigInteger("0");
		BigInteger bi10 = new BigInteger("10");
		
		while (! num.equals(bi0)){
			sum = sum.add(num.mod(bi10));
			num = num.divide(bi10);
		}
		return sum.intValue();
	}
			
}
