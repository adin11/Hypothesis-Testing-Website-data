import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv('website_ab_test.csv')
print("Dataset shape:", df.shape)
print("\nFirst few rows:\n", df.head())

# -----------------------------
# Theme distribution
# -----------------------------
print("\nTheme distribution (%):")
print(df['Theme'].value_counts(normalize=True) * 100)

# -----------------------------
# Grouped mean by Theme
# -----------------------------
grouped_data_by_theme = df.groupby('Theme').mean(numeric_only=True).sort_values(
    by='Conversion Rate', ascending=False)
print("\nAverage metrics by Theme:\n", grouped_data_by_theme)

# -----------------------------
# Hypothesis testing by metric
# -----------------------------

# 1. Conversion Rate
conversion_rate_light = df[df['Theme'] == 'Light Theme']['Conversion Rate']
conversion_rate_dark = df[df['Theme'] == 'Dark Theme']['Conversion Rate']
t_stat_conversion, p_value_conversion = ttest_ind(conversion_rate_light, conversion_rate_dark)

# 2. Click Through Rate
click_through_rate_light = df[df['Theme'] == 'Light Theme']['Click Through Rate']
click_through_rate_dark = df[df['Theme'] == 'Dark Theme']['Click Through Rate']
t_ctr, p_ctr = ttest_ind(click_through_rate_light, click_through_rate_dark)

# 3. Bounce Rate
bounce_rates_light = df[df['Theme'] == 'Light Theme']['Bounce Rate']
bounce_rates_dark = df[df['Theme'] == 'Dark Theme']['Bounce Rate']
t_stat_bounce, p_value_bounce = ttest_ind(bounce_rates_light, bounce_rates_dark, equal_var=False)

# 4. Scroll Depth
scroll_depth_light = df[df['Theme'] == 'Light Theme']['Scroll_Depth']
scroll_depth_dark = df[df['Theme'] == 'Dark Theme']['Scroll_Depth']
t_stat_scroll, p_value_scroll = ttest_ind(scroll_depth_light, scroll_depth_dark, equal_var=False)

# 5. Session Duration
session_duration_light = df[df['Theme'] == 'Light Theme']['Session_Duration']
session_duration_dark = df[df['Theme'] == 'Dark Theme']['Session_Duration']
t_stat_session, p_value_session = ttest_ind(session_duration_light, session_duration_dark, equal_var=False)

# -----------------------------
# Summary Table
# -----------------------------
comparison_table = pd.DataFrame({
    'Metric': ['Click Through Rate', 'Conversion Rate', 'Bounce Rate', 'Scroll Depth', 'Session Duration'],
    'T-Statistic': [t_ctr, t_stat_conversion, t_stat_bounce, t_stat_scroll, t_stat_session],
    'P-Value': [p_ctr, p_value_conversion, p_value_bounce, p_value_scroll, p_value_session]
})

print("\nHypothesis Test Summary:\n", comparison_table)














