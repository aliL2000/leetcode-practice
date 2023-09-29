import java.util.HashMap;
import java.util.Map;

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> copy = new HashMap<>();
        
        Node cur = head;
        while (cur != null) {
            Node copied = new Node(cur.val);
            copy.put(cur, copied);
            cur = cur.next;
        }
        
        cur = head;
        while (cur != null) {
            Node copied = copy.get(cur);
            copied.next = copy.get(cur.next);
            copied.random = copy.get(cur.random);
            cur = cur.next;
        }
        
        return copy.get(head);
    }
}