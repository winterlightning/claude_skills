import json, collections
from concurrent.futures import ProcessPoolExecutor
def check(icon_id):
    from icon_set.model.icons.registry import create
    return icon_id, create(icon_id).validate_icon().status
if __name__ == "__main__":
    prom = json.load(open("staging/json-solo/promoted.json"))["promoted"]
    want = {m["icon_id"]: m["status"] for m in prom}
    with ProcessPoolExecutor(10) as pool:
        got = dict(pool.map(check, list(want), chunksize=25))
    diff = [(k, want[k], got[k]) for k in want if want[k] != got[k]]
    print("live-engine statuses:", collections.Counter(got.values()), "mismatches vs staging:", len(diff), diff[:5])
