public class TestCompartment
{
    public static void main(String[] args)
    {
        Compartment arr[] = new Compartment[10];

        for(int i = 0; i < 10; i++)
        {
            int n = (int)(Math.random() * 4) + 1;

            if(n == 1)
            {
                arr[i] = new FirstClass();
            }
            else if(n == 2)
            {
                arr[i] = new Ladies();
            }
            else if(n == 3)
            {
                arr[i] = new General();
            }
            else
            {
                arr[i] = new Luggage();
            }

            System.out.println(arr[i].notice());
        }
    }
}