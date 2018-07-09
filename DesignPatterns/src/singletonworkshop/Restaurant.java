package singletonworkshop;

public class Restaurant {
    public static void main(String[] args) {
        Register r1 = Register.getSingleRegister();
        Gatekeeper g1 = new Gatekeeper(1,r1);
        System.out.println("number of guests when g1 taken on is "+g1.trackGuests());
        g1.addGuest();
        System.out.println("number of guests later is "+g1.trackGuests());
        g1.addGuest();
        g1.addGuest();
        System.out.println("number of guests when g1 leaves is "+g1.trackGuests());
        Register r2 = Register.getSingleRegister();
        Gatekeeper g2 = new Gatekeeper(2,r2);
        System.out.println("number of guests when g2 take on is "+g2.trackGuests());
    }
}
