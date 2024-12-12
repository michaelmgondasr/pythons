import streamlit as st
import pandas as pd
import numpy as np

st.title("NumPy Exercises")
st.markdown("---")

# Question 1
st.header("Question 1")
a1 = np.arange(1, 10).reshape(3, 3)
st.subheader("Matrix:")
st.write(a1)
st.markdown(f"**Code:** `np.arange(1, 10).reshape(3, 3)`")
st.markdown(f"**Shape:** {a1.shape}")
st.markdown(f"**Size:** {a1.size}")
st.markdown(f"**Data type:** {a1.dtype}")
st.markdown("---")

# Question 2
st.header("Question 2")
a2 = np.arange(1, 26).reshape(5, 5)
st.subheader("Matrix:")
st.write(a2)
st.markdown(f"**Code:** `np.arange(1, 26).reshape(5, 5)`")
st.markdown(f"**First row:** {a2[0, :].tolist()} (Code: `a2[0, :]`)")
st.markdown(f"**Last column:** {a2[:, -1].tolist()} (Code: `a2[:, -1]`)")
st.markdown("**2x2 sub-matrix from the center:**")
st.write(a2[2:4, 2:4])
st.markdown(f"**Code:** `a2[2:4, 2:4]`")
st.markdown("---")

# Question 3
st.header("Question 3")
a3 = np.array([1, 2, 3])
b3 = np.array([4, 5, 6])
st.markdown(f"**Element-wise addition:** {a3 + b3} (Code: `a3 + b3`)")
st.markdown(f"**Dot product:** {np.dot(a3, b3)} (Code: `np.dot(a3, b3)`)")
st.markdown(f"**Element-wise multiplication:** {a3 * b3} (Code: `a3 * b3`)")
st.markdown("---")

# Question 4
st.header("Question 4")
a4 = np.arange(1, 13)
reshaped_a4 = a4.reshape(3, 4)
flattened_a4 = reshaped_a4.flatten()
st.markdown(f"**1D array:** {a4.tolist()} (Code: `np.arange(1, 13)`)")
st.markdown("**Reshaped 3x4 matrix:**")
st.write(reshaped_a4)
st.markdown(f"**Code:** `a4.reshape(3, 4)`")
st.markdown(f"**Flattened back to 1D array:** {flattened_a4.tolist()} (Code: `reshaped_a4.flatten()`)")
st.markdown("---")

# Question 5
st.header("Question 5")
a5 = np.random.randint(1, 101, size=10)
st.markdown(f"**Random array:** {a5.tolist()} (Code: `np.random.randint(1, 101, size=10)`)")
st.markdown(f"**Mean:** {np.mean(a5):.2f} (Code: `np.mean(a5)`)")
st.markdown(f"**Median:** {np.median(a5)} (Code: `np.median(a5)`)")
st.markdown(f"**Standard deviation:** {np.std(a5):.2f} (Code: `np.std(a5)`)")
st.markdown("---")

# Question 6
st.header("Question 6")
a6 = np.array([10, 20, 30, 40, 50, 60])
greater_than_30 = a6[a6 > 30]
st.markdown(f"**Original array:** {a6.tolist()} (Code: `np.array([10, 20, 30, 40, 50, 60])`)")
st.markdown(f"**Elements greater than 30:** {greater_than_30.tolist()} (Code: `a6[a6 > 30]`)")
