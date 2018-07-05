package singleton;

import java.util.*;

public class SingleObj {
    private static  SingleObj instance;
    public int i;
    private SingleObj(){
        //Private constructor that prevents outside world from instantiating it
      System.out.println("Singleton object constructor");
    };
    public static SingleObj getInstance(){
        if(instance == null){
            instance = new SingleObj();
        }
        return instance;
    }
}


//public class SingleObj{
//    private static SingleObj instance;
//    private List<Integer> list = new ArrayList<>();
//
//    private SingleObj(){
//
//    }
//
//    public static SingleObj getInstance(){
//        if(instance==null){
//
//            synchronized (SingleObj.class){
//                //sleep
//                if(instance==null)
//                    instance = new SingleObj();
//            }
//        }
//        return instance;
//    }
//
//    void addTrack(int track){
//        list.add(track);
//    }
//
//    public List<Integer> getList() {
//        return list;
//    }
//}