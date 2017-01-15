import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;

import java.util.ArrayList;
import java.util.List;

public class KdTree {

    private static String NAMES = "ABCDEFGHIJKLMNOPQRST";

    private static class Node {
        private final String text;
        private boolean hor = false;
        private final Point2D point;
        private Node left, right = null;

        private Node(Point2D point, Node parent, int index) {
            this.point = point;
            if (parent != null)
                hor = !parent.hor;
            this.text = ""+NAMES.charAt(index % NAMES.length());
        }
    }

    private int size = 0;
    private Node root = null;

    public KdTree() {}

    public boolean isEmpty() {
        return size() == 0;
    }

    public int size() {
        return size;
    }

    private boolean left(Node n, Point2D p) {
        boolean left = n.hor? n.point.y() < p.y(): n.point.x() < p.x();
        return left;
    }

    private boolean add(Point2D p, Node parent) {
        if (p.equals(parent.point))
            return false;
        boolean left = left(parent, p);
        if (left) {
            if (parent.left == null) {
                parent.left = new Node(p, parent, size() + 1);
                return true;
            } else
                return add(p, parent.left);
        } else {
            if (parent.right == null) {
                parent.right = new Node(p, parent, size() + 1);
                return true;
            } else
                return add(p, parent.right);
        }
    }

    public void insert(Point2D p) {
        if (p == null)
            throw new NullPointerException("Point is NULL");
        if (root == null) {
            root = new Node(p, null, 0);
            size += 1;
        } else {
            if (add(p, root))
                size += 1;
        }
    }

    private boolean contains(Point2D p, Node n) {
        if (n == null)
            return false;
        if (n.point.equals(p))
            return true;
        boolean left = left(n, p);
        Node child = left? n.left: n.right;
        return contains(p, child);
    }

    public boolean contains(Point2D p) {
        if (p == null)
            throw new NullPointerException("Point is NULL");
        return contains(p, root);
    }

    private void draw(Node n) {
        if (n == null)
            return;
        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.setPenRadius(0.01);
        n.point.draw();
        StdDraw.text(n.point.x()+0.02, n.point.y()+0.02, n.text);
        StdDraw.setPenRadius(0.001);
        if (n.hor) {
            StdDraw.setPenColor(StdDraw.BLUE);
            StdDraw.line(0, n.point.y(), 1, n.point.y());
        } else {
            StdDraw.setPenColor(StdDraw.RED);
            StdDraw.line(n.point.x(), 0, n.point.x(), 1);
        }
        draw(n.left);
        draw(n.right);
    }

    public void draw() {
        draw(root);
    }

    private void range(RectHV rect, Node n, List<Point2D> result) {
        if (null == n)
            return;
        if (rect.contains(n.point))
            result.add(n.point);
        boolean left1 = n.hor? n.point.y() < rect.ymin(): n.point.x() < rect.xmin();
        boolean left2 = n.hor? n.point.y() < rect.ymax(): n.point.x() < rect.xmax();
        if (left1 || left2)
            range(rect, n.left, result);
        if (!left1 || !left2)
            range(rect, n.right, result);
    }

    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null)
            throw new NullPointerException("Point is NULL");
        List<Point2D> result = new ArrayList<Point2D>();
        range(rect, root, result);
        return result;
    }

    private Point2D nearest(Point2D p, Node n) {
        if (n == null)
            return null;
        Point2D[] points = new Point2D[]{nearest(p, n.left), nearest(p, n.right)};
        double minDist = p.distanceSquaredTo(n.point);
        Point2D result = n.point;
        for (Point2D np : points) {
            if (null == np) continue;
            double dist = p.distanceSquaredTo(np);
            if (dist < minDist) {
                minDist = dist;
                result = np;
            }
        }
        return result;
    }

    public Point2D nearest(Point2D p) {
        if (p == null)
            throw new NullPointerException("Point is NULL");
        return nearest(p, root);
    }
}
