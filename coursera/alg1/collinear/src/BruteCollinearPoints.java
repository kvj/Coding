import java.util.*;

public class BruteCollinearPoints {

    private final LineSegment[] segments;

    private void checkInput(Point[] points) {
        if (null == points) throw new NullPointerException("Array is null");
        for (int i = 0; i < points.length; i++) {
            if (points[i] == null) throw new NullPointerException("Point is null");
            for (int j = i+1; j < points.length; j++) {
                if (points[i].compareTo(points[j]) == Double.NEGATIVE_INFINITY) throw new IllegalArgumentException("Points are same");
            }
        }
    }

    public BruteCollinearPoints(Point[] points) {
        checkInput(points);
        List<List<Point>> lines = new ArrayList<List<Point>>();
        for (int i = 0; i < points.length; i++) {
            for (int j = i+1; j < points.length; j++) {
                double sIJ = points[i].slopeTo(points[j]);
                for (int k = j+1; k < points.length; k++) {
                    double sIK = points[i].slopeTo(points[k]);
                    if (sIJ != sIK) continue;
                    for (int l = k+1; l < points.length; l++) {
                        double sIL = points[i].slopeTo(points[l]);
                        if (sIJ != sIL) continue;
                        boolean newLine = true;
                        for (List<Point> line : lines) {
                            if (line.contains(points[i]) && line.contains(points[j])) {
                                newLine = false;
                                if (!line.contains(points[l]))
                                    line.add(points[l]);
                                break;
                            }
                        }
                        if (newLine) {
                            // Add point
                            List<Point> item = new ArrayList<Point>();
                            item.add(points[i]);
                            item.add(points[j]);
                            item.add(points[k]);
                            item.add(points[l]);
                            lines.add(item);
                        }
                    }
                }
            }
        }
        List<LineSegment> segs = new ArrayList<LineSegment>();
        for (List<Point> list : lines) {
            Collections.sort(list);
//            System.out.println("Line: "+list);
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
