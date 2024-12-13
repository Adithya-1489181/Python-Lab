import plotly.express as px

# Create a choropleth map
fig = px.choropleth(locations=['India', 'Afghanistan', 'Bangladesh', 'Bhutan', 'China', 'Nepal', 'Pakistan', 'Sri Lanka', 'Myanmar'], 
                    locationmode="country names",  # Corrected the locationmode value
                    color=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    color_continuous_scale="Viridis",
                    title="India and Its Neighboring Countries")

# Adjust the map scope to focus on Asia
fig.update_geos(scope="asia")

# Show the plot
fig.show()
