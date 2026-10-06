import csv
import json
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CSV_PATH = DATA_DIR / "bangalore_lakes.csv"
JSON_PATH = DATA_DIR / "bangalore_lakes.json"


@dataclass
class LakeDataError(Exception):
    lake_name: str
    field: str
    value: object
    reason: str

    def __str__(self):
        return f"{self.lake_name}: '{self.field}' = {self.value!r} -> {self.reason}"


def to_area(value, lake_name: str) -> float:
    try:
        area = float(value)
    except (TypeError, ValueError):
        raise LakeDataError(lake_name, "area_acres", value, "not a number")

    if area <= 0:
        raise LakeDataError(lake_name, "area_acres", value, "must be greater than 0")
    return area


@dataclass
class Lake:
    id: int
    name: str
    zone: str
    area_acres: float
    status: str
    water_quality: str

    @classmethod
    def from_csv_row(cls, row: dict) -> "Lake":
        return cls(
            id=int(row["id"]),
            name=row["name"],
            zone=row["zone"],
            area_acres=to_area(row["area_acres"], row["name"]),
            status=row["status"],
            water_quality=row["water_quality"],
        )

    @classmethod
    def from_json(cls, d: dict) -> "Lake":
        return cls(
            id=d["id"],
            name=d["name"],
            zone=d["zone"],
            area_acres=to_area(d["area_acres"], d["name"]),
            status=d["status"],
            water_quality=d["water_quality"],
        )


def load_lakes_csv(path: Path = CSV_PATH) -> list[Lake]:
    with open(path, "r", encoding="utf-8") as file:
        lakes=[]
        for r in csv.DictReader(file):
            lake=Lake.from_csv_row(r)
            lakes.append(lake)
        return lakes
        


def load_lakes_json(path: Path = JSON_PATH) -> list[Lake]:
    with open(path, "r", encoding="utf-8") as file:
        return [Lake.from_json(d) for d in json.load(file)["lakes"]]
