"""
====================================
Tutorial 5: Creating a dataset class
====================================
"""
# Authors: Pedro L. C. Rodrigues, Sylvain Chevallier
#
# https://github.com/plcrodrigues/Workshop-MOABB-BCI-Graz-2019

from moabb.datasets import VirtualReality
from moabb.datasets.braininvaders import bi2014a
from moabb.datasets.shopping import GoShoppingDataset
from moabb.datasets.shopping.bi_illiteracy import bi2014a_il, VirtualReality_il
from moabb.datasets.utils import blocks_reps
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


class CustomDataset1(GoShoppingDataset):
    def __init__(self):
        biVR = VirtualReality(virtual_reality=True, screen_display=True)
        runs =  blocks_reps([1,3], [1,2,3,4,5])
        shopping_list = [
            (biVR, 1, 'VR', runs),
            (biVR, 2, 'VR', runs),
        ]
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code="D1",
            interval=[0, 1.0],
            paradigm="p300"
        )

class CustomDataset2(GoShoppingDataset):
    def __init__(self):
        bi2014 = bi2014a()
        shopping_list = [
            (bi2014, 4, None, None),
            (bi2014, 7, None, None),
        ]
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code="D2",
            interval=[0, 1.0],
            paradigm="p300"
        )

class CustomDataset3(GoShoppingDataset):
    def __init__(self):
        shopping_list = [CustomDataset1(), CustomDataset2()]
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code="D3",
            interval=[0, 1.0],
            paradigm="p300"
        )

paradigm = P300()
datasets = [CustomDataset3()]

evaluation = WithinSessionEvaluation(
    paradigm=paradigm, datasets=datasets, overwrite=False, suffix="newdataset"
)
pipelines = {}
pipelines["MDM"] = make_pipeline(ERPCovariances(estimator="lwf"), MDM(metric="riemann"))
scores = evaluation.process(pipelines)

print(scores)