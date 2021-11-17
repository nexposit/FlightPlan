import pandas as pd
import math


# Calculates geographic distance
def haversine(lat1, long1, lat2, long2):
    rad = math.pi / 180
    dlat = lat2 - lat1
    dlong = long2 - long1
    R = 6372.795477598
    a = (math.sin(rad * dlat / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (math.sin(rad * dlong / 2)) ** 2
    dist = 2 * R * math.asin(math.sqrt(a))
    return dist


# Calculates the flight plan
def flight_plan(airport, sid, runway, waypoint, destination, iap):
    # Departure
    dp = departure[(departure["Airport"] == airport) & (departure["SID"] == sid) & (departure["Runway"] == runway)]
    dp = dp.drop(["Airport", "SID", "Runway"], axis=1)

    # Intermediate
    wp = pd.DataFrame()
    for i in waypoint:
        wp = pd.concat([wp, intermediate[intermediate["Waypoint"] == i]])

    # Arrival
    arr = arrival[(arrival["Airport"] == destination) & (arrival["IAP"] == iap)]
    arr = arr.drop(["Airport", "IAP"], axis=1)

    # Concatenate all waypoints
    waypoints = pd.concat([dp, wp, arr])

    # Calculate total distance between departure airport and waypoints
    waypoints.reset_index(drop=True, inplace=True)
    waypoints.loc[0, "Leg_distance"] = 0.0

    for i in range(1, waypoints.shape[0]):
        lat1 = waypoints.iloc[i - 1, 3]
        long1 = waypoints.iloc[i - 1, 4]
        lat2 = waypoints.iloc[i, 3]
        long2 = waypoints.iloc[i, 4]

        waypoints.loc[i, "Leg_distance"] = waypoints.iloc[i - 1, -1] + haversine(lat1, long1, lat2, long2)

    return waypoints


# Main
# Import all data
departure = pd.read_excel("SIDs_old.xlsx")
intermediate = pd.read_excel("WPs_old.xlsx")
arrival = pd.read_excel("IAPs_old.xlsx")


