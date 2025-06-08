# 💎 Diamond Data Analysis – Kunskapskontroll Python

This is a data storytelling and analysis project built with **Python**, **Pandas**, **Matplotlib**, and **Streamlit**. It presents insights and visualizations from a diamond dataset in an interactive web app.

🚀 **Live Demo:**  
[https://kunskapskontrollpython-cz8ixmmneinsxx5k6wg8ip.streamlit.app/](https://kunskapskontrollpython-cz8ixmmneinsxx5k6wg8ip.streamlit.app/)

---

## 📊 Features

- Load and clean diamond dataset
- Display key metrics (average price, carat, etc.)
- Visualizations:
  - Price vs Carat scatter plot
  - Distribution by cut, clarity, and color
  - Correlation heatmap
- Insightful summary and recommendations

---

## ▶️ Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/kunskapskontroll_python.git
   cd kunskapskontroll_python
   ```

2. **Create virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run del2/diamonds.py
   ```

---

## 🛠 Deployment Notes

- Avoid absolute file paths like `/Users/username/...`.
- Always use relative paths or dynamic path resolution:
  ```python
  import os
  file_path = os.path.join(os.path.dirname(__file__), "diamonds.csv")
  df = pd.read_csv(file_path)
  ```
- Ensure `diamonds.csv` is included in the repo (not in `.gitignore`).

---

## 🧠 Author

**Hiba Khaleel**  
Student at NBI Academy – Software Development Specialized in AI  
Project: Kunskapskontroll Python 

---
