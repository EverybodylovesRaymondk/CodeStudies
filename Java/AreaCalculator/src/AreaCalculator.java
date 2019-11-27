public class AreaCalculator {
    private static double INVALID_VALUE = -1;

    public static double area(double radius) {
        if (radius < 0) {
            return INVALID_VALUE;
        }
        double area = Math.pow(radius, 2) * Math.PI;
        return area;
    }

    public static double area(double x, double y) {
        if (x < 0 || y < 0) {
            return INVALID_VALUE;
        }
        double area = x * y;
        return area;
    }
}
