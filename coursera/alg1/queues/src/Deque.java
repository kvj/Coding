import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

    private class Node {

        Node(Item data) {
            this.data = data;
        }

        Item data;
        Node left = null;
        Node right = null;
    }

    private Node head = null;
    private Node tail = null;
    private int size = 0;

    public Deque() {

    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public int size() {
        return size;
    }

    private Node add(Item item) {
        if (item == null)
            throw new NullPointerException("Item is NULL");
        Node n = new Node(item);
        if (size() == 0) {
            head = tail = n;
            n = null;
        }
        size += 1;
        return n;
    }

    public void addFirst(Item item) {
        Node n = add(item);
        if (n != null) {
            n.right = head;
            head.left = n;
            head = n;
        }
    }

    public void addLast(Item item) {
        Node n = add(item);
        if (n != null) {
            n.left = tail;
            tail.right = n;
            tail = n;
        }
    }

    private void remove() {
        if (isEmpty())
            throw new NoSuchElementException("Queue is empty");
        size -= 1;
    }

    public Item removeFirst() {
        remove();
        Node n = head;
        head = head.right;
        if (head != null)
            head.left = null;
        return n.data;
    }

    public Item removeLast() {
        remove();
        Node n = tail;
        tail = tail.left;
        if (tail != null)
            tail.right = null;
        return n.data;
    }

    @Override
    public Iterator<Item> iterator() {
        return new Iterator<Item>() {

            Node n = head;

            @Override
            public boolean hasNext() {
                return n != null;
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException("Not supported");
            }

            @Override
            public Item next() {
                if (!hasNext())
                    throw new NoSuchElementException("No item in queue");
                Node nn = n;
                n = n.right;
                return nn.data;
            }
        };
    }

    public static void main(String[] args) {
        Deque<Integer> dq = new Deque<Integer>();
        dq.addFirst(2);
        dq.addFirst(1);
        dq.addLast(3);
        for (Integer v : dq) {
            System.out.println("Q: "+v+", "+dq.size()+", "+dq.isEmpty());
        }
        dq.removeFirst();
        dq.removeLast();
        for (Integer v : dq) {
            System.out.println("Q: "+v+", "+dq.size()+", "+dq.isEmpty());
        }
        dq.removeFirst();
        System.out.println("Q: "+dq.size()+", "+dq.isEmpty());
    }

}
