import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["units_sold"] * df["unit_price"]
    return df


def get_total_revenue(df):
    return df["revenue"].sum()


def get_sales_by_region(df):
    return df.groupby("region")["revenue"].sum().reset_index()


def get_sales_by_product(df):
    return df.groupby("product")["revenue"].sum().reset_index()


def get_top_product(df):
    product_sales = get_sales_by_product(df)
    top_product = product_sales.sort_values("revenue", ascending=False).iloc[0]
    return top_product["product"]