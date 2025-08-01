import pandas as pd
from pathlib import Path
from typing import List, TypedDict
import numpy as np

# Find project root (goes up from utils directory to thesis)
project_root = Path(__file__).resolve().parents[1]

# Construct data path relative to project root
data_rssi_path = project_root / 'data' / 'test_data.csv'
data_ap_path = project_root / 'data' / 'AP_crd.csv'

# Read the CSV file (test data) and replace RSSI values equal to 100 with -100
df_test = pd.read_csv(data_rssi_path).replace(100, -100)
# Read the AP coordinates CSV file
df_AP = pd.read_csv(data_ap_path)

def get_distances(df: pd.DataFrame, ap_df: pd.DataFrame, H: float) -> List[dict]:
    """
    Calculate distances from all AP coordinates to each point in the DataFrame.

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing position data with X, Y coordinates and LABEL
    ap_df : pandas.DataFrame
        DataFrame containing AP coordinates with columns 'AP', 'X', 'Y'
    H: float
        Height offset to be added to the Euclidean distance calculation
    Returns:
    --------
    list of dictionaries
        Each dictionary corresponds to a row in df, where:
        - keys are WAP identifiers
        - values are Euclidean distances from the point to each WAP
    """
    # Get all WAP columns from the test dataframe
    wap_columns = [col for col in df.columns if col.startswith('WAP')]

    # Create a mapping of WAP names to their coordinates
    ap_coords = {}
    for _, row in ap_df.iterrows():
        ap_name = row['AP']
        if ap_name in wap_columns:  # Only include APs that exist in the test data
            ap_coords[ap_name] = (row['x'], row['y'])

    # Calculate distances for each point
    distances_list = []
    for _, row in df.iterrows():
        point_coords = (row['X'], row['Y'])

        # Calculate distance to each AP
        distances = {}
        for wap_name in wap_columns:
            if wap_name in ap_coords:
                # Euclidean distance calculation
                ap_x, ap_y = ap_coords[wap_name]
                distance = ((point_coords[0] - ap_x) ** 2 + (point_coords[1] - ap_y) ** 2 + H ** 2) ** 0.5
                distances[wap_name] = round(distance, 2)
            else:
                # Handle missing AP coordinates
                distances[wap_name] = None

        distances_list.append(distances)

    return distances_list

distances = get_distances(df_test, df_AP, H=2.0)  # Assuming H is 2.0 meters

class LogParams(TypedDict):
    rho_0: float  # Signal path loss at the reference distance of 1 meter
    alpha: float  # Path loss exponent

def expected_rssi(distances: List[dict], df_ap: pd.DataFrame, log_params: LogParams) -> pd.DataFrame:
    """
    Calculate expected RSSI values based on distances to APs.

    Parameters:
    -----------
    distances : list of dict
        List of dictionaries containing distances to each AP for each point
    df_ap : pandas.DataFrame
        DataFrame containing AP coordinates and their RSSI values
    log_params : LogParams
        Dictionary containing parameters for the log-distance path loss model, including:
        - 'rho_0': Signal path loss at the reference distance of 1 meter
        - 'alpha': Path loss exponent
    Returns:
    --------
    pandas.DataFrame
        DataFrame with expected RSSI values added for each point
    """
    # Create a new DataFrame to hold the distances
    rssi_df = pd.DataFrame(distances)

    # Iterate through the rssi_df and calculate expected RSSI (each distance is substituted with the corresponding RSSI value)
    for wap in rssi_df.columns:
        if wap in df_ap['AP'].values:
            # Replace distances with expected RSSI values
            rssi_df[wap] = - log_params['rho_0'] - 10 * log_params['alpha'] * np.log10(rssi_df[wap])
            # Round the expected RSSI values to 2 decimal places
            rssi_df[wap] = rssi_df[wap].round(2)
    # Replace all rssi values less or equal to -100 with -100
    rssi_df = rssi_df.clip(lower=-100, upper=None)

    # Add the LABEL column from the original DataFrame
    rssi_df['LABEL'] = df_test['LABEL'].values
    # Add the DEVICE column from the original DataFrame
    rssi_df['DEVICE'] = df_test['DEVICE'].values
    # Add the X and Y coordinates from the original DataFrame
    rssi_df['X'] = df_test['X'].values
    rssi_df['Y'] = df_test['Y'].values

    return rssi_df
