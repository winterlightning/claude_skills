#!/usr/bin/env python3
"""Load the canonical normal, sub-icon, and container icon profiles.

``icon_profiles.json`` is the machine-readable source of truth.  This module
only resolves inheritance and exposes small, shared validation helpers so the
emitters and QA tools cannot silently grow their own canvas or keyshape rules.
``design`` and ``ship`` keys are compatibility aliases for the same native-size
canvas and stroke. No production stage downsamples an icon.
"""

from __future__ import annotations

from copy import deepcopy
import json
import math
from pathlib import Path
import re
from typing import Any, Mapping


PROFILE_SOURCE = Path(__file__).with_name("icon_profiles.json")
PROFILE_NAME_PATTERN = r"[a-z0-9]+(?:-[a-z0-9]+)*"
VALIDATION_FIELDS = (
    "gridStep", "majorGridStep", "geometryTolerance", "keyshapeTolerance",
    "minimumDistinctCenterlineDistance", "minimumEnclosedRadius", "minimumSolidFillDepth",
)
_PROFILE_FIELDS = {"label", "extends", "canvas", "strokeWidth", "keyshapes", "containerSlot", "validation"}
_TOKEN_FIELDS = {"name", "orientation", "shape", "width", "height", "diameter"}
_SLOT_FIELDS = {"x", "y", "w", "h", "acceptedProfile", "minimumClearSquare"}


def _object(value: Any, context: str, allowed: set[str], required: set[str] = frozenset()) -> Mapping:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    unknown = set(value) - allowed
    missing = required - set(value)
    if unknown:
        raise ValueError(f"{context} has unknown fields: {', '.join(sorted(map(str, unknown)))}")
    if missing:
        raise ValueError(f"{context} is missing {', '.join(sorted(missing))}")
    return value


def _number(value: Any, context: str, *, zero: bool = False, integer: bool = False) -> None:
    try:
        valid = not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value) and (value >= 0 if zero else value > 0) and (not integer or int(value) == value)
    except (OverflowError, ValueError):
        valid = False
    if not valid:
        qualifier = "nonnegative" if zero else "positive"
        raise ValueError(f"{context} must be a finite {qualifier} {'integer' if integer else 'number'}")


def _name(value: Any, context: str) -> None:
    if not isinstance(value, str) or not re.fullmatch(PROFILE_NAME_PATTERN, value) or value in {"constructor", "prototype"}:
        raise ValueError(f"{context} must be a safe kebab-case name")


def _validation(value: Any, context: str, *, complete: bool = False) -> None:
    _object(value, context, set(VALIDATION_FIELDS), set(VALIDATION_FIELDS) if complete else set())
    for field, number in value.items():
        _number(number, f"{context}.{field}", zero=field == "minimumSolidFillDepth")


def _validated_catalog(source: Any) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    """Validate raw configuration and resolve a detached inheritance catalog."""
    fields = {"schemaVersion", "defaultIconType", "validationDefaults", "profiles"}
    _object(source, "profile source", fields, fields)
    if type(source["schemaVersion"]) is not int or source["schemaVersion"] != 2:
        raise ValueError("profile source schemaVersion must be 2")
    _validation(source["validationDefaults"], "validationDefaults", complete=True)
    raw_profiles = source["profiles"]
    if not isinstance(raw_profiles, Mapping) or not raw_profiles:
        raise ValueError("profiles must be a nonempty object")
    _name(source["defaultIconType"], "defaultIconType")
    if source["defaultIconType"] not in raw_profiles:
        raise ValueError("defaultIconType must reference an existing profile")
    for name, raw in raw_profiles.items():
        _name(name, "profile name")
        context = f"profiles.{name}"
        _object(raw, context, _PROFILE_FIELDS, {"label"})
        if not isinstance(raw["label"], str) or not raw["label"].strip():
            raise ValueError(f"{context}.label must be a nonempty string")
        if "extends" in raw:
            _name(raw["extends"], f"{context}.extends")
            if raw["extends"] not in raw_profiles:
                raise ValueError(f"{context}.extends must reference an existing profile")
        if "canvas" in raw:
            _number(raw["canvas"], f"{context}.canvas", integer=True)
        if "strokeWidth" in raw:
            _number(raw["strokeWidth"], f"{context}.strokeWidth")
        if "validation" in raw:
            _validation(raw["validation"], f"{context}.validation")
        if "keyshapes" in raw:
            tokens = raw["keyshapes"]
            if not isinstance(tokens, list) or not tokens:
                raise ValueError(f"{context}.keyshapes must be a nonempty array")
            names = set()
            for index, token in enumerate(tokens):
                location = f"{context}.keyshapes[{index}]"
                _object(token, location, _TOKEN_FIELDS, _TOKEN_FIELDS - {"diameter"})
                _name(token["name"], f"{location}.name")
                if token["name"] in names:
                    raise ValueError(f"{context} has duplicate keyshape names")
                names.add(token["name"])
                for field in ("width", "height"):
                    _number(token[field], f"{location}.{field}")
                width, height = token["width"], token["height"]
                orientation, shape = token["orientation"], token["shape"]
                if orientation not in ("circle", "square", "portrait", "landscape"):
                    raise ValueError(f"{location}.orientation must be circle, square, portrait, or landscape")
                if shape not in ("circle", "rect"):
                    raise ValueError(f"{location}.shape must be circle or rect")
                if shape == "circle":
                    _number(token.get("diameter"), f"{location}.diameter")
                    if orientation != "circle" or width != height or width != token["diameter"]:
                        raise ValueError(f"{location} circle dimensions must equal its diameter and use circle orientation")
                elif ("diameter" in token or orientation == "circle" or
                      orientation == "square" and width != height or
                      orientation == "portrait" and height <= width or
                      orientation == "landscape" and width <= height):
                    raise ValueError(f"{location} rectangle dimensions must match its orientation and omit diameter")
        if raw.get("containerSlot") is not None:
            slot = _object(raw["containerSlot"], f"{context}.containerSlot", _SLOT_FIELDS, _SLOT_FIELDS)
            for field in ("x", "y", "w", "h", "minimumClearSquare"):
                _number(slot[field], f"{context}.containerSlot.{field}", zero=field in {"x", "y"})
            _name(slot["acceptedProfile"], f"{context}.containerSlot.acceptedProfile")
            if slot["acceptedProfile"] not in raw_profiles:
                raise ValueError(f"{context}.containerSlot.acceptedProfile must reference an existing profile")
    catalog = {}

    def materialize(name: str) -> dict[str, Any]:
        raw = deepcopy(dict(raw_profiles[name]))
        parent = raw.pop("extends", None)
        profile = deepcopy(catalog[parent]) if parent else {"validation": deepcopy(dict(source["validationDefaults"]))}
        overrides = raw.pop("validation", {})
        profile.update(raw)
        profile["validation"].update(overrides)
        if profile.get("containerSlot") is None:
            profile.pop("containerSlot", None)
        for field in ("canvas", "strokeWidth", "keyshapes"):
            if field not in profile:
                raise ValueError(f"profile {name!r} is missing {field}")
        canvas, stroke = int(profile["canvas"]), profile["strokeWidth"]
        profile["canvas"] = canvas
        if stroke > canvas:
            raise ValueError(f"profile {name!r} strokeWidth must fit its canvas")
        for token in profile["keyshapes"]:
            if token["width"] > canvas or token["height"] > canvas:
                raise ValueError(f"profile {name!r} keyshape {token['name']!r} must fit its canvas")
            if min(token["width"], token["height"]) < stroke:
                raise ValueError(f"profile {name!r} keyshape {token['name']!r} cannot be smaller than its strokeWidth")
        validation = profile["validation"]
        ratio = validation["majorGridStep"] / validation["gridStep"]
        if not math.isfinite(ratio) or ratio < 1 or not math.isclose(ratio, round(ratio), rel_tol=0, abs_tol=1e-9):
            raise ValueError(f"profile {name!r} majorGridStep must be an integer multiple of gridStep")
        profile.update(iconType=name, center={"x": canvas / 2, "y": canvas / 2},
                       designCanvas=canvas, shipCanvas=canvas, designStroke=stroke, shipStroke=stroke,
                       minimumDistinctCenterlineDistance=validation["minimumDistinctCenterlineDistance"])
        catalog[name] = profile
        return profile

    for name in raw_profiles:
        chain, seen, current = [], set(), name
        while current not in catalog:
            if current in seen:
                raise ValueError(f"cyclic icon profile inheritance: {' -> '.join([*chain, current])}")
            seen.add(current)
            chain.append(current)
            parent = raw_profiles[current].get("extends")
            if parent is None:
                break
            current = parent
        for dependency in reversed(chain):
            materialize(dependency)
    # Slot validation is a separate pass: accepted profiles may occur later.
    for name, profile in catalog.items():
        if "containerSlot" not in profile:
            continue
        slot = profile["containerSlot"]
        accepted = catalog[slot["acceptedProfile"]]
        canvas, accepted_canvas = profile["canvas"], accepted["canvas"]
        if slot["acceptedProfile"] == name:
            raise ValueError(f"profile {name!r} containerSlot cannot accept itself")
        if (slot["w"], slot["h"]) != (accepted_canvas, accepted_canvas):
            raise ValueError(f"profile {name!r} container slot must equal the accepted profile's canvas")
        if not accepted_canvas <= slot["minimumClearSquare"] <= min(slot["w"], slot["h"]):
            raise ValueError(f"profile {name!r} minimumClearSquare must fit the accepted canvas inside its slot")
        if (slot["x"] != (canvas - slot["w"]) / 2 or slot["y"] != (canvas - slot["h"]) / 2):
            raise ValueError(f"profile {name!r} container slot must be centered within its canvas")
    for name in catalog:
        chain, current = [], name
        while "containerSlot" in catalog[current]:
            if current in chain:
                raise ValueError(f"cyclic container acceptedProfile references: {' -> '.join([*chain, current])}")
            chain.append(current)
            current = catalog[current]["containerSlot"]["acceptedProfile"]
    return deepcopy(dict(source)), {name: catalog[name] for name in raw_profiles}


def validate_profile_source(source: Any) -> dict[str, Any]:
    """Return validated, detached raw schema-v2 source; raises ValueError."""
    return _validated_catalog(source)[0]


def resolve_profiles(source: Any) -> dict[str, dict[str, Any]]:
    """Pure resolution of a validated schema-v2 source, including derived aliases."""
    return _validated_catalog(source)[1]


_SOURCE, _PROFILES = _validated_catalog(json.loads(PROFILE_SOURCE.read_text(encoding="utf-8")))
SCHEMA_VERSION = _SOURCE["schemaVersion"]
DEFAULT_ICON_TYPE = _SOURCE["defaultIconType"]


def profile_names() -> tuple[str, ...]:
    """Return icon type names in canonical source order."""
    return tuple(_PROFILES)


def get_profile(icon_type: str | None = None) -> dict[str, Any]:
    """Return a detached, fully resolved icon profile."""
    name = DEFAULT_ICON_TYPE if icon_type is None else icon_type
    if name not in _PROFILES:
        raise ValueError(f"unknown iconType {name!r}; expected one of: {', '.join(_PROFILES)}")
    return deepcopy(_PROFILES[name])


def validation_settings(icon_type: str | None = None) -> dict[str, Any]:
    """Detached effective validator settings for a profile."""
    return get_profile(icon_type)["validation"]


def svg_native_size_issues(attributes: Mapping[str, str], icon_type: str = DEFAULT_ICON_TYPE) -> list[dict[str, str]]:
    """Reject reduced viewports or explicitly reduced intrinsic/CSS dimensions.

    Missing width/height remain readable for older SVG sources with a native
    viewBox. Canonical emitters always write both dimensions explicitly.
    Nonzero origins are permitted here for raster diagnostic viewport mapping;
    canonical structural validation still requires the exact emitted source.
    """
    profile = get_profile(icon_type)
    canvas = float(profile["designCanvas"])
    tolerance = profile["validation"]["geometryTolerance"]
    issues = []
    try:
        view = [float(value) for value in attributes.get("viewBox", "").replace(",", " ").split()]
        valid_view = len(view) == 4 and all(math.isfinite(value) for value in view) and all(abs(value - canvas) <= tolerance for value in view[2:])
    except ValueError:
        valid_view = False
    if not valid_view:
        issues.append({"code": "wrong-canvas", "detail": f"{icon_type} requires a native {canvas:g}x{canvas:g} viewBox"})
    dimensions = [(field, attributes[field]) for field in ("width", "height") if field in attributes]
    for declaration in attributes.get("style", "").split(";"):
        field, separator, value = declaration.partition(":")
        if separator and field.strip().lower() in {"width", "height", "min-width", "max-width", "min-height", "max-height"}:
            dimensions.append((f"style {field.strip()}", re.sub(r"\s*!important\s*$", "", value.strip(), flags=re.I)))
    for field, value in dimensions:
        match = re.fullmatch(r"\s*([-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?)\s*(?:px)?\s*", value)
        measured = float(match.group(1)) if match else math.nan
        if not math.isfinite(measured) or abs(measured - canvas) > tolerance:
            issues.append({"code": "wrong-render-size", "detail": f"{field} must be native {canvas:g}px, found {value!r}"})
    return issues


def document_icon_type(document: Mapping[str, Any]) -> str:
    """Read ``iconType`` with the backward-compatible normal default."""
    icon_type = document.get("iconType", DEFAULT_ICON_TYPE)
    if not isinstance(icon_type, str):
        raise ValueError("iconType must be a string")
    get_profile(icon_type)  # validate before returning it
    return icon_type


def profile_for_document(document: Mapping[str, Any]) -> dict[str, Any]:
    return get_profile(document_icon_type(document))


def validate_document_profile(
    document: Mapping[str, Any],
) -> tuple[str, dict[str, Any]]:
    """Validate editable canvas/stroke declarations against its icon profile."""
    icon_type = document_icon_type(document)
    profile = get_profile(icon_type)
    canvas = document.get("canvas", profile["designCanvas"])
    stroke = document.get("strokeWidth", profile["designStroke"])
    _number(canvas, "document.canvas", integer=True)
    _number(stroke, "document.strokeWidth")
    if canvas != profile["designCanvas"]:
        raise ValueError(
            f"{icon_type} design canvas is fixed at {profile['designCanvas']:g}"
        )
    if stroke != profile["designStroke"]:
        raise ValueError(
            f"{icon_type} design stroke is fixed at {profile['designStroke']:g}u"
        )
    if "containerSlot" in profile:
        validate_container_slot(document, profile)
    return icon_type, profile


def token_box(token: Mapping[str, Any], icon_type: str = DEFAULT_ICON_TYPE) -> tuple[float, float, float, float]:
    """Return centered design bounds ``(left, top, right, bottom)``."""
    profile = get_profile(icon_type)
    center = profile["center"]
    width = float(token["width"])
    height = float(token["height"])
    left = float(center["x"]) - width / 2.0
    top = float(center["y"]) - height / 2.0
    return left, top, left + width, top + height


def canonical_tokens(icon_type: str = DEFAULT_ICON_TYPE) -> list[dict[str, Any]]:
    """Return enriched token records, including their canonical bounds."""
    tokens = []
    for raw in get_profile(icon_type)["keyshapes"]:
        item = deepcopy(raw)
        item["bounds"] = list(token_box(item, icon_type))
        tokens.append(item)
    return tokens


def token_named(name: str, icon_type: str = DEFAULT_ICON_TYPE) -> dict[str, Any] | None:
    return next((item for item in canonical_tokens(icon_type) if item["name"] == name), None)


def validate_container_slot(
    document: Mapping[str, Any], profile: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    """Validate and enrich a container's protected sub-icon slot metadata."""
    profile = dict(profile or get_profile(document.get("iconType", "container" if "container" in profile_names() else DEFAULT_ICON_TYPE)))
    required = profile.get("containerSlot")
    if required is None:
        raise ValueError(f"profile {profile['iconType']!r} does not define a containerSlot")
    slot = document.get("containerSlot")
    if not isinstance(slot, Mapping):
        raise ValueError("container icons require containerSlot metadata")
    for field in ("x", "y", "w", "h"):
        _number(slot.get(field), f"containerSlot.{field}", zero=field in {"x", "y"})
        if slot.get(field) != required[field]:
            raise ValueError(
                f"containerSlot.{field} must be {required[field]:g}"
            )
    accepted_name = slot.get("acceptedKeyshape")
    if not isinstance(accepted_name, str) or not accepted_name:
        raise ValueError("containerSlot.acceptedKeyshape is required")
    accepted_profile = required["acceptedProfile"]
    token = token_named(accepted_name, accepted_profile)
    if token is None:
        allowed = ", ".join(
            item["name"] for item in canonical_tokens(accepted_profile)
        )
        raise ValueError(
            f"unknown containerSlot.acceptedKeyshape {accepted_name!r}; "
            f"expected one of: {allowed}"
        )
    left, top, right, bottom = token["bounds"]
    accepted_bounds = [
        float(slot["x"]) + left,
        float(slot["y"]) + top,
        float(slot["x"]) + right,
        float(slot["y"]) + bottom,
    ]
    clear_size = float(required["minimumClearSquare"])
    clear_left = float(slot["x"]) + (float(slot["w"]) - clear_size) / 2.0
    clear_top = float(slot["y"]) + (float(slot["h"]) - clear_size) / 2.0
    return {
        **dict(slot),
        "acceptedProfile": accepted_profile,
        "acceptedToken": token,
        "acceptedBounds": accepted_bounds,
        "minimumClearSquare": clear_size,
        "protectedBounds": [
            clear_left,
            clear_top,
            clear_left + clear_size,
            clear_top + clear_size,
        ],
        "protectedCenter": {
            "x": float(slot["x"]) + float(get_profile(accepted_profile)["center"]["x"]),
            "y": float(slot["y"]) + float(get_profile(accepted_profile)["center"]["y"]),
        },
    }


def source_document() -> dict[str, Any]:
    """Return a detached copy for generators that mirror the profile JSON."""
    return deepcopy(_SOURCE)
