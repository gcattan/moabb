from moabb.datasets.bnci import BNCI2014001
from moabb.evaluations.evaluations import CrossSubjectEvaluation
from moabb.paradigms.p300 import P300
import torch
import seaborn as sns

from braindecode import EEGClassifier
from braindecode.models import EEGNetv4
from sklearn.pipeline import Pipeline
from skorch.callbacks import EarlyStopping, EpochScoring
from skorch.dataset import ValidSplit

from moabb.pipelines.features import Resampler_Epoch
from moabb.pipelines.utils_pytorch import BraindecodeDatasetLoader, InputShapeSetterEEG
from pyriemann.estimation import XdawnCovariances
from pyriemann.classification import MDM
from sklearn.pipeline import make_pipeline

from matplotlib import pyplot as plt

# Set up GPU if it is there
cuda = torch.cuda.is_available()
device = "cuda" if cuda else "cpu"

# Hyperparameter
LEARNING_RATE = 0.0001
WEIGHT_DECAY = 0
BATCH_SIZE = 64
SEED = 42
VERBOSE = 1
EPOCH = 10
PATIENCE = 3

# Create the dataset
create_dataset = BraindecodeDatasetLoader()

# Set random Model
model = EEGNetv4(in_chans=1, n_classes=2, input_window_samples=100)

# Define a Skorch classifier
clf = EEGClassifier(
    module=model,
    criterion=torch.nn.CrossEntropyLoss,
    optimizer=torch.optim.Adam,
    optimizer__lr=LEARNING_RATE,
    batch_size=BATCH_SIZE,
    max_epochs=EPOCH,
    train_split=ValidSplit(0.2, random_state=SEED),
    device=device,
    callbacks=[
        EarlyStopping(monitor="valid_loss", patience=PATIENCE),
        EpochScoring(
            scoring="accuracy", on_train=True, name="train_acc", lower_is_better=False
        ),
        EpochScoring(
            scoring="accuracy", on_train=False, name="valid_acc", lower_is_better=False
        ),
        InputShapeSetterEEG(
            params_list=["in_chans", "input_window_samples", "n_classes"],
        ),
    ],
    verbose=VERBOSE,  # Not printing the results for each epoch
)

# Create the pipelines
paradigm = P300()

datasets = [BNCI2014001()]
##############################################################################
# Create Pipelines
# ----------------
#
# Pipelines must be a dict of sklearn pipeline transformer.

pipelines = {}

pipelines["EEGConformer"] = Pipeline(
    [
        ("resample", Resampler_Epoch(128)),
        ("braindecode_dataset", create_dataset),
        ("EEGConformer", clf),
    ]
)

pipelines["MDM"] = make_pipeline(
    # applies XDawn and calculates the covariance matrix, output it matrices
    XdawnCovariances(),
    MDM()
)


##############################################################################
# Run evaluation
# ----------------
#
# Compare the pipeline using a within session evaluation.

evaluation = CrossSubjectEvaluation(
    paradigm=paradigm,
    datasets=datasets,
    overwrite=True,
)

results = evaluation.process(pipelines)

print("Averaging the session performance:")
print(results.groupby("pipeline").mean("score")[["score", "time"]])


# ##############################################################################
# # Plot Results
# # ----------------
# #
# # Here we plot the results to compare two pipelines

fig, ax = plt.subplots(facecolor="white", figsize=[8, 4])
title = "TODO"
sns.stripplot(
    data=results,
    y="score",
    x="pipeline",
    ax=ax,
    jitter=True,
    alpha=0.5,
    zorder=1,
    palette="Set1",
)
sns.pointplot(data=results, y="score", x="pipeline", ax=ax, palette="Set1").set(
    title=title
)

ax.set_ylabel("ROC AUC")
ax.set_ylim(0.3, 1)

plt.show()


