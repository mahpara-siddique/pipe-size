import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate pipe diameter
def calculate_diameter(flow_rate, velocity):
    # Formula to calculate pipe diameter (d = sqrt(4 * Q / (pi * v)))
    # Where Q is flow rate (in cubic meters per second)
    # v is the velocity (in meters per second)
    diameter = math.sqrt(4 * flow_rate / (math.pi * velocity))
    return diameter

# Function to plot the graph
def plot_diameter_graph():
    # Define a range of flow rates (Q) and velocities (v)
    flow_rate_values = np.linspace(0.01, 1.0, 100)  # Range of flow rates (0.01 to 1.0 m³/s)
    velocity_values = np.linspace(0.1, 5.0, 50)  # Range of velocities (0.1 to 5.0 m/s)

    # Create a meshgrid for the flow rates and velocities
    flow_rate_grid, velocity_grid = np.meshgrid(flow_rate_values, velocity_values)

    # Calculate the pipe diameter for each combination of flow rate and velocity
    diameter_values = np.sqrt(4 * flow_rate_grid / (np.pi * velocity_grid))

    # Plotting the graph
    fig, ax = plt.subplots(figsize=(10, 6))
    cp = ax.contourf(flow_rate_grid, velocity_grid, diameter_values, cmap='viridis')
    fig.colorbar(cp, ax=ax, label='Pipe Diameter (m)')
    ax.set_xlabel('Flow Rate (m³/s)')
    ax.set_ylabel('Velocity (m/s)')
    ax.set_title('Pipe Diameter vs. Flow Rate and Velocity')

    # Display the plot in Streamlit
    st.pyplot(fig)

# Streamlit App
def main():
    # Set the page configuration with a title, icon, and layout style
    st.set_page_config(
        page_title="Pipe Sizing Helper",
        page_icon="💧",  # Water-related icon
        layout="centered",  # Center the content
    )
    
    # Title and description
    st.title("Pipe Sizing Helper 💧")
    st.markdown("Enter the flow rate and permissible velocity to get the recommended pipe diameter.")
    
    # Input fields for flow rate and velocity
    flow_rate = st.number_input("Enter Flow Rate (m³/s):", min_value=0.0, step=0.01)
    velocity = st.number_input("Enter Permissible Velocity (m/s):", min_value=0.0, step=0.1)
    
    # Create a button to calculate the recommended pipe diameter
    if st.button("Generate Pipe Diameter"):
        # Check if both flow rate and velocity are greater than zero
        if flow_rate > 0 and velocity > 0:
            diameter = calculate_diameter(flow_rate, velocity)
            st.write(f"The recommended pipe diameter is: **{diameter:.2f} meters**")
        else:
            st.error("Please enter valid values for flow rate and velocity.")
    
    # Show the graphical visualization of pipe diameter vs flow rate and velocity
    st.subheader("Graphical Visualization")
    plot_diameter_graph()

    # Add some helpful info or tips
    st.markdown("""
    ### Tips:
    - Flow rate (Q) is the volume of fluid passing through the pipe per unit of time (in cubic meters per second).
    - Permissible velocity (v) is the maximum allowable speed of the fluid inside the pipe (in meters per second).
    """)

if __name__ == "__main__":
    main()
