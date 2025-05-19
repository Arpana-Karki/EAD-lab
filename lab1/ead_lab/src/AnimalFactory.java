//Factory Pattern

public class AnimalFactory {
    public Animal getAnimal(String type) {
        if (type.equalsIgnoreCase("dog")) return new Dog();
        if (type.equalsIgnoreCase("cat")) return new Cat();
        return null;
    }
}
