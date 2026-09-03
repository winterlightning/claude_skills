#!/usr/bin/env python3
"""Legacy geometry registry for historical Unlimited Shapes instance documents.

New schema-v2 icons own exact geometry in their ``elements`` arrays and do not
import or extend this compatibility registry.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable


def n(value: float) -> float:
    return round(float(value), 3)


@dataclass(frozen=True)
class Shape:
    id: str
    name: str
    closed: bool
    natural: tuple[float, float]
    default: tuple[float, float]
    geometry: Callable[[float, float], tuple[str, dict[str, object]]]


def path(d: str, **attrs: object) -> tuple[str, dict[str, object]]:
    return "path", {"d": d, **attrs}


def ellipse(w: float, h: float) -> tuple[str, dict[str, object]]:
    return "ellipse", {"cx": n(w / 2), "cy": n(h / 2), "rx": n(w / 2), "ry": n(h / 2)}


def rect(w: float, h: float, radius: float = 0) -> tuple[str, dict[str, object]]:
    attrs: dict[str, object] = {"x": 0, "y": 0, "width": n(w), "height": n(h)}
    if radius:
        attrs["rx"] = n(radius)
    return "rect", attrs


def dashed_rectangle(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open multi-subpath rectangular outline using a fixed 4u dash/4u gap rhythm."""
    perimeter = 2 * (w + h)
    boundaries = (w, w + h, 2 * w + h, perimeter)

    def point_at(distance: float) -> tuple[float, float]:
        distance = min(max(distance, 0), perimeter)
        if distance <= w:
            return distance, 0
        if distance <= w + h:
            return w, distance - w
        if distance <= 2 * w + h:
            return 2 * w + h - distance, h
        return 0, perimeter - distance

    parts: list[str] = []
    start = 0.0
    while start < perimeter:
        end = min(start + 4, perimeter)
        x, y = point_at(start)
        parts.append(f"M {n(x)} {n(y)}")
        for boundary in boundaries:
            if start < boundary < end:
                x, y = point_at(boundary)
                parts.append(f"L {n(x)} {n(y)}")
        x, y = point_at(end)
        parts.append(f"L {n(x)} {n(y)}")
        start += 8
    return path(" ".join(parts))


def water_drop(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed symmetric teardrop with one pointed top and rounded bowl."""
    return path(
        f"M {n(w/2)} 0 Q {n(w)} {n(h*.45)} {n(w)} {n(h*.7)} "
        f"Q {n(w)} {n(h)} {n(w/2)} {n(h)} Q 0 {n(h)} 0 {n(h*.7)} "
        f"Q 0 {n(h*.45)} {n(w/2)} 0 Z"
    )


def tapered_spire(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed symmetric pointed contour with quadratic sides and a flat base."""
    return path(
        f"M {n(w/2)} 0 Q 0 {n(h*.7)} 0 {n(h)} "
        f"L {n(w)} {n(h)} Q {n(w)} {n(h*.7)} {n(w/2)} 0 Z"
    )


def faucet(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Wall faucet with horizontal inlet, quarter-turn spout, and T handle."""
    return path(
        f"M 0 {n(h*.5)} L {n(w*.75)} {n(h*.5)} "
        f"A {n(w*.25)} {n(h*.25)} 0 0 1 {n(w)} {n(h*.75)} L {n(w)} {n(h)} "
        f"M {n(w*.35)} {n(h*.5)} L {n(w*.35)} 0 "
        f"M {n(w*.2)} 0 L {n(w*.5)} 0"
    )


def open_end_wrench(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Horizontal ring-handle wrench with a 45-degree open jaw at the right."""
    radius = h / 2
    neck = w - radius
    return path(
        f"M {n(radius)} 0 A {n(radius)} {n(radius)} 0 1 1 {n(radius)} {n(h)} "
        f"A {n(radius)} {n(radius)} 0 1 1 {n(radius)} 0 "
        f"M {n(h)} {n(radius)} L {n(neck)} {n(radius)} "
        f"M {n(neck)} {n(radius)} L {n(w)} 0 M {n(neck)} {n(radius)} L {n(w)} {n(h)}"
    )


def gable(w: float, h: float) -> tuple[str, dict[str, object]]:
    rise = min(w / 2, h)
    d = (f"M 0 {n(h)} L 0 {n(rise)} L {n(w/2)} 0 L {n(w)} {n(rise)} L {n(w)} {n(h)} Z"
         if h > rise else f"M 0 {n(rise)} L {n(w/2)} 0 L {n(w)} {n(rise)} Z")
    return path(d)


def twin_gable(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed two-peak contour with one shared central valley."""
    rise = min(w / 4, h)
    return path(
        f"M 0 {n(h)} L 0 {n(rise)} L {n(w/4)} 0 L {n(w/2)} {n(rise)} "
        f"L {n(3*w/4)} 0 L {n(w)} {n(rise)} L {n(w)} {n(h)} Z"
    )


def open_gable(w: float, h: float) -> tuple[str, dict[str, object]]:
    rise = min(w / 2, h)
    head = f"L {n(w/2)} 0 L {n(w)} {n(rise)}"
    d = (f"M 0 {n(h)} L 0 {n(rise)} {head} L {n(w)} {n(h)}"
         if h > rise else f"M 0 {n(rise)} {head}")
    return path(d)


def arch(w: float, h: float) -> tuple[str, dict[str, object]]:
    ry = min(w / 2, h)
    head = f"A {n(w/2)} {n(ry)} 0 0 1 {n(w)} {n(ry)}"
    d = f"M 0 {n(h)} L 0 {n(ry)} {head} L {n(w)} {n(h)}" if h > ry else f"M 0 {n(ry)} {head}"
    return path(d)


def hook(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open J-hook with a long stem, semicircular bowl, and short return tip."""
    radius = w / 2
    bowl_y = max(radius, h - radius)
    tip_y = max(0, bowl_y - radius)
    return path(
        f"M 0 0 L 0 {n(bowl_y)} A {n(radius)} {n(radius)} 0 0 0 {n(w)} {n(bowl_y)} "
        f"L {n(w)} {n(tip_y)}"
    )


def cloud(w: float, h: float) -> tuple[str, dict[str, object]]:
    return path(
        f"M 0 {n(h*.65)} Q 0 {n(h*.35)} {n(w*.2)} {n(h*.35)} "
        f"Q {n(w*.25)} 0 {n(w*.5)} 0 Q {n(w*.75)} 0 {n(w*.8)} {n(h*.35)} "
        f"Q {n(w)} {n(h*.35)} {n(w)} {n(h*.65)} Q {n(w)} {n(h)} {n(w*.82)} {n(h)} "
        f"L {n(w*.18)} {n(h)} Q 0 {n(h)} 0 {n(h*.65)} Z"
    )


def hexagon(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed flat-top hexagon with 45-degree mitres when the box is at least as wide as tall."""
    inset = min(h / 2, w / 2)
    return path(
        f"M {n(inset)} 0 L {n(w - inset)} 0 L {n(w)} {n(h/2)} "
        f"L {n(w - inset)} {n(h)} L {n(inset)} {n(h)} L 0 {n(h/2)} Z"
    )


STAR_POINTS = 5
STAR_INNER = math.cos(math.radians(72)) / math.cos(math.radians(36))


def star(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed five-point star: the classic rating/favourite outline.

    Outer vertices sit every 72 degrees from the apex and the inner radius is
    cos(72)/cos(36), so each pair of edges is collinear with one pentagram
    line. The unit star is mapped onto the box, so the apex touches the top
    edge, the two upper arms the sides, and the two lower arms the bottom edge
    at every size.
    """
    vertices = []
    for step in range(2 * STAR_POINTS):
        radius = 1.0 if step % 2 == 0 else STAR_INNER
        angle = -math.pi / 2 + step * math.pi / STAR_POINTS
        vertices.append((radius * math.cos(angle), radius * math.sin(angle)))
    left = min(x for x, _ in vertices); right = max(x for x, _ in vertices)
    top = min(y for _, y in vertices); bottom = max(y for _, y in vertices)
    points = [((x - left) * w / (right - left), (y - top) * h / (bottom - top)) for x, y in vertices]
    runs = " ".join(f"L {n(x)} {n(y)}" for x, y in points[1:])
    return path(f"M {n(points[0][0])} {n(points[0][1])} {runs} Z")


SCALLOP_LOBES = 8
SCALLOP_VALLEY = 0.82


def scalloped_oval(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed radially lobed oval: eight equal outward bulges around one contour.

    One quadratic per lobe, running valley to valley with its control point on
    the crest ray. The control radius is solved from the valley radius so each
    crest lands exactly on the box ellipse, which puts the four cardinal extremes
    on the box edges at any aspect ratio; valleys sit on the 0.82 ellipse. Every
    lobe joins the next smoothly, and no segment doubles back, so the contour
    never closes a spurious pocket at a valley.
    """
    cx, cy = w / 2, h / 2
    half = math.pi / SCALLOP_LOBES
    crest = 2 - SCALLOP_VALLEY * math.cos(half)

    def place(radius: float, angle: float) -> tuple[float, float]:
        return cx + cx * radius * math.cos(angle), cy + cy * radius * math.sin(angle)

    start = place(SCALLOP_VALLEY, half)
    parts = [f"M {n(start[0])} {n(start[1])}"]
    for lobe in range(SCALLOP_LOBES):
        control = place(crest, 2 * half * (lobe + 1))
        end = place(SCALLOP_VALLEY, 2 * half * (lobe + 1) + half)
        parts.append(f"Q {n(control[0])} {n(control[1])} {n(end[0])} {n(end[1])}")
    return path(" ".join(parts) + " Z")


def head_profile(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open human head seen in profile, facing right, drawn as one continuous contour.

    Up the back of the neck, up the back of the skull, over the crown, down the
    forehead, out to the nose, in at the lip, out at the chin, down the front of
    the neck. Both neck runs leave the bottom edge vertically, so the head sits
    on a shoulder line or a frame instead of flaring into it. The contour uses
    quadratics throughout. `flipX` faces it left.
    """
    return path(
        f"M {n(w*.10)} {n(h)} "
        f"Q {n(w*.10)} {n(h*.80)} {n(w*.04)} {n(h*.66)} "
        f"Q 0 {n(h*.52)} 0 {n(h*.40)} "
        f"Q 0 0 {n(w*.44)} 0 "
        f"Q {n(w*.80)} 0 {n(w*.82)} {n(h*.28)} "
        f"Q {n(w*.84)} {n(h*.38)} {n(w)} {n(h*.50)} "
        f"Q {n(w*.90)} {n(h*.56)} {n(w*.84)} {n(h*.60)} "
        f"Q {n(w*.78)} {n(h*.66)} {n(w*.70)} {n(h*.76)} "
        f"Q {n(w*.68)} {n(h*.88)} {n(w*.68)} {n(h)}"
    )


def worker_profile(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open side-view worker with a separate head and one walking body contour."""
    radius = min(w * .20, h * .09)
    cx = w * .45
    return path(
        f"M {n(cx)} 0 A {n(radius)} {n(radius)} 0 1 1 {n(cx)} {n(2*radius)} "
        f"A {n(radius)} {n(radius)} 0 1 1 {n(cx)} 0 Z "
        f"M {n(cx)} {n(2*radius)} "
        f"Q {n(w*.20)} {n(h*.32)} {n(w*.38)} {n(h*.52)} "
        f"Q {n(w*.52)} {n(h*.68)} 0 {n(h)} "
        f"M {n(w*.38)} {n(h*.52)} Q {n(w*.62)} {n(h*.58)} {n(w)} {n(h*.70)} "
        f"M {n(w*.38)} {n(h*.52)} Q {n(w*.58)} {n(h*.72)} {n(w*.68)} {n(h)}"
    )


def worker_profile_solid(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Small worker profile with a round-cap point head and quadratic body."""
    radius = min(w * .18, h * .08)
    cx = w * .45
    cy = radius
    return path(
        f"M {n(cx)} {n(cy)} L {n(cx)} {n(cy)} "
        f"M {n(cx)} {n(2*radius)} "
        f"Q {n(w*.20)} {n(h*.32)} {n(w*.38)} {n(h*.52)} "
        f"Q {n(w*.52)} {n(h*.68)} 0 {n(h)} "
        f"M {n(w*.38)} {n(h*.52)} Q {n(w*.62)} {n(h*.58)} {n(w)} {n(h*.70)} "
        f"M {n(w*.38)} {n(h*.52)} Q {n(w*.58)} {n(h*.72)} {n(w*.68)} {n(h)}"
    )


def pig_outline(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed side-view pig body with a raised ear, snout, belly, and two feet."""
    return path(
        f"M 0 {n(h*.50)} "
        f"Q {n(w*.08)} {n(h*.12)} {n(w*.38)} {n(h*.12)} "
        f"Q {n(w*.44)} 0 {n(w*.54)} 0 "
        f"Q {n(w*.62)} {n(h*.12)} {n(w*.70)} {n(h*.14)} "
        f"Q {n(w*.90)} {n(h*.14)} {n(w)} {n(h*.40)} "
        f"Q {n(w)} {n(h*.65)} {n(w*.84)} {n(h*.70)} "
        f"Q {n(w*.82)} {n(h*.90)} {n(w*.72)} {n(h)} "
        f"Q {n(w*.60)} {n(h)} {n(w*.58)} {n(h*.76)} "
        f"Q {n(w*.40)} {n(h*.80)} {n(w*.30)} {n(h*.76)} "
        f"Q {n(w*.28)} {n(h)} {n(w*.16)} {n(h)} "
        f"Q {n(w*.04)} {n(h*.86)} 0 {n(h*.50)} Z"
    )


def broken_pig_outline(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Two separated pig halves divided by parallel zigzag crack edges.

    The canonical 40x22 frame is scaled proportionally into the requested box.
    At its natural aspect ratio, both crack contours use exact 45-degree runs.
    """
    x = lambda value: n(w * value / 40)
    y = lambda value: n(h * value / 22)
    return path(
        f"M {x(17)} {y(4)} "
        f"Q {x(16)} {y(0)} {x(12)} {y(0)} "
        f"Q {x(8)} {y(2)} {x(4)} {y(4)} "
        f"Q {x(0)} {y(6)} {x(0)} {y(11)} "
        f"Q {x(0)} {y(16)} {x(4)} {y(17)} "
        f"Q {x(4)} {y(21)} {x(8)} {y(22)} "
        f"Q {x(12)} {y(22)} {x(17)} {y(20)} "
        f"L {x(13)} {y(16)} L {x(17)} {y(12)} L {x(13)} {y(8)} L {x(17)} {y(4)} Z "
        f"M {x(27)} {y(4)} "
        f"Q {x(30)} {y(2)} {x(34)} {y(4)} "
        f"Q {x(40)} {y(4)} {x(40)} {y(10)} "
        f"Q {x(40)} {y(14)} {x(35)} {y(15)} "
        f"Q {x(34)} {y(20)} {x(30)} {y(22)} "
        f"Q {x(26)} {y(22)} {x(27)} {y(20)} "
        f"L {x(23)} {y(16)} L {x(27)} {y(12)} L {x(23)} {y(8)} L {x(27)} {y(4)} Z"
    )


def holding_hand(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open side-view hand contour with two gripping finger lobes and a wrist gap."""
    return path(
        f"M 0 {n(h*14/24)} "
        f"Q {n(w*4/24)} 0 {n(w*14/24)} 0 "
        f"L {n(w*20/24)} 0 "
        f"A {n(w*4/24)} {n(h*4/24)} 0 0 1 {n(w*20/24)} {n(h*8/24)} "
        f"L {n(w*16/24)} {n(h*8/24)} "
        f"A {n(w*4/24)} {n(h*4/24)} 0 0 0 {n(w*16/24)} {n(h*16/24)} "
        f"L {n(w*20/24)} {n(h*16/24)} "
        f"A {n(w*4/24)} {n(h*4/24)} 0 0 1 {n(w*20/24)} {n(h)} "
        f"L {n(w*14/24)} {n(h)} "
        f"Q {n(w*10/24)} {n(h)} {n(w*8/24)} {n(h*20/24)} "
        f"L 0 {n(h*20/24)}"
    )


def bottle_outline(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed shouldered bottle with a broad neck and ordinary 4u feet.

    The canonical 14x20 form uses an 8u neck, exact 45-degree shoulders, and
    4u circular lower corners.  Preserve that aspect ratio when the shoulder
    angle is identity-bearing.
    """
    neck = min(8.0, w - 4.0)
    shoulder = (w - neck) / 2
    neck_height = min(4.0, max(0.0, h - 12.0))
    shoulder_bottom = neck_height + shoulder
    radius = min(4.0, w / 2, max(0.0, (h - shoulder_bottom) / 2))
    return path(
        f"M {n(shoulder)} 0 L {n(w - shoulder)} 0 "
        f"L {n(w - shoulder)} {n(neck_height)} "
        f"L {n(w)} {n(shoulder_bottom)} L {n(w)} {n(h - radius)} "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(w - radius)} {n(h)} "
        f"L {n(radius)} {n(h)} "
        f"A {n(radius)} {n(radius)} 0 0 1 0 {n(h - radius)} "
        f"L 0 {n(shoulder_bottom)} L {n(shoulder)} {n(neck_height)} Z"
    )


def transfer_hand(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Compact open transfer palm with one thumb rise and finger block.

    At the canonical 20x12 size, the two exposed palm diagonals are exact 45
    degrees.  The open wrist and broad fingertip stay legible at true 24px
    without the dense finger lobes of the larger hand atoms.
    """
    return path(
        f"M 0 0 L {n(w * .2)} 0 "
        f"Q {n(w * .3)} 0 {n(w * .4)} {n(h * .25)} "
        f"L {n(w * .55)} {n(h * .5)} L {n(w * .9)} {n(h * .5)} "
        f"Q {n(w)} {n(h * .5)} {n(w)} {n(h * 2 / 3)} "
        f"Q {n(w)} {n(h * 5 / 6)} {n(w * .9)} {n(h * 5 / 6)} "
        f"L {n(w * .6)} {n(h * 5 / 6)} "
        f"Q {n(w * .45)} {n(h)} {n(w * .3)} {n(h)} L 0 {n(h * .5)}"
    )



def lens(w: float, h: float) -> tuple[str, dict[str, object]]:
    radius = (w*w + h*h) / (4*h)
    large = int(h > w)
    return path(f"M 0 {n(h/2)} A {n(radius)} {n(radius)} 0 {large} 1 {n(w)} {n(h/2)} "
                f"A {n(radius)} {n(radius)} 0 {large} 1 0 {n(h/2)} Z")


def ring(w: float, h: float) -> tuple[str, dict[str, object]]:
    cx, cy, rx, ry = w/2, h/2, w/2, h/2
    irx, iry = rx*.6, ry*.6
    return path(
        f"M {n(cx)} 0 A {n(rx)} {n(ry)} 0 1 0 {n(cx)} {n(h)} A {n(rx)} {n(ry)} 0 1 0 {n(cx)} 0 Z "
        f"M {n(cx)} {n(cy-iry)} A {n(irx)} {n(iry)} 0 1 0 {n(cx)} {n(cy+iry)} "
        f"A {n(irx)} {n(iry)} 0 1 0 {n(cx)} {n(cy-iry)} Z", **{"fill-rule": "evenodd"})


def trapezoid(w: float, h: float) -> tuple[str, dict[str, object]]:
    inset = min(h / math.tan(math.pi / 3), w * 0.4)
    return path(f"M {n(inset)} 0 L {n(w - inset)} 0 L {n(w)} {n(h)} L 0 {n(h)} Z")


def flared_horn(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed, right-opening horn with a narrow rear and full-height bell.

    The two quadratic rails keep the flare natural at compact sizes, with
    whole-unit coordinates in the canonical 24x16 geometry.
    The form is intentionally generic enough for speaker bells, funnels, and
    nozzles as well as acoustic horns.
    """
    return path(
        f"M 0 {n(h * 6 / 16)} "
        f"Q {n(w * .5)} {n(h * .25)} {n(w)} 0 "
        f"L {n(w)} {n(h)} "
        f"Q {n(w * .5)} {n(h * .75)} 0 {n(h * .625)} Z"
    )


def sloped_box(w: float, h: float) -> tuple[str, dict[str, object]]:
    rise = min(w * math.tan(math.pi / 12), h)
    return path(f"M 0 {n(rise)} L {n(w)} 0 L {n(w)} {n(h)} L 0 {n(h)} Z")


def s_bend(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open S-bend made from two tangent, opposite-sweep quarter ellipses."""
    rx, ry = w / 2, h / 2
    return path(
        f"M 0 0 A {n(rx)} {n(ry)} 0 0 1 {n(rx)} {n(ry)} "
        f"A {n(rx)} {n(ry)} 0 0 0 {n(w)} {n(h)}"
    )


def bulb_outline(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open symmetric bulb globe tapering to two neck endpoints."""
    return path(
        f"M {n(w/3)} {n(h)} "
        f"Q {n(w/3)} {n(3*h/4)} {n(w/6)} {n(5*h/8)} "
        f"Q 0 {n(h/2)} 0 {n(3*h/8)} "
        f"Q 0 0 {n(w/2)} 0 "
        f"Q {n(w)} 0 {n(w)} {n(3*h/8)} "
        f"Q {n(w)} {n(h/2)} {n(5*w/6)} {n(5*h/8)} "
        f"Q {n(2*w/3)} {n(3*h/4)} {n(2*w/3)} {n(h)}"
    )


def lobed_drop(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed asymmetric drop with a folded lobe and inward notch."""
    return path(
        f"M {n(w*21/32)} 0 "
        f"Q {n(w*24/32)} 0 {n(w*27/32)} {n(h*6/40)} "
        f"Q {n(w)} {n(h*19/40)} {n(w)} {n(h*28/40)} "
        f"Q {n(w)} {n(h)} {n(w*.5)} {n(h)} "
        f"Q 0 {n(h)} 0 {n(h*28/40)} "
        f"Q 0 {n(h*18/40)} {n(w*9/32)} {n(h*10/40)} "
        f"Q {n(w*11/32)} {n(h*10/40)} {n(w*9/32)} {n(h*17/40)} "
        f"Q {n(w*9/32)} {n(h*21/40)} {n(w*13/32)} {n(h*21/40)} "
        f"Q {n(w*15/32)} {n(h*21/40)} {n(w*15/32)} {n(h*17/40)} "
        f"Q {n(w*15/32)} {n(h*10/40)} {n(w*19/32)} {n(h*5/40)} "
        f"Q {n(w*20/32)} {n(h*2/40)} {n(w*21/32)} 0 Z"
    )


def stepped_cog(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Sparse orthogonal cog with four broad cardinal teeth."""
    points = (
        (14,0),(22,0),(22,6),(30,6),(30,14),
        (36,14),(36,22),(30,22),(30,30),(22,30),
        (22,36),(14,36),(14,30),(6,30),(6,22),
        (0,22),(0,14),(6,14),(6,6),(14,6),
    )
    coords = [(n(w*x/36), n(h*y/36)) for x,y in points]
    return path("M " + " L ".join(f"{x} {y}" for x,y in coords) + " Z")


def twin_lobed_drop(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed symmetric double-lobed drop with a central cleft."""
    return path(
        f"M {n(w/2)} {n(h)} "
        f"Q 0 {n(h*26/36)} 0 {n(h*12/36)} "
        f"Q 0 {n(h*2/36)} {n(w*9/36)} 0 "
        f"Q {n(w*15/36)} 0 {n(w/2)} {n(h*8/36)} "
        f"Q {n(w*21/36)} 0 {n(w*27/36)} 0 "
        f"Q {n(w)} {n(h*2/36)} {n(w)} {n(h*12/36)} "
        f"Q {n(w)} {n(h*26/36)} {n(w/2)} {n(h)} Z"
    )


def lightning_bolt(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed upright lightning bolt with two exact 45-degree canonical flanks.

    The natural 20x24 frame gives the two identity-bearing diagonals exact
    14u-by-14u and 12u-by-12u runs. Other portrait sizes retain the same simple
    six-vertex topology without leaving the instance box.
    """
    top = min(w*.7, h)
    inner = w*.4
    bottom = max(0, h-(w-inner))
    return path(
        f"M {n(w*.7)} 0 L 0 {n(top)} L {n(inner)} {n(top)} "
        f"L {n(inner)} {n(h)} L {n(w)} {n(bottom)} "
        f"L {n(w*.7)} {n(bottom)} Z"
    )


def puzzle_piece(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed jigsaw piece with two outward tabs and two inward sockets.

    The top and right tabs reach the box edges; the bottom and left sockets
    cut into the body while straight perimeter runs still reach the remaining
    edges. Eight quadratics keep the lobes smooth and cubic-free at any size.
    """
    return path(
        f"M 0 {n(h*.2)} L {n(w*.35)} {n(h*.2)} "
        f"Q {n(w*.35)} 0 {n(w*.5)} 0 Q {n(w*.65)} 0 {n(w*.65)} {n(h*.2)} "
        f"L {n(w*.8)} {n(h*.2)} L {n(w*.8)} {n(h*.35)} "
        f"Q {n(w)} {n(h*.35)} {n(w)} {n(h*.5)} Q {n(w)} {n(h*.65)} {n(w*.8)} {n(h*.65)} "
        f"L {n(w*.8)} {n(h)} L {n(w*.65)} {n(h)} "
        f"Q {n(w*.65)} {n(h*.8)} {n(w*.5)} {n(h*.8)} Q {n(w*.35)} {n(h*.8)} {n(w*.35)} {n(h)} "
        f"L 0 {n(h)} L 0 {n(h*.65)} "
        f"Q {n(w*.2)} {n(h*.65)} {n(w*.2)} {n(h*.5)} Q {n(w*.2)} {n(h*.35)} 0 {n(h*.35)} Z"
    )


def phone_handset_outline(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Closed diagonal telephone handset with flared earpieces.

    The canonical square frame keeps each exposed straight run horizontal,
    vertical, or at 45 degrees. Quadratic shoulders join the two earpieces to
    the curved receiver body without encoding any secondary phone detail.
    """
    x = lambda value: n(w * value / 36)
    y = lambda value: n(h * value / 36)
    return path(
        f"M {x(6)} 0 L {x(12)} 0 Q {x(14)} 0 {x(15)} {y(2)} "
        f"L {x(20)} {y(7)} Q {x(21)} {y(8)} {x(20)} {y(9)} "
        f"L {x(17)} {y(12)} Q {x(15)} {y(14)} {x(17)} {y(15)} "
        f"L {x(21)} {y(19)} Q {x(23)} {y(21)} {x(24)} {y(19)} "
        f"L {x(27)} {y(16)} Q {x(29)} {y(14)} {x(30)} {y(16)} "
        f"L {x(35)} {y(21)} Q {x(36)} {y(23)} {x(36)} {y(24)} "
        f"L {x(36)} {y(30)} Q {x(36)} {y(33)} {x(33)} {y(36)} "
        f"Q {x(29)} {y(36)} {x(25)} {y(34)} "
        f"Q {x(12)} {y(30)} {x(2)} {y(20)} Q 0 {y(17)} 0 {y(14)} "
        f"L 0 {y(9)} Q 0 {y(7)} {x(2)} {y(6)} "
        f"L {x(5)} {y(3)} Q {x(6)} {y(2)} {x(6)} 0 Z"
    )


SPIRAL_QUARTERS = 5
SPIRAL_RATIO = 0.86


def _spiral_frame() -> tuple[list[tuple[float, float]], list[float]]:
    """Junction points and radii of the canonical unit spiral.

    Each quarter arc turns 90 degrees clockwise and shrinks by SPIRAL_RATIO.
    The next centre is placed on the shared normal at the junction, so the
    contour is tangent-continuous. Every junction sits on a multiple of 90
    degrees, so each arc's extremes are its own endpoints and the endpoint
    list alone gives the exact bounds.
    """
    radii = [SPIRAL_RATIO ** step for step in range(SPIRAL_QUARTERS)]
    points = [(radii[0], 0.0)]
    centre = (0.0, 0.0)
    for step, radius in enumerate(radii):
        start = step * math.pi / 2
        if step:
            centre = (points[step][0] - radius * math.cos(start),
                      points[step][1] - radius * math.sin(start))
        end = start + math.pi / 2
        points.append((centre[0] + radius * math.cos(end), centre[1] + radius * math.sin(end)))
    return points, radii


def spiral(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open inward-winding spiral of tangent-continuous quarter arcs."""
    points, radii = _spiral_frame()
    left = min(x for x, _ in points); right = max(x for x, _ in points)
    top = min(y for _, y in points); bottom = max(y for _, y in points)
    sx = w / (right - left); sy = h / (bottom - top)
    place = lambda point: (n((point[0] - left) * sx), n((point[1] - top) * sy))
    x, y = place(points[0])
    parts = [f"M {x} {y}"]
    for step, radius in enumerate(radii):
        x, y = place(points[step + 1])
        parts.append(f"A {n(radius * sx)} {n(radius * sy)} 0 0 1 {x} {y}")
    return path(" ".join(parts))


def open_twin_gable(w: float, h: float) -> tuple[str, dict[str, object]]:
    """`twin-gable` without its base: one open two-peak zigzag."""
    rise = min(w / 4, h)
    peaks = (f"L {n(w/4)} 0 L {n(w/2)} {n(rise)} L {n(3*w/4)} 0 L {n(w)} {n(rise)}")
    d = (f"M 0 {n(h)} L 0 {n(rise)} {peaks} L {n(w)} {n(h)}"
         if h > rise else f"M 0 {n(rise)} {peaks}")
    return path(d)


GAPPED_HEAD_RATIO = 0.5


def gapped_rounded_rectangle(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Rounded rectangle whose head edge is interrupted by one centred gap.

    The contour is the closed ``rounded-rectangle`` broken in the middle of its
    head: it runs clockwise from the gap's right lip, around all four ordinary
    4u corners, and back to the gap's left lip. The gap is exactly half the box
    width, so the two head runs are equal and the opening stays centred at every
    size. The corner radius carries the ordinary 4u token and clamps to the head
    run and half-height, so the runs can never invert on a small or short box.
    """
    gap = w * GAPPED_HEAD_RATIO
    left, right = (w - gap) / 2, (w + gap) / 2
    radius = min(4, left, h / 2)
    return path(
        f"M {n(right)} 0 L {n(w-radius)} 0 "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(w)} {n(radius)} L {n(w)} {n(h-radius)} "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(w-radius)} {n(h)} L {n(radius)} {n(h)} "
        f"A {n(radius)} {n(radius)} 0 0 1 0 {n(h-radius)} L 0 {n(radius)} "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(radius)} 0 L {n(left)} 0"
    )


def corner_gapped_rounded_rectangle(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Rounded frame with a lower-left cutout for a foreground overlap."""
    radius = min(4, w / 2, h / 2)
    bottom_lip = w * .75
    return path(
        f"M 0 {n(radius)} "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(radius)} 0 L {n(w-radius)} 0 "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(w)} {n(radius)} L {n(w)} {n(h-radius)} "
        f"A {n(radius)} {n(radius)} 0 0 1 {n(w-radius)} {n(h)} L {n(bottom_lip)} {n(h)}"
    )


def open_shell(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Two asymmetric quadratic shell lips sharing a hinge and opening to the right."""
    return path(
        f"M 0 {n(h/2)} Q {n(w*.3)} 0 {n(w*.8)} 0 Q {n(w)} 0 {n(w)} {n(h*.25)} "
        f"M 0 {n(h/2)} Q {n(w*.3)} {n(h)} {n(w*.75)} {n(h)} Q {n(w)} {n(h)} {n(w)} {n(h*.75)}"
    )


def oyster_shell(w: float, h: float) -> tuple[str, dict[str, object]]:
    """One asymmetric oyster rim with a compact right-facing mouth."""
    return path(
        f"M {n(w*.53)} {n(h*.38)} "
        f"Q {n(w*.82)} {n(h*.28)} {n(w*.98)} {n(h*.08)} "
        f"Q {n(w)} 0 {n(w*.83)} 0 "
        f"Q {n(w*.43)} 0 {n(w*.16)} {n(h*.25)} "
        f"Q 0 {n(h*.42)} 0 {n(h*.55)} "
        f"Q {n(w*.03)} {n(h*.78)} {n(w*.27)} {n(h*.94)} "
        f"Q {n(w*.58)} {n(h*1.0648)} {n(w*.85)} {n(h*.93)} "
        f"Q {n(w)} {n(h*.86)} {n(w)} {n(h*.73)} "
        f"Q {n(w)} {n(h*.63)} {n(w*.85)} {n(h*.60)} "
        f"Q {n(w*.75)} {n(h*.58)} {n(w*.67)} {n(h*.55)}"
    )


def side_gapped_rounded_rectangle(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Rounded frame with a centred gap in its left side for an entering arm."""
    radius = min(4, w / 2, h / 2)
    gap_top, gap_bottom = h * .375, h * .625
    return path(
        f"M 0 {n(gap_bottom)} L 0 {n(h-radius)} "
        f"A {n(radius)} {n(radius)} 0 0 0 {n(radius)} {n(h)} L {n(w-radius)} {n(h)} "
        f"A {n(radius)} {n(radius)} 0 0 0 {n(w)} {n(h-radius)} L {n(w)} {n(radius)} "
        f"A {n(radius)} {n(radius)} 0 0 0 {n(w-radius)} 0 L {n(radius)} 0 "
        f"A {n(radius)} {n(radius)} 0 0 0 0 {n(radius)} L 0 {n(gap_top)}"
    )


def shark_fin(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open asymmetric fin contour with a long convex face and short trailing edge."""
    return path(
        f"M 0 {n(h)} Q {n(w/4)} {n(h*3/8)} {n(w)} 0 "
        f"Q {n(w*4/5)} {n(h/2)} {n(w*4/5)} {n(h)}"
    )


def wave_line(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Two-cycle horizontal wave made from four tangent quadratic lobes."""
    mid = h / 2
    return path(
        f"M 0 {n(mid)} Q {n(w/8)} {n(-h/2)} {n(w/4)} {n(mid)} "
        f"Q {n(3*w/8)} {n(3*h/2)} {n(w/2)} {n(mid)} "
        f"Q {n(5*w/8)} {n(-h/2)} {n(3*w/4)} {n(mid)} "
        f"Q {n(7*w/8)} {n(3*h/2)} {n(w)} {n(mid)}"
    )


def gripping_hand(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Open side-view palm with a separate broad finger wrap around a tool grip."""
    return path(
        f"M {n(w/2)} 0 Q {n(w/3)} 0 {n(w/6)} {n(h/5)} L 0 {n(2*h/5)} "
        f"Q 0 {n(3*h/5)} {n(w/12)} {n(4*h/5)} Q {n(5*w/24)} {n(h)} {n(w/3)} {n(h)} "
        f"Q {n(w/2)} {n(h)} {n(7*w/12)} {n(4*h/5)} L {n(2*w/3)} {n(7*h/10)} "
        f"Q {n(3*w/4)} {n(3*h/5)} {n(11*w/12)} {n(3*h/5)} Q {n(w)} {n(3*h/5)} {n(w)} {n(3*h/4)} "
        f"Q {n(w)} {n(9*h/10)} {n(7*w/8)} {n(9*h/10)} L {n(2*w/3)} {n(9*h/10)} "
        f"M {n(7*w/12)} {n(3*h/10)} L {n(5*w/6)} {n(3*h/10)} "
        f"Q {n(w)} {n(3*h/10)} {n(w)} {n(9*h/20)} Q {n(w)} {n(3*h/5)} {n(5*w/6)} {n(3*h/5)} "
        f"L {n(2*w/3)} {n(3*h/5)}"
    )


def gapped_eye(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Quadratic eye outline with a broad lower-right cutout for an overlapping handle."""
    return path(
        f"M 0 {n(h/2)} Q {n(w/2)} {n(-h/2)} {n(w)} {n(h/2)} "
        f"M 0 {n(h/2)} Q {n(w*.275)} {n(h)} {n(w*.55)} {n(h)} "
        f"M {n(w*.85)} {n(3*h/4)} Q {n(w*.925)} {n(9*h/14)} {n(w)} {n(h/2)}"
    )


RADIAL_TICK_COUNT = 12
RADIAL_TICK_INNER = 0.8


def radial_ticks(w: float, h: float) -> tuple[str, dict[str, object]]:
    """Twelve evenly spaced radial ticks between the 0.8 inner ellipse and the box edges.

    Endpoints keep four decimals rather than the usual three: a tick is only
    0.2 of the box radius long, so the extra precision keeps the short rays
    evenly spaced at small sizes.
    """
    cx, cy = w / 2, h / 2
    parts = []
    for step in range(RADIAL_TICK_COUNT):
        angle = math.radians(step * 360 / RADIAL_TICK_COUNT)
        cos, sin = math.cos(angle), math.sin(angle)
        parts.append(
            f"M {round(cx + RADIAL_TICK_INNER * cx * cos, 4)} {round(cy + RADIAL_TICK_INNER * cy * sin, 4)} "
            f"L {round(cx + cx * cos, 4)} {round(cy + cy * sin, 4)}"
        )
    return path(" ".join(parts))


SHAPES = [
    Shape("circle", "Circle", True, (20, 20), (8, 8), ellipse),
    Shape("ellipse", "Ellipse", True, (20, 12), (10, 6), ellipse),
    Shape("square", "Square", True, (20, 20), (8, 8), rect),
    Shape("rectangle", "Rectangle", True, (20, 12), (10, 6), rect),
    Shape("dashed-rectangle", "Dashed rectangle", False, (20, 28), (12, 20), dashed_rectangle),
    Shape("water-drop", "Water drop", True, (12, 18), (8, 12), water_drop),
    Shape("tapered-spire", "Tapered spire", True, (24, 32), (16, 24), tapered_spire),
    Shape("rounded-square", "Rounded square", True, (20, 20), (8, 8), lambda w,h: rect(w,h,min(w,h)*.2)),
    Shape("rounded-rectangle", "Rounded rectangle", True, (24, 32), (16, 20), lambda w,h: rect(w,h,min(4,w/2,h/2))),
    Shape("pill", "Pill", True, (20, 8), (10, 4), lambda w,h: rect(w,h,min(w,h)/2)),
    Shape("triangle", "Triangle", True, (20, 20), (8, 8), lambda w,h: path(f"M {n(w/2)} 0 L {n(w)} {n(h)} L 0 {n(h)} Z")),
    Shape("right-triangle", "Right triangle", True, (20, 20), (8, 8), lambda w,h: path(f"M 0 0 L {n(w)} {n(h)} L 0 {n(h)} Z")),
    Shape("diamond", "Diamond", True, (20, 20), (8, 8), lambda w,h: path(f"M {n(w/2)} 0 L {n(w)} {n(h/2)} L {n(w/2)} {n(h)} L 0 {n(h/2)} Z")),
    Shape("gable", "Gable", True, (14, 20), (8, 12), gable),
    Shape("twin-gable", "Twin gable", True, (40, 32), (16, 12), twin_gable),
    Shape("sloped-box", "Sloped box", True, (24, 18), (16, 14), sloped_box),
    Shape("trapezoid", "Trapezoid", True, (24, 12), (16, 8), trapezoid),
    Shape("flared-horn", "Flared horn", True, (24, 16), (24, 16), flared_horn),
    Shape("cut-corner-box", "Cut-corner box", True, (20, 20), (12, 12), lambda w,h: path(f"M 0 {n(min(w,h)/2)} L {n(min(w,h)/2)} 0 L {n(w)} 0 L {n(w)} {n(h)} L 0 {n(h)} Z")),
    Shape("hexagon", "Hexagon", True, (24, 16), (16, 12), hexagon),
    Shape("star", "Star", True, (20, 20), (16, 16), star),
    Shape("dome", "Dome", True, (20, 10), (10, 5), lambda w,h: path(f"M 0 {n(h)} A {n(w/2)} {n(h)} 0 0 1 {n(w)} {n(h)} Z")),
    Shape("cloud", "Cloud", True, (24, 14), (16, 10), cloud),
    Shape("scalloped-oval", "Scalloped oval", True, (20, 20), (16, 16), scalloped_oval),
    Shape("lens", "Lens", True, (20, 12), (12, 7), lens),
    Shape("lobed-drop", "Lobed drop", True, (20, 24), (12, 16), lobed_drop),
    Shape("stepped-cog", "Stepped cog", True, (20, 20), (12, 12), stepped_cog),
    Shape("twin-lobed-drop", "Twin-lobed drop", True, (20, 20), (12, 12), twin_lobed_drop),
    Shape("lightning-bolt", "Lightning bolt", True, (20, 24), (20, 24), lightning_bolt),
    Shape("puzzle-piece", "Puzzle piece", True, (20, 20), (20, 20), puzzle_piece),
    Shape("phone-handset-outline", "Phone handset outline", True, (36, 36), (36, 36), phone_handset_outline),
    Shape("quarter-circle", "Quarter circle", True, (20, 20), (8, 8), lambda w,h: path(f"M 0 {n(h)} L 0 0 A {n(w)} {n(h)} 0 0 1 {n(w)} {n(h)} Z")),
    Shape("ring", "Ring", True, (20, 20), (8, 8), ring),
    Shape("dot", "Dot", False, (4, 4), (4, 4), lambda w,h: path(f"M {n(w/2)} {n(h/2)} L {n(w/2)} {n(h/2)}")),
    Shape("line", "Line", False, (20, 2), (8, 1), lambda w,h: path(f"M 0 {n(h/2)} L {n(w)} {n(h/2)}")),
    Shape("diagonal-line", "Diagonal line", False, (20, 20), (8, 8), lambda w,h: path(f"M 0 {n(h)} L {n(w)} 0")),
    Shape("curve", "Curve", False, (20, 12), (10, 6), lambda w,h: path(f"M 0 {n(h)} Q {n(w/2)} {n(-h)} {n(w)} {n(h)}")),
    Shape("s-curve", "S-curve", False, (20, 20), (8, 8), lambda w,h: path(f"M 0 {n(h)} C {n(w/2)} {n(h)} {n(w/2)} 0 {n(w)} 0")),
    Shape("s-bend", "S-bend", False, (20, 20), (12, 12), s_bend),
    Shape("arc", "Arc", False, (20, 10), (10, 5), lambda w,h: path(f"M 0 {n(h)} A {n(w/2)} {n(h)} 0 0 1 {n(w)} {n(h)}")),
    Shape("quarter-arc", "Quarter arc", False, (20, 20), (8, 8), lambda w,h: path(f"M 0 0 A {n(w)} {n(h)} 0 0 1 {n(w)} {n(h)}")),
    Shape("bulb-outline", "Bulb outline", False, (24, 32), (12, 16), bulb_outline),
    Shape("open-rectangle", "Open rectangle", False, (20, 20), (8, 10), lambda w,h: path(f"M 0 {n(h)} L 0 0 L {n(w)} 0 L {n(w)} {n(h)}")),
    Shape("arch", "Arch", False, (20, 20), (10, 12), arch),
    Shape("hook", "Hook", False, (8, 16), (8, 14), hook),
    Shape("faucet", "Faucet", False, (24, 20), (20, 16), faucet),
    Shape("open-end-wrench", "Open-end wrench", False, (24, 8), (20, 8), open_end_wrench),
    Shape("open-gable", "Open gable", False, (20, 20), (12, 14), open_gable),
    Shape("head-profile", "Head profile", False, (24, 32), (18, 24), head_profile),
    Shape("worker-profile", "Worker profile", False, (20, 40), (18, 40), worker_profile),
    Shape("worker-profile-solid", "Worker profile solid", False, (12, 24), (12, 24), worker_profile_solid),
    Shape("pig-outline", "Pig outline", True, (40, 22), (40, 22), pig_outline),
    Shape("broken-pig-outline", "Broken pig outline", True, (40, 22), (40, 22), broken_pig_outline),
    Shape("holding-hand", "Holding hand", False, (24, 24), (24, 24), holding_hand),
    Shape("bottle-outline", "Bottle outline", True, (14, 20), (14, 20), bottle_outline),
    Shape("transfer-hand", "Transfer hand", False, (20, 12), (20, 12), transfer_hand),
    Shape("radial-ticks", "Radial ticks", False, (20, 20), (12, 12), radial_ticks),
    Shape("open-twin-gable", "Open twin gable", False, (40, 32), (16, 12), open_twin_gable),
    Shape("spiral", "Spiral", False, (22, 20), (16, 14), spiral),
    Shape("gapped-rounded-rectangle", "Gapped rounded rectangle", False, (24, 32), (16, 20), gapped_rounded_rectangle),
    Shape("corner-gapped-rounded-rectangle", "Corner-gapped rounded rectangle", False, (28, 20), (28, 20), corner_gapped_rounded_rectangle),
    Shape("open-shell", "Open shell", False, (40, 32), (32, 24), open_shell),
    Shape("oyster-shell", "Oyster shell", False, (40, 32), (40, 32), oyster_shell),
    Shape("side-gapped-rounded-rectangle", "Side-gapped rounded rectangle", False, (20, 32), (18, 32), side_gapped_rounded_rectangle),
    Shape("shark-fin", "Shark fin", False, (20, 24), (20, 24), shark_fin),
    Shape("wave-line", "Wave line", False, (40, 8), (32, 8), wave_line),
    Shape("gripping-hand", "Gripping hand", False, (24, 20), (24, 20), gripping_hand),
    Shape("gapped-eye", "Gapped eye", False, (40, 28), (40, 28), gapped_eye),
]

BY_ID = {shape.id: shape for shape in SHAPES}


def get_shape(shape_id: str) -> Shape:
    try:
        return BY_ID[shape_id]
    except KeyError as exc:
        raise ValueError(f"shapeId {shape_id!r} is not in the atomic catalog") from exc
