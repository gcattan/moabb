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
        return len(self.shopping_list.keys())

    def __init__(self, shopping_list: dict, events: dict, code: str, interval: list, paradigm: str, sessions_per_subject: int):
        self.shopping_list = shopping_list
        super().__init__(
            subjects=list(range(1, self.count + 1)),
            sessions_per_subject=sessions_per_subject,
            events=events,
            code=code,
            interval=interval,
            paradigm=paradigm,
        )

    def _get_single_subject_data(self, shopped_subject):
        """return data for a single subject"""
        dataset, subject, sessions, runs = self.shopping_list[shopped_subject]
        subject_data = dataset._get_single_subject_data(subject)
        if sessions is None:
            return subject_data
        elif isinstance(sessions, list):
            sessions_data = {f"{session}": subject_data[session] for session in sessions}
        else:
            sessions_data = {f"{sessions}": subject_data[sessions]}

        if runs is None:
            return sessions_data
        elif isinstance(runs, list):
            for session in sessions_data.keys():
                sessions_data[session] = {f"{run}": sessions_data[session][run] for run in runs}
            return sessions_data
        else:
            for session in sessions_data.keys():
                sessions_data[session] = {f"{runs}": sessions_data[session][runs]}
            return sessions_data
        
        

    def data_path(
        self, shopped_subject, path=None, force_update=False, update_path=None, verbose=None
    ):
        dataset, subject, _, _ = self.shopping_list[shopped_subject]
        path = dataset.data_path(subject)
        print("--------------------", path)
        return path
