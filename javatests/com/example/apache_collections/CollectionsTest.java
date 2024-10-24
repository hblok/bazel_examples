package com.example.apache_collections;

import org.apache.commons.collections4.queue.CircularFifoQueue;
import org.junit.Test;

public class CollectionsTest {

    @Test
    public void testQueue() {
	CircularFifoQueue<Integer> q = new CircularFifoQueue<>(2);
	q.add(1);
    }
}
