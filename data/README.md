# Data

Nothing in this folder except this file is committed. Download the sources below yourself.

| Source | What it gives | Licence / terms | Where to put it |
|---|---|---|---|
| Monstein et al. (2022), *Large landing trajectory data set for go-around analysis*, Zenodo, DOI [10.5281/zenodo.7148117](https://doi.org/10.5281/zenodo.7148117) (use the **augmented** file) | ~9M labelled 2019 landings, ~33k go-arounds, METAR | CC BY 4.0 | `data/raw/zenodo/` |
| OpenSky *Weekly 24 Hours of State Vector Data* (Mondays, 2017–2022) — [scientific datasets](https://opensky-network.org/data/scientific) | 10 s state vectors for 2019 Mondays (v2 trajectories) | OpenSky terms of use (non-commercial research) | `data/raw/opensky_states/` |
| OpenSky historical DB via Trino (optional, if access is granted) | Full-resolution state vectors | OpenSky terms of use | `data/raw/trino/` |
| OpenSky live REST API | Live state vectors for the demo | OpenSky terms of use | not stored |

Suggested layout:

```
data/
  raw/        # untouched downloads
  interim/    # filtered/cleaned (Parquet)
  processed/  # model-ready feature tables
```

Raw OpenSky data must not be redistributed. Credit both OpenSky and Monstein et al. wherever results are shown.
