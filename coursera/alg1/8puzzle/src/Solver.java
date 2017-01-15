import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Solver {

    private final List<Board> solution;

    private static class Node {

        private final Board board;
        private final int moves;
        private final Node prev;

        private Node(Board board, int moves, Node prev) {
            this.board = board;
            this.moves = moves;
            this.prev = prev;

        }
        private int priority() {
            return moves + board.manhattan();
        }
    }

    private static class NodePQ extends MinPQ<Node> {
        private NodePQ(Board initial) {
            super(new Comparator<Node>() {
                @Override
                public int compare(Node o1, Node o2) {
                    return o1.priority() - o2.priority();
                }
            });
            insert(new Node(initial, 0, null));
        }
    }

    public Solver(Board initial) {
        this.solution = solve(initial);
    }

    private Node next(NodePQ pq, List<Board> list) {
        Node s = pq.delMin();
        if (null != list)
            list.add(s.board);
        if (s.board.isGoal())
            return s; // Found solution
        for (Board n : s.board.neighbors()) {
            if (null != s.prev && s.prev.board.equals(n))
                continue; // Skip prev
            pq.insert(new Node(n, s.moves+1, s));
        }
        return null;
    }

    private List<Board> solve(Board initial) {
        Board twin = initial.twin();
        NodePQ pq = new NodePQ(initial);
        NodePQ pqTwin = new NodePQ(twin);
        List<Board> list = new ArrayList<Board>();
        while (true) {
            Node s = next(pq, list);
            Node sTwin = next(pqTwin, null);
            if (s != null)
                return list; // Found solution
            if (sTwin != null)
                return null; // Not solvable
        }
    }

    public boolean isSolvable() {
        return null != solution;
    }

    public int moves() {
        return null != solution ? solution.size()-1 : -1;
    }

    public Iterable<Board> solution() {
        return solution;
    }

    public static void main(String[] args) {
//        Board b = new Board(new int[][] {{0, 1, 3}, {4, 2, 5}, {7, 8, 6}});
//        Board b = new Board(new int[][] {{1, 2, 3}, {4, 5, 6}, {8, 7, 0}});
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] blocks = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);
        Solver s = new Solver(initial);
        if (s.isSolvable()) {
            System.out.println("Minimum number of moves = "+s.moves());
            for (Board bb : s.solution()) {
                System.out.println(bb);
            }
        } else {
            System.out.println("No solution possible");
        }
    }
}
