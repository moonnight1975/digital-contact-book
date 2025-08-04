import java.util.*;
public class contact {

    public static void add_contact(Scanner sc){
        
        System.out.println("Enter name: ");
        String name = sc.next();
        System.out.print("Enter phone number: ");
        int phone = sc.nextInt();
        System.out.println("Enter email: ");
        String email =sc.next();
         System.out.println("Adding a new contact...");
        System.out.println("Contact added: " + name + ", " + phone+","+email);
        System.out.println();
       
    }

    public static void remove_contact(Scanner sc){
        System.out.println("Removing a contact...");

    }
    public static void list_contacts(int contactCount, Scanner sc){
         System.out.println("No contacts found.");
         System.out.println("Do you want to add a contact? ");
        System.out.println("1. Yes");
        System.out.println("2. No");
        System.out.print("Enter your choice: ");
        int choice = sc.nextInt();
        if (choice == 2) {
        add_contact(sc);
        if (contactCount == 0) {
           
        } else {
            System.out.println("Listing all contacts...");
        }}

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ch;
        System.out.println("=== CONTACT ===");
        System.out.println("1. Add Contact");
        System.out.println("2. Remove Contact");
        System.out.println("3. List Contacts");
        System.out.println("4. Exit");
        System.out.print("Enter your choice: ");
        ch=sc.nextInt();

        
        switch(ch){
            case 1:
            add_contact(sc);
            break;

            case 2:
            remove_contact(sc);
            break;

            case 3:
            list_contacts(0, sc);
            break;

            case 4:
            System.out.println("Exiting...");
            System.exit(0);
                break;

                default:
            System.out.println("Invalid choice!! Please try again : )");
        }

    }
}