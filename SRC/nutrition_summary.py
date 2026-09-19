

"""Nutrition analysis module used in Parts 2 and 3 of Lab 2."""


class NutritionAnalyzer:
    """Explore descriptive statistics for selected nutrition features."""

    def __init__(self, dataframe):
        """Store the food DataFrame used by the analysis methods."""
        self.dataframe = dataframe

    def describe_features(self, feature_names):
        """Return descriptive statistics for the selected feature columns."""
        return self.dataframe[feature_names].describe()

    def build_nutrition_summary(self):
        """Return a dictionary with sugar summary"""
        summary = {}
        summary.update(self.summarize_sugars())
        summary.update(self.summarize_proteins())
        return summary

    def summarize_sugars(self):
        """Return dictionary with mean sugar and median sugar"""
        return {"mean_sugar": self.dataframe["sugars_100g"].mean(), "median_sugar": self.dataframe["sugars_100g"].median()}

    def summarize_proteins(self):
        """Return a dictionary with mean protein and median protein"""
        return {"mean_proteins": self.dataframe["proteins_100g"].mean(),"median_proteins": self.dataframe["proteins_100g"].median()}