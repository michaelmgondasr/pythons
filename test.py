import streamlit as st
import pandas as pd
import numpy as np

# Question 1
a1 = np.arange(1, 10).reshape(3, 3)
st.write("Question 1:")
a1
st.write("Shape:", a1.shape)
st.write("Size:", a1.size)
st.write("Data type:", a1.dtype)

# Question 2
a2 = np.arange(1, 26).reshape(5, 5)
st.write("\nQuestion 2:")
st.write("Matrix:\n", a2)
st.write("First row:", a2[0, :])
st.write("Last column:", a2[:, -1])
st.write("2x2 sub-matrix from the center:\n", a2[2:4, 2:4])

# Question 3
a3 = np.array([1, 2, 3])
b3 = np.array([4, 5, 6])
st.write("\nQuestion 3:")
st.write("Element-wise addition:", a3 + b3)
st.write("Dot product:", np.dot(a3, b3))
st.write("Element-wise multiplication:", a3 * b3)

# Question 4
a4 = np.arange(1, 13)
reshaped_a4 = a4.reshape(3, 4)
flattened_a4 = reshaped_a4.flatten()
st.write("\nQuestion 4:")
st.write("1D array:", a4)
st.write("Reshaped 3x4 matrix:\n", reshaped_a4)
st.write("Flattened back to 1D array:", flattened_a4)

# Question 5
a5 = np.random.randint(1, 101, size=10)
st.write("\nQuestion 5:")
st.write("Random array:", a5)
st.write("Mean:", np.mean(a5))
st.write("Median:", np.median(a5))
st.write("Standard deviation:", np.std(a5))

# Question 6
a6 = np.array([10, 20, 30, 40, 50, 60])
greater_than_30 = a6[a6 > 30]
st.write("\nQuestion 6:")
st.write("Original array:", a6)
st.write("Elements greater than 30:", greater_than_30)
