import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv(
    "/Users/hibakhaleel/Desktop/Kunskapskontroll/del2/diamonds.csv")
df['price_per_carat'] = df['price'] / df['carat']

# Categorize features
df["carat_category"] = pd.cut(df["carat"], bins=[0, 0.5, 1, 1.5, 2, 5], labels=[
                              "Very Small", "Small", "Medium", "Large", "Very Large"])
df["clarity"] = pd.Categorical(df["clarity"], categories=[
                               "I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"], ordered=True)
df["color"] = pd.Categorical(df["color"], categories=[
                             "J", "I", "H", "G", "F", "E", "D"], ordered=True)
df["cut"] = pd.Categorical(df["cut"], categories=[
                           "Fair", "Good", "Very Good", "Premium", "Ideal"], ordered=True)

# Define clarity level


def classify_clarity(c):
    if c in ['I1', 'SI2', 'SI1']:
        return 'Low'
    elif c in ['VS2', 'VS1']:
        return 'Medium'
    elif c in ['VVS2', 'VVS1', 'IF']:
        return 'High'
    else:
        return 'Unknown'


df['clarity_level'] = df['clarity'].apply(classify_clarity)

# Most expensive diamond details
most_exp = df[df['price'] == df['price'].max()].iloc[0]
numerical_avgs = df[['carat', 'depth', 'table', 'x', 'y', 'z']].mean()
most_exp_features = most_exp[['carat', 'depth', 'table', 'x', 'y', 'z']]

# Streamlit UI
st.title("Diamonds Data Analysis")

st.header("Correlation Matrix")
corr = df.corr(numeric_only=True)
fig_corr = px.imshow(corr, text_auto=True, title="Feature Correlation Heatmap")
st.plotly_chart(fig_corr)

st.header("Relation Between Price and Carat with Feature Filter")
color_feature = st.selectbox("Select feature to color by", [
                             "clarity", "cut", "color", "carat_category"])
fig_scatter = px.scatter(df, x="carat", y="price", color=df[color_feature], trendline="ols", opacity=0.6,
                         title=f"Carat vs Price colored by {color_feature.title()}")
st.plotly_chart(fig_scatter)

# Most Expensive Diamond Section
st.header(" Most Expensive Diamond Analysis")

st.subheader("Diamond Details")
st.markdown(f"""
- **\U0001F4B0 Price**: ${most_exp['price']}
- **Carat**: {most_exp['carat']} (_{most_exp['carat_category']}_)
- **Cut**: {most_exp['cut']}
- **Color**: {most_exp['color']}
- **Clarity**: {most_exp['clarity']} (_{most_exp['clarity_level']}_)
- **Dimensions (mm)**: {most_exp['x']} x {most_exp['y']} x {most_exp['z']}
- **Depth**: {most_exp['depth']}%
- **Table**: {most_exp['table']}%
""")

st.markdown("###  Final Observation")
st.info("""
The most expensive diamond stands out due to its **very large carat size (2.29)**, 
which significantly exceeds the dataset average (0.80). It also has a **Premium cut** 
and **VS2 clarity**, offering good brilliance. Despite not having the top clarity or color grade, 
its **size and cut** drive the price up to **$18,823**.
""")

# Comparison Plot
st.subheader("Feature Comparison: Most Expensive Diamond vs Average")
fig, ax = plt.subplots(figsize=(10, 5))
numerical_avgs.plot(kind='bar', color='skyblue', width=0.4,
                    position=0, label='Average', ax=ax)
most_exp_features.plot(kind='bar', color='gold', width=0.4,
                       position=1, label='Most Expensive', ax=ax)
plt.title("Numerical Feature Comparison")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)
