from models import Lake, LakeDataError, load_lakes_csv


def summarize_by_zone(lakes: list[Lake]) -> dict[str, dict]:
    """Return {zone: {"count": int, "total": float}}."""
    summary = {}
    for lake in lakes:
        if lake.zone not in summary:
            summary[lake.zone] = {"count": 0, "total": 0.0}

        summary[lake.zone]["count"] = summary[lake.zone]["count"] + 1
        summary[lake.zone]["total"] = summary[lake.zone]["total"] + lake.area_acres
    return summary


def get_total(item):
    zone, data = item
    return data["total"]


def print_report(summary: dict[str, dict]) -> None:
    """Print zones sorted by total area (largest first), then the grand total."""
    print("Zone           Lakes   Total     Avg")

    rows = sorted(summary.items(), key=get_total, reverse=True)
    grand_total = 0.0

    for zone, data in rows:
        count = data["count"]
        total = data["total"]
        avg = total / count
        grand_total = grand_total + total

        print(f"{zone:<14}{count:>6}{total:>8.1f}{avg:>8.1f}")

    print()
    print(f"Total area of all lakes: {grand_total:.1f} acres")


if __name__ == "__main__":
    try:
        lakes = load_lakes_csv()
    except LakeDataError as e:
        print("Bad data in CSV:", e)
        raise SystemExit(1)

    summary = summarize_by_zone(lakes)
    print_report(summary)
