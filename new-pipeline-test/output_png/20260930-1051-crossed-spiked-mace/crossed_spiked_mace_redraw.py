"""crossed-spiked-mace (redraw of the new-pipeline traced SVG).

Plan: two spiked maces crossed in an X on SQUARE (centerline box
(6,6)-(42,42)), the keyshape the metrics suggested; the pair is mirror-
symmetric about x=24.
- head: one closed contour per mace, a radius-5 ring (inner hole 6) with
  three triangular spikes merged into its perimeter, as in the generated
  image. Each spike's base is a 3-4-5 lattice pair on the ring ((-4,-3) and
  (-3,-4) for the upper-left one), so the base is centred on the 45-degree
  diagonal and the apex sits on that diagonal 6 out from the centre. Spikes
  point away from the handle: up-left, up-right and down-left for the left
  mace (mirrored for the right one). Centres (12,12) and (36,12) put the outer
  apexes exactly on the box: (6,6), (42,6), (6,18), (42,18).
- handles: one 45-degree line per mace from the ring's lattice point
  centre+(3,4) (mirrored (-3,4)) to (41,42) / (7,42), the bottom extreme.
  They cross at the lattice point (24,25), where both are split so the four
  halves share that point and are related with `connect`.
Dropped: the image's over/under break in the rear handle. The break must
leave 8 on centerlines either side of the front handle, which left the rear
handle's upper piece (4.2 long) hidden in the ring ink at 48 px and the rear
mace reading as a detached head; steepening the handles only grew it to 6.4
and the pair still read as broken. A plain X keeps both maces whole.
Lucide `swords`/`sword` gave the crossed-X construction; the ring + merged
spikes head follows the generated image, reduced to three spikes.

Metric issues (crossed-spiked-mace_metrics.json):
- stroke-width (info, trace 2.37): redrawn at stroke 4 and every gap
  budgeted for 4.
- keyshape-short-axis (warn, y filled 85%): the outer spike apexes now reach
  y=6 and the handle ends y=42, so SQUARE is met on all four sides.
- clearance e0/e1, e0/e2, e0/e4, e1/e2, e1/e4, e2/e4 (errors, 1.6-5.5 apart):
  these came from the trace outlining each handle as two parallel edges that
  run within 2 of each other at the crossing. Each handle is now one
  centerline and the two meet at a declared shared point, so no unrelated
  parts pass closer than 8 (heads to the other handle 12.7, head to head 12).
- clearance e2/e3 (error, 6.39) and loose-join e2/e3 (info, 0.53 short): the
  handle now starts exactly on the ring's lattice point, shares it with the
  two ring arcs and is related with `connect`.
- hole x2 (errors, 4.56 and 4.44 wide): each ring is radius 5 on centerlines,
  an inner hole of 6, the spikes only widening it.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "79c8a226-7026-5ab4-a2e4-203abe5e9998"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1051-crossed-spiked-mace/crossed-spiked-mace_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
R = 5                        # ring radius: inner hole 2*R - 4 = 6
HEAD = (12, 12)              # left head centre; right head mirrors about AXIS
SPIKE = 6                    # apex offset along each diagonal
JOINT = (3, 4)               # handle leaves the ring here (3-4-5 lattice point)
HANDLE_END = (41, 42)        # left mace's handle end, on y = x + 1
CROSS = (24, 25)             # y = x + 1 meets x + y = 49 on the lattice


def _mirror(point):
    return (2 * AXIS - point[0], point[1])


class CrossedSpikedMaceRedraw(Solo48):
    icon_id = "crossed-spiked-mace-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weapon"
    aliases = ("crossed maces", "morning star", "spiked club", "flail")
    keywords = ("mace", "weapon", "medieval", "battle", "combat", "knight",
                "war", "spike", "crossed", "rpg", "game")

    def _head(self, name, mirror):
        cx, cy = HEAD

        def p(dx, dy):
            point = (cx + dx, cy + dy)
            return _mirror(point) if mirror else point

        sweep = not mirror
        # Ring points clockwise from the handle joint; each spike replaces the
        # short arc between two lattice points centred on a diagonal.
        joint = p(*JOINT)
        self.add_arc(f"{name}-arc-1", joint, p(-3, 4), radius_x=R, sweep=sweep)
        self.add_line(f"{name}-spike-1a", p(-3, 4), p(-SPIKE, SPIKE))
        self.add_line(f"{name}-spike-1b", p(-SPIKE, SPIKE), p(-4, 3))
        self.add_arc(f"{name}-arc-2", p(-4, 3), p(-4, -3), radius_x=R, sweep=sweep)
        self.add_line(f"{name}-spike-2a", p(-4, -3), p(-SPIKE, -SPIKE))
        self.add_line(f"{name}-spike-2b", p(-SPIKE, -SPIKE), p(-3, -4))
        self.add_arc(f"{name}-arc-3", p(-3, -4), p(3, -4), radius_x=R, sweep=sweep)
        self.add_line(f"{name}-spike-3a", p(3, -4), p(SPIKE, -SPIKE))
        self.add_line(f"{name}-spike-3b", p(SPIKE, -SPIKE), p(4, -3))
        self.add_arc(f"{name}-arc-4", p(4, -3), joint, radius_x=R, sweep=sweep)
        self.add_contour(
            name,
            f"{name}-arc-1", f"{name}-spike-1a", f"{name}-spike-1b",
            f"{name}-arc-2", f"{name}-spike-2a", f"{name}-spike-2b",
            f"{name}-arc-3", f"{name}-spike-3a", f"{name}-spike-3b",
            f"{name}-arc-4",
            closed=True,
        )
        return joint

    def build(self) -> None:
        front_joint = self._head("head-left", mirror=False)
        rear_joint = self._head("head-right", mirror=True)

        # Both handles run at 45 degrees and are split where they cross, so
        # the four halves share the lattice point CROSS.
        self.add_line("handle-left-upper", front_joint, CROSS)
        self.add_line("handle-left-lower", CROSS, HANDLE_END)
        self.add_line("handle-right-upper", rear_joint, CROSS)
        self.add_line("handle-right-lower", CROSS, _mirror(HANDLE_END))
        for side in ("left", "right"):
            self.relate("connect", f"handle-{side}-upper", f"head-{side}-arc-1")
            self.relate("connect", f"handle-{side}-upper", f"head-{side}-arc-4")
        self.relate("connect", "handle-left-upper", "handle-left-lower",
                    "handle-right-upper", "handle-right-lower")
