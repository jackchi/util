import java.util.Observer;
import java.util.Observable;

class PostBox extends Observable {

    private String mail;

    public String getMail(){
        return mail;
    }

    public void newMail(String mail){
        this.mail = mail;
        setChanged();
        notifyObservers(mail);
    }

    public static void main(String[] args) {
        PostBox communal = new PostBox();
        PostBox jackBox = new PostBox();
        PostBox hebronBox = new PostBox();
        Resident jack = new Resident("jack");
        Resident hebron = new Resident("hebron");
        communal.addObserver(jack);
        communal.addObserver(hebron);
        jackBox.addObserver(jack);
        hebronBox.addObserver(hebron);
        communal.newMail("Notice to All");
        jackBox.newMail("Notice to Jack");
        hebronBox.newMail("Notice to Hebron");
    }
}

class Resident implements Observer{
    String name  = null;
    public Resident(String name){
        this.name = name;
    }
    @Override
    public void update(Observable o, Object arg) {
        System.out.println(name + ": Mail received: " + arg);
    }
}
