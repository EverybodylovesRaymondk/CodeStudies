package com.company;

public class Main {

    public static void main(String[] args) {
        System.out.println("10 000 at 2% interest = " + calculateInterest(10000, 2.0));

        for (int i = 0; i < 5; i++) {
            System.out.println("Loop " + i + " Hello!");
        }
        //using the for statement call the calculateInterest method with
        //the amount 10000 with an interestRate of 2,3,4,5,6,7,8
        //and print the results to the console window
        for (int i = 2; i < 9; i++) {
            System.out.println("10 000 at " + i + "% interest = " + String.format("%.2f", calculateInterest(10000, i)));
        }
        System.out.println("**************");
        //How would you modify the for loop above to do the same thing as
        //shown but start at 8% and end at 2%
        for (int i = 8; i >= 2; i--) {
            System.out.println("10 000 at " + i + "% interest = " + String.format("%.2f", calculateInterest(10000, i)));
        }
        System.out.println("************************");
        int count=0;
        for(int i=10; i<50; i++){
            if(isPrime(i)){
                count++;
                System.out.println("Number "+i+" is prime number");
                if(count==10){
                    System.out.println("Exiting for loop");
                    break;
                }
            }
        }
    }

    //Create a for statement using any rage of numbers
    // determine if the number is is a prime number using isPrime method below
    //if it is a prime number, print it out and increment a count of the number of prime numbers found
    //if that count is 3 exit the for loop
    //hint user the break; statement to exit
//------------Supplied Code-------------------
    public static boolean isPrime(int n) {

        if (n == 1) {
            return false;
        }
        for (int i = 2; i <= (long)Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
///----------------------------------------
    public static double calculateInterest(double amount, double interestRate) {
        return Math.round(amount * (interestRate / 100));
    }

}
