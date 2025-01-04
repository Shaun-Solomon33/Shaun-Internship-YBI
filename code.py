# Chatbot Program with Linear Regression
# This chatbot responds to greetings and farewells, and can also perform simple linear regression.
# If the input doesn't match, it returns a default response

import random

class SimpleChatbot:
    """A simple chatbot that responds to greetings, farewells, and can perform linear regression."""

    def __init__(self, name):
        """Initialize the chatbot with a name and predefined responses."""
        self.name = name
        self.greetings = ['Hi there!', 'Hello!', 'Hey!', 'Hi!']
        self.farewells = ['Goodbye!', 'See you later!', 'Bye!', 'Take care!']
        self.default_response = "I'm sorry, I don't understand that."
        self.linear_regression_help = "To perform linear regression, please provide data points in the form 'x1,y1 x2,y2 ...'."

    def greet(self):
        """Return a random greeting from the list of greetings."""
        return random.choice(self.greetings)

    def farewell(self):
        """Return a random farewell from the list of farewells."""
        return random.choice(self.farewells)

    def respond(self, user_input):
        """Respond to the user's input based on recognized patterns."""
        user_input = user_input.lower()
        if any(greet in user_input for greet in ['hello', 'hi']):
            return self.greet()
        elif any(farewell in user_input for farewell in ['bye', 'goodbye']):
            return self.farewell()
        elif 'linear regression' in user_input:
            return self.linear_regression_help
        elif self._is_valid_data_input(user_input):
            return self.perform_linear_regression(user_input)
        else:
            return self.default_response

    def _is_valid_data_input(self, user_input):
        """Check if the user input contains valid data points for linear regression."""
        try:
            # Try to parse the input into pairs of floats
            points = [tuple(map(float, pair.split(','))) for pair in user_input.split()]
            return all(len(pair) == 2 for pair in points)  # Ensure all pairs have two values
        except ValueError:
            return False

    def perform_linear_regression(self, data):
        """Perform simple linear regression on the provided data."""
        # Parse the input data into (x, y) pairs
        points = [tuple(map(float, pair.split(','))) for pair in data.split()]
        x_vals = [p[0] for p in points]
        y_vals = [p[1] for p in points]

        # Calculate the slope (m) and intercept (b)
        n = len(x_vals)
        sum_x = sum(x_vals)
        sum_y = sum(y_vals)
        sum_x_squared = sum(x ** 2 for x in x_vals)
        sum_xy = sum(x * y for x, y in points)

        # Using the formulas for simple linear regression
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        b = (sum_y - m * sum_x) / n

        return f"The linear equation is: y = {m:.2f}x + {b:.2f}"

if __name__ == '__main__':
    bot = SimpleChatbot('ChatBot')
    print('Bot:', bot.greet())

    while True:
        user_input = input('You: ')
        if user_input.lower() in ['bye', 'goodbye']:
            print('Bot:', bot.farewell())
            break
        print('Bot:', bot.respond(user_input))
