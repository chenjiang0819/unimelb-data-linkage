# AI Project Review

## Project Summary

A coursework notebook comparing handwritten product-linkage heuristics and classical yeast classification/feature-engineering experiments.

Chen Jiang’s original data-analysis coursework. The notebook retains the original weighted Hamming comparisons, price blocks, KNN/entropy-tree models, feature interactions and clustering experiments; the provided VAT helper keeps its attribution.

## Original Engineering Strengths

The original linkage work decomposes record similarity into title, description, manufacturer and price contributions. Explicit weights and a threshold expose the author’s domain assumptions and make the matching decision inspectable at attribute level.

Price-based blocking is implemented directly through buckets and candidate pairs. Comparing candidate completeness and comparison reduction connects computational cost to retained matches, rather than treating matching as an opaque library call.

The classification section tries several concrete ways to construct features: products and ratios, KMeans cluster labels, and supervised mutual-information selection. It contrasts KNN settings and an entropy decision tree, showing an experimental progression from preprocessing to representation choices.

## Technical Highlights

The original linkage score and price-bucket concept remain intact. Pair-level evaluation now retains every ground-truth pair, including multiple valid links for one Amazon product, and computes reduction against the full cross-product candidate universe.

A small notebook helper fits medians, centering means, KMeans features and feature selection on training rows only. The original classifiers, interaction formulas, cluster count and fixed split remain recognizable; full-data summaries and elbow plots are descriptive.

## 2026 Maintenance Improvements

- Repaired modern pandas numeric-price handling and DictVectorizer record orientation; removed unused web-session construction.
- Corrected best-match evaluation and many-to-many blocking counts.
- Moved all learned preprocessing and feature selection inside the training boundary; handled zero-denominator interaction features.
- Pinned tested dependencies and random settings, saved verified notebook outputs, and added a portable clean-kernel verifier plus leakage regressions.

The changes retain the project's original mechanisms and strengthen their execution
boundaries and verification contract. They do not substitute a new project concept.

## Verification

- Python 3.12 isolated environment: all 12 code cells executed successfully from a clean kernel.
- Four regression methods passed: held-out features/labels cannot alter training features, finite/repeated features, numeric price validation, and many-to-many blocking completeness/denominator.
- Repeated clean-kernel runs produced identical stdout metrics; the elbow figure was visually inspected.
- Schema validation and the project-local verifier passed. Evidence: Linkage_before_execution.json, Linkage_final_execution.json, Linkage_unit_final.log, Linkage_portable_verification.log.

Verification is limited to the commands and cases listed above; passing these checks is not a claim of universal correctness.

## Skills Demonstrated

Record linkage, explicit heuristic scoring, candidate blocking, classical ML experimentation, feature construction, evaluation design, training/test isolation and reproducible notebooks.

## Engineering Assessment

This project is useful evidence of how the author decomposes data tasks and tests alternative representations. The maintained notebook makes that experimental reasoning reproducible and gives learned transformations a defensible training boundary.

## Maintenance Transparency

The original implementation is preserved in `archive/handwritten-original` at
`32466de4d958bcee41d5f0f8788cf85f8537f3d3`. The reviewed maintained version contains a later AI-assisted engineering
maintenance pass focused on verification, robustness, testing, and documentation
while retaining the original project approach.
