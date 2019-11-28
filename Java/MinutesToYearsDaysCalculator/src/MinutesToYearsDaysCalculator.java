public class MinutesToYearsDaysCalculator {

    private static String INVALID_MESSAGE = "Invalid Value";
    private static long MINUTES_IN_A_YEAR = (365 * 24 * 60);
    private static long MINUTES_IN_A_DAY = (24 * 60);

    public static void printYearsAndDays(long minutes) {
        if (minutes >= 0) {
            long year = minutes / MINUTES_IN_A_YEAR;
            long days = (minutes % MINUTES_IN_A_YEAR) / MINUTES_IN_A_DAY;
            System.out.println(minutes + " min " + "= " + year + " y and " + days + " d");
        } else System.out.println(INVALID_MESSAGE);
    }

}
