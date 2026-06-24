import plotly.express as px
import pandas as pd


class VisualizationEngine:

    def histogram(
        self,
        file_path: str,
        column: str
    ):

        dataframe = pd.read_csv(
            file_path
        )

        figure = px.histogram(
            dataframe,
            x=column
        )

        return figure.to_json()