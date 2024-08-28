# src/models/train_model.py

import os
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import matplotlib.pyplot as plt
import sys
# Get the absolute path of the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', '..')

# Add the parent directory to the sys.path
sys.path.append(parent_dir)
import src.visualization.visualize as viz

def train_xgboost_model(df):
    X = df.drop(columns=['Time', 'Speed', 'Acceleration', 'Cycle'])
    y = df['Speed']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.05)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)
    
    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")

    # Save metrics
    metrics = {'RMSE': rmse, 'MAE': mae}
    metrics_file = os.path.join("reports", "metrics.txt")
    with open(metrics_file, "w") as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")
    print(f"Metrics saved to {metrics_file}")
    
    # Plot and save feature importance
    viz.plot_feature_importance(model, X.columns)
    
    return model, X_test, y_test, y_pred

def save_model(model, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    model_file = os.path.join(output_dir, 'xgboost_model.pkl')
    joblib.dump(model, model_file)
    print(f"Model saved to {model_file}")

def main():
    processed_data_dir = "data/processed"
    processed_file = os.path.join(processed_data_dir, 'features_data.csv')
    
    df = pd.read_csv(processed_file)
    model, X_test, y_test, y_pred = train_xgboost_model(df)
    
    models_dir = "models"
    save_model(model, models_dir)
    
    # Plot actual vs predicted
    viz.plot_actual_vs_predicted(y_test, y_pred)
    
    # Plot residuals
    viz.plot_residuals(y_test, y_pred)

if __name__ == "__main__":
    main()
