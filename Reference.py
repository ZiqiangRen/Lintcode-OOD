/**
 * Definition of Node:
 * class Node {
 *     public int val;
 *     public Node(int val) {
 *         this.val = val;
 *     }
 * }
 */
public class ReferenceManager {
    public Node node;

    public void copyValue(Node obj) {
        // copy value from obj to node
        if (obj == null){
            return;
        }
        node = new Node(obj.val);
    }

    public void copyReference(Node obj) {
        // copy reference from obj to node
        node = obj;
    }
}
