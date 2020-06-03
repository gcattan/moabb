"""
A paradigm defines how the raw data will be converted to trials ready to be
processed by a decoding algorithm. This is a function of the paradigm used,
i.e. in motor imagery one can have two-class, multi-class, or continuous
paradigms; similarly, different preprocessing is necessary for ERP vs ERD
paradigms.
"""
# flake8: noqa
try:
    from ...moabb.paradigms.p300 import *
    from ...moabb.paradigms.motor_imagery import *
    from ...moabb.paradigms.ssvep import *
except:
    from moabb.paradigms.p300 import *
    from moabb.paradigms.motor_imagery import *
    from moabb.paradigms.ssvep import *
