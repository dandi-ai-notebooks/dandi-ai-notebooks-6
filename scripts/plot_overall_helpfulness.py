
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the data
df = pd.read_csv("reviews_export.csv")

# Compute breakdown
breakdown = df.groupby("dandiset_id")["overall-helpfulness"].value_counts().unstack(fill_value=0)
breakdown = breakdown[[2, 1, 0]] if set([0, 1, 2]).issubset(breakdown.columns) else breakdown
breakdown.reset_index(inplace=True)
breakdown.set_index("dandiset_id", inplace=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
# Use consistent color scheme: Very helpful (2), Moderately helpful (1), Not helpful (0)
colors = ['#2E8B57', '#9370DB', '#555555']
breakdown.plot(kind="bar", stacked=True, color=colors, ax=ax)
ax.set_title("Overall Helpfulness by Dandiset ID")
ax.set_xlabel("Dandiset ID")
ax.set_ylabel("Number of Responses")
ax.set_xticklabels(breakdown.index, rotation=45)
# Set legend with reversed order to match other plots
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], ["Not helpful (0)", "Moderately helpful (1)", "Very helpful (2)"], title="Helpfulness Score")
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

plt.tight_layout()
plt.savefig("images/overall_helpfulness_by_dandiset.png", dpi=300)
