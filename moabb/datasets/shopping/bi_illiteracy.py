from ..braininvaders import bi2014a, VirtualReality
from .go_shopping import GoShoppingDataset

def block_rep(blocks: list, reps: list):
    return [f'block_{b}-repetition_{r}' for b in blocks for r in reps]

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
            7: (bi2014, 41, None, None),
            8: (bi2014, 42, None, None),
            9: (bi2014, 45, None, None),
            10: (bi2014, 46, None, None),
            11: (bi2014, 47, None, None),
            12: (bi2014, 48, None, None),
            13: (bi2014, 50, None, None),
            14: (bi2014, 51, None, None),
            15: (bi2014, 52, None, None),
            16: (bi2014, 53, None, None),
            17: (bi2014, 55, None, None),
            18: (bi2014, 61, None, None)
        }
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code=f"{bi2014a.code}+IL",
            interval=[0, 1.0],
            paradigm="p300"
        )

class VirtualRealiyt_il(GoShoppingDataset):
    def __init__(self):
        biVR = VirtualReality(virtual_reality=True, screen_display=True)
        runs =  block_rep([1,3], [1,2,3,4,5])
        shopping_list = {
            1: (biVR, 1, 'VR', runs),
            2: (biVR, 2, ['VR','PC'], runs),
            3: (biVR, 4, 'VR', runs),
            4: (biVR, 5, 'PC', runs),
            5: (biVR, 6, ['VR','PC'], runs),
            6: (biVR, 8, 'PC', runs),
            7: (biVR, 9, ['VR','PC'], runs),
            8: (biVR, 10, ['VR','PC'], runs),
            9: (biVR, 11, 'VR', runs),
            10: (biVR, 12, 'PC', runs),
            11: (biVR, 13, 'VR', runs),
            12: (biVR, 14, 'VR', runs),
            13: (biVR, 15, ['VR','PC'], runs),
            14: (biVR, 18, 'VR', runs),
            15: (biVR, 20, 'PC', runs),
        }
        GoShoppingDataset.__init__(
            self,
            shopping_list=shopping_list,
            events=dict(Target=2, NonTarget=1),
            code=f"{biVR.code}+IL",
            interval=[0, 1.0],
            paradigm="p300"
        )
