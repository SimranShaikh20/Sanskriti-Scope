from haversine import haversine
import pandas as pd

def get_route_recommendations(df, start_district, top_n=4):
    # Ensure numeric lat/lon
    df["LATITUDE"] = pd.to_numeric(df["LATITUDE"], errors='coerce')
    df["LONGITUDE"] = pd.to_numeric(df["LONGITUDE"], errors='coerce')
    df = df.dropna(subset=["LATITUDE", "LONGITUDE"])

    if start_district not in df["REGION"].values:
        return pd.DataFrame()

    origin = df[df["REGION"] == start_district].iloc[0]
    origin_coords = (origin["LATITUDE"], origin["LONGITUDE"])

    df_rest = df[df["REGION"] != start_district].copy()

    df_rest["DISTANCE_KM"] = df_rest.apply(
        lambda row: haversine(origin_coords, (row["LATITUDE"], row["LONGITUDE"])), axis=1
    )

    df_rest["SCORE"] = (
        df_rest["ENDANGERED"].apply(lambda x: 2 if x == "Endangered" else 1)
        + df_rest["UNESCOLISTED"].apply(lambda x: 1 if x == "Yes" else 0)
        - 0.01 * df_rest["DISTANCE_KM"]
    )

    recommendations = df_rest.sort_values("SCORE", ascending=False).head(top_n)
    return recommendations
