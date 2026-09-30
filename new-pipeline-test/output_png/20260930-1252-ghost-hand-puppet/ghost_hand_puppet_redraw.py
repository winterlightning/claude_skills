"""ghost-hand-puppet (redraw of the new-pipeline traced SVG).

Plan: a ghost glove puppet on CIRCLE (centerline radius 20 about (24,24)),
mirrored across x=24.
- body: one closed contour. A dome (arc centre (24,17), r 13, apex (24,4))
  drops into straight walls at x=11 / x=37; each wall carries a mitten lobe
  (horizontal edges y=24 and y=32, 8 apart, closed by a r 4 cap centred at
  (9,28) / (39,28), tips at x=5 / x=43), then continues down to a straight
  hem at y=39 that stands in for the open cuff.
- eyes: two short vertical strokes (x=20 / x=28, y 19..22) that read as the
  hollow oval eyes at 48 px; 8 apart and 9 from each wall.
- wrist: one stroke from the hem centre (24,39) down to (24,44), split into the
  hem so it shares an endpoint and is declared connected.
Extremes: dome apex (24,4) and wrist end (24,44) sit on radius 20; the lobe
tips (radius 19.5) and hem corners (radius 19.8) stay inside.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 and every gap re-budgeted for it.
- keyshape-short-axis (VRECT_M, y 97%): not applicable after the keyshape
  change below; the dome apex and wrist end now reach the CIRCLE radius.
- clearance e3/e4 (eyes 3.0 apart): eyes are 8 apart on centerlines.
- clearance e0/e3, e0/e4 (eyes 2.3 from the head walls): the body is widened
  so each eye is 9 from its wall and >= 9.2 from the dome and lobe roots
  (at exactly 8 the curved body contour came back review).
- clearance e0/e2, e1/e2 (cuff ellipse 4.1 from the hem and the wrist): the
  two-arc cuff ellipse is replaced by a single hem line, so there is no
  second cuff arc to crowd the hem or the wrist.
- hole at (23.9, 8.2), 3.1 wide: this was the sliver between the eye tops
  and the dome; the eyes now sit 8+ below the dome and inside the body, so no
  enclosed pocket is formed besides the body interior itself.
Deliberate changes: keyshape CIRCLE instead of the suggested VRECT_M. Two
eyes 8 apart with 8 to each wall force a 24-26-wide head, which in VRECT_M's 28
(or VRECT_L's 32) leaves the mitten lobes 1-3 units of reach and the puppet
reads as a plain rounded box; CIRCLE's 40-wide middle gives the lobes 6 units
while the dome and wrist still use the full height. The hollow oval eyes are
strokes (a hollow eye needs r >= 5 for a 6-unit hole). The cuff ellipse is a
hem line (an ellipse needs 8 between its arcs, which the height cannot spare).
Lucide: ghost informed the dome-over-walls construction and stroke eyes;
hand-puppet style lobes are original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a6b4c9d3-7980-446c-ac11-08ac236338e8"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1252-ghost-hand-puppet/ghost-hand-puppet_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 24                    # mirror axis
TOP = 4                    # dome apex
HEAD_R = 13                # dome radius -> walls at CX -/+ 13
DOME_Y = TOP + HEAD_R      # 17, dome centre / wall top
WL, WR = CX - HEAD_R, CX + HEAD_R   # 11, 37
ARM_Y0, ARM_Y1 = 24, 32    # lobe edges (8 apart)
CAP_R = (ARM_Y1 - ARM_Y0) // 2      # 4
REACH = 2                  # straight lobe edge before the cap
HEM_Y = 39
WRIST_Y = 44
EYE_DX, EYE_Y0, EYE_Y1 = 4, 19, 22


class GhostHandPuppetRedraw(Solo48):
    icon_id = "ghost-hand-puppet-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/toys"
    aliases = ("ghost-puppet", "hand-puppet-ghost", "glove-puppet")
    keywords = ("ghost", "puppet", "hand puppet", "glove", "halloween", "toy", "spooky", "theater")

    def build(self) -> None:
        lx, rx = WL - REACH, WR + REACH   # 9, 39: cap centres
        members = []

        def seg(kind, start, end, **arc):
            name = f"body-{len(members) + 1}"
            if kind == "L":
                self.add_line(name, start, end)
            else:
                self.add_arc(name, start, end, **arc)
            members.append(name)
            return name

        seg("A", (WL, DOME_Y), (WR, DOME_Y), radius_x=HEAD_R, sweep=True)
        seg("L", (WR, DOME_Y), (WR, ARM_Y0))
        seg("L", (WR, ARM_Y0), (rx, ARM_Y0))
        seg("A", (rx, ARM_Y0), (rx, ARM_Y1), radius_x=CAP_R, sweep=True)
        seg("L", (rx, ARM_Y1), (WR, ARM_Y1))
        seg("L", (WR, ARM_Y1), (WR, HEM_Y))
        seg("L", (WR, HEM_Y), (CX, HEM_Y))
        hem_left = seg("L", (CX, HEM_Y), (WL, HEM_Y))
        seg("L", (WL, HEM_Y), (WL, ARM_Y1))
        seg("L", (WL, ARM_Y1), (lx, ARM_Y1))
        seg("A", (lx, ARM_Y1), (lx, ARM_Y0), radius_x=CAP_R, sweep=True)
        seg("L", (lx, ARM_Y0), (WL, ARM_Y0))
        seg("L", (WL, ARM_Y0), (WL, DOME_Y))
        self.add_contour("body", *members, closed=True)

        self.add_line("wrist", (CX, HEM_Y), (CX, WRIST_Y))
        self.relate("connect", "wrist", hem_left)

        self.add_line("eye-left", (CX - EYE_DX, EYE_Y0), (CX - EYE_DX, EYE_Y1))
        self.add_line("eye-right", (CX + EYE_DX, EYE_Y0), (CX + EYE_DX, EYE_Y1))
