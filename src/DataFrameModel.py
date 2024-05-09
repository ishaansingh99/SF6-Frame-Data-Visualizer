import sys
import re
import pandas as pd
import numpy as np
from PySide6.QtCore import QAbstractTableModel, Qt


class DataFrameModel(QAbstractTableModel):

    def __init__(self, df: pd.DataFrame, parent=None):
        super().__init__(parent)
        self._data = df

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
            
    def setDataFrame(self, df):
        self.beginResetModel()
        self._data = df
        self.endResetModel()