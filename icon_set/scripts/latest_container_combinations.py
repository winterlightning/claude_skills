"""Resolve and compose current published container pairs without modifying the catalog."""
import json
import re
from pathlib import Path
from urllib.parse import urlencode


def read_json(path):
    return json.loads(path.read_text())


class LatestContainerPairs:
    def __init__(self, root, data_root):
        self.root = Path(root).resolve()
        self.catalog = read_json(self.root / "gallery/combinations.json")
        gallery = read_json(self.root / "gallery/icons.json")
        metadata = {r["key"]: r for r in gallery["icons"]}
        self.records = {}
        for family, folder in (("container", "container64"), ("symbol", "symbol32")):
            for record in read_json(self.root / folder / "manifest.json")["icons"]:
                uid = record["icon_id"]
                key = family + "/" + uid
                merged = dict(metadata.get(key, {}), **record)
                merged.update(key=key, family=family, asset_path=self.root / folder / (uid + ".svg"))
                # Gallery owns the current explicit revision relationship and creation date.
                for field in ("variant_of", "variant_root", "created_at"):
                    if field in metadata.get(key, {}):
                        merged[field] = metadata[key][field]
                self.records[key] = merged
        self.areas = read_json(Path(data_root) / "container-content-areas.json")["areas"]
        self.prefs = read_json(Path(data_root) / "container-placement-preferences.json")
        self.art_cache = {}
        self.children = {}
        for key, r in {**metadata, **self.records}.items():
            parent = r.get("variant_of")
            if parent:
                self.children.setdefault(r["family"] + "/" + parent, []).append(key)

    def latest(self, choices, family, sizes):
        candidates = set()
        pending = [g.get("key", family + "/" + g["icon_id"]) for g in choices]
        while pending:
            key = pending.pop()
            if key in candidates or not key.startswith(family + "/"):
                continue
            candidates.add(key)
            pending.extend(self.children.get(key, []))
        eligible = []
        for key in candidates:
            r = self.records.get(key)
            if not r or r.get("validation", {}).get("status") != "valid":
                continue
            if family == "symbol" and sizes == "32":
                if (r.get("sizing_mode") or r.get("profile") != "SYMBOL32"
                        or r.get("canvas_size") != 32
                        or r.get("canvas_width", 32) != 32 or r.get("canvas_height", 32) != 32):
                    continue
            eligible.append(r)
        # A published descendant supersedes its ancestor, regardless of equal timestamps.
        parents = {family + "/" + r["variant_of"] for r in eligible if r.get("variant_of")}
        leaves = [r for r in eligible if r["key"] not in parents]
        def rank(r):
            revisions = re.findall(r"(?:^|-)v(\d+)(?:-|$)", r["icon_id"])
            return (r.get("created_at") or "", int(revisions[-1]) if revisions else 1, r["icon_id"])
        return max(leaves, key=rank) if leaves else None

    def artwork(self, record):
        from .audit_native_container_pairs import load_art
        key = record["key"]
        if key not in self.art_cache:
            path = record["asset_path"].resolve()
            if not path.is_relative_to(self.root):
                raise ValueError("Asset outside published catalog")
            self.art_cache[key] = load_art(path)
        return self.art_cache[key]

    def compose(self, pair, sizes):
        from .container_placement import render
        from .container_vector_geometry import VectorInk, vector_zone, check_pair
        refs = self.catalog["references"]
        main = self.latest(pair.get("main_generated", refs[pair["main_id"]].get("generated", [])), "container", sizes)
        sub = self.latest(pair.get("sub_generated", refs[pair["sub_id"]].get("generated", [])), "symbol", sizes)
        result = dict(pair_id=pair["id"], concept=pair["concept"],
                      main_key=main["key"] if main else None, symbol_key=sub["key"] if sub else None,
                      fully_validated=False)
        if not main or not sub:
            return dict(result, status="missing", reason="No eligible published " + ("container" if not main else "symbol"))
        try:
            host, child = self.artwork(main), self.artwork(sub)
            if host.canvas != (64, 64):
                raise ValueError("Container canvas must be 64×64")
            area = self.areas.get(main["icon_id"], {})
            fresh = area.get("source_sha256") == host.sha256
            ink = VectorInk.from_art(host)
            info, inner, outer = vector_zone(ink, area if fresh else {})
            center = (self.prefs.get("container_centers", {}).get(main["icon_id"])
                      or (area.get("center") if fresh else None) or info.get("center_units") or [32, 32])
            center = self.prefs.get("optical_overrides", {}).get(main["icon_id"], {}).get(sub["icon_id"], center)
            width, height = child.canvas
            dx, dy = center[0] - width/2, center[1] - height/2
            svg = render(host, child, (1, dx, dy))
            metrics = check_pair(ink, VectorInk.from_art(child, (1, dx, dy)), inner, outer)
            return dict(result, status=metrics["status"], fit=metrics,
                        review_required=True, native_symbol_size=[width, height],
                        center=center, scale=1, container_sha256=host.sha256, symbol_sha256=child.sha256,
                        interior=info, svg=svg,
                        svg_url="/api/combinations/container/svg?" + urlencode(dict(id=pair["id"], sizes=sizes)))
        except (OSError, ValueError, KeyError) as error:
            return dict(result, status="blocked", reason=str(error))

    def response(self, query):
        one = lambda key, default="": query.get(key, [default])[0]
        sizes = one("sizes", "32")
        if sizes != "32":
            raise ValueError("Only standard 32×32 symbols are supported; sizes must be 32")
        try:
            limit, offset = int(one("limit", "10")), int(one("offset", "0"))
        except ValueError:
            raise ValueError("limit and offset must be integers") from None
        if not 1 <= limit <= 500 or offset < 0:
            raise ValueError("limit must be 1–500 and offset must be nonnegative")
        rows = sorted((r for r in self.catalog["rows"] if r["kind"] == "container"
                       and (not one("id") or r["id"] == one("id"))
                       and one("q").casefold() in (r["concept"] + " " + r["id"]).casefold()), key=lambda r: r["id"])
        return dict(total=len(rows), limit=limit, offset=offset,
                    next_offset=offset+limit if offset+limit < len(rows) else None,
                    sizes=sizes, selection="Published valid descendants; newest creation date among eligible revision leaves, then numeric revision and ID. Saved manual artwork is not included.",
                    instruction="Native-size composition previews; fit pass is not visual approval. Missing and blocked pairs remain in the results.",
                    pairs=[self.compose(r, sizes) for r in rows[offset:offset+limit]])
