public class Percolation {

    private final int[] arr;
    private final int n;
    private int opened = 0;

    public Percolation(int n) {
        if (n <= 0)
            throw new IllegalArgumentException("n <= 0");
        arr = new int[n*n + 2];
        this.n = n;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1; // No connections
        }
        arr[0] = 0; // Open top
        arr[arr.length-1] = arr.length-1; // Open bottom
    }

    private void checkRowCol(int row, int col) {
        if (row < 1 || row > n)
            throw new IndexOutOfBoundsException("row is out of bounds: "+row);
        if (col < 1 || col > n)
            throw new IndexOutOfBoundsException("col is out of bounds: "+col);
    }

    private int rowColToIndex(int row, int col) {
        return 1 + (row-1)*n + (col-1);
    }

    private int root(int idx) {
        // Find root of tree
        while (arr[idx] != idx)
            idx = arr[idx];
        return idx;
    }

    private void union(int p, int q) {
        int rp = root(p);
        int rq = root(q);
        if (rq < rp)
            arr[rp] = rq;
        else
            arr[rq] = rp;
    }

    public void open(int row, int col) {
        if (isOpen(row, col)) return; // No action necessary
        int idx = rowColToIndex(row, col);
        arr[idx] = idx; // Open
        if (row > 1 && isOpen(row-1, col))
            union(idx, rowColToIndex(row-1, col));
        if (row < n && isOpen(row+1, col))
            union(idx, rowColToIndex(row+1, col));
        if (col > 1 && isOpen(row, col-1))
            union(idx, rowColToIndex(row, col-1));
        if (col < n && isOpen(row, col+1))
            union(idx, rowColToIndex(row, col+1));
        if (row == 1)
            arr[idx] = 0; // Top
        if (row == n) {
            if (arr[idx] < arr[arr.length-1])
                arr[arr.length-1] = arr[idx];
        }
        opened += 1; // New opened
    }

    public boolean isOpen(int row, int col) {
        checkRowCol(row, col);
        return arr[rowColToIndex(row, col)] != -1;
    }

    public boolean isFull(int row, int col) {
        if (!isOpen(row, col))
            return false;

        int r = root(rowColToIndex(row, col));
        return r == 0; // top and this are connected
    }

    public int numberOfOpenSites() {
        return opened;
    }

    public boolean percolates() {
        int r0 = root(0);
        int rl = root(arr.length-1);
        return r0 == rl; // top and bottom have same root
    }

    public static void main(String[] args) {
        Percolation p = new Percolation(3);
        p.open(1, 1);
        System.out.println("1, 1 "+p.percolates());
        p.open(2, 2);
        System.out.println("1, 1 "+p.percolates());
        p.open(3, 2);
        System.out.println("1, 1 "+p.percolates());
        p.open(2, 1);
        System.out.println("1, 1 "+p.percolates());
    }
}
