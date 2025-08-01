# Site Survey-free RSSI-based Indoor Positioning System

## Overview

This project implements a **Site Survey-free RSSI-based Indoor Positioning System** using advanced optimization algorithms including **Differential Evolution** and **SLSQP (Sequential Least Squares Programming)**. The system estimates device positions in indoor environments using Received Signal Strength Indicator (RSSI) measurements from Bluetooth Low-Energy (BLE) Access Points (APs) without requiring extensive site surveys.

## 🎯 Key Features

- **Site Survey-free**: Eliminates the need for extensive manual calibration
- **Multiple Positioning Algorithms**:
  - Nearest-Neighbor (NN) baseline algorithm
  - Mean-Chebyshev distance algorithm
  - SLSQP optimization for improved accuracy
- **Advanced Path Loss Modeling**: Log-distance path loss model with optimizable parameters
- **Parallel Processing**: Multi-core parameter optimization using ProcessPoolExecutor
- **Comprehensive Statistical Analysis**: 
  - Paired statistical tests with large sample methodology
  - Normality assessment and non-parametric testing
  - Effect size analysis and practical significance evaluation
  - Multiple comparison correction (Bonferroni)
- **Distance Metrics Analysis**: Euclidean, Chebyshev, and Standardized Euclidean comparisons
- **Professional Visualization**: Publication-quality plots with customizable fonts and comprehensive graphical analysis

## 📁 Project Structure

```
thesis/
├── data/                           # Dataset files
│   ├── AP_crd.csv                 # Access Point coordinates
│   ├── filtered_data.csv          # Preprocessed dataset
│   ├── raw_data.csv              # Original RSSI measurements
│   └── test_data.csv             # Test dataset
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── 1.data_cleaning.ipynb     # Data preprocessing and cleaning
│   ├── 2.test_set.ipynb          # Test set preparation and validation
│   ├── 3.tools_set.ipynb         # Algorithm implementations and testing
│   ├── 4.pairwise_distances.ipynb # Distance analysis and metrics comparison
│   ├── 5.graphics.ipynb          # Visualization and results plotting
│   └── 6.statistical_analysis.ipynb # Comprehensive statistical analysis
├── output/                        # Generated results and analysis data
│   ├── nn_results_by_params.csv  # NN algorithm results by parameters
│   ├── nn_results_by_device.csv  # NN algorithm results by device
│   ├── optimized_results_*.csv   # SLSQP optimization results
│   ├── optimal_parameters_by_algorithm.csv # Best parameters for each algorithm
│   ├── grouped_device_results.csv # Device-grouped performance data
│   ├── *_pairwise_distances_*.csv # Distance analysis results
│   └── optimized_device_stats.csv # Statistical summaries by device
├── figures/                       # Generated plots and publication figures
│   ├── algorithm_statistical_comparison.pdf # Statistical comparison plots
│   ├── positioning_error_comparison.pdf    # Algorithm performance comparison
│   ├── optimal_parameters_barplot.pdf      # Parameter optimization results
│   ├── pairwise_distances_comparison.pdf   # Distance metrics analysis
│   └── cumulative_error_distribution.pdf   # Error distribution analysis
├── utils/                         # Utility functions
│   └── tools.py                  # Core algorithms and utilities
├── main.py                       # Main application entry point
├── pyproject.toml                # Project configuration
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Required packages (automatically installed with uv or pip)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd thesis
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

### Dependencies

- **pandas** (≥2.3.0): Data manipulation and analysis
- **numpy** (≥2.3.1): Numerical computing
- **scipy** (≥1.16.0): Scientific computing, optimization, and statistical analysis
- **matplotlib** (≥3.10.3): Plotting and visualization
- **seaborn** (≥0.13.2): Statistical data visualization
- **scikit-learn** (≥1.7.0): Machine learning utilities and metrics
- **jupyter** (≥1.1.1): Interactive notebook environment
- **pyswarms** (≥1.3.0): Particle swarm optimization

## 📊 Datasets

### Input Data

- **`AP_crd.csv`**: Access Point coordinates (X, Y positions)
- **`test_data.csv`**: RSSI measurements from mobile devices
- **`raw_data.csv`**: Original unprocessed RSSI data

### Generated Data

- **Algorithm Results**: Performance metrics for NN, Mean-Chebyshev, and SLSQP algorithms
- **Optimization Results**: SLSQP algorithm performance across devices and parameters
- **Statistical Analysis**: Comprehensive paired analysis results and significance testing
- **Pairwise Distances**: Distance analysis using various metrics (Euclidean, Chebyshev, Standardized Euclidean)
- **Parameter Optimization**: Optimal parameter combinations for each algorithm and ρ₀ value

## 🔬 Methodology

### Log-Distance Path Loss Model

The system uses the log-distance path loss model:

```
RSSI = -ρ₀ - 10α log₁₀(d)
```

Where:
- **ρ₀**: Signal path loss at reference distance (1 meter)
- **α**: Path loss exponent
- **d**: Distance from transmitter to receiver

### Positioning Algorithms

1. **Nearest-Neighbor (NN)**:
   - Baseline algorithm using RSSI fingerprinting
   - Fast computation with moderate accuracy

2. **Mean-Chebyshev Distance**:
   - Distance-based positioning using Chebyshev metric
   - Intermediate performance between NN and SLSQP

3. **SLSQP Optimization**:
   - Sequential Least Squares Programming
   - Minimizes positioning error through parameter optimization
   - Significantly improved accuracy over baseline methods

### Optimization Framework

- **Parameter Space**: ρ₀ ∈ [40, 80] dB, α ∈ [1.0, 7.0]
- **Parallel Processing**: Multi-core optimization for efficiency
- **Statistical Analysis**: Comprehensive performance comparison with proper statistical methodology
- **Large Sample Analysis**: Robust statistical testing with n≈1420 samples per condition
- **Multiple Testing Correction**: Bonferroni adjustment for family-wise error rate control

## 📈 Results and Analysis

### Performance Metrics

- **Average Positioning Error**: Mean error across all test points
- **Algorithm Comparison**: NN vs Mean-Chebyshev vs SLSQP performance analysis
- **Parameter Sensitivity**: Error variation across (ρ₀, α) combinations
- **Statistical Significance**: Rigorous hypothesis testing with appropriate corrections
- **Effect Size Analysis**: Practical significance assessment using Cohen's d
- **Confidence Intervals**: 95% CI for mean differences and performance metrics
- **Normality Assessment**: Comprehensive testing for appropriate statistical method selection

### Visualization

The project generates publication-quality visualizations including:

- **Algorithm Performance Comparison**: 
  - Individual algorithm performance across ρ₀ values
  - Direct algorithm comparison with statistical significance markers
  - Effect size visualization with Cohen's d interpretation
  - P-value distributions and significance thresholds
- **Statistical Analysis Plots**:
  - Normality assessment with histograms and Q-Q plots
  - Paired differences distributions for non-zero cases
  - Comprehensive statistical comparison matrices
- **Distance Analysis**: 
  - Pairwise distance comparisons across metrics
  - Distance distribution analysis and visualization
- **Parameter Optimization**:
  - Optimal parameter identification across algorithms
  - Performance improvement quantification
- **Professional Typography**: Bookman Old Style fonts for academic presentation
- **Mathematical Notation**: Proper rendering of Greek symbols and statistical notation

## 📝 Usage

### Running the Analysis

1. **Data Preprocessing**:
```bash
jupyter notebook notebooks/1.data_cleaning.ipynb
```

2. **Test Set Preparation**:
```bash
jupyter notebook notebooks/2.test_set.ipynb
```

3. **Algorithm Implementation**:
```bash
jupyter notebook notebooks/3.tools_set.ipynb
```

4. **Distance Analysis**:
```bash
jupyter notebook notebooks/4.pairwise_distances.ipynb
```

5. **Results Visualization**:
```bash
jupyter notebook notebooks/5.graphics.ipynb
```

6. **Statistical Analysis**:
```bash
jupyter notebook notebooks/6.statistical_analysis.ipynb
```

### Key Functions

Located in `utils/tools.py`:

- **`get_distances()`**: Calculate distances between devices and APs
- **`expected_rssi()`**: Compute expected RSSI using path loss model
- **`nearest_neighbor_positioning()`**: NN algorithm implementation
- **`optimize_position()`**: SLSQP optimization algorithm
- **`comprehensive_normality_test_large()`**: Large sample normality testing
- **`statistical_comparison()`**: Comprehensive paired statistical analysis

## 🎓 Academic Context

This project is part of a thesis research on indoor positioning systems. The work focuses on:

- **Eliminating Site Surveys**: Reducing deployment complexity and calibration requirements
- **Algorithm Optimization**: Improving positioning accuracy through advanced optimization techniques
- **Comparative Analysis**: Rigorous statistical comparison with proper hypothesis testing
- **Statistical Methodology**: Large sample analysis with appropriate corrections for multiple testing
- **Practical Implementation**: Real-world applicability with comprehensive performance evaluation
- **Distance Metrics Evaluation**: Multi-metric analysis for robust positioning assessment

## 📊 Key Findings

- **Algorithm Performance Hierarchy**: SLSQP(+) > Mean-Chebyshev > NN in positioning accuracy
- **Statistical Significance**: SLSQP(+) shows significant improvements at extreme ρ₀ values (40.0, 42.5, 72.5, 75.0, 77.5, 80.0 dB)
- **Effect Sizes**: Small but consistent improvements (Cohen's d ≈ 0.073 ± 0.037)
- **Practical Impact**: Mean improvement of ~30.6 mm in positioning accuracy
- **Parameter Optimization**: Optimal (ρ₀, α) combinations identified for each algorithm
- **Statistical Robustness**: Large sample analysis (n≈1420) with proper multiple testing correction
- **Distance Metrics**: Comprehensive analysis across Euclidean, Chebyshev, and Standardized Euclidean metrics
- **Scalability**: Parallel processing enables large-scale parameter exploration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📄 License

This project is part of academic research. Please cite appropriately if used in academic work.

## 🔗 References

- Log-distance path loss model for indoor environments
- SLSQP optimization algorithm documentation
- RSSI-based indoor positioning literature
- Statistical analysis methodology for large samples
- Wilcoxon signed-rank test for non-parametric paired comparisons
- Cohen's d effect size interpretation guidelines
- Bonferroni correction for multiple testing

---

**Author**: Bráulio Pinto
**Institution**: Federal University of Amazonas - Institute of Computing
**Year**: 2025