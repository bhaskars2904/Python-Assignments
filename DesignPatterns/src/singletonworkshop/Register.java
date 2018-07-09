package singletonworkshop;

public class Register {
    private static Register register;
    private Register(){}
    private int guests;
    public static Register getSingleRegister(){
        if(register == null){
            register = new Register();
        }
        return register;
    }
    public void increaseGuests(){
        guests += 1;
    }
    public int numGuests(){
        return guests;
    }
}
