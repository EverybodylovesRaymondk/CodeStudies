package com.company;

import java.sql.SQLOutput;

public class Main {

    public static void main(String[] args) {

        float myMinFloatValue = Float.MIN_VALUE;
        float myMAXFloatValue = Float.MAX_VALUE;
        System.out.println("Float minimum value = "+myMinFloatValue);
        System.out.println("Float maximum value = "+myMAXFloatValue);

        double myMinDoubleValue = Double.MIN_VALUE;
        double myMAXDoubleValue = Double.MAX_VALUE;
        System.out.println("Double minimum value = "+myMinDoubleValue);
        System.out.println("Double maximum value = "+myMAXDoubleValue);

        int myIntValue=5/3;
        float myFloatValue=5f/3f;
        double myDoubleValue=5.00/3.00;
        System.out.println("myIntValue = " +myIntValue);
        System.out.println("myFloatValue = " +myFloatValue);
        System.out.println("myDoubleValue = " +myDoubleValue);

        double numberOfPounds=200d;
        double convertedKilograms = numberOfPounds * 0.45359237d;
        System.out.println("Converted kilograms= " + convertedKilograms );

        double pi = 3.1415927d;
        double anotherNumber =3_000_000.4_567_890d;
        System.out.println(pi);
        System.out.println(anotherNumber);

    }
}
