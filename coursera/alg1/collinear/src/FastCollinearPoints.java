import java.util.*;

public class FastCollinearPoints {

    private final LineSegment[] segments;

    private class SlopeInfo {
        private final Point p;
        private final double s;

        SlopeInfo(Point p, double s) {
            this.p = p;
            this.s = s;
        }
    }

    private void checkInput(Point[] points) {
        if (null == points) throw new NullPointerException("Array is null");
        for (int i = 0; i < points.length; i++) {
            if (points[i] == null) throw new NullPointerException("Point is null");
            for (int j = i+1; j < points.length; j++) {
                if (points[i].compareTo(points[j]) == Double.NEGATIVE_INFINITY) throw new IllegalArgumentException("Points are same");
            }
        }
    }

    public FastCollinearPoints(Point[] points) {
        checkInput(points);
        List<List<Point>> lines = new ArrayList<List<Point>>();
        SlopeInfo[] slopes = new SlopeInfo[points.length-1];
        for (int i = 0; i < points.length; i++) {
            for (int j = 0, idx = 0; j < points.length; j++) {
                if (i == j) continue;
                slopes[idx++] = new SlopeInfo(points[j], points[i].slopeTo(points[j]));
            }
            Arrays.sort(slopes, new Comparator<SlopeInfo>() {
                @Override
                public int compare(SlopeInfo o1, SlopeInfo o2) {
                    if (o1.s == o2.s) return 0;
                    return o1.s>o2.s? 1: -1;
                }
            });
            for (int j = 0; j < slopes.length; j++) {
                for (int k = j+1; k <= slopes.length; k++) {
                    if (k == slopes.length || slopes[j].s != slopes[k].s) {
                        // Last
                        if (k - j >= 3) {
                            boolean notFound = true;
                            for (List<Point> line : lines) {
                                if (line.contains(slopes[j].p) && line.contains(slopes[j+1].p)) {
                                    notFound = false; // Already created
                                    break;
                                }
                            }
                            // Long enough
                            if (notFound) {
                                List<Point> item = new ArrayList<Point>();
                                item.add(points[i]);
                                for (int l = 0; l < k-j; l++) {
                                    item.add(slopes[j+l].p);
                                }
                                lines.add(item);
                            }
                        }
                        break;
                    }
                }
            }
        }
        List<LineSegment> segs = new ArrayList<LineSegment>();
        for (List<Point> list : lines) {
            Collections.sort(list);
            segs.add(new LineSegment(list.get(0), list.get(list.size()-1)));

        }
        this.segments = segs.toArray(new LineSegment[0]);
    }

    public int numberOfSegments() {
        return segments.length;
    }

    public LineSegment[] segments() {
        return segments;
    }
}
