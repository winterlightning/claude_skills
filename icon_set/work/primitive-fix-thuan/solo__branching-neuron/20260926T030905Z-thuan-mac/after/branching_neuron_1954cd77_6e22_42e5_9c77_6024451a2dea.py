"""A neuron: a star-shaped cell body whose six points each run out and fork into dendrites.

Symbol plan: six-fold about (24,24), one arm per 60 degrees with arms pointing straight up
and down. The cell body is a concave six-point star: its points sit at radius P, joined by
inward-curving r-SIDE arcs. From each point a short stem runs out to radius F and forks
into two straight dendrites spread +-SPREAD degrees, ending on radius 20. Knots are
rounded to the grid after turning, so arms are equal to within half a unit.
Lucide construction: no neuron glyph; the concave star body follows Lucide's 'star' of
arcs, the forks its straight 'git-fork'/'network' branches.
Keyshape CIRCLE: dendrite tips reach centerline radius 19.5-20 about (24,24).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1954cd77-6e22-42e5-9c77-6024451a2dea"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__branching-neuron/20260926T030905Z-thuan-mac/reference/neurons_1954cd77-6e22-42e5-9c77-6024451a2dea.svg"
AUTHOR = "claude-opus-5-5"

P, F, TIP, SPREAD, SIDE = 11, 14, 19.9, 40, 10


def _polar(r, deg):
    a = math.radians(deg)
    return (24 + r * math.cos(a), 24 + r * math.sin(a))


def _grid(p):
    return (round(p[0]), round(p[1]))


def _tip(fork, deg):
    # walk from the fork along `deg` until radius TIP
    fx, fy = fork[0] - 24, fork[1] - 24
    dx, dy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    b = fx * dx + fy * dy
    length = -b + math.sqrt(b * b - (fx * fx + fy * fy - TIP * TIP))
    return (fork[0] + length * dx, fork[1] + length * dy)


class BranchingNeuron(Solo48):
    icon_id = "branching-neuron"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/biology"
    aliases = ("neurons", "neuron", "nerve-cell")
    keywords = ("neuron", "nerve", "brain", "cell", "dendrite", "synapse", "neuroscience", "biology")

    def build(self) -> None:
        arms = [-90 + 60 * i for i in range(6)]
        points = [_grid(_polar(P, a)) for a in arms]
        for i, a in enumerate(arms):
            self.add_arc(f"body-{i + 1}", points[i], points[(i + 1) % 6], radius_x=SIDE, sweep=False)
            fork = _grid(_polar(F, a))
            self.add_line(f"stem-{i + 1}", points[i], fork)
            self.add_line(f"dendrite-{i + 1}a", fork, _grid(_tip(fork, a - SPREAD)))
            self.add_line(f"dendrite-{i + 1}b", fork, _grid(_tip(fork, a + SPREAD)))
            self.relate("connect", "body", f"stem-{i + 1}")
            self.relate("connect", f"stem-{i + 1}", f"dendrite-{i + 1}a")
            self.relate("connect", f"stem-{i + 1}", f"dendrite-{i + 1}b")
            self.relate("connect", f"dendrite-{i + 1}a", f"dendrite-{i + 1}b")
        self.add_contour("body", *[f"body-{i + 1}" for i in range(6)], closed=True)
