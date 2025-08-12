import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load and clean the data
df = pd.read_csv(r"C:\Users\Joel Zerubabel\ML1\road_acccidents_ML_mini_project.csv")
df.columns = df.columns.str.strip()  # Remove accidental spaces
df.drop(['sno', 'latitude', 'longitude'], axis=1, inplace=True)

def fatalities(year):
    # Define relevant columns
    cols = [
        f'death_by_lorries__{year}',
        f'death_by_carsjeeps_{year}',
        f'death_by_buses{year}',
        f'death_by_twowheelers_{year}',
        f'death_by_threewheelers__{year}',
        f'death_by_others_{year}'
    ]
    
    # Ensure numeric
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce').fillna(0)
    df['district'] = df['district'].astype(str).str.strip()
    
    # Handle fatality total column
    fatal_col = f'{year}_fatal'
    if fatal_col in df.columns:
        df[fatal_col] = pd.to_numeric(df[fatal_col], errors='coerce').fillna(0)
        df['Unclassified'] = df[fatal_col] - df[cols].sum(axis=1)
        df['Unclassified'] = df['Unclassified'].clip(lower=0)
    else:
        df['Unclassified'] = 0
    
    # Group by district to merge duplicates
    df_grouped = df.groupby('district', as_index=False)[cols + ['Unclassified']].sum()
    
    # Plot
    df_grouped.set_index('district').plot(
        kind='bar',
        stacked=True,
        figsize=(16, 9),
        color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB3E6', '#A0A0A0']
    )
    
    plt.xticks(rotation=90)
    plt.xlabel('Districts')
    plt.ylabel('Number of Fatalities by Vehicle Type')
    plt.title(f'Fatalities by Vehicle Type in {year}')
    plt.legend(title='Vehicle Types')
    plt.tight_layout()
    plt.show()

# Example usage
#fatalities(2021)

def no_of_fatalities(df):
    
    columns=df[['district','2020_fatal','2021_fatal','2020_nonfatal','2021_nonfatal']]
    
    
    df_melt=columns.melt(id_vars=['district'], value_vars=['2020_fatal','2021_fatal','2020_nonfatal','2021_nonfatal'] ,var_name="case_type", value_name='count')
    df_melt[['year','case']]=df_melt['case_type'].str.split('_',expand=True)
    plt.figure(figsize=(12,6))
    bar_plot=sns.barplot(x='district',y='count',hue='case_type',data=df_melt)
    plt.xticks(rotation=90,ha='right')
    for bar in bar_plot.containers:
        bar_plot.bar_label(bar, label_type='edge')
    
    plt.xlabel('Districts')
    plt.ylabel('Year of Fatalities')
    plt.tight_layout()
    plt.title('Number of Fatalities in 2020 and 2021')
    plt.show()

no_of_fatalities(df)