import org.junit.*;
import static org.junit.Assert.*;

/**
 * @author Jack Chi
 * Testing for Singleton uniqueness
 */
public class SingletonTest {
    private StaticLogger oneStatic = null, twoStatic = null;
    private EnumLogger oneEnum =null, twoEnum = null;

    @Before
    public  void setUp() {
        oneStatic = StaticLogger.getInstance();
        twoStatic = StaticLogger.getInstance();
        oneEnum = EnumLogger.INSTANCE;
        twoEnum = EnumLogger.INSTANCE;
    }

    @Test
    public void testStaticUnique() {
        assertTrue(oneStatic == twoStatic);
    }

    @Test
    public void testEnumUnique() {
        assertTrue(oneEnum == twoEnum);
    }

}
