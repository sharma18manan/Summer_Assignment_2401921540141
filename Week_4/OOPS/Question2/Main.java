public class Main {

    public static void main(String[] args) {

        Outer obj = new Outer();
        obj.display();

        Outer.Inner innerObj = obj.new Inner();
        innerObj.display();
    }
}