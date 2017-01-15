import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Random;

public class RandomizedQueue<Item> implements Iterable<Item> {

    private static final int MIN_SIZE = 10;
    private int head = 0;
    private int len = 0;
    private Item[] arr = null;

    public RandomizedQueue() {
        resize(2);
    }

    public boolean isEmpty() {
        return len == 0;
    }

    public int size() {
        return len;
    }

    public void enqueue(Item item) {
        if (null == item)
            throw new NullPointerException("Item is NULL");
        if (arr == null || size() >= arr.length) {
            resize(size()*2);
        }
        arr[(head + len) % arr.length] = item;
        len += 1;
    }

    public Item dequeue() {
        if (isEmpty())
            throw new NoSuchElementException("Queue is empty");
        if (arr.length > MIN_SIZE && size() < arr.length / 4) {
            resize(arr.length/2);
        }
        Item n = arr[head];
        head = (head + 1) % arr.length;
        len -= 1;
        return n;
    }

    private Item at(int index) {
        return arr[(head + index) % arr.length];
    }

    private void resize(int size) {
        Item[] arr = (Item[]) new Object[size];
        for (int i = 0; i < size(); i++) {
            arr[i] = at(i);
        }
        head = 0;
        this.arr = arr;
    }

    private int[] perm(int size) {
        Random r = new Random();
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = i;
        }
        for (int i = 0; i < size; i++) {
            // Shuffle
            int i1 = r.nextInt(size);
            int i2 = r.nextInt(size);
            int t = result[i2];
            result[i2] = result[i1];
            result[i1] = t;
        }
        return result;
    }

    public Item sample() {
        if (isEmpty())
            throw new NoSuchElementException("Queue is empty");
        return at(new Random().nextInt(size()));
    }

    @Override
    public Iterator<Item> iterator() {
        int[] indexes = perm(size());
        return new Iterator<Item>() {

            int idx = 0;

            @Override
            public boolean hasNext() {
                return idx < size();
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException("Not implemented");
            }

            @Override
            public Item next() {
                if (!hasNext())
                    throw new NoSuchElementException("No item in queue");
                Item n = at(indexes[idx]);
                idx += 1;
                return n;
            }
        };
    }
    public static void main(String[] args) {
        RandomizedQueue<Integer> q = new RandomizedQueue<>();
        for (int i = 0; i < 20; i++) {
            q.enqueue(1+i);
        }
        for (Integer v : q) {
            System.out.println("Q: "+v+", "+q.isEmpty()+", "+q.size()+", "+q.sample());
        }
        for (int i = 0; i < 15; i++) {
            q.dequeue();
        }
        for (Integer v : q) {
            System.out.println("Q: "+v+", "+q.isEmpty()+", "+q.size()+", "+q.sample());
        }
        for (int i = 0; i < 20; i++) {
            q.enqueue(100+i);
        }
        for (Integer v : q) {
            System.out.println("Q: "+v+", "+q.isEmpty()+", "+q.size()+", "+q.sample());
        }
    }
}
