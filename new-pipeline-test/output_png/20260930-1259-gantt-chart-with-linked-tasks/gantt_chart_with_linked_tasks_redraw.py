"""gantt-chart-with-linked-tasks (redraw of the new-pipeline traced SVG).

Plan: a Gantt chart with three hollow task bars stepping down from upper
left to lower right, each bar linked to the next by a right-angle
finish-to-start connector, as in the generated image.
- Repeat definition: every bar is the same rounded rectangle, BAR_W x BAR_H
  on centerlines, corner radius R, shifted by (STEP_X, STEP_Y) per row.
- Links: leave a bar's right edge at mid-height, run right LINK_RUN (8),
  then drop straight down into the top edge of the next bar. Each bar wall
  is split at the attachment point so link and bar share an endpoint, and
  only those pairs are declared "connect".
Keyshape: VRECT_L (centerline box (8,4)-(40,44)) instead of the suggested
HRECT_M. A hollow bar needs its top and bottom walls 8 apart on centerlines
(the exact parallel-edge MIC inside one contour; 6-tall bars were rejected),
and horizontally overlapping rows need 8 between them, so three rows cost
3 x 8 + 2 x 8 = 40 on the vertical axis. HRECT_M gives 28, HRECT_L 32 and
SQUARE 36; only VRECT_L's 40 fits. The 32 width then gives bars of 12
stepped by 10 (the link drop must sit 8 right of the bar it leaves and land
on the next bar's top, so the step is at least 8 + R).
Extremes: x=8 (bar 1 left), x=40 (bar 3 right), y=4 (bar 1 top), y=44
(bar 3 bottom).
Clearances (centerlines): row to row 8; link drop to the bar it leaves 8;
link run to the next bar's top 12; bar 2 left end to link 1 drop 10.

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- keyshape-short-axis (warn): fixed by moving to VRECT_L and touching all
  four box edges exactly (see above). The drawing is now taller than wide
  (the trace was 2.18:1 wide); that is the cost of hollow bars at stroke 4.
- clearance e0/e1 (7.49), e2/e3 (3.91), e2/e4 (3.85): fixed; the trace's
  near-touching link corners and bar walls are rebuilt as clean T-junctions
  on split bar walls, and all unconnected parts are >= 8 apart.
- holes at [19.2,19.4] and [31.8,26.7] (1.4-1.6 wide): fixed; these were
  the pinched slivers where the traced links met the bars and no longer
  exist. Each bar interior is 8 x 12 on centerlines (4 x 8 of open ink):
  it passes the build's hole gate, but is under the metric's 6-unit ink
  target, which would need 3 x 10 + 2 x 8 = 46 (more than any keyshape).
Lucide construction: `chart-gantt` / `gantt-chart` (staggered horizontal
task bars) with rounded `rect` corners from `rectangle-horizontal`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "012ac09f-44c3-417b-a7cd-1dcaf5b7540e"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1259-gantt-chart-with-linked-tasks/"
    "gantt-chart-with-linked-tasks_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LEFT, TOP = 8, 4        # bar 1 top-left corner (VRECT_L box corner)
BAR_W, BAR_H = 12, 8    # task bar on centerlines
R = 2                   # bar corner radius
STEP_X, STEP_Y = 10, 16  # per-row shift: 2-unit overlap, 8 between rows
LINK_RUN = 8            # link leaves the bar and runs right this far


class GanttChartWithLinkedTasksRedraw(Solo48):
    icon_id = "gantt-chart-with-linked-tasks-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/chart"
    aliases = ("gantt chart", "linked tasks", "task dependencies",
               "project timeline")
    keywords = ("gantt", "chart", "tasks", "dependency", "timeline",
                "schedule", "project", "planning", "roadmap", "link")

    def _bar(self, name, x0, y0, top_split=None, right_split=None):
        """Closed rounded bar, clockwise from the top-left corner's end.

        Walls are split at ``top_split`` (x on the top edge) and
        ``right_split`` (y on the right edge) so a link can share the node.
        """
        x1, y1 = x0 + BAR_W, y0 + BAR_H
        members = []

        def line(a, b):
            seg = f"{name}-{len(members) + 1}"
            self.add_line(seg, a, b)
            members.append(seg)

        def corner(a, b):
            seg = f"{name}-{len(members) + 1}"
            self.add_arc(seg, a, b, radius_x=R, sweep=True)
            members.append(seg)

        inner = [(top_split, y0)] if top_split and x0 + R < top_split < x1 - R else []
        top = [(x0 + R, y0)] + inner + [(x1 - R, y0)]
        for a, b in zip(top, top[1:]):
            line(a, b)
        corner((x1 - R, y0), (x1, y0 + R))
        right = [(x1, y0 + R)] + ([(x1, right_split)] if right_split else []) + [(x1, y1 - R)]
        for a, b in zip(right, right[1:]):
            line(a, b)
        corner((x1, y1 - R), (x1 - R, y1))
        line((x1 - R, y1), (x0 + R, y1))
        corner((x0 + R, y1), (x0, y1 - R))
        line((x0, y1 - R), (x0, y0 + R))
        corner((x0, y0 + R), (x0 + R, y0))
        self.add_contour(name, *members, closed=True)

    def build(self) -> None:
        mid = BAR_H // 2
        origins = [(LEFT + i * STEP_X, TOP + i * STEP_Y) for i in range(3)]
        drops = [x + BAR_W + LINK_RUN for x, _ in origins[:2]]  # 28, 39

        for i, (x, y) in enumerate(origins):
            self._bar(
                f"bar-{i + 1}", x, y,
                top_split=drops[i - 1] if i else None,
                right_split=y + mid if i < 2 else None,
            )

        for i, (x, y) in enumerate(origins[:2]):
            start = (x + BAR_W, y + mid)
            elbow = (drops[i], y + mid)
            end = (drops[i], origins[i + 1][1])
            self.add_polyline(f"link-{i + 1}", start, elbow, end)
            self.relate("connect", f"bar-{i + 1}", f"link-{i + 1}")
            self.relate("connect", f"link-{i + 1}", f"bar-{i + 2}")
