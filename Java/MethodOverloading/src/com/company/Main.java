package com.company;

public class Main {

    public static void main(String[] args) {
        int newscore = calculateScore("Tim", 500);
        System.out.println("New Score is " + newscore);
        calculateScore(75);
        calculateScore();
        calcFeetAndInchesToCentimeters(0, 1);
        calcFeetAndInchesToCentimeters(100);
        //Create a method called calcFeetAndInchesToCentimeters
        // It needs to have 2 parameters (Feet , Inches)
        //Validate that parameter 1 >=0 and parameter 2 >=0 >=12 , return -1 if either is invalid.
        //Calculate how many centimeters comprises the feet and inches as passed and return the calculation results
        //
        //Create a 2nd method with the same name but 1 parameter (inches)
        //Validate that parameter is >=0, Returning -1 if not.
        //Calculate how many feet are in the inches.
        //call the other overloaded method passing the correct feet and inches.
        //Calculate so that it can calculate correctly
        //1 inch = 2.54 cm and 1 foot =12 inches

    }

    public static int calculateScore(String playername, int score) {
        System.out.println("Player " + playername + " scored " + score + "points");
        return score * 1000;
    }

    public static int calculateScore(int score) {
        System.out.println("Unnamed Player " + " scored " + score + " points");
        return score * 1000;

    }

    public static int calculateScore() {
        System.out.println("No player name , no player score  ");
        return 0;
    }

    public static double calcFeetAndInchesToCentimeters(double ft, double in) {
        if ((ft < 0) || ((in < 0) || (in > 12))) {
            System.out.println("Invalid parameters");
            return -1;
        }
        double centimeters = (((ft * 12) * 2.54) + (in * 2.54));

        System.out.println(ft + " Feet " + in + " Inches = " + centimeters + " cm");
        return centimeters;
    }

    public static double calcFeetAndInchesToCentimeters(double in) {
        if (in < 0) {
            return -1;
        }
        double feet = (int) in / 12;
        double remainingInches = (int) in % 12;
        System.out.println(in + " is equal to " + feet + "ft and " + remainingInches + "inches");
        return calcFeetAndInchesToCentimeters(feet, remainingInches);
    }
}
