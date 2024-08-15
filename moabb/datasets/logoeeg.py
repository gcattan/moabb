#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pandas as pd
import mne
import numpy as np
from scipy.io import loadmat

from moabb.datasets import download as dl
from moabb.datasets.base import BaseDataset


# ALPHAWAVES_URL = "https://zenodo.org/record/2348892/files/"

EVENTS_LOGOEEG = dict(autism=1, nonautism=2)

class LogoEEG(BaseDataset):
    """Alphawaves dataset

    """

    def __init__(self):
        subject_list = [1, 2, 3]
        super().__init__(
            subjects=subject_list,
            sessions_per_subject=1,
            events=EVENTS_LOGOEEG,
            code="LogoEEG",
            interval=[0, 10],
            paradigm="rstate",
            doi="https://doi.org/10.5281/zenodo.2348892",
        )

    def _get_single_subject_data(self, subject):
        """return data for a single subject"""

        filepath = self.data_path(subject)[0]

        event_label = filepath.split('_')[-1].split('.csv')[0]
        event = EVENTS_LOGOEEG[event_label]
        print(event)

        data = pd.read_csv(filepath)

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
        

        S = data[raw_signals].astype(float)
        S.dropna(inplace=True)
        stim = S['RAW_TP9'] * 0
        stim.iloc[1] = event
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
            'PPG_Red',
            "stim",
        ]
        chtypes = ["eeg"] * 4 + ['misc'] * 6 + ['bio'] * 3 + ["stim"]
        X = np.concatenate([S, stim[:, None]], axis=1).T

        info = mne.create_info(
            ch_names=chnames, sfreq=250, ch_types=chtypes, verbose=False
        )
        raw = mne.io.RawArray(data=X, info=info, verbose=False)

        return {f"0{event_label}": {"0": raw}}

    def data_path(
        self, subject, path=None, force_update=False, update_path=None, verbose=None
    ):

        if subject not in self.subject_list:
            raise (ValueError("Invalid subject number"))

        # url = "{:s}subject_{:02d}.mat".format(ALPHAWAVES_URL, subject)
        # file_path = dl.data_path(url, "LOGOEEG")
        file_path = f'C:/Users/ZZ03MC820/Downloads/mindmonitor_s{subject}_autism.csv'
        if(not os.path.isfile(file_path)):
            file_path = f'C:/Users/ZZ03MC820/Downloads/mindmonitor_s{subject}_nonautism.csv'

        return [file_path]
