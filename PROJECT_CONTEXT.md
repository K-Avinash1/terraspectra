# PROJECT_CONTEXT.md — TerraSpectra (living checkpoint)

Last updated: 10 Nov 2026 (Day 1, kickoff) by Claude. Status key: Not started / In progress / Implemented-not-tested / Tested-verified / Blocked / Deferred / Completed.

## 1. Identity
- Project: TerraSpectra: Hyperspectral Crop Disease Forecasting (Infotact Solutions, ref ITS/DSML/1452, Team Group No 2, Batch-22 DS&ML)
- Team: Avinash (leader; data, ML, backend, merges) and Zahra Fathima (frontend, React/TS, GIS UI)
- Start 10 Nov 2026 | Internal target: working product 29 Nov 2026 | Official deadline 10 Dec 2026

## 2. Official requirements checklist (source: Vol. II project doc, SOP v1.1, assignment letter)
Mandatory (from official docs):
- [ ] Hyperspectral cube ingestion with Rasterio/GDAL (HDF5/GeoTIFF) — Not started
- [ ] PCA on 200+ bands — Not started
- [ ] 3D-CNN in PyTorch (healthy vs stressed pixels) — Not started
- [ ] ViT / self-attention integration (hybrid) — Not started
- [ ] FastAPI inference API with tiling + stitching of large rasters — Not started
- [ ] React app + Deck.gl map with heatmap overlay aligned to real GPS — Not started
- [ ] Analytics panel: acreage at risk + anomalies — Not started
- [ ] Timeline slider for historical progression — Not started (only if data has real temporal observations)
- [ ] Mid-review audit: memory handling of 3D tensor batches; Deck.gl alignment — Not started
- [ ] Deliverables per letter: source code, documentation, project report, PPT, model evaluation, final demo — Not started
Recommended (our additions): Grad-CAM/attention explainability, baseline models (RF/SVM) for comparison, spatially-split evaluation, upload validation, report export, automated tests.
Optional: weather/sensor cards (no data source -> do NOT fake).

## 3. Open scope questions (need Avinash's decision)
1. Official doc says "mock data" for early weeks; master prompt requires real data for final results -> resolution: mock only for UI/API/pipeline tests, labelled; final = real.
2. Official doc says "ESA Sentinel missions" as hyperspectral source; Sentinel-2 is multispectral -> not to be called hyperspectral.
3. "Predict 3 weeks before symptoms" -> only claim forecasting if dataset has temporal labels; otherwise call it early detection / classification.
4. Mapbox (doc) vs MapLibre GL (no token, free) as Deck.gl basemap -> recommendation: MapLibre. Awaiting approval.
5. Exact Mid Review date (window 20–27 of month per SOP) -> confirm from dashboard/mentor.
6. Whether Work Distribution Document must be re-submitted for this project.

## 4–5. Dataset
- Approved dataset: NONE yet (selection pending Avinash's approval, planned Day 2–3).
- Candidates under review: see kickoff comparison (4TU potato late blight, Danespo potato late blight, USDA tomato bacterial spot, UAV wheat yellow rust, others). Download links/licences must be verified before approval.

## 6. Repository and branches
- Repo name (proposed): terraspectra (GitHub, owner K-Avinash1) — Not created yet
- Branches: main, avinash-dev, zahra-dev ONLY (no integration branch)
- Infotact dashboard: Avinash GitHub @K-Avinash1 already connected; repo+branch not yet linked; Zahra must connect her own GitHub and zahra-dev

## 7. Folder structure (planned)
terraspectra/
  backend/ (FastAPI app, tests)
  ml/ (preprocessing, models, training, evaluation)
  frontend/ (React + TS + Deck.gl)
  data/ (git-ignored; README with download instructions)
  docs/ (architecture, dataset, model docs, schedule)
  PROJECT_CONTEXT.md, README.md, .gitignore, .env.example

## 8–16. Progress
- Milestones completed: kickoff plan delivered (Day 1)
- Files created: none in repo yet
- Models trained: none | API endpoints: none | Frontend features: none | Integration: none | Tests: none
- Known bugs: none
- Decisions: two-branch workflow; VS Code primary; Colab GPU only if needed; real data for final; synthetic labelled

## 17–23. Next actions
- Current day: Day 1 (10 Nov), schedule status: on plan
- Avinash next: create repo, branches, first commit, connect avinash-dev to Infotact dashboard (Commit tracking toggle ON, Save connection)
- Zahra next: accept invite, clone, switch to zahra-dev, first commit, connect her account + zahra-dev on her dashboard
- Shared next: verify both Commits tabs show commits
- Infotact compliance: project saved on dashboard (done); GitHub repo (pending); commits 0/10; write-ups 0/2 (Week 1, Week 2)
- Exact next action: Avinash creates the GitHub repository `terraspectra`

## 24. Commands and environment
- Planned: Python 3.11 venv, PyTorch CPU build, Node 20 LTS, VS Code. Not yet installed/verified.

## 25. Risks
- Mid-review window may open as early as 20 Nov: only 11 calendar days of commits exist from 10–20 Nov and 10 commit days are required in the 14 days before review -> commit meaningfully almost every day from Day 1.
- Final review needs a commit on EVERY day of the 20 days before it (SOP 3.2) -> daily commits through 10 Dec.
- No verified open dataset yet combines georeferencing + disease labels + temporal progression.
- Large hyperspectral files (tens of GB) vs laptop RAM/disk.
- Zahra is a beginner in Git/React/APIs.

## Schedule (10–29 Nov, then stabilization)
| Day | Date | Avinash | Zahra | Shared / checks |
|---|---|---|---|---|
| 1 | Tue 10 Nov | Create repo, branches, skeleton commit, connect avinash-dev | Accept invite, clone, zahra-dev, first commit, connect zahra-dev | Both Commits tabs show activity |
| 2 | Wed 11 Nov | Python/Node env, folder structure, architecture doc, dataset comparison for approval | Vite + React + TS scaffold, run dev server, git basics | Dataset decision meeting |
| 3 | Thu 12 Nov | Approve + start dataset download, inspection notebook | App shell: sidebar, header, design tokens from reference UIs | Update PROJECT_CONTEXT |
| 4 | Fri 13 Nov | Load cubes (h5py/rasterio), metadata + CRS + wavelength check | MapLibre + Deck.gl base map component | Map renders real coordinates |
| 5 | Sat 14 Nov | EDA: band stats, mean spectra per class, PCA | Upload page UI (drop zone, validation status table) | Review EDA together |
| 6 | Sun 15 Nov | Preprocessing pipeline, patch extraction, leakage-safe split | API client, TS types from contract | Commit every day from here (final-review rule) |
| 7 | Mon 16 Nov | FastAPI skeleton (/health, /validate), 3D-CNN code | Results layout using labelled sample JSON | API contract frozen v1 |
| 8 | Tue 17 Nov | 3D-CNN baseline training (CPU smoke, Colab only if needed) | Heatmap layer rendering | Week-1 write-up due on dashboard |
| 9 | Wed 18 Nov | Evaluation: confusion matrix, per-class metrics, RF/SVM baseline | Layer controls + spectral signature chart (Plotly) | Memory audit of 3D batches |
| 10 | Thu 19 Nov | /upload + real validation; export checkpoint | Upload wired to API | Mid-review evidence pack |
| 11 | Fri 20 Nov | Baseline inference to map; merge to main | Overlay alignment check | MID REVIEW READY (window 20–27); viva round 1; Week-2 write-up |
| 12 | Sat 21 Nov | ViT / hybrid implementation | Analytics panel (class summary, confidence) | |
| 13 | Sun 22 Nov | Hybrid training | Acreage-at-risk panel (pixel area from raster transform) | |
| 14 | Mon 23 Nov | Model comparison (3D-CNN vs ViT vs hybrid vs RF) | Comparison page | Metrics table into docs |
| 15 | Tue 24 Nov | Explainability (Grad-CAM/attention), /predict | Explanation overlay UI | |
| 16 | Wed 25 Nov | Raster tiling + stitching + tests | Loading/empty/error states | |
| 17 | Thu 26 Nov | Tiling integrated, performance | Report export UI; timeline only if temporal data | |
| 18 | Fri 27 Nov | End-to-end test with real data | Bug fixes | Mid-review window closes today |
| 19 | Sat 28 Nov | Backend tests, docs, README | Frontend tests, responsive polish | |
| 20 | Sun 29 Nov | Feature freeze, full E2E, merge to main, tag v1.0 | Demo rehearsal | Internal target met |
| 21–26 | 30 Nov–5 Dec | Report, PPT, bug fixes, viva prep | User docs, demo video, social media video | Final window opens 5 Dec |
| 27–31 | 6–10 Dec | Final review, submissions | Final review | Official deadline 10 Dec |