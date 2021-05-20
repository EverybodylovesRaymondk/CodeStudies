package com.company;

public class Main {
    static void stringData (){
        String myString = "This is a string";
        System.out.println("myString is equal to " + myString);
        myString = myString + ", and this is more";
        System.out.println("myString is equal to " + myString);
        myString = myString + " \u00A9 2017";
        System.out.println("myString is equal to " + myString);

        String numberString = "250.55";
        numberString = numberString + "/49.95";
        System.out.println(numberString);

        String lastString = "10";
        int myInt = 50;
        lastString = lastString + myInt;
        System.out.println("LastString is equal to " + lastString);
        System.out.printf("Last sting = %s",(String)lastString);
    }

    public static void main(String[] args) {
	stringData();
    }
}
