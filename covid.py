import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the csv file
df = pd.read_csv('covid.csv')

# Print the data to check if it was read correctly
print(df)

# Plot confirmed cases and deaths by country using line plot
df.plot(x='Country', y='Confirmed')
df.plot(x='Country', y='Deaths')

# Plot confirmed cases and deaths by country using line plot with figure size of (15,5)
plt.figure(figsize=(15, 5))
plt.plot(df.Country, df.Confirmed.values)
plt.xticks(rotation=90)

# Save the plot as png image 'img1.png'
plt.ioff()
plt.savefig('img1.png', bbox_inches='tight', pad_inches=0.2, format='png')

# Plot confirmed cases and deaths by country using line plot with figure size of (30,5)
plt.figure(figsize=(30, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values)
plt.plot(df.Country, df.Deaths.values)

# Save the plot as png image 'img2.png'
plt.ioff()
plt.savefig('img2.png', bbox_inches='tight', pad_inches=0.2, format='png')

# Plot confirmed cases and deaths by country using line plot with figure size of (15,5)
# Include labels and legend
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, label='Confirmed')
plt.plot(df.Country, df.Deaths.values, label='Deaths')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')

# Save the plot as png image 'img3.png'
plt.ioff()
plt.savefig('img3.png', bbox_inches='tight', pad_inches=0.2, format='png')

# Plot confirmed cases and deaths by country using line plot with grid and figure size of (15,5)
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, label='Confirmed')
plt.plot(df.Country, df.Deaths.values, label='Deaths')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')

# Save the plot as png image 'img4.png'
plt.ioff()
plt.grid()
plt.savefig('img4.png', bbox_inches='tight', pad_inches=0.2, format='png')

# Plot confirmed cases and deaths by country using line plot with pattern '*' and 'v' and figure size of (15,5)
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, '*--', label='Confirmed', c='r')
plt.plot(df.Country, df.Deaths.values, 'v:', label='Deaths', c='b')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')

# Save the plot as png image 'img5.png'
plt.ioff()
plt.grid()
plt.savefig('img5.png', bbox_inches='tight', pad_inches=0.2, format='png')

# Call a subprocess to run the script "scroll.py"
subprocess.call("dashboard.py", shell=True)
