package com.company;

public class Main {

    static void operator() {
        // Normal operators
        int result = (1 + 2) * 10 / 2;
        System.out.println(result);

        // Remainder operator
        int Rresult = 7 % 3;
        System.out.println(Rresult);
        System.out.printf("The remainder of 7 / 3 =%s", Rresult);

    }

    static void operator_shorthand() {
        int result = 1;

        // adding 2 (1+2 = 3)
        result += 2;
        System.out.println(result);

        // subtracting 1 (3-1=2)
        result--;
        System.out.println(result);

        // Multiply by 10 (2*10=20)
        result *= 10;
        System.out.println(result);

        //Dividing by 5 (20/5 =4)
        result /= 5;
        System.out.println(result);
    }

    static void if_else() {
        boolean isAlien = false;
        if (isAlien == false) {
            System.out.println("It is not an alien!!\n");
            System.out.println("I'm scarred!!");
        } else {
            System.out.println("it is an alien");
        }

        int topScore = 100;
        if (topScore == 100) {
            System.out.println("You have top score");
        }
        // And &&
        int secondTopScore = 60;
        if ((topScore > secondTopScore) && (topScore < 110)) {
            System.out.println("Greater than second top score and less than 110");
        }
        // Or ||
        if ((topScore > 90) || (secondTopScore >= 110)) {
            System.out.println("Either or both of the conditions are true");
        }
    }

    static void ternary() {

        /** Create the isCar variable as false, then create wasCar as a check on isCar if it was then true else false*/

        boolean isCar = false;
        boolean wasCar = isCar ? true : false;
        if (wasCar) {
            System.out.println("It was a car");
        } else {
            System.out.println("It was not a car");
        }
    }

    static void operator_challenge() {
        double val1 = 20.00;
        double val2 = 80.00;
        double val3 = (val1 + val2) * 100.00;
        double val4 = val3 % 40.00;
        boolean val5 = (val4 == 0) ? true : false;
        System.out.println(val5);

        if (!val5) {
            System.out.println("Got some remainder");
        } else {
            System.out.println("No remainder");
        }
    }

    public static void main(String[] args) {
        operator();
        System.out.println('\n');
        operator_shorthand();
        System.out.println('\n');
        if_else();
        System.out.println('\n');
        ternary();
        System.out.println('\n');
        operator_challenge();
    }
}