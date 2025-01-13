import streamlit as st

# Define the dataset of questions and answers
qa_data = {
    "What is the difference between JDK, JRE, and JVM?": 
    """- **JVM (Java Virtual Machine):** Executes Java bytecode\n
    - **JRE (Java Runtime Environment):** Contains JVM and libraries to run Java applications\n
    - **JDK (Java Development Kit):** Contains JRE plus development tools like compiler, debugger\n""",

    "Explain the difference between == and .equals() method":
    """- `==` compares object references (memory location)\n
    - `.equals()` compares actual content of objects\n
    ```java\n
    String s1 = new String("Hello");\n
    String s2 = new String("Hello");\n
    System.out.println(s1 == s2);        // false\n
    System.out.println(s1.equals(s2));   // true\n
    ```\n""",

    "What are access modifiers in Java?":
    """- **public:** Accessible from anywhere\n
    - **private:** Accessible only within the same class\n
    - **protected:** Accessible within same package and subclasses\n
    - **default (no modifier):** Accessible within same package\n""",

    "Explain the final keyword in Java":
    """- **Final variable:** Cannot be reassigned\n
    - **Final method:** Cannot be overridden\n
    - **Final class:** Cannot be inherited\n
    ```java\n
    final int MAX_SIZE = 100;  // Constant\n
    final class ImmutableClass {}  // Cannot be extended\n
    ```\n""",

    "What is method overloading?":
    """Multiple methods in same class with same name but different parameters\n
    ```java\n
    class Calculator {\n
        int add(int a, int b) { return a + b; }\n
        double add(double a, double b) { return a + b; }\n
    }\n
    ```\n""",

    "What are list comprehensions?": 
    """A concise way to create lists\n
    ```python\n
    squares = [x**2 for x in range(10)]\n
    even_squares = [x**2 for x in range(10) if x % 2 == 0]\n
    ```\n""",

    "Explain decorators":
    """Functions that modify other functions\n
    ```python\n
    def log_decorator(func):\n
        def wrapper(*args, **kwargs):\n
            print(f"Calling {func.__name__}")\n
            return func(*args, **kwargs)\n
        return wrapper\n

    @log_decorator\n
    def add(a, b):\n
        return a + b\n
    ```\n""",

    "What is Big O Notation?":
    """Describes the performance or complexity of an algorithm\n
    - O(1): Constant time\n
    - O(log n): Logarithmic time (binary search)\n
    - O(n): Linear time\n
    - O(n²): Quadratic time (nested loops)\n""",

    "Explain Binary Search Algorithm":
    """Search algorithm for sorted arrays by repeatedly dividing search interval\n
    ```python\n
    def binary_search(arr, target):\n
        left, right = 0, len(arr) - 1\n
        while left <= right:\n
            mid = (left + right) // 2\n
            if arr[mid] == target:\n
                return mid\n
            elif arr[mid] < target:\n
                left = mid + 1\n
            else:\n
                right = mid - 1\n
        return -1\n
    ```\n""",

    "What is a Stack? Implement basic stack operations":
    """Last In First Out (LIFO) data structure\n
    ```python\n
    class Stack:\n
        def __init__(self):\n
            self.items = []\n
        
        def push(self, item):\n
            self.items.append(item)\n
        
        def pop(self):\n
            return self.items.pop() if not self.is_empty() else None\n
        
        def is_empty(self):\n
            return len(self.items) == 0\n
    ```\n""",

    "Explain Dynamic Programming":
    """Solving complex problems by breaking into simpler subproblems\n
    ```python\n
    def fibonacci_dp(n):\n
        dp = [0] * (n + 1)\n
        dp[1] = 1\n
        for i in range(2, n + 1):\n
            dp[i] = dp[i-1] + dp[i-2]\n
        return dp[n]\n
    ```\n""",

    "Implement Quick Sort Algorithm":
    """Divide and conquer sorting algorithm\n
    ```python\n
    def quick_sort(arr):\n
        if len(arr) <= 1:\n
            return arr\n
        pivot = arr[len(arr) // 2]\n
        left = [x for x in arr if x < pivot]\n
        middle = [x for x in arr if x == pivot]\n
        right = [x for x in arr if x > pivot]\n
        return quick_sort(left) + middle + quick_sort(right)\n
    ```\n""",

    "What is the OSI Model?":
    """7-layer model describing network communication\n
    - **Physical Layer:** Physical transmission\n
    - **Data Link Layer:** Device-to-device data transfer\n
    - **Network Layer:** Routing and addressing\n
    - **Transport Layer:** End-to-end communication\n
    - **Session Layer:** Maintains connection\n
    - **Presentation Layer:** Data formatting\n
    - **Application Layer:** Network services\n""",

    "Difference between TCP and UDP":
    """- **TCP (Transmission Control Protocol):**\n
      * Connection-oriented\n
      * Reliable, ordered delivery\n
      * Error checking\n
      * Slower but guaranteed delivery\n
    - **UDP (User Datagram Protocol):**\n
      * Connectionless\n
      * No guarantee of delivery\n
      * Faster\n
      * Used for streaming, gaming\n""",

    "What are cloud service models?":
    """- **IaaS (Infrastructure as a Service):** Provides virtualized computing resources\n
    - **PaaS (Platform as a Service):** Provides development environment\n
    - **SaaS (Software as a Service):** Provides complete application\n""",

    "What is Kubernetes?":
    """Container orchestration platform\n
    - Automates deployment and scaling of containerized applications\n
    - Features:\n
      * Load balancing\n
      * Self-healing\n
      * Automatic rollouts and rollbacks\n""",

    "Difference between struct and class":
    """- **struct:** Default public members\n
    - **class:** Default private members\n
    ```cpp\n
    struct Student { int id; };  // Public by default\n
    class Employee {\n
        int salary;  // Private by default\n
    public:\n
        void setSalary(int s) { salary = s; }\n
    };\n
    ```\n""",

    "Explain References vs Pointers":
    """- **Reference:**\n
      * Cannot be null\n
      * Cannot be reassigned\n
      * Must be initialized at declaration\n
    - **Pointer:**\n
      * Can be null\n
      * Can be reassigned\n
      * Can point to different memory locations\n""",

    "Explain Move Semantics":
    """Efficiently transferring resources between objects\n
    ```cpp\n
    class Resource {\n
        int* data;\n
    public:\n
        // Move constructor\n
        Resource(Resource&& other) noexcept {\n
            data = other.data;\n
            other.data = nullptr;\n
        }\n
    };\n
    ```\n""",

    "Smart Pointers in C++":
    """- **unique_ptr:** Exclusive ownership\n
    - **shared_ptr:** Shared ownership with reference counting\n
    - **weak_ptr:** Non-owning reference to shared object\n"""
}






st.title("Technical Interview Chatbot")
st.markdown("Ask a question, and I will try to provide the exact answer from my knowledge base!")




# Initialize conversation history in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "assistant", "content": "How may I help you today?"}
    ]

# Display the conversation messages
st.markdown("### Chat History")
for message in st.session_state.conversation:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")

# Input field for user's question
user_prompt = st.text_input("Your message here", key="user_input")

# Case-insensitive QA data (You should define `qa_data` with your questions and answers)
qa_data_lower = {key.lower(): value for key, value in qa_data.items()}

if user_prompt:
    # Append user message to conversation
    st.session_state.conversation.append({"role": "user", "content": user_prompt})
    st.markdown(f"**You:** {user_prompt}")

    # Get the response
    question_lower = user_prompt.lower()
    answer = qa_data_lower.get(
        question_lower, "Sorry, I don't have an answer to that question. Please try a different one!"
    )

    # Append assistant response to conversation
    st.session_state.conversation.append({"role": "assistant", "content": answer})
    st.markdown(f"**Bot:** {answer}")
