# Product Linkage and Yeast Classification

A coursework notebook comparing handwritten product-linkage heuristics and classical yeast classification/feature-engineering experiments.

Chen Jiang’s University of Melbourne computing coursework.

University: University of Melbourne  

## Implementation

The provided VAT helper retains its attribution; Chen implemented the linkage heuristics and classification experiments.

Attribute-level similarity scoring, best-match selection, price-bucket candidate generation, missing-data summaries, mean centering/standardization, KNN and entropy-tree comparisons, interaction features, cluster-label features and mutual-information selection.

## Technical approach

The original linkage score and price-bucket concept remain intact. Pair-level evaluation now retains every ground-truth pair, including multiple valid links for one Amazon product, and computes reduction against the full cross-product candidate universe.

A small notebook helper fits medians, centering means, KMeans features and feature selection on training rows only. The original classifiers, interaction formulas, cluster count and fixed split remain recognizable; full-data summaries and elbow plots are descriptive.

## Run

Use Python 3.12: `python3 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.txt`. Open the original notebook from this directory, or run `.venv/bin/python -B verify_notebook.py` for schema validation, a fresh kernel, HTML/notebook artifacts in `.build/`, and regression tests.

## Checks and results

- Python 3.12 isolated environment: all 12 code cells executed successfully from a clean kernel.
- Four regression methods passed: held-out features/labels cannot alter training features, finite/repeated features, numeric price validation, and many-to-many blocking completeness/denominator.
- Repeated clean-kernel runs produced identical stdout metrics; the elbow figure was visually inspected.

## 2026 maintenance

- Repaired modern pandas numeric-price handling and DictVectorizer record orientation; removed unused web-session construction.
- Corrected best-match evaluation and many-to-many blocking counts.
- Moved all learned preprocessing and feature selection inside the training boundary; handled zero-denominator interaction features.
- Pinned tested dependencies and random settings, saved verified notebook outputs, and added a portable clean-kernel verifier plus leakage regressions.

These changes are 2026 AI-assisted maintenance of the original student implementation.

## Usage notes

- The reused test split compares many representations; it is not a final independent benchmark after model/feature tuning.
- Full-data preprocessing summaries and the elbow chart are descriptive and do not justify unbiased predictive claims.
- Price blocking is a heuristic: observed pair completeness is about 0.948 and comparison reduction about 0.237 on the bundled full linkage data.
- Dependencies are pinned at tested direct/numerical versions; other transitive packages may still resolve differently.
