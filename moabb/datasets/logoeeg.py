#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pandas as pd
import mne
import numpy as np
from scipy.io import loadmat

from moabb.datasets import download as dl
from moabb.datasets.base import BaseDataset


ALPHAWAVES_URL = "https://zenodo.org/record/2348892/files/"


class LogoEEG(BaseDataset):
    """Alphawaves dataset

    """

    def __init__(self):
        subject_list = list(range(1, 6 + 1)) + list(range(8, 20 + 1))
        super().__init__(
            subjects=subject_list,
            sessions_per_subject=1,
            events=dict(start=1),
            code="LogoEEG",
            interval=[0, 10],
            paradigm="rstate",
            doi="https://doi.org/10.5281/zenodo.2348892",
        )

    def _get_single_subject_data(self, subject):
        """return data for a single subject"""

        dirpath = self.data_path(subject)[0]
        filepath = os.listdir(dirpath)[0]

        data = pd.read_csv(os.path.join(dirpath, filepath))
        raw_signals = [
            'RAW_TP9',
            'RAW_AF7',
            'RAW_AF8',
            'RAW_TP10',
            'Gyro_X',
            'Gyro_Y',
            'Gyro_Z',
            'Accelerometer_X',
            'Accelerometer_Y',
            'Accelerometer_Z',
            'PPG_Ambient',
            'PPG_IR',
            'PPG_Red'
        ]
        

        S = data[raw_signals]
        stim = data['TimeStamp'] * 0
        stim[0] = 1
        chnames = [
            "TP9",
            "AF7",
            "AF8",
            "TP10",
            'Gyro_X',
            'Gyro_Y',
            'Gyro_Z',
            'Acc_X',
            'Acc_Y',
            'Acc_Z',
            'PPG_Ambient',
            'PPG_IR',
            'PPG_Red'
            "stim",
        ]
        chtypes = ["eeg"] * 4 + ['misc'] * 6 + ['bio'] * 3 + ["stim"]
        X = np.concatenate([S, stim[:, None]], axis=1).T

        info = mne.create_info(
            ch_names=chnames, sfreq=512, ch_types=chtypes, verbose=False
        )
        raw = mne.io.RawArray(data=X, info=info, verbose=False)

        return {"0": {"0": raw}}

    def data_path(
        self, subject, path=None, force_update=False, update_path=None, verbose=None
    ):

        if subject not in self.subject_list:
            raise (ValueError("Invalid subject number"))

        # url = "{:s}subject_{:02d}.mat".format(ALPHAWAVES_URL, subject)
        # file_path = dl.data_path(url, "LOGOEEG")
        file_path = 'C:\Users\ZZ03MC820\Downloads\mindmonitor.csv'

        return [file_path]
