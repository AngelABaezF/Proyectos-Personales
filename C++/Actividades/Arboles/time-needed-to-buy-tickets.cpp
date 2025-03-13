// Angel Alexander Baez Flores - A01425613
class Nodo {
public:
    int value;
    int index;
    Nodo* next;
    Nodo(int data, int idx) {
        value = data;
        index = idx;
        next = nullptr;
    }
};

class Fila {
private:
    Nodo* front;
    Nodo* back;
public:
    Fila() {
        front = nullptr;
        back = nullptr;
    }

    void enqueue(int data, int idx) {
        Nodo* nuevo = new Nodo(data, idx);
        if (front == nullptr) {
            front = nuevo;
            back = nuevo;
        } else {
            back->next = nuevo;
            back = nuevo;
        }
    }

    int dequeue() {
        if (front == nullptr)
            return -1;
        Nodo* borrado = front;
        front = front->next;
        if (front == nullptr) back = nullptr;
        int value = borrado->value;
        delete borrado;
        return value;
    }

    Nodo* getFront() {
        return front;
    }

    bool isEmpty() {
        return front == nullptr;
    }
};
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        Fila fila;
        int n = tickets.size();
        for (int i = 0; i < n; i++) {
            fila.enqueue(tickets[i], i);
        }
        int time = 0;
        while (!fila.isEmpty()) {
            Nodo* current = fila.getFront();
            int ticketsLeft = current->value;
            int personIndex = current->index;
            time++;
            ticketsLeft--;
            fila.dequeue();
            if (ticketsLeft > 0) {
                fila.enqueue(ticketsLeft, personIndex);
            }

            if (personIndex == k && ticketsLeft == 0) {
                return time;
            }
        }
        return time;
    }
};