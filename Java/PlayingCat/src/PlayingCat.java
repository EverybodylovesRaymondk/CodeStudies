public class PlayingCat {
    public static boolean isCatPlaying(boolean summer,int temperature){
        int lowerLimit = 25;
        int upperLimit = summer ? 45 : 35; //The "?" is for the value of summer if it summer is yes then it is 45 if no then it is 35

        if (temperature >= lowerLimit && temperature <= upperLimit) {
            return true;
        }
        return false;
    }
}
