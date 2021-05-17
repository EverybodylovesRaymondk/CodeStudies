package com.company;

public class Main {

    static void Primitive_Types () {
        //Int
        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        System.out.println("Integer Minimum Value = " + myMinIntValue);
        System.out.println("Integer Maximum Value = " + myMaxIntValue);
        System.out.println("Busted Max Value  = " + (myMaxIntValue + 1));
        System.out.println("Busted Mim Value  = " + (myMinIntValue - 1));

        //Byte
        byte myMinByteValue = Byte.MIN_VALUE;
        byte myMaxByteValue = Byte.MAX_VALUE;
        System.out.println("Byte Minimum Value = " + myMinByteValue);
        System.out.println("Byte Minimum Value = " + myMaxByteValue);

        //Short
        short myMinShortValue = Short.MIN_VALUE;
        short myMaxShortValue = Short.MAX_VALUE;
        System.out.println("Short Minimum Value = " + myMinShortValue);
        System.out.println("Short Minimum Value = " + myMaxShortValue);

        //Long
        long myMinLongValue = Long.MIN_VALUE;
        long myMaxLongValue = Long.MAX_VALUE;
        System.out.println("Long Minimum Value = " + myMinLongValue);
        System.out.println("Long Minimum Value = " + myMaxLongValue);
    }

    static void Primitive_Types_Challenge () {

        //Byte
        byte myByteValue = 10;

        //Short
        short myShortValue = 20;

        //Int
        int myIntValue = 50;

        //Long
        long myLongValue = 50000 + (10 * (myByteValue + myShortValue + myIntValue));
        System.out.println("Primitive_Types_Challenge total = " + myLongValue);

    }

    static void Float_Double () {
        //Float
        float myMinFloat = Float.MIN_VALUE;
        float myMaxFloat = Float.MAX_VALUE;
        System.out.println("Min Float Value = " + myMinFloat);
        System.out.println("Max Float Value = " + myMaxFloat);

        //Double
        double myMinDouble = Double.MIN_VALUE;
        double myMaxDouble = Double.MAX_VALUE;
        System.out.println("Min Double Value = " + myMinDouble);
        System.out.println("Max Double Value = " + myMaxDouble);


    }

    static void Float_Double_Challenge () {
        /**Convert lbs to kg*/
        double pounds = 50.27;
        double kg = pounds * 0.45359237;
        System.out.println(kg);
    }

    static void Char_Boolean (){
        //Char
        char myChar = 'D';

        //Boolean
        boolean myTrueBool = true;
        boolean myFalseBool = false;
    }


    public static void main(String[] args) {
        Primitive_Types();
        System.out.println("############################################");
        Primitive_Types_Challenge();
        System.out.println("############################################");
        Float_Double();
        System.out.println("############################################");
        Float_Double_Challenge();
        System.out.println("############################################");
        Char_Boolean();

    }
}
