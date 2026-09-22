"""Read-only queue of container requirements lacking a published standard SYMBOL32."""
import re


def generation_queue(combinations, manifest, primitives, query, statuses=None):
    one = lambda key, default="": query.get(key, [default])[0]
    if one("kind", "container") != "container" or one("family", "symbol") != "symbol":
        raise ValueError("This queue supports kind=container and family=symbol only.")
    reason_filter = one("reason")
    if reason_filter and reason_filter not in ("no_standard_32px_symbol", "no_linked_drawing"):
        raise ValueError("reason must be no_standard_32px_symbol or no_linked_drawing.")
    statuses = statuses or {}
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
        group = groups.setdefault(uid, {"choices": {}, "exports": {}, "uses": {}})
        for g in row.get("sub_generated", refs[uid].get("generated", [])):
            group["choices"][g["icon_id"]] = g
        for export in row.get("sub_exports", []):
            group["exports"].setdefault(export["icon"], export)
        group["uses"][row["id"]] = dict(combination_id=row["id"], concept=row["concept"],
                                        main_id=row["main_id"], main_icon_id=row.get("main_icon_id"))
    items = []
    covered = marked_text = 0
    for uid, group in sorted(groups.items()):
        if native.intersection(group["choices"]):
            covered += 1
            continue
        if statuses.get(uid, {}).get("reason") == "text_number":
            marked_text += 1
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
        choices = [dict(g, python_source=group["exports"].get(g["icon_id"], {}).get("python_source"))
                   for g in sorted(group["choices"].values(), key=lambda g: g["icon_id"])]
        reason = "no_standard_32px_symbol" if choices else "no_linked_drawing"
        if reason_filter and reason != reason_filter:
            continue
        if choices:
            candidates = "\n".join(
                f"- `{c['icon_id']}` ({c.get('model_validation') or 'unknown'}) — "
                f"`{c['python_source'] or 'path unknown; find by icon_id in icon_set/model/icons/symbol/'}`"
                for c in choices)
            brief = (f"# {name} — fix the existing symbol icon\n\n"
                     f"Source identity: {uid}\n"
                     f"Reference: {reference_url or 'No reference SVG; inspect the source identity.'}\n\n"
                     "An independent SYMBOL32 model already exists for this requirement but isn't a standard "
                     "32×32 symbol yet (failing validation, under review, or a non-standard size/sizing_mode). "
                     "Do not author a new file. Inspect the candidate(s) below, find the failing check with the "
                     "project's validation tooling, and edit the geometry in place until it passes as a plain "
                     "32×32 SYMBOL32 icon. If it is genuinely text/number content that cannot fit the profile, "
                     "report that instead of forcing a fix.\n\n"
                     f"Existing candidate(s):\n{candidates}")
        else:
            brief = (f"# {name}\n\nSource identity: {uid}\n"
                     f"Reference: {reference_url or 'No reference SVG; inspect the source identity and typeface catalog.'}\n"
                     "Author with $icon-symbol on SYMBOL32: 32×32 canvas, 4px stroke. "
                     "Inspect the reference first; no existing drawing is linked to this requirement. "
                     "Route text to the shared typeface guidance; report when it cannot fit the requested profile. "
                     "Validate and visually review before publication.")
        items.append(dict(uuid=uid, source_id=uid, concept=name, category=category, batch=batch,
                          family="symbol", profile="SYMBOL32", skill="icon-symbol", canvas_size=32,
                          proposed_icon_id=proposed, reference_path=reference_path,
                          reference_url=reference_url, brief_source="template", brief=brief,
                          reason=reason, existing_candidates=choices,
                          combination_count=len(group["uses"]), combinations=list(group["uses"].values())))
    return dict(total=len(items), offset=offset, limit=limit,
                next_offset=offset + limit if offset + limit < len(items) else None,
                kind="container", family="symbol", profile="SYMBOL32", reason=reason_filter or None,
                requirements_total=len(groups), covered_requirements=covered,
                marked_text_requirements=marked_text,
                missing_requirements=len(groups)-covered-marked_text,
                instruction="One row per source requirement, not per variant or combination. Recheck before authoring; equivalent references may share a symbol. "
                            "Requirements already marked text/number are excluded from missing_requirements and from the briefs.",
                briefs=items[offset:offset+limit])
