package singletonworkshop;

public class Gatekeeper {
    private int id;
    private Register register;
    Gatekeeper(int id, Register register){
        this.id = id;
        this.register = register;
    }
    public void addGuest(){
        register.increaseGuests();
    }
    public int trackGuests(){
        return register.numGuests();
    }
}
