package com.company;

public class Main {

    public static void main(String[] args) {
//        int count = 0;
////        while (count != 6) {
////            System.out.println("Count value is " + count);
////            count++;
////        }
//        count=6;
//        do{
//            System.out.println("Count Value was "+count);
//            count ++;
//            if(count >100){
//                break;
//            }
//        }while (count !=6);
//
//    }
//        int number = 4;
//        int finishNumber = 20;
//
//        while (number <= finishNumber){
//            number ++;
//            if(!isEvenNumber(number)){
//                continue;
//            }
//
//            System.out.println("Even number "+number);
//        }
        //Modify the code above
        //Make it also record the total of even numbers it has found
        //and break once 5 ar found
        //and at the end, display the total number of even numbers found.

        int number = 4;
        int finishNumber = 20;
        int evenNumbersFound = 0;

        while (number <= finishNumber) {
            number++;
            if (!isEvenNumber(number)) {
                continue;
            }
            System.out.println("Even number " + number);
            evenNumbersFound++;
            if (evenNumbersFound >= 5) {
                break;
            }

        }
        System.out.println("Total even numbers found = " + evenNumbersFound);
    }

    //    Create a method called isEvenNumber that takes a parameter of int
//    Its purpose is to determine if the argument passed to the method is an even number or not
//    return true if an even number, other wise return false;
    public static boolean isEvenNumber(int number) {
        if ((number % 2) == 0) {
            return true;
        } else {
            return false;
        }
    }

}