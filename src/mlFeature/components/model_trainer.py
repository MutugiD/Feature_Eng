import os
import joblib
import pandas as pd
from mlFeature import logger
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from mlFeature.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        train_data = train_data.drop(['date'], axis=1)
        test_data = test_data.drop(['date'], axis=1)
        
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        xgb_params = {
            "seed": self.config.seed,
            "n_estimators": self.config.n_estimators,
            "max_depth": self.config.max_depth,
            "eval_metric": self.config.eval_metric,
            "learning_rate": self.config.learning_rate,
            "min_child_weight": self.config.min_child_weight,
            "subsample": self.config.subsample,
            "colsample_bytree": self.config.colsample_bytree,
            "colsample_bylevel": self.config.colsample_bylevel,
            "gamma": self.config.gamma
        }

        xgb_model = XGBRegressor(**xgb_params)
        
        grid_search_params = {
            "estimator": xgb_model,
            "param_grid": self.config.param_grid,
            "cv": self.config.cv,
            "refit": self.config.refit,
            "scoring": self.config.scoring
        }

        gs = GridSearchCV(**grid_search_params)
        gs.fit(train_x, train_y)
        joblib.dump(gs, os.path.join(self.config.root_dir, self.config.model_name))



