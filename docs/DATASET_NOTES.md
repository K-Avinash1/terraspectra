# Dataset notes (TerraSpectra)

Status: candidates under evaluation. No final dataset approved yet.

| Dataset | Source | Licence | Format | Georeferenced | Fit |
|---|---|---|---|---|---|
| Javidan tomato HSI | Zenodo 10.5281/zenodo.15800414 | CC BY 4.0 | .mat, 400-950 nm | No (leaf-level) | Model science (PCA, 3D-CNN, ViT) |
| S2-PDD potato (UAV) | 4TU 10.4124/ff427e5c-d454-4d03-a090-d504329e3cb3 | To verify | PNG + NPZ tiles (3/10/20 bands) | To verify | Field-level detection of symptomatic plants |

## Rejected
- 4TU latent blight potato (88.5 GB zip): too large.
- USDA tomato bacterial spot (15.4 GB, non-geospatial): too large for this project.
- Danespo potato (204 bands): no public download link found.

## Honest limits
- No verified dataset supports forecasting disease weeks ahead; the feature is called early disease detection.
- Synthetic or sample data is allowed only for UI, API and pipeline tests, and must be labelled.

## Javidan tomato: technical findings (12 Nov)
- Licence: CC BY 4.0 (Zenodo record page).
- Numbered .mat files are 3-D cubes, shape (140, 280, 550), float64; *_features.mat are EfficientNet features (processed, not used).
- No wavelength vector in the files. Assumed even spacing over 400-950 nm (paper range); unverified.
- Leaves were excised and imaged once on days 1, 3, 5, 7 (not tracked over time); plant IDs not provided.
- Visible symptoms: day 5 (A. alternata, B. cinerea), day 7 (A. solani, F. oxysporum); controls never.
- Leakage rules: split by whole cube only; fit PCA/scalers on training cubes only; leave-one-cube-out evaluation.

## S2-PDD
- Licence: CC BY-NC 4.0 (confirm with mentor/HR for internship use).
- Released: RGB tiles plus 3/10/20-band hyperspectral tiles; no full cube; no geo file listed.

## Cube scale check (12 Nov)
- File naming: 2 cubes per class per day (Day_one, Day_three, Day_five, Day_seven), about 40 cubes in total.
- Healthy_1: values 0-0.79 (reflectance-like). Botrytis_cinerea_1: values 0-4095 (raw-counts-like). Full scan results are in docs/cube_stats.csv.
- Risk: if scale differs by class, a model can learn the scale instead of the disease. Do not train until this is resolved.
- Author email sent about calibration, wavelengths and plant IDs (S2-PDD authors contacted earlier).
- S2-PDD README: no coordinates or CRS documented; 20-band centres 420-970 nm; labels are YOLO text files.
