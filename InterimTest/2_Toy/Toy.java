public class Toy {
    private int id;
    private String name;
    private int quantity; 
    private double weight; 

    public Toy(int id, String name, int quantity, double weight) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.weight = weight;
    }

    public String getName() {
        return name;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public int getQuantity() {
        return quantity;
    }


    public void decreaseQuantity() {
        quantity--;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Название: " + name + ", Доступно, шт: " + quantity + ", Вес, %: " + weight;
    }

    public int getId() {
        return 0;
    }
} 
    
