import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def load_data(filepath):
    df = pd.read_csv(filepath)
    print("Dataset shape:", df.shape)
    print("\nFirst few rows:\n", df.head())
    return df

def theme_distribution(df):
    print("\nTheme distribution (%):")
    print(df['Theme'].value_counts(normalize=True) * 100)


def grouped_metrics_by_theme(df):
    grouped = df.groupby('Theme').mean(numeric_only=True).sort_values(by='Conversion Rate', ascending=False)
    print("\nAverage metrics by Theme:\n", grouped)
    return grouped


def perform_ttest(df, column):
    group_light = df[df['Theme'] == 'Light Theme'][column]
    group_dark = df[df['Theme'] == 'Dark Theme'][column]
    
    # Assume unequal variance (Welch's t-test) for general use
    t_stat, p_val = ttest_ind(group_light, group_dark, equal_var=False)
    return t_stat, p_val


def hypothesis_test_summary(df):
    metrics = ['Click Through Rate', 'Conversion Rate', 'Bounce Rate',
               'Scroll_Depth', 'Session_Duration']

    results = []

    for metric in metrics:
        t_stat, p_val = perform_ttest(df, metric)
        results.append({
            'Metric': metric,
            'T-Statistic': t_stat,
            'P-Value': p_val
        })

    summary_df = pd.DataFrame(results)
    print("\nHypothesis Test Summary:\n", summary_df)
    return summary_df


def main():
    filepath = 'website_ab_test.csv'
    df = load_data(filepath)
    
    theme_distribution(df)
    grouped_metrics_by_theme(df)
    hypothesis_test_summary(df)

if __name__ == "__main__":
    main()
