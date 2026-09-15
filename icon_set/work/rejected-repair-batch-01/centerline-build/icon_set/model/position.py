"""Placement types for composition.

``Position`` is re-exported from :mod:`primitives` so the geometry AST and the
composition model share one definition. ``PlacedIcon`` binds an icon to its
integer translation; :class:`~icon_set.model.icons.combined.CombinedIcon` keeps
these pairs private so icon/position parity cannot be broken by a caller.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .primitives import Position

if TYPE_CHECKING:  # pragma: no cover - typing only
    from .icons.base import Icon

__all__ = ["Position", "PlacedIcon"]


@dataclass(frozen=True)
class PlacedIcon:
    icon: "Icon"
    position: Position
