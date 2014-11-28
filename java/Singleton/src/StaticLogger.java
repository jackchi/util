
/**
 * Singleton Pattern with static factory
 */
public class StaticLogger {

    private static final StaticLogger INSTANCE = new StaticLogger(); // only place for constructor
    private StaticLogger() { }

    public static StaticLogger getInstance() {
        return INSTANCE;
    }
    public void out(String s){
        System.out.println(s);
    }
}

