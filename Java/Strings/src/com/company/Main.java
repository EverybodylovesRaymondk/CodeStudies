package com.company;

public class Main {

    public static void main(String[] args) {
        /*video 31*/
        //byte
        //short
        //int
        //long
        //float
        //double
        //char
        //boolean
        String myString="This is a string";
        System.out.println("myString is equal to "+myString);
        myString = myString + ", this is more.";
        System.out.println("myString is equal to "+myString);
        myString = myString + "\u00a9 2019";
        System.out.println("myString is equal to "+myString);
        String numberString = "250.55";
        numberString=numberString+"49.95";
        System.out.println(numberString);
        String lastString = "10";
        int MyInt = 50;
        lastString=lastString+MyInt;
        System.out.println("LastString is equal to " +lastString);
        double doubleNumber = 120.47d;
        lastString=lastString+doubleNumber;
        System.out.println("LastString is equal to " +lastString);
    }
}
