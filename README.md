# Shaun-Internship-YBI
This project is a simple chatbot that can respond to greetings, farewells, and also perform basic linear regression. The chatbot is written in Python and uses random greetings and farewells. Additionally, it allows users to input data points and computes a linear regression equation.

## Features
- Responds to common greetings (e.g., 'hello', 'hi').
- Responds to farewells (e.g., 'bye', 'goodbye').
- Computes a simple linear regression equation based on user-provided data.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/simple-chatbot-linear-regression.git
   ```

2. Navigate to the project directory:
   ```bash
   cd simple-chatbot-linear-regression
   ```

3. (Optional) Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the chatbot by executing the script:
```bash
python Simple_Chatbot.py
```

### Interacting with the Chatbot
The chatbot supports the following types of interactions:

1. **Greeting**: Input a greeting like 'hello' or 'hi', and the chatbot will respond with a random greeting.

2. **Farewell**: Say 'bye' or 'goodbye', and the chatbot will respond with a farewell and end the session.

3. **Linear Regression**: Input 'linear regression' to trigger the chatbot's instructions on providing data. Then, input data points in the form `x1,y1 x2,y2 ...` (e.g., `1,2 2,3 3,5`). The chatbot will calculate the best-fit line and return the equation `y = mx + b`.

### Example Interaction
```
You: hello
Bot: Hi there!
You: linear regression
Bot: To perform linear regression, please provide data points in the form 'x1,y1 x2,y2 ...'.
You: 1,2 2,3 3,5
Bot: The linear equation is: y = 1.50x + 0.50
You: goodbye
Bot: Take care!
```
