public class DecimalComparator {
    public static boolean areEqualByThreeDecimalPlaces(double nr1 , double nr2){
        nr1=(int)(nr1*1000);
        nr2=(int)(nr2*1000);
        if(nr1 == nr2){
            return true;
        }return false;

    }
}
