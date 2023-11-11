ml-ethereum_from_coinbased_in_realtime 
==============================

Read Ethereum ticker from Coinbase in realtime.

Business Problem
------------

Quick setup
------------

1. Export environment variables
    ```
    # Bash
   $ export ABC="asd123"
    ```

2. Clone the project, cd into the project folder and run
    ```
    $ git clone https://github.com/mkaesz/xyz
    $ cd xyz
    $ make init
    ```

## See it in action
### Hosted on Streamlit Cloud
- [Live Dashboard with model predictions](https://ml-nyctaxidemandpredictor-benvmeyfusqdlquxsmvnak.streamlit.app/)
- [Live Dashboard with model monitoring ](https://ml-nyctaxidemandpredictor-ywu8raur4dgutsjodzcap9.streamlit.app/)

### Run it locally
Model predictions

    $ make frontend
    
Model monitoring

    $ make monitoring

Technologies, Frameworks, Services, Tools
------------

| Category                        | Used in this repo               |
|---------------------------------|---------------------------------|
| Type                            | Batch                     |
| Language                        | Python 3                        |
| Dependency Management           | Poetry                          |
| ML Framework                    | Scikit-Learn                    |
| ML Algorithm                    | LightGBM, XGBoost               |
| Hyperparameter Tuning Framework | Optuna                          |
| Feature Store                   | Hopsworks                       |
| Model Registry                  | Hopsworks                       |
| Web Application Framework       | Streamlit                       |
| Workflow Tool                   | Github Actions                  |
| Hosting                         | Streamlit Community Cloud       |
| Serving                         | Streamlit Community Cloud       |

Project Organization
------------

```
ml-ethereum_from_coinbased_in_realtime/
├── .github/workflows            # Github Actions pipelines. Execute the pipelines in src/pipelines.
├── LICENSE     
├── README.md                  
├── Makefile                     # Makefile with commands like `make data` or `make train`    
├── pyproject.toml               # Poetry config file                                    
├── configs                      # Config files (models and training hyperparameters)
│   └── model1.yaml              
│
├── data                         
│   ├── external                 # Data from third party sources.
│   ├── interim                  # Intermediate data that has been transformed.
│   ├── processed                # The final, canonical data sets for modeling.
│   └── raw                      # The original, immutable data dump.
│
├── docs                         # Project documentation.
│
├── models                       # Trained and serialized models.
│
├── notebooks                    # Jupyter notebooks.
│
├── references                   # Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                      # Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures                  # Generated graphics and figures to be used in reporting.
│
├── requirements.txt             # The requirements file for reproducing the analysis environment.
└── src                          # Source code for use in this project.
    ├── __init__.py              # Makes src a Python module.
    │
    ├── data                     # Data engineering scripts.
    │   ├── build_features.py    
    │   ├── cleaning.py          
    │   ├── ingestion.py         
    │   ├── labeling.py          
    │   ├── splitting.py         
    │   └── validation.py 
    ├── helpers                  # Helpers and utilities. 
    │      
    ├── models                   # ML model engineering (a folder for each model).
    │   └── model1      
    │       ├── dataloader.py    
    │       ├── hyperparameters_tuning.py 
    │       ├── model.py         
    │       ├── predict.py       
    │       ├── preprocessing.py 
    │       └── train.py         
    │
    ├── pipelines                # Pipelines for feature engineering, training and inference.
    │
    ├── ui                       # Web applications.
    │
    └── visualization            # Scripts to create exploratory and results oriented visualizations.
        ├── evaluation.py        
        └── exploration.py       
```

Credits
------------

Based on a tutorial from Pau Labarta Bajo.