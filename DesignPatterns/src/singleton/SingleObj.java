package singleton;

import java.util.*;

public class SingleObj {
    public int i;
    SingleObj(){}
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