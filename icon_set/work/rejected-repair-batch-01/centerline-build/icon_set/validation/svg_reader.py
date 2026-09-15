"""Minimal reader for the documents this package emits.

Deliberately strict and deliberately small. It exists for the round-trip check
(section 5 step 7): parse an emitted document back and confirm the canvas,
canonical style, and path data survive, and that no transform or clip has crept
in. It is not a general SVG parser and must not become one.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from xml.etree import ElementTree

SVG_NS = "http://www.w3.org/2000/svg"
_FORBIDDEN_ATTRS = ("transform", "clip-path", "mask", "style", "filter")
_NUMBER = re.compile(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?")


class SvgRoundTripError(ValueError):
    """The emitted document did not reparse into the same canonical scene."""


@dataclass(frozen=True)
class ParsedSvg:
    width: int
    height: int
    view_box: tuple[float, float, float, float]
    style: dict[str, str]
    paths: tuple[tuple[str, str], ...]


def _strip(tag: str) -> str:
    return tag.split("}", 1)[-1]


def parse_svg(document: str) -> ParsedSvg:
    try:
        root = ElementTree.fromstring(document)
    except ElementTree.ParseError as error:
        raise SvgRoundTripError(f"document is not well-formed XML: {error}") from error
    if _strip(root.tag) != "svg":
        raise SvgRoundTripError(f"root element is {_strip(root.tag)!r}, expected 'svg'")
    if not root.tag.startswith("{" + SVG_NS + "}"):
        raise SvgRoundTripError("root element is not in the SVG namespace")

    view_box_raw = root.get("viewBox")
    if view_box_raw is None:
        raise SvgRoundTripError("missing viewBox")
    numbers = [float(value) for value in _NUMBER.findall(view_box_raw)]
    if len(numbers) != 4:
        raise SvgRoundTripError(f"viewBox must have four numbers, got {view_box_raw!r}")

    style = {
        key: value
        for key, value in root.attrib.items()
        if key in ("fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin")
    }

    paths: list[tuple[str, str]] = []
    for element in root.iter():
        for attribute in _FORBIDDEN_ATTRS:
            if element.get(attribute) is not None:
                raise SvgRoundTripError(
                    f"<{_strip(element.tag)}> carries a forbidden {attribute!r} attribute"
                )
        tag = _strip(element.tag)
        if tag == "path":
            data = element.get("d")
            if not data:
                raise SvgRoundTripError("a <path> has no d attribute")
            paths.append((element.get("id") or "", data))
        elif tag in ("g", "use", "image", "symbol", "defs"):
            raise SvgRoundTripError(f"<{tag}> is not part of the canonical output")

    return ParsedSvg(
        width=int(root.get("width", "0")),
        height=int(root.get("height", "0")),
        view_box=(numbers[0], numbers[1], numbers[2], numbers[3]),
        style=style,
        paths=tuple(paths),
    )
