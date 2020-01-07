package com.company;

public class Main {

    public static void main(String[] args) {
        // Create a for statement using a rage of numbers from 1 to 1000 inclusive
        //Sum all the numbers that can be divided by 3 and also 5
        //For those numbers that met the above condition, print out the number.
        //break out of the loop once you find 5 numbers that meet the conditions
        //After breaking ot of the loop print the sum of the numbers that met the above conditions.
        int count = 0;
        int sum =0;

        for(int i=1;1<=1000;i++){
            if((i%3==0)&&(i%5==0)){
                count++;
                sum +=i;
                System.out.println("Found Number = "+i);
            }
            if (count == 5){
                break;
            }
        }
        System.out.println("Sum = "+sum);
    }

}
