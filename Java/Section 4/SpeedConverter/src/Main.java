public class Main {
    public static void main(String[] args) {
        double kilos = 10.5;
        long miles = SpeedConverter.toMilesPerHour(kilos);
        System.out.println(miles);
        SpeedConverter.printConversion(kilos);
    }
}
