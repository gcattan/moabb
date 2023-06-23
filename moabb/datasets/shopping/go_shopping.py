"""
Build a custom dataset using subjects from other datasets.
"""

from moabb.datasets.braininvaders import VirtualReality

from .. import download as dl
from ..base import BaseDataset


ALEX_URL = "https://zenodo.org/record/806023/files/"


class GoShoppingDataset(BaseDataset):
    """TODO
    selection:
        {
            subject1: (dataset1, subject, session, runs)
            subject2:
        }
    """

    @property
    def count(self):
        return len(self.selection.keys())

    def __init__(self, selection: dict, events: dict, code: str, interval: list, paradigm: str):
        self.selection = selection
        super().__init__(
            subjects=list(range(1, self.count + 1)),
            sessions_per_subject=1,
            events=events,
            code=code,
            interval=interval,
            paradigm=paradigm,
        )

    def _get_single_subject_data(self, shopped_subject):
        """return data for a single subject"""
        dataset, subject, session, runs = self.selection[shopped_subject]
        if session is None:
            sessions_data = dataset._get_single_subject_data(subject)
            return sessions_data
        if runs is None:
            runs_data = dataset._get_single_subject_data(subject)[session]
            return {"session_0": runs_data}
        sessions_data = dataset._get_single_subject_data(subject)[session]
        if isinstance(runs, list):
            runs_data = {f"run_{i}": sessions_data[runs[i]] for i in range(len(runs))}
            return {"session_0": runs_data}
        else:
            run_data = sessions_data[runs]
            return {"session_0": { "run_0": run_data}}
        
        

    def data_path(
        self, shopped_subject, path=None, force_update=False, update_path=None, verbose=None
    ):
        dataset, subject, _, _ = self.selection[shopped_subject]
        path = dataset.data_path(subject)
        print("--------------------", path)
        return path
