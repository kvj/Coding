import edu.princeton.cs.algs4.StdIn;

public class Permutation {

    public static void main(String[] args) {
        int k = Integer.parseInt(args[0]);
        String[] strs = StdIn.readString().split(" ");
        RandomizedQueue<String> q = new RandomizedQueue<String>();
        for (String s : strs) {
            q.enqueue(s);
        }
        int i = 0;
        for (String s : q) {
            if (i > k) break;
            System.out.println(s);
            i += 1;
        }
    }

}
