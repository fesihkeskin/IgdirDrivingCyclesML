# Advanced Driving Cycle Generation Using XGBoost: A Case Study in Iğdır, Türkiye

Welcome to the repository for our paper, "[Advanced Driving Cycle Generation Using XGBoost: A Case Study in Iğdır, Türkiye](https://doi.org/10.1109/IDAP64064.2024.10710756)."

This repository contains the code and data used in our study, which presents a novel framework for driving cycle generation leveraging On-Board Diagnostics (OBD) data and the XGBoost algorithm. The case study focuses on [Igdir, Turkey](https://www.google.com/maps/dir/39.9186162,44.0435286/39.9228033,44.0456321/39.930725,44.047373/39.9374025,44.0801313/39.9044083,44.0610306/39.9185878,44.0435193/@39.917033,44.0667609,14z/data=!4m2!4m1!3e0!5m1!1e1?entry=ttu&g_ep=EgoyMDI0MDgyNy4wIKXMDSoASAFQAw%3D%3D), known for its complex and diverse urban traffic patterns. Our framework outperforms traditional methods like Markov chains, offering more accurate and region-specific tools for vehicle performance and emissions evaluation.

---

## Project Structure

The project is organized as follows:

```sh
IgdirDrivingCyclesML/
├── data/
│   ├── processed/                 # Processed datasets
│   │   ├── combined_data.csv       # Combined driving data from all cycles
│   │   ├── cycle_lengths.txt       # Length of each driving cycle
│   │   └── features_data.csv       # Feature-engineered dataset
│   └── raw/                        # Raw datasets
│       ├── D01.txt                 # Raw driving data for cycle D01
│       ├── D02.txt                 # Raw driving data for cycle D02
│       ├── ...                     # (Additional raw data files)
│       └── segment_sizes.mat       # MATLAB file containing segment sizes
├── docs/                           # Documentation
├── models/                         # Trained models
│   └── xgboost_model.pkl           # Serialized XGBoost model
├── notebooks/                      # Jupyter notebooks
│   └── driving_cycle.ipynb         # Notebook for analysis
├── references/                     # References and scripts
├── reports/                        # Reports, figures, and metrics
├── src/                            # Source code
├── README.md                       # This README file
├── environment.yml                 # Conda environment configuration
└── requirements.txt                # Python dependencies
```

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Conda (recommended) or Python's `virtualenv`

### Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/IgdirDrivingCyclesML.git
   cd IgdirDrivingCyclesML
   ```

2. **Create the Conda environment**:
   ```bash
   conda env create -f environment.yml
   conda activate igdir-driving-cycles
   ```

   Alternatively, if you're using `virtualenv`, install dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
---

## Usage

### Step 1: Data Processing
```bash
python src/data/make_dataset.py
```

### Step 2: Feature Engineering
```bash
python src/features/build_features.py
```

### Step 3: Model Training
```bash
python src/models/train_model.py
```

### Step 4: Model Prediction
```bash
python src/models/predict_model.py
```

### Step 5: Manual Data Split and Testing
```bash
python src/models/manual_split_test.py
```

---

## Documentation and Visualizations

- **Figures**: Saved in `reports/figures/`.
- **Reports and Logs**: Saved in `reports/`.

---

## Citation

If you use this repository in your research or work, please cite our paper:

```diff
@InProceedings{Keskin2024,
  author    = {Keskin, Fesih},
  booktitle = {2024 8th International Artificial Intelligence and Data Processing Symposium (IDAP)},
  title     = {Advanced Driving Cycle Generation Using XGBoost: A Case Study in Iğdır, Türkiye},
  year      = {2024},
  month     = sep,
  pages     = {1--6},
  publisher = {IEEE},
  doi       = {10.1109/idap64064.2024.10710756},
}
```
```diff
F. Keskin, "Advanced Driving Cycle Generation Using XGBoost: A Case Study in Iğdır, Türkiye," 2024 8th International Artificial Intelligence and Data Processing Symposium (IDAP), Malatya, Turkiye, 2024, pp. 1-6, doi: 10.1109/IDAP64064.2024.10710756.
```

---

## License

The code and data in this repository are licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## Contact

For questions or feedback, please contact: [fesih.keskin@igdir.edu.tr](mailto:fesih.keskin@igdir.edu.tr).
