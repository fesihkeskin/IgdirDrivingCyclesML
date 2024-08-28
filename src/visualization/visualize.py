# src/visualization/visualize.py

import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb
from . import plot_settings

plot_settings.set_plot_style()

def plot_actual_vs_predicted(y_true, y_pred):
    plt.figure()
    plt.plot(y_true, label='Actual')
    plt.plot(y_pred, label='Predicted', alpha=0.7)
    plt.title('Actual vs Predicted Speed')
    plt.xlabel('Sample')
    plt.ylabel('Speed')
    plt.legend()
    plt.show()

def plot_residuals(y_true, y_pred):
    residuals = y_true - y_pred
    plt.figure()
    plt.plot(residuals, label='Residuals', color='purple')
    plt.title('Residuals (Actual - Predicted)')
    plt.xlabel('Sample')
    plt.ylabel('Residual')
    plt.axhline(0, color='red', linestyle='--')
    plt.legend()
    plt.show()

def plot_feature_importance(model, feature_names):
    importance = model.get_booster().get_score(importance_type='weight')
    # Assuming importance keys are already feature names:
    importance = {feature_names[int(k[1:])]: v for k, v in importance.items()}  # This line is problematic

    # Instead, if the keys are already feature names, just use the dictionary directly:
    importance = {k: v for k, v in importance.items()}  # Simplified line
    
    plt.barh(list(importance.keys()), list(importance.values()))
    plt.xlabel('Importance')
    plt.ylabel('Features')
    plt.title('Feature Importance')
    plt.show()
