public class MegaBytesConverter {
    public static void printMegaBytesAndKiloBytes(int kiloBytes) {
        if (kiloBytes >= 0) {
            int megabytes = kiloBytes / 1024;
            int remkb = kiloBytes % 1024;
            System.out.printf("%s KB = %S MB and %s KB", kiloBytes, megabytes, remkb);
        } else {
            System.out.println("Invalid Value");
        }
    }
}