import numpy as np
import pandas as pd

def engineer_features(data):
    out = data.copy()
    out["bmi_missing"] = out["bmi"].isna().astype(int)
    out["smoking_status"] = out["smoking_status"].fillna("Unknown")
    out["age_group"] = pd.cut(
        out["age"], bins=[0, 18, 40, 60, 80, np.inf],
        labels=["0-17", "18-39", "40-59", "60-79", "80+"], right=False
    ).astype(str)
    # Neutral numerical bins: average glucose is not necessarily fasting glucose.
    out["glucose_category"] = pd.cut(
        out["avg_glucose_level"], bins=[0, 100, 126, np.inf],
        labels=["Below 100", "100 to <126", "126+"], right=False
    ).astype(str)
    out["ever_married"] = out["ever_married"].map({"No": 0, "Yes": 1})
    out["Residence_type"] = out["Residence_type"].map({"Rural": 0, "Urban": 1})
    return out.drop(columns=["id"])
