# Ostertag_SS2022_EEGSemesterProject

The goal of this project is to analyze and document an EEG dataset using MNE-Python. The project was for the lecture `Signal processing and Analysis of human brain potentials (EEG)` by [Benedikt Ehinger](https://github.com/behinger) in the summer term 2022.

Magnus Ostertag, 3178706

## overview

Here, I analyzed the data from a visual oddball experiment with a prolonged effect at 300ms. The analysis consists of three consecutive steps:

1. preprocessing: filtering, re-referencing, independent component analysis (ICA) in `cleaning.ipynb`
2. data cleaning: time, channel, and subjects in `cleaning.ipynb`
3. event-related peak (ERP) analysis: subjectwise extraction of the study-relevant ERP peaks and their statistical testing in `event_related_potentials.ipynb`

From four possible further analysis steps, the following two were chosen:

- mass univariate: research questions based on a multiple regression of the main experimental contrast, controlling for reaction time in `mass_univeriate.ipynb`
  - TODO
- time-frequency: research questions based on a calculation of an induced time-frequency analysis of the main experimental contrast in `time_frequency.ipynb`
  - TODO

The results are saved to `Results/`. Specifically, there is a folder for the ICA-results with `ICA/` and a file for the ERP-results with `erp_date.csv`.

I used a global configuration file with `configuration.py`.
As other helper functions, I am using code from [Marijn van Vliet ](https://github.com/wmvanvliet) with `fnames` (for managing lists of filenames) and from [Benedikt Ehinger](https://github.com/behinger) with `eeg_utils` (was used mainly for the exercises) and `eeg_semesterproject` (to load precomputed cleaning data). I am thankful to them.

## running the code

1. download the [p3 dataset](https://figshare.com/ndownloader/files/25672073?private_link=5dcdc5388d4b3f37296d) and extract it to `Data/`. Also download the [subject demographics](?) and put it into `Data/`
2. create and use a virtual python environment (`python3 -m venv venv` and `source venv/bin/activate`) and install the requirements with `pip3 install -r requirements.txt`
3. start jupyter notebook with `jupyter notebook` and run selected notebooks, or use `VS code` with the given `settings.json`

## literature

- Kappenman, Farrens, Zhang, Stewart and Luck (2021): [ERP CORE: An open resource for human event-related potential research](https://doi.org/10.1016/j.neuroimage.2020.117465)
- for a more technical and in detail documentation see also the wiki accompanying the published data and the P3 Analysis Procedures by the same authors
- van Vliet (2020): [Seven quick tips for analysis scripts in neuroimaging](https://doi.org/10.1371/journal.pcbi.1007358)
- Widmann, Schröger and Maess (2015): [Digital ﬁlter design for electrophysiological data – a practical approach](https://doi.org/10.1016/j.jneumeth.2014.08.002)
- de Cheveigne and Nelken (2019): [Filters: When, Why, and How (Not) to Use Them](https://doi.org/10.1016/j.neuron.2019.02.039)
- [mne documentation](https://mne.tools/stable/index.html) and especially the [tutorials](https://mne.tools/stable/auto_tutorials/index.html)
- [practicing ICA labeling](https://labeling.ucsd.edu/tutorial) from the UC San Diego
