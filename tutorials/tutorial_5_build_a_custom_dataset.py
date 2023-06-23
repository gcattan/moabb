"""
====================================
Tutorial 5: Creating a dataset class
====================================
"""
# Authors: Pedro L. C. Rodrigues, Sylvain Chevallier
#
# https://github.com/plcrodrigues/Workshop-MOABB-BCI-Graz-2019

from moabb.datasets import VirtualReality
from moabb.datasets.shopping import GoShoppingDataset
from moabb.paradigms.p300 import P300
from pyriemann.classification import MDM
from pyriemann.estimation import Covariances, ERPCovariances, XdawnCovariances
from sklearn.pipeline import make_pipeline

from moabb.datasets import download as dl
from moabb.datasets.base import BaseDataset
from moabb.evaluations import WithinSessionEvaluation
from moabb.paradigms import LeftRightImagery


##############################################################################
# Creating some Data
# ------------------
#
# To illustrate the creation of a dataset class in MOABB, we first create an
# example dataset saved in .mat file. It contains a single fake recording on
# 8 channels lasting for 150 seconds (sampling frequency 256 Hz). We have
# included the script that creates this dataset and have uploaded it online.
# The fake dataset is available on the
# `Zenodo website <https://sandbox.zenodo.org/record/369543>`_

def block_rep(blocks: list, reps: list):
    return [f'block_{b}-repetition_{r}' for b in blocks for r in reps]

class BiWithIlliteracy(GoShoppingDataset):
    def __init__(self):
        biVR = VirtualReality(virtual_reality=True, screen_display=True)
        selection = {
            1: (biVR, 1, 'VR', block_rep([1,2], [1,2,3,4,5])),
            2: (biVR, 2, 'VR', 'block_1-repetition_1'),
        }
        GoShoppingDataset.__init__(
            self,
            selection=selection,
            events=dict(Target=2, NonTarget=1),
            code="BI-ILL",
            interval=[0, 1.0],
            paradigm="p300"
        )
 
paradigm = P300()
datasets = [BiWithIlliteracy()]

evaluation = WithinSessionEvaluation(
    paradigm=paradigm, datasets=datasets, overwrite=False, suffix="newdataset"
)
pipelines = {}
pipelines["MDM"] = make_pipeline(ERPCovariances(), MDM(metric="riemann"))
scores = evaluation.process(pipelines)

print(scores)