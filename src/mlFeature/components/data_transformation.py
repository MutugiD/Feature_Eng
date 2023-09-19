import os
import numpy as np
import pandas as pd
from pathlib import Path
from mlFeature import logger
from sklearn.model_selection import train_test_split
from mlFeature.entity.config_entity import (DataTransformationConfig)

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def get_mov_avg_std(self, df, col, N):
        mean_list = df[col].rolling(window=N, min_periods=1).mean()
        std_list = df[col].rolling(window=N, min_periods=1).std()
        
        mean_list = np.concatenate((np.array([np.nan]), np.array(mean_list[:-1])))
        std_list = np.concatenate((np.array([np.nan]), np.array(std_list[:-1])))
        
        df_out = df.copy()
        df_out[col + '_mean'] = mean_list
        df_out[col + '_std'] = std_list
        return df_out


    def train_test_spliting(self):
        df = pd.read_csv(self.config.data_path)
        df.columns = [str(x).lower().replace(' ', '_') for x in df.columns]
        df['range_hl'] = df['high'] - df['low']
        df['range_oc'] = df['open'] - df['close']

        N = 3  # Move N definition above its usage
        lag_cols = ['close', 'range_hl', 'range_oc', 'volume']
        shift_range = [x + 1 for x in range(N)]  # Properly calculate shift_range
        
        for col in lag_cols:
            for i in shift_range:
                new_col = f'{col}_lag_{i}'
                df[new_col] = df[col].shift(i)
        
        cols_list = [
            "close",
            "range_hl",
            "range_oc",
            "volume"
        ]
        
        for col in cols_list:
            df = self.get_mov_avg_std(df, col, N)  # Use self.get_mov_avg_std
            train, test = train_test_split(df)  # Specify test_size here
            
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
            
            logger.info("Split data into training and test sets")
            logger.info(train.shape)
            logger.info(test.shape)

