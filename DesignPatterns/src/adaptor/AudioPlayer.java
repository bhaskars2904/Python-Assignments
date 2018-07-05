package adaptor;

public class AudioPlayer implements MediaPlayer {

    private MediaAdaptor mediaAdaptor;
    @Override
    public void play(String mediaType, String filename) {
        if(mediaType == "mp3"){
            System.out.println("playing mp3 file "+filename);
        }
        else if(mediaType.equalsIgnoreCase("vlc")||mediaType.equalsIgnoreCase("mp4")){
            mediaAdaptor = new MediaAdaptor(mediaType);
            mediaAdaptor.play(mediaType, filename);
        }
        else{
            System.out.println("invalid type");
        }
    }
}
