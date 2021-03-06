"""

"""
# Standard Libraries
import os
import copy

# External Libraries
import mlflow.pyfunc


MODEL_EXAMPLE_SUBPATH = "viz.html"
MODEL_DATA_SUBPATH = "viz.pkl"


class Style(mlflow.pyfunc.PythonModel):
    """"""

    def predict(self, context, model_input):
        pass

    def __init__(
        self,
        artifact_uri,
    ):
        import cloudpickle

        self.artifact_uri = artifact_uri
        with open(self.artifact_uri, "rb") as f:
            self.model = cloudpickle.load(f)

    def __str__(self):
        """"""
        return self.__repr__()

    def _repr_html_(self):
        """"""
        return self.model.to_html()

    def display(self, model_input):
        """"""
        model = copy.deepcopy(self.model)
        model.data = model_input
        return model

    @staticmethod
    def save(model, path):
        """"""
        import cloudpickle

        with open(os.path.join(path, MODEL_DATA_SUBPATH), "wb") as out:
            cloudpickle.dump(model, out)
