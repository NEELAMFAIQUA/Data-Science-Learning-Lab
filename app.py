import streamlit as st

from lab import ROWS, group_mean, pearson_correlation

st.set_page_config(page_title="Data Science Learning Lab", page_icon="🔬")
st.title("Data Science Learning Lab")
st.markdown(
    "### Lesson: describe before you model\n"
    "Use the sample study-practice table to compare groups and explore "
    "relationships. The data is fictional."
)
st.dataframe(ROWS, use_container_width=True)
grouped = group_mean(ROWS, "group", "score")
st.subheader("Average score by group")
st.bar_chart(grouped)
correlation = pearson_correlation(
    [row["minutes"] for row in ROWS],
    [row["score"] for row in ROWS],
)
st.metric("Practice minutes / score correlation", f"{correlation:.2f}")
st.info(
    "A correlation describes a pattern in this small sample; it does not show "
    "that practice time caused score changes."
)
