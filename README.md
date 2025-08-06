# 🛍️ Customer Segmentation using K-Means Clustering

This project uses **K-Means Clustering** to group retail store customers based on their **annual income** and **spending score**, helping identify customer segments for targeted marketing and business strategies.

---

## 📊 Dataset

The dataset is hardcoded and includes:

| CustomerID | AnnualIncome (k$) | SpendingScore (1–100) |
|------------|-------------------|------------------------|
| 1          | 15                | 39                     |
| 2          | 16                | 81                     |
| 3          | 17                | 6                      |
| 4          | 18                | 77                     |
| 5          | 19                | 40                     |
| 6          | 50                | 85                     |
| 7          | 52                | 20                     |
| 8          | 53                | 90                     |
| 9          | 85                | 99                     |
| 10         | 86                | 55                     |

---

## 🧠 What It Does

- Applies **K-Means Clustering** using `scikit-learn`
- Uses the **Elbow Method** to find the optimal number of clusters
- Visualizes the customer clusters using `matplotlib` and `seaborn`
- Prints the **cluster centers** for analysis

---

## 📦 Libraries Used

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Install them with:

```bash
pip install pandas matplotlib seaborn scikit-learn
