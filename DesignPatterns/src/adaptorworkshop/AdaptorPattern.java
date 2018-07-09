package adaptorworkshop;

public class AdaptorPattern {
    public static void main(String[] args) {
        MediaPlayer mediaPlayer = new AudioPlayer();
        mediaPlayer.play("fsvf","111");
        mediaPlayer.play("mp3","222");
        mediaPlayer.play("mp4", "333");
        mediaPlayer.play("vlc", "444");
    }
}
