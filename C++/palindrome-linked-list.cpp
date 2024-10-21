class Solution
{
    class Nodo
    {
    public:
        int value;
        Nodo *next;
        Nodo(int data)
        {
            value = data;
            next = nullptr;
        }
    };
    class Pila
    {
    private:
        Nodo *top;

    public:
        Pila()
        {
            top = nullptr;
        }
        void push(int data)
        {
            Nodo *nuevo = new Nodo(data);
            if (top == nullptr)
                top = nuevo;
            else
            {
                nuevo->next = top;
                top = nuevo;
            }
        }
        int pop()
        {
            if (top == nullptr)
                return -1;
            Nodo *borrado = top;
            top = top->next;
            int value = borrado->value;
            delete borrado;
            return value;
        }
        void mostrar()
        {
            Nodo *actual = top;
            while (actual != nullptr)
            {
                cout << actual->value << " ";
                actual = actual->next;
            }
            cout << endl;
        }
        bool vacia()
        {
            if (top == nullptr)
                return true;
            else
                return false;
        };
    };

public:
    bool isPalindrome(ListNode *head)
    {
        if (head->next == nullptr)
            return true;
        ListNode *slow = head;
        ListNode *fast = head;
        Pila *pila = new Pila();
        while (fast != nullptr && fast->next != nullptr)
        {
            pila->push(slow->val);
            slow = slow->next;
            fast = fast->next;
        }
        pila->mostrar();
        cout << fast << endl;
        if (fast != nullptr)
            slow = slow->next;
        while (!pila->pop())
        {
            if (pila->vacia() == !slow->val)
                return false;
            slow = slow->next;
        }
        return true;
    }
};