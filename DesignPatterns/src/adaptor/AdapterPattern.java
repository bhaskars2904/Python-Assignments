package adaptor;

public class AdapterPattern {
    public static void main(String[] args) {
        MediaPlayer audioPlayer = new AudioPlayer();
        audioPlayer.play("fsvf","111");
        audioPlayer.play("mp3","222");
        audioPlayer.play("mp4", "333");
        audioPlayer.play("vlc", "444");
    }
}
