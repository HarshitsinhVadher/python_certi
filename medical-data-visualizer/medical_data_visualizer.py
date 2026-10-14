import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: Import the data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2: Add an overweight column. BMI = weight(kg) / height(m)^2. If BMI > 25, overweight = 1, else 0
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3: Normalize cholesterol and gluc: 0 if value is 1, 1 if value is more than 1
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4
def draw_cat_plot():
    # 5: Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6: Group and reformat the data in df_cat to split it by cardio.
    # Show the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7: Convert the data into long format and create a chart
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig

    # 8: Get the figure for the output and save it
    fig.savefig('catplot.png')
    return fig


# 9
def draw_heat_map():
    # 10: Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11: Calculate the correlation matrix
    corr = df_heat.corr()

    # 12: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 14: Plot the correlation matrix using seaborn's heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 15: Save and return the figure
    fig.savefig('heatmap.png')
    return fig
