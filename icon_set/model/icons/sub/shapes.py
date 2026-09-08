"""Geometric shape nouns.

Radial subjects take CIRCLE and are measured by radial extent; rectilinear ones
take SQUARE. Both are full-canvas tokens -- CIRCLE radially, SQUARE to all four
edges -- so a rectilinear shape here is authored to the 2..30 centerline box.

Regular pentagons, five-point stars and regular octagons have no exact integer
vertices at any useful radius. Their vertices are placed on the nearest grid
point to the true radius, which the CIRCLE touch rule accepts; the octagon is
authored as a chamfered square so every vertex is exact.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Sub32


class Circle(Sub32):
    icon_id = "circle"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("ring", "o")
    keywords = ("round", "radio", "dot", "outline")

    def build(self) -> None:
        self.add_arc("half-top", (2, 16), (30, 16), radius_x=14)
        self.add_arc("half-bottom", (30, 16), (2, 16), radius_x=14)
        self.add_contour("ring", "half-top", "half-bottom", closed=True)


class Square(Sub32):
    icon_id = "square"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("box", "stop", "rectangle")
    keywords = ("checkbox", "frame", "block")

    def build(self) -> None:
        self.add_polyline("outline", (2, 2), (30, 2), (30, 30), (2, 30), closed=True)


class Diamond(Sub32):
    icon_id = "diamond"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("rhombus", "decision")
    keywords = ("flowchart", "gem", "rotate")

    def build(self) -> None:
        self.add_polyline("outline", (16, 2), (30, 16), (16, 30), (2, 16), closed=True)


class TriangleUp(Sub32):
    icon_id = "triangle-up"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("caret-up-solid-outline", "warning-shape")
    keywords = ("alert", "up", "peak")

    def build(self) -> None:
        self.add_polyline("outline", (16, 2), (30, 30), (2, 30), closed=True)


class TriangleDown(Sub32):
    icon_id = "triangle-down"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    keywords = ("down", "descend", "funnel")

    def build(self) -> None:
        self.add_polyline("outline", (2, 2), (30, 2), (16, 30), closed=True)


class TriangleRight(Sub32):
    icon_id = "triangle-right"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/control"
    aliases = ("play",)
    keywords = ("play", "start", "forward")

    def build(self) -> None:
        self.add_polyline("outline", (2, 2), (30, 16), (2, 30), closed=True)


class TriangleLeft(Sub32):
    icon_id = "triangle-left"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/control"
    aliases = ("play-back",)
    keywords = ("rewind", "back", "previous")

    def build(self) -> None:
        self.add_polyline("outline", (30, 2), (2, 16), (30, 30), closed=True)


class Hexagon(Sub32):
    icon_id = "hexagon"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    keywords = ("cell", "badge", "honeycomb")

    def build(self) -> None:
        self.add_polyline(
            "outline",
            (11, 2), (21, 2), (30, 16), (21, 30), (11, 30), (2, 16),
            closed=True,
        )


class Octagon(Sub32):
    icon_id = "octagon"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("stop-sign",)
    keywords = ("stop", "halt", "sign")

    def build(self) -> None:
        # A chamfered square: every vertex lands exactly on the grid, unlike a
        # trigonometric regular octagon.
        self.add_polyline(
            "outline",
            (11, 2), (21, 2), (30, 11), (30, 21),
            (21, 30), (11, 30), (2, 21), (2, 11),
            closed=True,
        )


class Pentagon(Sub32):
    icon_id = "pentagon"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    keywords = ("polygon", "five", "shield")

    def build(self) -> None:
        self.add_polyline(
            "outline", (16, 2), (29, 12), (24, 27), (8, 27), (3, 12), closed=True
        )


class Star(Sub32):
    icon_id = "star"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("favourite", "favorite", "rating")
    keywords = ("bookmark", "rate", "highlight")

    def build(self) -> None:
        self.add_polyline(
            "outline",
            (16, 2), (19, 12), (29, 12), (21, 18), (24, 27),
            (16, 21), (8, 27), (11, 18), (3, 12), (13, 12),
            closed=True,
        )


class Sparkle(Sub32):
    icon_id = "sparkle"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("star-four", "shine", "ai")
    keywords = ("magic", "glint", "new", "generate")

    def build(self) -> None:
        # Four concave quarter-circles, each centred on a canvas corner, so the
        # sides curve inward between the tips. Straight sides read as a chunky
        # diamond rather than a sparkle.
        self.add_arc("edge-ne", (16, 2), (30, 16), radius_x=14, sweep=False)
        self.add_arc("edge-se", (30, 16), (16, 30), radius_x=14, sweep=False)
        self.add_arc("edge-sw", (16, 30), (2, 16), radius_x=14, sweep=False)
        self.add_arc("edge-nw", (2, 16), (16, 2), radius_x=14, sweep=False)
        self.add_contour(
            "outline", "edge-ne", "edge-se", "edge-sw", "edge-nw", closed=True
        )


class Target(Sub32):
    icon_id = "target"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("radio-selected", "bullseye")
    keywords = ("focus", "aim", "selected", "concentric")

    def build(self) -> None:
        # Radii 14 and 6 leave 8 units of centerline spacing. Radius 7 would sit
        # exactly on the SUB32 minimum, where the spacing engine's curve
        # flattening bound cannot certify a pass and returns REVIEW instead;
        # curved parts need real margin, not a threshold-exact fit.
        self.add_arc("outer-top", (2, 16), (30, 16), radius_x=14)
        self.add_arc("outer-bottom", (30, 16), (2, 16), radius_x=14)
        self.add_contour("ring-outer", "outer-top", "outer-bottom", closed=True)
        self.add_arc("inner-top", (10, 16), (22, 16), radius_x=6)
        self.add_arc("inner-bottom", (22, 16), (10, 16), radius_x=6)
        self.add_contour("ring-inner", "inner-top", "inner-bottom", closed=True)


class Heart(Sub32):
    icon_id = "heart"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    aliases = ("like", "love")
    keywords = ("favourite", "favorite", "save", "romance")

    def build(self) -> None:
        # Four pieces per side, chosen so every junction is tangent-continuous
        # and every extreme is exact:
        #
        #   lobe-inner   notch (16,8) -> crest (10,4)   ellipse centre (10,8)
        #   lobe-outer   crest (10,4) -> widest (2,12)  circle  centre (10,12)
        #   shoulder     widest (2,12) -> (6,20)        circle  centre (12,12)
        #   side         (6,20) -> tip (16,28)          straight
        #
        # The lobe-outer and shoulder circles are both centred on y 12, so both
        # are vertical at the widest point and meet without a corner. The
        # shoulder leaves (6,20) at 36.9 degrees and the side runs at 38.7, so
        # that junction is within two degrees of tangent too. A straight side
        # taken directly from the widest point instead puts a 41-degree kink
        # exactly where the eye reads the shoulder, and the icon flattens into
        # a V with two horns.
        #
        # Proportions follow the Lucide heart: widest points around 40 percent
        # of the height, a shallow cleft, and a tip that the round join softens
        # into Lucide's small bottom radius on its own.
        self.add_arc("lobe-left-inner", (16, 8), (10, 4), radius_x=6, radius_y=4, sweep=False)
        self.add_arc("lobe-left-outer", (10, 4), (2, 12), radius_x=8, sweep=False)
        self.add_arc("shoulder-left", (2, 12), (6, 20), radius_x=10, sweep=False)
        self.add_line("side-left", (6, 20), (16, 28))
        self.add_line("side-right", (16, 28), (26, 20))
        self.add_arc("shoulder-right", (26, 20), (30, 12), radius_x=10, sweep=False)
        self.add_arc("lobe-right-outer", (30, 12), (22, 4), radius_x=8, sweep=False)
        self.add_arc("lobe-right-inner", (22, 4), (16, 8), radius_x=6, radius_y=4, sweep=False)
        self.add_contour(
            "outline",
            "lobe-left-inner", "lobe-left-outer", "shoulder-left", "side-left",
            "side-right", "shoulder-right", "lobe-right-outer", "lobe-right-inner",
            closed=True,
        )
