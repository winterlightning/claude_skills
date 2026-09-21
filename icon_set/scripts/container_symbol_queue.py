"""Read-only queue of container requirements lacking a published standard SYMBOL32."""
import re


def generation_queue(combinations, manifest, primitives, query):
    one = lambda key, default="": query.get(key, [default])[0]
    if one("kind", "container") != "container" or one("family", "symbol") != "symbol":
        raise ValueError("This queue supports kind=container and family=symbol only.")
    try:
        limit, offset = int(one("limit", "50")), int(one("offset", "0"))
    except ValueError:
        raise ValueError("limit and offset must be integers.") from None
    if not 1 <= limit <= 500 or offset < 0:
        raise ValueError("limit must be 1–500 and offset must be nonnegative.")
    native = {r["icon_id"] for r in manifest["icons"]
              if r.get("family") == "symbol" and r.get("profile") == "SYMBOL32"
              and not r.get("sizing_mode") and r.get("canvas_size") == 32
              and r.get("canvas_width", 32) == 32 and r.get("canvas_height", 32) == 32
              and r.get("validation", {}).get("status") == "valid"}
    refs = combinations["references"]
    sources = {r["uuid"]: r for r in primitives["rows"]}
    groups = {}
    for row in combinations["rows"]:
        if row["kind"] != "container":
            continue
        uid = row["sub_id"]
        group = groups.setdefault(uid, {"choices": {}, "uses": {}})
        for g in row.get("sub_generated", refs[uid].get("generated", [])):
            group["choices"][g["icon_id"]] = g
        group["uses"][row["id"]] = dict(combination_id=row["id"], concept=row["concept"],
                                        main_id=row["main_id"], main_icon_id=row.get("main_icon_id"))
    items = []
    covered = 0
    for uid, group in sorted(groups.items()):
        if native.intersection(group["choices"]):
            covered += 1
            continue
        ref, source = refs[uid], sources.get(uid, {})
        name = ref.get("concept") or uid
        category, batch = source.get("category", ""), source.get("batch")
        if one("category") and one("category") != category:
            continue
        if one("batch") and one("batch") != batch:
            continue
        if one("q").casefold() not in (name + " " + uid).casefold():
            continue
        reference = ref.get("reference_url")
        reference_url = "/gallery/" + reference if reference else None
        path = source.get("path")
        reference_path = primitives.get("root_label", "pictographic-primitives").rstrip("/") + "/" + path if path else None
        proposed = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        if not proposed or not proposed[0].isalpha():
            proposed = "symbol-" + proposed
        choices = sorted(group["choices"].values(), key=lambda g: g["icon_id"])
        reason = "no_standard_32px_symbol" if choices else "no_linked_drawing"
        brief = (f"# {name}\n\nSource identity: {uid}\n"
                 f"Reference: {reference_url or 'No reference SVG; inspect the source identity and typeface catalog.'}\n"
                 "Author with $icon-symbol on SYMBOL32: 32×32 canvas, 4px stroke. "
                 "Inspect the reference and existing candidates first; reuse and link an appropriate existing "
                 "standard symbol if available. Otherwise create or repair an independent Python symbol model. "
                 "Preserve existing variants and source identity. Do not use a resize or variable-width export "
                 "as standard SYMBOL32 coverage. Route text to the shared typeface guidance; report when it "
                 "cannot fit the requested profile. Validate and visually review before publication. "
                 "This is a symbol requirement, not an instruction to create a duplicate file.")
        items.append(dict(uuid=uid, source_id=uid, concept=name, category=category, batch=batch,
                          family="symbol", profile="SYMBOL32", skill="icon-symbol", canvas_size=32,
                          proposed_icon_id=proposed, reference_path=reference_path,
                          reference_url=reference_url, brief_source="template", brief=brief,
                          reason=reason, existing_candidates=choices,
                          combination_count=len(group["uses"]), combinations=list(group["uses"].values())))
    return dict(total=len(items), offset=offset, limit=limit,
                next_offset=offset + limit if offset + limit < len(items) else None,
                kind="container", family="symbol", profile="SYMBOL32",
                requirements_total=len(groups), covered_requirements=covered,
                missing_requirements=len(groups)-covered,
                instruction="One row per source requirement, not per variant or combination. Recheck before authoring; equivalent references may share a symbol.",
                briefs=items[offset:offset+limit])
