import org.junit.*;

import static org.junit.Assert.*;

public class PostalServiceTest {
    private PostBox communal = new PostBox(), jackBox = new PostBox(), hebronBox = new PostBox();
    private Resident jack = new Resident("jack"), hebron = new Resident("hebron");

    @Before
    public void setUp() throws Exception {
        communal.addObserver(jack);
        communal.addObserver(hebron);
        jackBox.addObserver(jack);
        hebronBox.addObserver(hebron);
    }

    @Test
    public void testMultipleObservers(){
        communal.newMail("both");
        assertEquals(jack.mail, "both");
        assertEquals(hebron.mail, "both");
    }

    @Test
    public void testUniqueSetObservers(){
        communal.addObserver(jack); // should still be 2
        assertEquals(communal.countObservers(), 2);
        assertEquals(jackBox.countObservers(), 1);
    }

    @Test
    public void testSingleObserver(){
        hebronBox.newMail("for hebron");
        assertEquals(hebron.mail, "for hebron");
    }
}