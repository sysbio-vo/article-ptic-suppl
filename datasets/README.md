# Datasets used for testing

```
├── DILI_CAMDA_challenge
│   ├── DILI_incorrect_labels.tsv
│   ├── DILI_initial_set.csv
│   ├── DILI_validation_set_1.tsv
│   └── DILI_validation_set_2.tsv
├── IMDB_Dataset.csv
├── parsed_livertox.csv
├── pubmed_negatives.csv
└── README.md
```

## [DILI CAMDA Challenge](http://camda2021.bioinf.jku.at/contest_dataset#literature_ai_for_drug_induced_liver_injury)

* `DILI_incorrect_labels.tsv` - articles with incorrect PubMed IDs verified by DILI experts at the FDA (not known on at the beginning of the challenge).
* `DILI_initial_set.csv` - first dataset, provided by CAMDA organisers (orifinally consited of negative and positive examples separately, later combined by us for convenience).
* `DILI_validation_set_1.tsv` - second dataset, provided by CAMDA, labels are unknown.
* `DILI_validation_set_1.tsv` - third, provided by CAMDA, labels are unknown.

## Other datasets

* `IMDB_Dataset.csv` - classical [IMDB dataset from Kaggle](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).
* `parsed_livertox.csv` - parse [LiverTox](https://www.ncbi.nlm.nih.gov/books/NBK547852/) database, unbiased and easily accessed information on the diagnosis, cause, frequency, clinical patterns and management of liver injury attributable to prescription and nonprescription medications and selected herbal and dietary supplements.
* `pubmed_negatives.csv` - a selection of pubmed articles with non-DILI topics.
