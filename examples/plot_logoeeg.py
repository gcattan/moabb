"""
================================
Logo EEG experiment
================================

"""

# License: BSD (3-clause)

import warnings

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from pyriemann.channelselection import ElectrodeSelection
from pyriemann.estimation import Covariances
from pyriemann.spatialfilters import Xdawn
from pyriemann.tangentspace import TangentSpace
from pyriemann.classification import MDM
from sklearn.base import TransformerMixin
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold, cross_val_score

from moabb import set_log_level
from moabb.datasets import LogoEEG, EVENTS_LOGOEEG
from moabb.evaluations import CrossSessionEvaluation, CrossSubjectEvaluation
from moabb.paradigms import RestingStateToP300Adapter


# Suppressing future and runtime warnings for cleaner output
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=RuntimeWarning)

set_log_level("info")

paradigm = RestingStateToP300Adapter(events=EVENTS_LOGOEEG, tmin=0, tmax=2, resample=250)
datasets = [LogoEEG()]



pipelines = {}


pipelines["Cov+TS+LDA"] = make_pipeline(
    Covariances(estimator="lwf"), MDM()
)

X, y, meta = paradigm.get_data(datasets[0], subjects=[1, 2, 3, 4, 5, 6])

cv = StratifiedKFold(n_splits=2)
scores = cross_val_score(pipelines["Cov+TS+LDA"], X, y, cv=cv, scoring="balanced_accuracy")
print(scores)

exit()
