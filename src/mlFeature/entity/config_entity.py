from dataclasses import dataclass
from pathlib import Path

@dataclass 
class DataIngestionConfig: 
  root_dir: Path
  source_URL: str
  local_data_file: Path
  unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    seed: int
    n_estimators: int
    max_depth: int
    eval_metric: str
    learning_rate: float
    min_child_weight: int
    subsample: float
    colsample_bytree: float 
    colsample_bylevel: float 
    gamma: float
    estimator: str
    param_grid: dict 
    cv: int
    refit: bool
    scoring: str
    target_column: str
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str