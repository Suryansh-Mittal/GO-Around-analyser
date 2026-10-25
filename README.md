# Go-Around Analyser

**Predicting aborted landings (go-arounds) from open ADS-B flight data.**

A go-around is an aborted landing: the crew stops the approach, climbs away and tries again. This project estimates how likely a go-around is for an arriving flight, first from the conditions it will land in (v1), then from how the approach is actually being flown (v2).

> Status: **in development.** No results yet. Metrics will be added here only from real runs.

## Versions

| Version | Question | Inputs |
|---|---|---|
| **v1: pre-arrival risk** | Given the conditions, how likely is a go-around? | Airport, runway, aircraft type, operator, time, METAR weather, recent traffic |
| **v2: in-flight risk** | Given how this approach is being flown, how likely is a go-around? | v1 + trajectory features (glide-path deviation, speed, sink rate, alignment) |

## Planned demo

- **Live airport map**: inbound aircraft coloured by risk, current conditions
- **Approach profile**: vertical profile vs the 3° glide path, speed and sink rate, stabilisation gates
- **Replay mode**: real 2019 go-arounds
- **Model report**: PR curve, calibration, capture at top-k%, SHAP, held-out airports, v1 vs v2

## Repository layout

```
contracts/   JSON data contract between backend and frontend (schemas + samples)
src/goaround/  data pipeline, features, modelling
backend/     live poller (OpenSky REST, server-side only)
web/         static frontend (GitHub Pages)
notebooks/   exploration
tests/       tests (incl. contract validation)
data/        local data only, never committed (see data/README.md)
```

## Setup

```bash
mamba env create -f environment.yml   # mamba ships with Miniforge; uses far less memory than conda
conda activate goaround
cp .env.example .env   # add your OpenSky API client ID and secret
pytest
```

See [`data/README.md`](data/README.md) for downloading the datasets.

## Data and credits

- Go-around labels: R. Monstein, B. Figuet, T. Krauth, M. Waltert, M. Dettling, *Large landing trajectory data set for go-around analysis*, Zenodo, 2022, DOI [10.5281/zenodo.7148117](https://doi.org/10.5281/zenodo.7148117) (CC BY 4.0). Paper: [10.3390/engproc2022028002](https://doi.org/10.3390/engproc2022028002).
- Flight data: [The OpenSky Network](https://opensky-network.org). Used under OpenSky's terms of use for non-commercial research. Raw data is not redistributed in this repository.
- Tooling: [traffic](https://github.com/xoolive/traffic) (X. Olive) and [pyopensky](https://github.com/open-aviation/pyopensky).

## Licence

Code: [MIT](LICENSE). Data remains under its original licences and terms.
