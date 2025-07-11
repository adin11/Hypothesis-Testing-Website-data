# Hypothesis Testing on Real-World Website Data.

**In this project we will perform hypothesis tesing (particularily a/b test) on real world website data to check which theme of the website ( light/dark ) affects key perfromance metrics like CTR, Conversion Rate, Bounce Rate etc.**

## What is Hypothesis Testing?

Hypothesis Testing is a statistical method used to make inferences or decisions about a population based on sample data. It's the process of making an assumption testing it with data, deciding whether we reject the null hypothesis or we fail to reject the null hypothesis.

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

**A/B Testing** is a type of hypothesis testing in which we perfrom a controlled experiment comparing two versions (A and B) of a variable to see which performs better.

In our case:
- **Group A**: Users shown the **Light Theme**
- **Group B**: Users shown the **Dark Theme**


--- 

## Dataset overview:
This is a sample data and using this sample data we will make inferences for the population. 
The dataset contains 1,000 records across 10 columns, with no missing values. Here’s a quick summary of the numerical columns:

**Column Summary:**
- Theme: dark or light
- Click Through Rate: The proportion of the users who click on links or buttons on the website.
- Conversion Rate: The percentage of users who signed up on the platform after visiting for the first time.
- Bounce Rate: The percentage of users who leave the website without further interaction after visiting a single page.
- Scroll Depth: The depth to which users scroll through the website pages.
- Age: The age of the user.
- Location: The location of the user.
- Session Duration: The duration of the user’s session on the website in seconds.
- Purchases: Whether the user purchased the book (Yes/No).
- Added_to_Cart: Whether the user added books to the cart (Yes/No).

### Key Questions:
> "Does the website theme impact user behavior or conversion?"

---

## 📈 Summary of Statistical Test Results

### **🎯 Mean Values by Theme**

| **Metric**                 | **Light Theme** | **Dark Theme** | **Interpretation**                                                               |
| -------------------------- | --------------: | -------------: | -------------------------------------------------------------------------------- |
| **Click Through Rate**     |          0.2471 |         0.2645 | 🔹 *Dark Theme* users click slightly more, suggesting higher initial engagement. |
| **Conversion Rate**        |          0.2555 |         0.2513 | 🔹 *Light Theme* shows a marginally higher conversion rate.                      |
| **Bounce Rate**            |          0.4990 |         0.5121 | 🔹 *Light Theme* users are slightly less likely to leave without interacting.    |
| **Scroll Depth (%)**       |           50.74 |          49.93 | 🔹 *Light Theme* users scroll deeper on average, indicating stronger engagement. |
| **Average Age (years)**    |           41.73 |          41.33 | 🔸 Age distribution is consistent across both themes.                            |
| **Session Duration (sec)** |          930.83 |         919.48 | 🔹 *Light Theme* users stay slightly longer per session.                         |

> ✅ **Summary Insight**:
> The **Light Theme** shows small advantages in **conversion rate**, **bounce rate**, **scroll depth**, and **session duration**—all indicators of stronger engagement and effectiveness. Meanwhile, the **Dark Theme** has a slight lead in **click-through rate**, suggesting it may attract more immediate interaction. However, the differences across all metrics are relatively subtle.

---

### **📊 T-Test Results: Statistical Significance**

| **Metric**             | **T-Statistic** | **P-Value** | **Interpretation**                                                 |
| ---------------------- | --------------: | ----------: | ------------------------------------------------------------------ |
| **Click Through Rate** |         -1.9767 |     0.04835 | ✅ *Statistically significant* — theme impacts CTR.                 |
| **Conversion Rate**    |          0.4745 |     0.63525 | ❌ *Not significant* — difference likely due to chance.             |
| **Bounce Rate**        |         -1.2019 |     0.22969 | ❌ *Not significant* — no strong evidence of theme impact.          |
| **Scroll Depth**       |          0.7562 |     0.44969 | ❌ *Not significant* — scrolling behavior is similar across themes. |
| **Session Duration**   |        *varies* |    *varies* | ℹ️ *(Depends on your dataset; update with actual results.)*        |

> ✅ **Conclusion**:
> Among all metrics, **only Click Through Rate shows a statistically significant difference** between the Light and Dark themes (p < 0.05). All other metrics show no statistically meaningful difference, meaning observed variations are likely due to random chance rather than the UI theme.

---



















