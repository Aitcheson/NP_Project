import matplotlib.pyplot as plt

# Sample data for two lines
x = [5, 16, 25, 32, 40]  # Input size
y1 = [0.01, 0.09, 20, 54, 190]  # Completion time for line 1
y2 = [0.01, 0.01, 0.01, 0.01, 0.1]  # Completion time for line 2

# Create the plot
plt.plot(x, y1, label="Exact", marker='o', color='b')  # Plot the first line
plt.plot(x, y2, label="Approximation", marker='x', color='r')  # Plot the second line

# Add labels and title
plt.xlabel("Input Size")
plt.ylabel("Completion Time")
plt.title("Plot of Completion Time vs. Input Size")

# Add legend
plt.legend()

# Display the plot
plt.show()
