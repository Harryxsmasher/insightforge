from pathlib import Path

import pandas as pd


class AnalysisEngine:

    def analyze(
        self,
        file_path: str
    ):

        dataframe = pd.read_csv(
            file_path
        )

        analysis = {

            "row_count": len(dataframe),

            "column_count": len(
                dataframe.columns
            ),

            "column_names": dataframe.columns.tolist(),

            "missing_values":

                dataframe.isnull()
                .sum()
                .to_dict(),

            "data_types":

                dataframe.dtypes
                .astype(str)
                .to_dict()

        }

        return analysis