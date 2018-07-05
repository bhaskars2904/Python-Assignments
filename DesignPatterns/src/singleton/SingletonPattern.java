package singleton;

public class SingletonPattern {
    public static void main(String[] args) {
        s1.i = 1;
        s2.i = 2;
        System.out.println("s1.i = "+s1.i);
        System.out.println("s2.i = "+s2.i);
    }
    static SingleObj s1 = SingleObj.getInstance();
    static SingleObj s2 = SingleObj.getInstance();
}

//public class SingletonPattern {
//    public static void main(String[] args) {
//        SingleObj o1 = SingleObj.getInstance();
//        SingleObj o2 = SingleObj.getInstance();
//
//        Register r1 = new Register(o1, 4);
//        Register r2 = new Register(o2, 5);
//
//        r1.register();
//        r2.register();
//
//        System.out.println(o1.getList());
//        System.out.println(o2.getList());
//
//    }
//}
//
//class Register{
//    private final int id;
//    private SingleObj manager;
//    Register(SingleObj manager, int id){
//        this.manager = manager;
//        this.id = id;
//    }
//
//    void register(){
//        manager.addTrack(id);
//    }
//}
