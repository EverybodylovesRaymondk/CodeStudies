public class TeenNumberChecker {
    public static boolean hasTeen(int nr1, int nr2, int nr3){
        if(nr1>=13 && nr1<=19){
            return true;
        }else if(nr2>=13&&nr2<=19){
            return true;
        }else if (nr3>=13&&nr3<=19){
            return true;
        }
        return false;
    }
    public static boolean isTeen(int nr4){
        if(nr4>=13&&nr4<=19){
            return true;
        }return false;
    }
}
