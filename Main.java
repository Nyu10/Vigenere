public class Main{
    public static void main(String[]args){
        System.out.println(encodeSingle("C","C"));
    }
    public static String encodeSingle(String plainletter, String keyletter){
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int index1= alphabet.indexOf(plainletter);
        int index2=alphabet.indexOf(keyletter);
        int newIndex = (index1+index2) % 26;
        return alphabet.substring(newIndex,newIndex+1);
    }
}