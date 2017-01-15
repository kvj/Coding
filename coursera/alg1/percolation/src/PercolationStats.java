import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private final double[] data;
    private final int t;

    public PercolationStats(int n, int trials) {
        if (n <= 0) throw new IllegalArgumentException("n <= 0");
        if (trials <= 0) throw new IllegalArgumentException("trials <= 0");
        data = new double[trials];
        this.t = trials;
        for (int i = 0; i < data.length; i++) {
            Percolation p = new Percolation(n);
            while (!p.percolates()) {
                while (true) {
                    int row = StdRandom.uniform(1, n+1);
                    int col = StdRandom.uniform(1, n+1);
                    if (p.isOpen(row, col)) continue;
                    p.open(row, col);
                    break;
                }
            }
            data[i] = (double) p.numberOfOpenSites() / (n * n);
        }
    }

    public double mean() {
        return StdStats.mean(data);
    }

    public double stddev() {
        return StdStats.stddev(data);
    }

    public double confidenceLo() {
        return mean() - (1.96*stddev())/Math.sqrt(t);
    }

    public double confidenceHi() {
        return mean() + (1.96*stddev())/Math.sqrt(t);
    }

    public static void main(String[] args) {
        PercolationStats ps = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        System.out.println("mean                    = "+ps.mean());
        System.out.println("stddev                  = "+ps.stddev());
        System.out.println("95% confidence interval = "+ps.confidenceLo()+", "+ps.confidenceHi());
    }

}
