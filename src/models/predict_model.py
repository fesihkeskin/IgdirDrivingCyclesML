# src/models/predict_model.py

import os
import pandas as pd
import joblib
import src.visualization.visualize as viz

def load_model(model_dir):
    model_file = os.path.join(model_dir, 'xgboost_model.pkl')
    model = joblib.load(model_file)
    return model

def make_forecast(df, model):
    X = df.drop(columns=['Time', 'Speed', 'Acceleration', 'Cycle'])
    predictions = model.predict(X)
    df['Predicted_Speed'] = predictions
    return df

def save_predictions(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'predictions.csv')
    df.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

def main():
    processed_data_dir = "data/processed"
    processed_file = os.path.join(processed_data_dir, 'features_data.csv')
    model_dir = "models"
    
    df = pd.read_csv(processed_file)
    model = load_model(model_dir)
    
    predictions_df = make_forecast(df, model)
    
    reports_dir = "reports"
    save_predictions(predictions_df, reports_dir)

    # Visualize predictions
    viz.plot_actual_vs_predicted(predictions_df['Speed'], predictions_df['Predicted_Speed'])

if __name__ == "__main__":
    main()
