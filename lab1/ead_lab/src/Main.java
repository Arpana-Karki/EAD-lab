// Design Patterns

public class Main {
   
    //for Singeleton Design Pattern
    public static void main(String[] args) {
        DatabaseHelper dbHelper = DatabaseHelper.getInstance();
         System.out.println("DatabaseHelper instance: " + dbHelper);
     
        //for Factory Design Pattern
        AnimalFactory factory = new AnimalFactory();

        Animal a1 = factory.getAnimal("dog");
        a1.speak();  // Woof!

        Animal a2 = factory.getAnimal("cat");
        a2.speak();  // Meow!
    }
}
