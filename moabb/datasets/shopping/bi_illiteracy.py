from ..utils import blocks_reps
from ..braininvaders import bi2014a, VirtualReality
from .go_shopping import GoShoppingDataset


class bi2014a_il(GoShoppingDataset):
    def __init__(self):
        bi2014 = bi2014a()
        shopping_list = [
            (bi2014, 4, None, None),
            (bi2014, 7, None, None),
            (bi2014, 33, None, None),
            (bi2014, 34, None, None),
            (bi2014, 36, None, None),
            (bi2014, 38, None, None),
            (bi2014, 42, None, None),
            (bi2014, 45, None, None),
            (bi2014, 46, None, None),
            (bi2014, 47, None, None),
            (bi2014, 48, None, None),
            (bi2014, 50, None, None),
            (bi2014, 51, None, None),
            (bi2014, 52, None, None),
            (bi2014, 53, None, None),
            (bi2014, 55, None, None),
            (bi2014, 61, None, None)
        ]
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
            (biVR, 4, None, None),
            (biVR, 10, None, None),
            (biVR, 13, "VR", None),
            (biVR, 15, "VR", None),
        }
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code=f"{biVR.code}+IL",
            interval=[0, 1.0],
            paradigm="p300"
        )
