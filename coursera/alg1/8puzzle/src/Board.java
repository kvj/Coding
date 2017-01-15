import java.util.ArrayList;
import java.util.List;

public class Board {

    private final int[][] board;

    public Board(int[][] blocks) {
        if (null == blocks)
            throw new NullPointerException("Argument is NULL");
        this.board = new int[blocks.length][blocks.length];
        for (int i = 0; i < blocks.length; i++) {
            for (int j = 0; j < blocks.length; j++) {
                this.board[i][j] = blocks[i][j];
            }
        }
    }

    public int dimension() {
        return board.length;
    }

    private boolean ok(int v) {
        if (v < 0) return false;
        if (v >= dimension()) return false;
        return true;
    }

    private boolean ok(int i, int j) {
        return ok(i) && ok(j);
    }

    private int[] correct(int v) {
        // Return right position for value
        return new int[]{(v-1) / dimension(), (v-1) % dimension()};
    }

    public int hamming() {
        int r = 0;
        for (int i = 0; i < dimension(); i++) {
            for (int j = 0; j < dimension(); j++) {
                if (board[i][j] == 0) continue;
                int[] c = correct(board[i][j]);
                if (c[0] != i || c[1] != j)
                    r += 1;
            }
        }
        return r;
    }

    private int abs(int v) {
        if (v < 0) return -v;
        return v;
    }

    public int manhattan() {
        int r = 0;
        for (int i = 0; i < dimension(); i++) {
            for (int j = 0; j < dimension(); j++) {
                if (board[i][j] == 0) continue;
                int[] c = correct(board[i][j]);
                r += abs(c[0] - i) + abs(c[1] - j);
            }
        }
        return r;
    }

    public boolean isGoal() {
        return hamming() == 0;
    }

    public Board twin() {
        for (int i = 0; i < dimension(); i++) {
            for (int j = 0; j < dimension(); j++) {
                if (board[i][j] != 0) {
                    int[][] moves = {{i-1, j}, {i+1, j}, {i, j-1}, {i, j+1}};
                    for (int[] move : moves) {
                        if (ok(move[0], move[1]) && board[move[0]][move[1]] != 0) {
                            // New Board and exchange
                            Board b = new Board(board);
                            b.board[move[0]][move[1]] = board[i][j];
                            b.board[i][j] = board[move[0]][move[1]];
                            return b;
                        }
                    }
                }
            }
        }
        return this;
    }

    @Override
    public boolean equals(Object obj) {
        if (null == obj) return false;
        if (!obj.getClass().equals(getClass()))
            return false;
        Board b = (Board) obj;
        if (b.dimension() != dimension()) return false;
        for (int i = 0; i < dimension(); i++) {
            for (int j = 0; j < dimension(); j++) {
                if (board[i][j] != b.board[i][j]) return false;
            }
        }
        return true;
    }

    public Iterable<Board> neighbors() {
        List<Board> boards = new ArrayList<Board>();
        for (int i = 0; i < dimension(); i++) {
            for (int j = 0; j < dimension(); j++) {
                if (board[i][j] == 0) {
                    int[][] moves = {{i-1, j}, {i+1, j}, {i, j-1}, {i, j+1}};
                    for (int[] move : moves) {
                        if (ok(move[0], move[1])) {
                            // New Board and exchange
                            Board b = new Board(board);
                            b.board[move[0]][move[1]] = 0;
                            b.board[i][j] = board[move[0]][move[1]];
                            boards.add(b);
                        }
                    }
                    break;
                }
            }
        }
        return boards;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(dimension());
        sb.append('\n');
        for (int i = 0; i < dimension(); i++) {
            for (int j = 0; j < dimension(); j++) {
                sb.append(String.format("%2d  ", board[i][j]));
            }
            sb.append('\n');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
    }
}
