public class Hello {


    public static void main(String[] args){
//        System.out.println("Hello, Raymond");
        int myFirstNumber = (10+5)+(2*10);
        int mySecondNumber = 12;
        int myThirdNumber = myFirstNumber * 2;
        int myTotal= myFirstNumber + mySecondNumber + myThirdNumber;
//        System.out.println("The Total : "+ myTotal);
//        int myLastOne= 1000- myTotal;
//        System.out.println("Last Total : "+myLastOne);
        System.out.printf("Hello %s, this is %s your numbers are as follow: \n1) %s\n2) %s\n3) %s\n",
                "Raymond","Josh",myFirstNumber,mySecondNumber,myThirdNumber);
        System.out.printf("The total is %s",myTotal);;
    }
}
