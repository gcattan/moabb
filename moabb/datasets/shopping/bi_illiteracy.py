from ..braininvaders import bi2014a, VirtualReality, bi2014b, bi2015a, bi2015b
from .go_shopping import GoShoppingDataset

class base_il(GoShoppingDataset):
    def __init__(self, shopping_list, dataset):
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code=f"{dataset.code}+IL",
            interval=[0, 1.0],
            paradigm="p300"
        )

class bi2014a_il(base_il):
    def __init__(self):
        dataset = bi2014a()
        shopping_list = [
            (dataset, 4, None, None),
            (dataset, 7, None, None),
            (dataset, 33, None, None),
            (dataset, 34, None, None),
            (dataset, 36, None, None),
            (dataset, 38, None, None),
            (dataset, 42, None, None),
            (dataset, 45, None, None),
            (dataset, 46, None, None),
            (dataset, 47, None, None),
            (dataset, 48, None, None),
            (dataset, 50, None, None),
            (dataset, 51, None, None),
            (dataset, 52, None, None),
            (dataset, 53, None, None),
            (dataset, 55, None, None),
            (dataset, 61, None, None)
        ]
        base_il.__init__(
            self,
            shopping_list=shopping_list,
            dataset=dataset
        )

class bi2014b_il(base_il):
    def __init__(self):
        dataset = bi2014b()
        shopping_list = [
            # TODO
        ]
#         ['pair 03, subject 1 (cola)',
#  'pair 03, subject 2 (cola)',
#  'pair 04, subject 1 (cola)',
#  'pair 04, subject 2 (cola)',
#  'pair 09, subject 1 (cola)',
#  'pair 09, subject 2 (cola)',
#  'pair 10, subject 1 (solo)',
#  'pair 10, subject 1 (cola)',
#  'pair 10, subject 2 (solo)',
#  'pair 10, subject 2 (cola)',
#  'pair 13, subject 2 (cola)',
#  'pair 14, subject 1 (cola)',
#  'pair 14, subject 2 (cola)',
#  'pair 18, subject 1 (cola)']
        base_il.__init__(
            self,
            shopping_list=shopping_list,
            dataset=dataset
        )

class bi2015a_il(base_il):
    def __init__(self):
        dataset = bi2015a()
        shopping_list = [
            (dataset, 1, ['session_1', 'session_2', 'session_3'], None),
            (dataset, 39, ['session_2', 'session_3'], None)
        ]
        base_il.__init__(
            self,
            shopping_list=shopping_list,
            dataset=dataset
        )

class bi2015b_il(base_il):
    def __init__(self):
        dataset = bi2015b()
        shopping_list = [
            # TODO
        ]
#         ['pair 01, session 1, subject 2',
#  'pair 01, session 2, subject 2',
#  'pair 01, session 3, subject 2',
#  'pair 01, session 4, subject 2',
#  'pair 02, session 1, subject 2',
#  'pair 02, session 2, subject 2',
#  'pair 02, session 3, subject 2',
#  'pair 02, session 4, subject 2',
#  'pair 03, session 1, subject 2',
#  'pair 03, session 2, subject 2',
#  'pair 03, session 3, subject 2',
#  'pair 03, session 4, subject 2',
#  'pair 04, session 2, subject 2',
#  'pair 04, session 3, subject 2',
#  'pair 04, session 4, subject 2',
#  'pair 05, session 1, subject 2',
#  'pair 05, session 2, subject 2',
#  'pair 06, session 1, subject 2',
#  'pair 06, session 2, subject 2',
#  'pair 06, session 3, subject 2',
#  'pair 07, session 1, subject 2',
#  'pair 07, session 2, subject 2',
#  'pair 07, session 3, subject 2',
#  'pair 07, session 4, subject 2',
#  'pair 08, session 1, subject 2',
#  'pair 08, session 2, subject 2',
#  'pair 08, session 3, subject 2',
#  'pair 08, session 4, subject 2',
#  'pair 09, session 1, subject 2',
#  'pair 09, session 2, subject 2',
#  'pair 09, session 3, subject 2',
#  'pair 09, session 4, subject 2',
#  'pair 10, session 1, subject 2',
#  'pair 10, session 2, subject 2',
#  'pair 10, session 3, subject 2',
#  'pair 10, session 4, subject 2',
#  'pair 11, session 2, subject 2',
#  'pair 11, session 3, subject 2',
#  'pair 11, session 4, subject 2',
#  'pair 12, session 1, subject 2',
#  'pair 12, session 2, subject 2',
#  'pair 12, session 3, subject 2',
#  'pair 12, session 4, subject 2',
#  'pair 13, session 1, subject 2',
#  'pair 13, session 2, subject 2',
#  'pair 13, session 3, subject 2',
#  'pair 13, session 4, subject 2',
#  'pair 14, session 1, subject 2',
#  'pair 15, session 1, subject 2',
#  'pair 15, session 2, subject 2',
#  'pair 15, session 3, subject 2',
#  'pair 15, session 4, subject 2',
#  'pair 16, session 1, subject 2',
#  'pair 16, session 2, subject 2',
#  'pair 16, session 3, subject 2',
#  'pair 16, session 4, subject 2',
#  'pair 17, session 1, subject 2',
#  'pair 17, session 2, subject 2',
#  'pair 17, session 3, subject 2',
#  'pair 17, session 4, subject 2',
#  'pair 18, session 1, subject 1',
#  'pair 18, session 1, subject 2',
#  'pair 18, session 2, subject 1',
#  'pair 18, session 2, subject 2',
#  'pair 18, session 3, subject 1',
#  'pair 18, session 3, subject 2',
#  'pair 18, session 4, subject 1',
#  'pair 18, session 4, subject 2',
#  'pair 19, session 1, subject 2',
#  'pair 19, session 2, subject 2',
#  'pair 19, session 3, subject 2',
#  'pair 19, session 4, subject 2']
        base_il.__init__(
            self,
            shopping_list=shopping_list,
            dataset=dataset
        )

class VirtualReality_il(base_il):
    def __init__(self):
        dataset = VirtualReality(virtual_reality=True, screen_display=True)
        shopping_list = {
            (dataset, 4, None, None),
            (dataset, 10, None, None),
            (dataset, 13, "VR", None),
            (dataset, 15, "VR", None),
        }
        base_il.__init__(
            self,
            shopping_list=shopping_list,
            dataset=dataset
        )
