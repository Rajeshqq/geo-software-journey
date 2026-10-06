from models import Lake, load_lakes_json


def under_rejuvenation(lakes: list[Lake]) -> list[Lake]:
    result = []
    for lake in lakes:
        if lake.status == "Under Rejuvenation":
            result.append(lake)
    return result


def poor_quality(lakes: list[Lake]) -> list[Lake]:
    result = []
    for lake in lakes:
        if lake.water_quality == "Poor":
            result.append(lake)
    return result


if __name__ == "__main__":
    lakes = load_lakes_json()

    rejuv = under_rejuvenation(lakes)
    print("Lakes under rejuvenation:", len(rejuv))
    for lake in rejuv:
        print("  -", lake.name)

    poor = poor_quality(rejuv)
    print()
    print("Of those, poor water quality:", len(poor))
    for lake in poor:
        print("  -", lake.name)
