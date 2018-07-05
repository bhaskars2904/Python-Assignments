package adaptor;

public class VlcPlayer implements AdvancedMediaPlayer {
    @Override
    public void playvlc(String filename) {
        System.out.println("playing vlc file "+filename);
    }

    @Override
    public void playmp4(String filename) {

    }
}
