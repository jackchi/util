/**
 * Enum version of Singleton pattern
 */
public enum EnumLogger {
    INSTANCE;

    public void out(String s){
        System.out.println(s);
    }
}
