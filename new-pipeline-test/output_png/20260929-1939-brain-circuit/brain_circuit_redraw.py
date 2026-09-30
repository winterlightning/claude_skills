"""brain-circuit (redraw of the new-pipeline traced SVG).

Plan: a frontal two-hemisphere brain on CIRCLE (centerline radius 20 about
(24,24)), mirrored about x=24 and y=24, with two right-angle circuit traces
arranged point-symmetrically about the centre, as in the generated image.
- outline: one closed contour of six r10 arcs, three lobes per hemisphere.
  Every lobe centre sits 10 from (24,24), so each lobe apex lands exactly on
  the radius-20 keyshape edge: top lobes (18,16)/(30,16), side lobes
  (14,24)/(34,24), bottom lobes (18,32)/(30,32).  Neighbouring lobes meet on
  integer grid points: the top cleft (24,8), notches (8,16), (8,32),
  (40,16), (40,32) and the bottom cleft (24,40).
- left trace: terminal at (16,23), drops from (16,25) to (16,31), then runs
  right to (23,31).
- right trace: the left trace rotated 180 degrees about (24,24): from (25,17)
  right to (32,17), down to (32,23), into the terminal at (32,25).
  The corners stop one unit short of the exact-8 spots next to the notches
  (the sampled distance check cannot certify an exact 8).
- terminals: r2 rings sharing the trace endpoint (declared connections).
Construction reference: lucide/brain-circuit (lobed outline, straight
circuit runs ending in round terminals); coordinates rebuilt on the 48 grid,
the trace supplied only the subject and the layout.

Metric issues:
- stroke-width (info, 2.89 after fit): redrawn at stroke 4 with every gap
  budgeted at 8 on centerlines.
- stroke-count (warn, 9 strokes, budget 6): fixed, 5 strokes (outline, two
  traces, two terminals).
- clearance e0/e6, e0/e7, e1/e4, e1/e8, e6/e8 (midline fissures vs traces and
  terminals, 4.2-7.6): fixed by dropping the two midline fissure strokes; the
  top and bottom clefts of the outline keep the two-hemisphere read, and the
  trace ends (25,17)/(23,31) sit 9 from them.
- clearance e2/e4, e2/e5, e3/e7, e3/e8 (outline vs terminals and traces,
  4.2-7.1): fixed; every trace point and terminal is 8+ from the outline.
- clearance e4/e6 (terminal vs trace, 6.15): fixed; each terminal touches
  only its own trace end (declared) and is 8.8+ from the other trace.
- loose-join e0/e3, e2/e3 (0.42 gaps at the bottom cleft): fixed; the outline
  is one closed contour whose arcs share exact integer endpoints.
- hole (slivers 1.0/1.02 wide at [14.8,17.9] and [33.2,29.9]): fixed; no
  stroke crosses or grazes another, so no slivers are enclosed.  The r2
  terminal rings are complete 4x4 circles (small-circle hole exception).
Not kept: the hollow open-circle terminals and the two midline fissures.
Inside a radius-20 brain the free centerline area is only about 22x20.  A
valid variant with r3 rings (terminals (16,24)/(32,24)) was built and
rendered: its 2-unit holes are barely visible and at 48 px the ring+trace
pairs read as the digits "2 3", so the terminals are solid r2 pads (Lucide's
dot terminals), as in the approved 20260928 redraw.  The fissures cannot
share the 8-unit budget with the traces crossing the midline region.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "994c360d-a3ef-411d-83b6-1227713cc09e"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1939-brain-circuit/brain-circuit_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24             # canvas centre
LOBE_R = 10        # lobe centres sit 10 from C, so apexes reach radius 20
TERMINAL_R = 2
# Outline walked clockwise from the top cleft: lobe end points.
OUTLINE = ((24, 8), (40, 16), (40, 32), (24, 40), (8, 32), (8, 16))
TERMINAL = (16, 23)                         # left terminal centre
TRACE = ((16, 25), (16, 31), (23, 31))      # left trace, terminal -> centre


def rot(p):
    """Point reflection through the canvas centre."""
    return (2 * C - p[0], 2 * C - p[1])


class BrainCircuitRedraw(Solo48):
    icon_id = "brain-circuit-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ("ai-brain", "neural-circuit")
    keywords = ("brain", "circuit", "ai", "artificial intelligence", "neural",
                "machine learning", "mind", "technology")

    def _ring(self, name, centre, join):
        # Two half arcs split at the join point and its opposite.
        opposite = (2 * centre[0] - join[0], 2 * centre[1] - join[1])
        self.add_arc(f"{name}-a", join, opposite, radius_x=TERMINAL_R)
        self.add_arc(f"{name}-b", opposite, join, radius_x=TERMINAL_R)
        self.add_contour(name, f"{name}-a", f"{name}-b", closed=True)

    def build(self) -> None:
        ids = []
        for i, start in enumerate(OUTLINE):
            end = OUTLINE[(i + 1) % len(OUTLINE)]
            self.add_arc(f"lobe-{i}", start, end, radius_x=LOBE_R)
            ids.append(f"lobe-{i}")
        self.add_contour("outline", *ids, closed=True)

        for side, flip in (("left", lambda p: p), ("right", rot)):
            self._ring(f"terminal-{side}", flip(TERMINAL), flip(TRACE[0]))
            self.add_polyline(f"trace-{side}", *(flip(p) for p in TRACE))
            self.relate("connect", f"trace-{side}", f"terminal-{side}")
