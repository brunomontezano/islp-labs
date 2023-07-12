# Import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# Set seed
rng = np.random.default_rng (3)

# Create a line plot with two random normal distributions (default)
fig, ax = plt.subplots(figsize=(8, 8))
x = rng.standard_normal(100)
y = rng.standard_normal(100)
ax.plot(x, y)
plt.show()

# Create a scatter plot using the parameter fmt with 'o' value
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x, y, 'o')
plt.show()

# Create scatter plot with function scatter
# I changed the figure size to 16:9
# I also added some labels
fig , ax = plt.subplots(figsize =(16, 9))
ax.scatter(x, y, marker='o')
ax.set_xlabel('This is the x-axis')
ax.set_ylabel('This is the y-axis')
ax.set_title('Plot of X vs. Y')
plt.show()

# Change the figure size
fig , ax = plt.subplots(figsize =(16, 9))
fig.set_size_inches(12,3)
plt.show()

# Create subplots
# Grid with 2 rows and 3 columns and total size of 15:5
fig, axes = plt.subplots(nrows=2,
                         ncols=3,
                         figsize=(15, 5))
# Change plot from first row in the second column
axes[0, 1].plot(x, y, 'o')
# Change plot from second row in the third column
axes[1, 2].scatter(x, y, marker='+')
plt.show()

# I could save the figure with the commented code below
fig.savefig("output/Figure.png", dpi=300)

# I could change the range of x-axis for example and re-save it
axes[0, 1].set_xlim([-1, 1])
fig.savefig("output/Figure_updated.png")

# Now let's create a contour plot
fig, ax = plt.subplots(figsize=(8, 8))
x = np.linspace(-np.pi, np.pi, 50)
y = x
f = np.multiply.outer(np.cos(y), 1 / (1+ x**2))
ax.contour(x, y, f)
plt.show()

# Add more levels to the image
fig, ax = plt.subplots(figsize=(8, 8))
ax.contour(x, y, f, levels = 45)
plt.show()

# Similar to contour but produces a color-coded plot dependent to "z",
# in this case, "f". It is basically a heatmap
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(f)
plt.show()