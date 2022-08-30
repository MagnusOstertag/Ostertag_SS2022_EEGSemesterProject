# where all the global variables are defined

from fnames import FileNames
from pathlib import Path

# save directories
path_git_root = Path.cwd()
path_results = Path(path_git_root / 'Results')
path_ica_results = Path(path_results / 'ICA')
path_annotation_results = Path(path_results / 'Annotations')

# data directories
fname = FileNames()
fname.add('bids_root', "Data/p3")

# participants analyzed
participants = ('036', '024', '032')  # ('001','025','040')

# monitor delay [s]
monitor_delay = 0.026

# filter params [Hz]
high_pass_cutoff_freq = 0.1
low_pass_cutoff_freq = 45

# downsampling [Hz]
resampling_freq = 256

# epochs [s]
tmin = -0.2
tmax = 0.8

# channel pick
pick = 'Pz'

# permutation t-test
n_permutations = 5000
seed_ttest = 42
significant_tmin = 0.255
significant_tmax = 0.66
recommended_tmin = 0.3
recommended_tmax = 0.6

# ICA
seed_ICA = 42
