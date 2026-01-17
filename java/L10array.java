public class L10array {
    public static void main(String[] args) {
        int  n=4;
        int[] am = new int[n];
        for (int i = 0; i <= n; i++) {
            am[i] = i;
        }
        for (int j = 0; j <= n; j++) {
            System.out.println(am[j]);
        }
    }
}
