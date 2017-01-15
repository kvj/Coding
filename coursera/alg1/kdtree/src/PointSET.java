import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class PointSET {

    private Set<Point2D> set = new TreeSet<Point2D>();

    public PointSET() {}

    public boolean isEmpty() {
        return set.isEmpty();
    }

    public int size() {
        return set.size();
    }

    public void insert(Point2D p) {
        if (p == null)
            throw new NullPointerException("Point is NULL");
        set.add(p);
    }

    public boolean contains(Point2D p) {
        if (p == null)
            throw new NullPointerException("Point is NULL");
        return set.contains(p);
    }

    public void draw() {
        for (Point2D p : set) {
            p.draw();
        }
    }

    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null)
            throw new NullPointerException("Point is NULL");
        List<Point2D> result = new ArrayList<Point2D>();
        for (Point2D p : set) {
            if (rect.contains(p))
                result.add(p);
        }
        return result;
    }

    public Point2D nearest(Point2D p) {
        if (p == null)
            throw new NullPointerException("Point is NULL");
        Point2D result = null;
        double minDist = -1;
        for (Point2D pp : set) {
            double dist = pp.distanceSquaredTo(p);
            if (dist < minDist || minDist == -1) {
                minDist = dist;
                result = pp;
            }
        }
        return result;
    }

    public static void main(String[] args) {
    }
}
