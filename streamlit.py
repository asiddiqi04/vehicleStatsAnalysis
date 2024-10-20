import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset (replace 'your_data.csv' with your actual file path)
# Assuming your data is stored in a CSV or JSON file
#df = pd.read_json('output_2024.json')  # Or use pd.read_json('your_data.json')

df = pd.read_json('vehicleStats2015_2024.json')

df['City (L/100 km)'] = pd.to_numeric(df['City (L/100 km)'], errors='coerce')
df['Highway (L/100 km)'] = pd.to_numeric(df['Highway (L/100 km)'], errors='coerce')
df['Combined (L/100 km)'] = pd.to_numeric(df['Combined (L/100 km)'], errors='coerce')
df['CO2 emissions (g/km)'] = pd.to_numeric(df['CO2 emissions (g/km)'], errors='coerce')



st.title("Canadian Vehicle Statistics Visualized")


st.write("""
This app visualizes key data on the fuel consumption, CO2 emissions, and other specifications of various vehicles in Canada. 
Explore the graphs below to gain insights into the performance of different vehicle classes, fuel types, and years.
""")

st.header("Fuel Efficiency by Vehicle Class")

selected_classes = st.multiselect('Select Vehicle Classes to Display', df['Vehicle class'].unique())



# st.write(df)
grouped_df = df.groupby('Vehicle class')[['City (L/100 km)', 'Highway (L/100 km)', 'Combined (L/100 km)']].mean().reset_index()


if selected_classes:
    filtered_df = grouped_df[grouped_df['Vehicle class'].isin(selected_classes)]
    # filtered_df = df[df['Vehicle class'].isin(selected_classes)]
    # for vehicle_class in selected_classes:
    #     class_data = filtered_df[filtered_df['Vehicle class'] == vehicle_class]
    #     plt.plot(class_data['Model year'], class_data['Combined (L/100 km)'], label=vehicle_class)

    #     # Add labels and title
    # plt.xlabel("Year")
    # plt.ylabel("Combined Efficiency (L/100 km)")
    # plt.title("Vehicle Efficiency Over Time by Class")
    # plt.legend(title="Vehicle Class")
    # plt.grid(True)


    # # Display the plot in Streamlit
    # st.pyplot(plt)
else:
    # If no selection is made, display the entire dataset
    filtered_df = grouped_df

fig, ax = plt.subplots(figsize=(8, 6))

bar_width = 0.25
index = np.arange(len(filtered_df['Vehicle class']))

# Plot three bars side by side for each vehicle class
ax.bar(index, filtered_df['City (L/100 km)'], bar_width, label='City')
ax.bar(index + bar_width, filtered_df['Highway (L/100 km)'], bar_width, label='Highway')
ax.bar(index + 2 * bar_width, filtered_df['Combined (L/100 km)'], bar_width, label='Combined')

# Set labels and title
ax.set_xlabel('Vehicle Class', fontsize=14)
ax.set_ylabel('Fuel Consumption (L/100 km)', fontsize=14)
ax.set_title('Fuel Efficiency by Vehicle Class', fontsize=16)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(filtered_df['Vehicle class'], rotation=45)  # Rotate labels for better visibility
ax.legend()

# Adjust layout to prevent overlap
plt.tight_layout()


# Display the chart in Streamlit
st.pyplot(fig)







st.header("Vehicle Comparison")
st.write("""
In this section you can choose up to 4 vehicles and compare statistics
""")

max_vehicles = 4
selected_make = st.multiselect("Select the Makes of the Vehicles", df['Make'].unique())

# if len(selected_make) > max_vehicles:
#     st.error("You can only select up to " + str(max_vehicles) + " vehicle makes.")
# else:
if selected_make:
    make_df = df[df['Make'].isin(selected_make)]
    selected_models = st.multiselect("Select which models you would like to compare", make_df['Model'].unique())

    selected_models_df = make_df[make_df['Model'].isin(selected_models)]
    if len(selected_models) > max_vehicles:
        st.error("You can only select up to " + str(max_vehicles) + " vehicle models.")
    else:
        if selected_models_df.empty:
            st.write("Please select at least one model to compare.")
        else:
            # Create dynamic columns based on the number of selected models
            model_metrics = st.columns(len(selected_models))

            for idx, model in enumerate(selected_models):
                model_data = selected_models_df[selected_models_df['Model'] == model].iloc[0]  # Get the data for the specific model

                with model_metrics[idx]:  # Place in the corresponding column
                    st.subheader(f"{model_data['Model']}")
                    st.metric(label = "City (L/100 km)", value = model_data['City (L/100 km)'])
                    st.metric(label = "Highway (L/100 km)", value = model_data['Highway (L/100 km)'])
        print(selected_models_df)
else:
    st.write("Please select at least one vehicle make.")



# Fuel Consumption Comparison in a given year 




# Fuel Consumption trends overtime 




