
import pandas as pd # dung su ly du lieu dang bang doc , loc du lieu tu csv excel

def xulydulieu(df, physiological_ranges):
    df = df.copy()

    zero_sensitive_columns = [
        'Glucose',
        'BloodPressure',
        'SkinThickness',
        'Insulin',
        'BMI'
    ]

    # ===== Xử lý giá trị 0 =====
    for col in zero_sensitive_columns:
        if col not in df.columns:
            continue

        zero_mask = df[col] == 0

        if zero_mask.any():
            median_val = df.loc[df[col] > 0, col].median()

            if pd.isna(median_val):
                continue

            df.loc[zero_mask, col] = median_val

    # ===== Lọc dữ liệu 1 lần =====
    mask = pd.Series(True, index=df.index)

    for col, (min_val, max_val) in physiological_ranges.items():
        if col in df.columns:
            mask &= (df[col] >= min_val) & (df[col] <= max_val)

    df = df[mask]

    return df