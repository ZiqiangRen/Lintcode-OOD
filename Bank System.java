public class BankSystem {
    private Map<Integer, Client> clients;
    
    public BankSystem(){
        clients = new LinkedHashMap<>();
    }
    /**
     * @param id: user account id
     * @param amount: the number of bank deposits
     * @param timestamp: the data of bank transaction
     * @return: nothing
     */
    public void deposite(int id, int amount, long timestamp) {
        if (clients.containsKey(id)) {
            clients.get(id).deposit(amount, timestamp);
        } else {
            clients.put(id, new Client());
            clients.get(id).deposit(amount, timestamp);
        }
    }

    /**
     * @param id: user account id
     * @param amount : the number of bank withdraw
     * @param timestamp: the data of bank transaction
     * @return: if user account can not withdraw the number of amount,return false. else return true
     */
    public boolean withdraw(int id, int amount , long timestamp) {
        if (clients.containsKey(id)) {
            if (clients.get(id).getAmount(timestamp) < amount) {
                return false;
            }
            clients.get(id).withdraw(amount, timestamp);
            return true;
        } else {
            return false;
        }
    }

    /**
     * @param id: user account id
     * @param startTime: start time
     * @param endTime: end time
     * @return: need return two numbers,the first one is start time account balance,the second is end time account balance
     */
    public int[] check(int id, long startTime, long endTime) {
        if (clients.containsKey(id)) {
            Client client = clients.get(id);
            return new int[] {client.getAmount(startTime), client.getAmount(endTime)};
        } else {
            return new int[0];
        }
    }
}

class Client {
    public int amount;
    public List<Long> timestamps;
    public Map<Long, Integer> events;
    
    public Client() {
        this.amount = 0;
        timestamps = new ArrayList<>();
        events = new LinkedHashMap<>();
    }
    
    public void deposit(int amount, long timestamp) {
        this.amount += amount;
        timestamps.add(timestamp);
        events.put(timestamp, this.amount);
    }
    
    public void withdraw(int amount, long timestamp) {
        this.amount -= amount;
        timestamps.add(timestamp);
        events.put(timestamp, this.amount);
    }
    
    public int getAmount(long timestamp) {
        for (int i = 0; i < timestamps.size(); i++) {
            if (i == timestamps.size() - 1 && timestamp >= timestamps.get(i)) {
                return events.get(timestamps.get(i));
            }
            
            if (i == 0 && timestamp < timestamps.get(i)) {
                return 0;
            }
            
            if (i + 1 < timestamps.size() && timestamps.get(i) <= timestamp && timestamps.get(i + 1) > timestamp) {
                return events.get(timestamps.get(i));
            }
        }
        return 0;
    }
}
