#!/usr/bin/env python3
"""Load the canonical normal, sub-icon, and container icon profiles.

``icon_profiles.json`` is the machine-readable source of truth.  This module
only resolves inheritance and exposes small, shared validation helpers so the
emitters and QA tools cannot silently grow their own canvas or keyshape rules.
"""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any, Mapping


PROFILE_SOURCE = Path(__file__).with_name("icon_profiles.json")
_SOURCE = json.loads(PROFILE_SOURCE.read_text(encoding="utf-8"))
SCHEMA_VERSION = _SOURCE["schemaVersion"]
DEFAULT_ICON_TYPE = _SOURCE["defaultIconType"]
_RAW_PROFILES = _SOURCE["profiles"]


def _resolved(name: str, trail: tuple[str, ...] = ()) -> dict[str, Any]:
    if name not in _RAW_PROFILES:
        allowed = ", ".join(sorted(_RAW_PROFILES))
        raise ValueError(f"unknown iconType {name!r}; expected one of: {allowed}")
    if name in trail:
        raise ValueError(f"cyclic icon profile inheritance: {' -> '.join((*trail, name))}")
    raw = deepcopy(_RAW_PROFILES[name])
    parent = raw.pop("extends", None)
    profile = _resolved(parent, (*trail, name)) if parent else {}
    profile.update(raw)
    profile["iconType"] = name
    return profile


def profile_names() -> tuple[str, ...]:
    """Return icon type names in canonical source order."""
    return tuple(_RAW_PROFILES)


def get_profile(icon_type: str | None = None) -> dict[str, Any]:
    """Return a detached, fully resolved icon profile."""
    return _resolved(DEFAULT_ICON_TYPE if icon_type is None else icon_type)


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
    if canvas != profile["designCanvas"]:
        raise ValueError(
            f"{icon_type} design canvas is fixed at {profile['designCanvas']:g}"
        )
    if stroke != profile["designStroke"]:
        raise ValueError(
            f"{icon_type} design stroke is fixed at {profile['designStroke']:g}u"
        )
    if icon_type == "container":
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
    profile = dict(profile or get_profile("container"))
    required = profile["containerSlot"]
    slot = document.get("containerSlot")
    if not isinstance(slot, Mapping):
        raise ValueError("container icons require containerSlot metadata")
    for field in ("x", "y", "w", "h"):
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


# Fail fast if the source is malformed or internally inconsistent.
for _name in profile_names():
    _profile = get_profile(_name)
    for _field in (
        "designCanvas",
        "shipCanvas",
        "designStroke",
        "shipStroke",
        "minimumDistinctCenterlineDistance",
        "center",
        "keyshapes",
    ):
        if _field not in _profile:
            raise ValueError(f"profile {_name!r} is missing {_field}")
    if _profile["minimumDistinctCenterlineDistance"] <= 0:
        raise ValueError(
            f"profile {_name!r} minimumDistinctCenterlineDistance must be positive"
        )
    if _profile["designCanvas"] / _profile["shipCanvas"] != _profile["designStroke"] / _profile["shipStroke"]:
        raise ValueError(f"profile {_name!r} canvas and stroke scales disagree")
    if (
        _profile["center"]["x"] != _profile["designCanvas"] / 2
        or _profile["center"]["y"] != _profile["designCanvas"] / 2
    ):
        raise ValueError(f"profile {_name!r} center must be the design-canvas center")
    if len({item["name"] for item in _profile["keyshapes"]}) != len(_profile["keyshapes"]):
        raise ValueError(f"profile {_name!r} has duplicate keyshape names")

_container = get_profile("container")
_slot = _container["containerSlot"]
_accepted = get_profile(_slot["acceptedProfile"])
if (_slot["w"], _slot["h"]) != (
    _accepted["designCanvas"],
    _accepted["designCanvas"],
):
    raise ValueError("container slot must equal the accepted profile's design canvas")
if _slot["minimumClearSquare"] < _accepted["designCanvas"]:
    raise ValueError(
        "container minimum clear square must fit the accepted profile's design canvas"
    )
if _slot["minimumClearSquare"] > min(_slot["w"], _slot["h"]):
    raise ValueError("container minimum clear square must fit inside its slot")
if (
    _slot["x"] != (_container["designCanvas"] - _slot["w"]) / 2
    or _slot["y"] != (_container["designCanvas"] - _slot["h"]) / 2
):
    raise ValueError("container slot must be centered on the container canvas")
