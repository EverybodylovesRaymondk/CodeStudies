public class IntEqualityPrinter {

    public static String INVALID_INPUT = "Invalid Value";
    public static String ALL_THE_SAME = "All numbers are equal";
    public static String ALL_DIFFERENT = "All numbers are different";

    public static void printEqual(int firstValue, int secondVale, int thirdValue) {
        if ((firstValue < 0) || (secondVale < 0) || (thirdValue < 0)) {
            System.out.println(INVALID_INPUT);
        } else if (firstValue == secondVale && secondVale == thirdValue) {
            System.out.println(ALL_THE_SAME);
        } else if (firstValue != secondVale && secondVale != thirdValue && firstValue!=thirdValue) {
            System.out.println(ALL_DIFFERENT);
        } else System.out.println("Neither all are equal or different");
    }
}
