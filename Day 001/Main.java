public class Main {
    public static void main(String[] args) {
        int[] arr = {3,5,1,6,8,2};
        int Max = arr[0];
        int Min = arr[0];

        for (int num : arr) {
            if (num > Max) Max = num;
            if (num < Min) Min = num;
        }
        System.out.println("Maximum number in this array is "+Max);
        System.out.println("Minimum number in this array is "+Min);
    }
}