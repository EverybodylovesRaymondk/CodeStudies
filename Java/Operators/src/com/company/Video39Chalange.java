package com.company;

import com.sun.jdi.Value;

public class Video39Chalange {
    public static void main(String[] args) {
        double myFistValue = 20.00d;
        double mySecondValue = 80.00d;
        double myVauesTotal = (myFistValue + mySecondValue) * 100;
        System.out.println("My Values total = " + myVauesTotal);
        double theRemainder = myVauesTotal % 40.00d;
        System.out.println("Remainder = " + theRemainder);
        boolean isNoRemainder = (theRemainder == 0) ? true : false;
        System.out.println("isNoRemainder = " + isNoRemainder);
        if (!isNoRemainder) {
            System.out.println("Got some remainder");
        }

    }
}