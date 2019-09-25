package com.company;

public class Main {

    public static void main(String[] args) {

        int myValue = 10000;
        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntVale = Integer.MAX_VALUE;
        System.out.println("Integer Minimum Value = "+myMinIntValue);
        System.out.println("Integer Maximum Value = "+myMaxIntVale);
       /* System.out.println("Busted MAx value = "+(myMaxIntVale+1));
        System.out.println("Busted Min Value = "+(myMinIntValue -1));

        int myMaxIntTest = 2_147_483_647; //This will cause a error because the value is greater than the max value for the  int data type**/

        byte myMinByteValue=Byte.MIN_VALUE;
        byte myMaxByteValue=Byte.MAX_VALUE;
        System.out.println("Byte Min Value ="+myMinByteValue);
        System.out.println("Byte MAx Value ="+myMaxByteValue);

        short myMinShortValue=Short.MIN_VALUE;
        short myMaxShortValue=Short.MAX_VALUE;
        System.out.println("Short Min Value ="+myMinShortValue);
        System.out.println("Short MAx Value ="+myMaxShortValue);
        
        long myLongValue = 100L;
        long myMinLongValue=Long.MIN_VALUE;
        long myMaxLongValue=Long.MAX_VALUE;
        System.out.println("Long Min Value ="+myMinLongValue);
        System.out.println("Long MAx Value ="+myMaxLongValue);
        long bigLongLiteralValue=2_147_483_647_234L;
        System.out.println(bigLongLiteralValue);
        short bigShortLiteralValue= 32767;

        int myTotal=(myMinIntValue / 2);

        byte myNewByteValue= (byte) (myMinByteValue / 2);

        short myNewShortValue = (short) (myMinShortValue/2);


    }
}
