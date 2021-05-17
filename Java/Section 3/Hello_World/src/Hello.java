import java.util.Scanner;
public class Hello {
    public static void main(String[] args){
        /** Will ask for a username and then print it */

        Scanner myobj = new Scanner(System.in);
        System.out.println("What is your name ?");
        String name = myobj.nextLine();
        System.out.printf("Hello World this is %s",name);
 }
}