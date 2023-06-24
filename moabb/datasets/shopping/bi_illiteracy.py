from ..utils import blocks_reps
from ..braininvaders import bi2014a, VirtualReality
from .go_shopping import GoShoppingDataset


class bi2014a_il(GoShoppingDataset):
    def __init__(self):
        bi2014 = bi2014a()
        shopping_list = {
            1: (bi2014, 4, None, None),
            2: (bi2014, 7, None, None),
            3: (bi2014, 33, None, None),
            4: (bi2014, 34, None, None),
            5: (bi2014, 36, None, None),
            6: (bi2014, 38, None, None),
            7: (bi2014, 42, None, None),
            8: (bi2014, 45, None, None),
            9: (bi2014, 46, None, None),
            10: (bi2014, 47, None, None),
            11: (bi2014, 48, None, None),
            12: (bi2014, 50, None, None),
            13: (bi2014, 51, None, None),
            14: (bi2014, 52, None, None),
            15: (bi2014, 53, None, None),
            16: (bi2014, 55, None, None),
            17: (bi2014, 61, None, None)
        }
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code=f"{bi2014.code}+IL",
            interval=[0, 1.0],
            paradigm="p300"
        )

class VirtualReality_il(GoShoppingDataset):
    def __init__(self):
        biVR = VirtualReality(virtual_reality=True, screen_display=True)
        shopping_list = {
            1: (biVR, 4, None, None),
            2: (biVR, 10, None, None),
            3: (biVR, 13, "VR", None),
            4: (biVR, 15, "VR", None),
        }
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code=f"{biVR.code}+IL",
            interval=[0, 1.0],
            paradigm="p300"
        )
