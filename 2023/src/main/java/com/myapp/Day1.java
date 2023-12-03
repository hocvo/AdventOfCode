package com.myapp;

/**
 * Hello world!
 *
 */
public class Day1 
{
    public static String []digitsString = {"zero", "one", "two", "three","four", "five", "six", "seven", "eight", "nine"};
    public static String []digits = {"0","1","2","3","4","5","6","7","8","9"};
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        part1();
        part2();
    }
    public static void part2() {
        int sum = 0;
        for (String s : Utils.parseInput("day1.txt")) {
            int num = 0;

            // find first digit
            int first = Integer.MAX_VALUE;
            int temp = 0;
            for (int i = 0; i < digitsString.length; i++) {
                int curIndex = s.indexOf(digitsString[i]);
                if (curIndex == -1 ) continue;
                if (curIndex < first) {
                    // save the new index and store the digit as integer
                    first = curIndex;
                    temp = i;
                }
            }
            for (int i = 0; i < digits.length; i++) {
                int curIndex = s.indexOf(digits[i]);
                if (curIndex == -1 ) continue;
                if (curIndex < first) {
                    // save the new index and store the digit as integer
                    first = curIndex;
                    temp = i;
                }
            }
            num += temp * 10;
            
            // find last digit
            temp = 0;
            int lastIndex = -1; // keep track of the last index
            for (int i = 0; i < digitsString.length; i++) {
                int curIndex = s.lastIndexOf(digitsString[i]);
                if (curIndex == -1) continue;
                if (curIndex > lastIndex) {
                    // save the new index and store the digit as integer
                    lastIndex = curIndex;
                    temp = i;
                }
            }
            for (int i = 0; i < digits.length; i++) {
                int curIndex = s.lastIndexOf(digits[i]);
                if (curIndex == -1) continue;
                if (curIndex > lastIndex) {
                    // save the new index and store the digit as integer
                    lastIndex = curIndex;
                    temp = i;
                }
            }
            num += temp;
            sum += num;
        }
        System.out.println(sum);
    }
    public static void part1() {
        int sum = 0;
        for (String s : Utils.parseInput("day1.txt")) {
            int num = 0;
            char[] allChar = s.toCharArray();
            for (char c : allChar) {
                if (Character.isDigit(c) ) {
                    num += Integer.valueOf(String.valueOf(c)) *10;
                    break;
                }
            }
            for (int i = allChar.length-1; i >= 0 ; i--) {
                char c = allChar[i];
                if (Character.isDigit(c) ) {
                    num += Integer.valueOf(String.valueOf(c));
                    break;
                }
            }
            sum += num;
        }
        System.out.println(sum);
    }

}
