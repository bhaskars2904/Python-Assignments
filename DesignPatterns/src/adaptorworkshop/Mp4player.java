package adaptorworkshop;

public class Mp4player implements AdvancedMediaPlayer {

    @Override
    public void playvlc(String filename) {

    }

    @Override
    public void playmp4(String filename) {
        System.out.println("playing mp4 file "+filename);
    }
}