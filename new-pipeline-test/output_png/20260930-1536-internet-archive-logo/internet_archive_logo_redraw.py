"""internet-archive-logo (redraw of the new-pipeline traced SVG).

Plan: the Internet Archive temple, mirrored about x=24 on SQUARE
(centerline box (6,6)-(42,42)).
- pediment: one closed triangle, apex (24,6), eaves (6,18) / (42,18); its
  bottom edge doubles as the entablature and is split at every column top.
- columns: four equal vertical lines at x = 9, 19, 29, 39 (pitch 10, so
  each bay's inner opening is 6 ink wide), hanging from the entablature
  (y=18) to the base (y=42) as shared-endpoint T joins.
- base: one horizontal line (6,42)-(42,42), split at every column foot.
Traced shape: 20260930-1536-internet-archive-logo/internet-archive-logo_raw.svg.

Metric issues fixed:
- clearance e0/e1 (roof vs. entablature 3.59): the pediment is 12 tall
  instead of ~9 and closed as one triangle contour; its opening is ~6.9
  inscribed ink, so the fitted-raster hole (4.2 < 6) is fixed too.
- clearance e0-e2..e5 and e2..e5-e6 (columns 4 from the entablature and
  base): the columns now connect to both as declared T joins, the way
  the logo's columns carry the roof, instead of floating 4 units away.
- clearance e1/e2, e1/e5 (roof slope vs. outer columns 5.5): the outer
  columns join the entablature at x=9 / x=39, under the roof edge.
- stroke-count (7 > 6): roof + entablature is one contour, 6 strokes.
- stroke-width (info): drawn at stroke 4 with gaps budgeted for it.
Not fixed: narrow-join at the eaves (the triangle meets its base at
~34 deg). That angle is what a low pediment is; a steeper roof would eat
the column height, so the round join is kept as a deliberate corner.
No useful Lucide match: lucide/landmark is the same temple idea (roof,
columns, base) and informed the connected construction; its coordinates
were not used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bee109f7-7025-4eb4-9ddc-33b7df1410c4"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1536-internet-archive-logo/"
    "internet-archive-logo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, RIGHT = 6, 42      # eave / base ends
APEX_Y = 6
EAVE_Y = 18              # entablature and column tops
BASE_Y = 42
PITCH = 10               # column spacing
COLUMNS = tuple(AXIS + PITCH * k // 2 for k in (-3, -1, 1, 3))  # 9 19 29 39


class InternetArchiveLogoRedraw(Solo48):
    icon_id = "internet-archive-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("internet archive", "archive.org")
    keywords = ("internet archive", "archive", "library", "temple", "columns",
                "wayback machine", "logo", "brand")

    def build(self) -> None:
        # Pediment: right roof slope, entablature right-to-left split at each
        # column top, then the left roof slope back to the apex.
        self.add_line("roof-r", (AXIS, APEX_Y), (RIGHT, EAVE_Y))
        stops = [RIGHT, *reversed(COLUMNS), LEFT]
        beam = []
        for i, (x0, x1) in enumerate(zip(stops, stops[1:])):
            beam.append(f"beam-{i}")
            self.add_line(beam[-1], (x0, EAVE_Y), (x1, EAVE_Y))
        self.add_line("roof-l", (LEFT, EAVE_Y), (AXIS, APEX_Y))
        self.add_contour("pediment", "roof-r", *beam, "roof-l", closed=True)

        stops = [LEFT, *COLUMNS, RIGHT]
        base = []
        for i, (x0, x1) in enumerate(zip(stops, stops[1:])):
            base.append(f"base-{i}")
            self.add_line(base[-1], (x0, BASE_Y), (x1, BASE_Y))
        self.add_contour("base", *base)

        for i, x in enumerate(COLUMNS):
            name = f"column-{i}"
            self.add_line(name, (x, EAVE_Y), (x, BASE_Y))
            # beam runs right-to-left: column i sits between beam 3-i and 4-i.
            self.relate("connect", name, f"beam-{3 - i}")
            self.relate("connect", name, f"base-{i}")
