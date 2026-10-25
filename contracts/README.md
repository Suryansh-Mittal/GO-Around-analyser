# JSON data contract (v0.1)

The backend and offline pipeline write these files; the static frontend only reads them.

| File | Written by | Read by | Schema |
|---|---|---|---|
| `live.json` | live poller, every ~20 s | Screen 1: live map | [`schemas/live.schema.json`](schemas/live.schema.json) |
| `flights/{icao24}_{unix}.json` | poller (live) / pipeline (replays) | Screens 2–3: profile, replay | [`schemas/flight.schema.json`](schemas/flight.schema.json) |
| `metrics.json` | offline evaluation | Screen 4: model report | [`schemas/metrics.schema.json`](schemas/metrics.schema.json) |

## Conventions

- Units: feet (altitude/height), knots (speed), ft/min (vertical rate), nautical miles (distance), metres (lateral deviation), degrees true (heading).
- Times: ISO 8601 UTC (`Z`). `points[].t` is seconds since `start_utc`.
- `icao24` is lowercase hex; airports are 4-letter ICAO.
- Unknown values are `null`, never `0`.
- `headwind_kt` is negative for a tailwind. `glide_dev_ft` is positive above the 3° path. `lateral_dev_m` is positive right of the centreline.
- `risk_band`: `low` / `medium` / `high` (thresholds set from the calibrated model).
- Bump `schema_version` on any breaking change.

## Samples

`samples/` holds hand-made files with `"sample": true`, for frontend development only. They are synthetic and contain **no real results**; `metrics.json` is left empty until real runs exist.

`pytest` validates every sample against its schema.
