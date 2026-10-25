"""Validate the sample JSON files against the data-contract schemas."""

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1] / "contracts"
SCHEMAS = ROOT / "schemas"
SAMPLES = ROOT / "samples"

CASES = [
    ("live.schema.json", SAMPLES / "live.json"),
    ("metrics.schema.json", SAMPLES / "metrics.json"),
    *[("flight.schema.json", p) for p in sorted((SAMPLES / "flights").glob("*.json"))],
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("schema_name", sorted(p.name for p in SCHEMAS.glob("*.json")))
def test_schema_is_valid(schema_name):
    Draft202012Validator.check_schema(load(SCHEMAS / schema_name))


@pytest.mark.parametrize("schema_name,sample", CASES, ids=lambda x: getattr(x, "name", x))
def test_sample_matches_schema(schema_name, sample):
    validator = Draft202012Validator(load(SCHEMAS / schema_name))
    errors = sorted(validator.iter_errors(load(sample)), key=lambda e: list(e.path))
    assert not errors, "\n".join(f"{list(e.path)}: {e.message}" for e in errors)


def test_flight_filename_matches_content():
    for p in (SAMPLES / "flights").glob("*.json"):
        icao24, _ = p.stem.split("_")
        assert load(p)["icao24"] == icao24, p.name
