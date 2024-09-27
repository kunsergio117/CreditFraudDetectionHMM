CreditFraudDetectionHMM/
│
├── data/
│   ├── raw/                  # Directory for raw CSV data
│   └── processed/            # Directory for processed data
│
├── models/
│   ├── __init__.py           # Make this directory a package
│   ├── hmm_model.py          # Implementations related to the HMM
│   └── rnn_model.py          # Implementations related to the RNN
│
├── scripts/
│   ├── data_preprocessing.py # Scripts for data preprocessing
│   └── train.py              # Script to train both models
│
├── notebooks/
│   ├── exploration.ipynb     # Jupyter notebooks for exploratory data analysis
│   └── evaluation.ipynb      # For model evaluation and comparison
│
├── interface/
│   ├── dashboard.py          # Code for creating the user interface (e.g., with Streamlit or Flask)
│   └── templates/            # HTML templates if using a web framework like Flask
│
├── utils/
│   ├── common.py             # Utility functions that can be used across the project
│   └── visualization.py      # Functions for plotting and visualizations
│
├── tests/
│   ├── test_hmm.py           # Unit tests for HMM model
│   ├── test_rnn.py           # Unit tests for RNN model
│   └── test_utils.py         # Unit tests for utility functions
│
├── requirements.txt          # List of required Python packages
├── README.md                 # Documentation for your project
└── .gitignore                # Git ignore file

To Joseph:
under interface directory, we will be using Flask as a framework for presenting the dashboard or alerts to the user for credit fraud,
if you feel more comfortable with some other framework like Django you can use it, I just thought that Flask was the simplest and easiest to integrate with this existing
structure.

If you are using Flask, the interface directory will look like this:
├── interface/
│   ├── app.py                 # Main Flask application
│   ├── templates/             # HTML templates for rendering views
│   │   ├── layout.html        # Base template
│   │   └── index.html         # Home page template
│   └── static/                # Static files (CSS, JavaScript, images)