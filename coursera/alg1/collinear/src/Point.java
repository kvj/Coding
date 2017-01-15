import edu.princeton.cs.algs4.StdDraw;

import java.util.Comparator;

public class Point implements Comparable<Point> {

    private final int x;
    private final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void draw() {
        StdDraw.point(x, y);
    }

    public void drawTo(Point that) {
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    public double slopeTo(Point that) {
        if (x == that.x) {
            return y == that.y? Double.NEGATIVE_INFINITY: Double.POSITIVE_INFINITY;
        }
        if (y == that.y) return 0.0;
        int c = compareTo(that); // Keep order
        return c >0 ? (double) (that.y - y) / (double) (that.x - x): (double) (y - that.y) / (double) (x - that.x);
    }

    @Override
    public int compareTo(Point that) {
        if (that.y == y) {
            return x - that.x;
        }
        return y - that.y;
    }

    public Comparator<Point> slopeOrder() {
        return new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                double s1 = slopeTo(o1);
                double s2 = slopeTo(o2);
                if (s1 == s2) return 0;
                return s1 > s2? 1: -1;
            }
        };
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
    }

}
