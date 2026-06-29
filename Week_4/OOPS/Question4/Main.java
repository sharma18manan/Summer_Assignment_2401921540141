public class Main {

    public static void main(String[] args) {

        Box box = new Box(10, 5);

        box.displayArea();

        Box3D box3d = new Box3D(10, 5, 4);

        box3d.displayArea();

        box3d.displayVolume();
    }
}