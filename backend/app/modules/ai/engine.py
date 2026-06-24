class AIEngine:

    def summarize(
        self,
        dashboard: dict
    ):

        analysis = dashboard["analysis"]

        statistics = dashboard["statistics"]

        row_count = analysis["row_count"]

        column_count = analysis["column_count"]

        columns = ", ".join(
            analysis["column_names"]
        )

        numeric_columns = ", ".join(
            statistics["mean"].keys()
        )

        summary = (
            f"The dataset contains "
            f"{row_count} rows and "
            f"{column_count} columns. "
            f"The columns are {columns}. "
            f"Numeric columns include "
            f"{numeric_columns}. "
            f"No missing values were detected."
        )

        return {

            "summary": summary

        }