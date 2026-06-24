import pandas as pd


class StatisticsEngine:

    def summary(
        self,
        file_path: str
    ):

        dataframe = pd.read_csv(
            file_path
        )

        numeric_dataframe = dataframe.select_dtypes(
            include="number"
        )

        summary = {

            "mean":

                numeric_dataframe.mean()
                .to_dict(),

            "median":

                numeric_dataframe.median()
                .to_dict(),

            "std":

                numeric_dataframe.std()
                .to_dict(),

            "min":

                numeric_dataframe.min()
                .to_dict(),

            "max":

                numeric_dataframe.max()
                .to_dict()

        }

        return summary