# 🧪 Hypothesis Testing & A/B Analysis on Website Themes

## 📖 What is Hypothesis Testing?

**Hypothesis testing** is a statistical method used to make data-driven decisions. It helps determine whether a specific effect or difference observed in a sample is statistically significant or likely due to random chance.

In simple terms:
> "Are the differences we see in data real — or just coincidence?"

It’s a core concept in **data science**, especially in business decision-making, product experiments, and marketing analytics.

---

## 🎯 Project Objective: A/B Testing Website Themes

This project involves an A/B test between two website themes: **Light Theme** and **Dark Theme**. We analyze user behavior metrics to determine if the **theme design affects key engagement KPIs**, such as:

- Click Through Rate
- Conversion Rate
- Bounce Rate
- Scroll Depth
- Session Duration

Using hypothesis testing (specifically **Welch’s t-tests**), we evaluate whether the differences in these metrics are statistically significant.

---

## 🔬 A/B Testing Explained

**A/B Testing** is a controlled experiment comparing two versions (A and B) of a variable to see which performs better.

In our case:
- **Group A**: Users shown the **Light Theme**
- **Group B**: Users shown the **Dark Theme**

Each user is randomly assigned to one group, and key metrics are recorded.

### Key Question:
> "Does the website theme impact user behavior or conversion?"

---

## 📈 Summary of Statistical Test Results

| Metric               | T-Statistic | P-Value | Interpretation                  |
|----------------------|-------------|---------|----------------------------------|
| Click Through Rate   | -1.9767     | 0.04835 | Significant difference          |
| Conversion Rate      | 0.4745      | 0.63525 | Not significant                 |
| Bounce Rate          | -1.2019     | 0.22969 | Not significant                 |
| Scroll Depth         | 0.7562      | 0.44969 | Not significant                 |
| Session Duration     | *varies*    | *varies*| *(depends on your dataset)*    |

> ✅ **Interpretation**: The only metric showing a significant difference is **Click Through Rate**. All other differences are likely due to chance (p-value > 0.05).

---

## 🖼️ Visualizations & Screenshots

For better understanding, include screenshots of the following in a `screenshots/` folder:

- Box plots comparing each metric by theme (use Seaborn or Plotly)
- A bar chart showing group-wise means
- A heatmap of correlation between metrics (optional)

📁 Suggested structure:
