from haversine import haversine
import pandas as pd

def get_route_recommendations(df, start_district, top_n=4):
    if start_district not in df["Region"].values:
        return []

    # Get origin
    origin = df[df["Region"] == start_district].iloc[0]
    origin_coords = (origin["latitude"], origin["longitude"])

    # Exclude the starting district
    df_rest = df[df["Region"] != start_district].copy()

    # Calculate distances
    df_rest["distance_km"] = df_rest.apply(
        lambda row: haversine(origin_coords, (row["latitude"], row["longitude"])), axis=1
    )

    # Score destinations: endangered > UNESCO > closer distance
    df_rest["score"] = (
        df_rest["Endangered"].apply(lambda x: 2 if x == "Endangered" else 1)
        + df_rest["UNESCO Listed"].apply(lambda x: 1 if x == "Yes" else 0)
        - 0.01 * df_rest["distance_km"]
    )

    recommendations = df_rest.sort_values("score", ascending=False).head(top_n)
    return recommendations
