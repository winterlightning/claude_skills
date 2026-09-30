"""gantt-chart-with-progress-dividers (redraw of the new-pipeline traced SVG, run 20260930-1303).

Plan: a Gantt chart read as staggered hollow task bars, each split by one
vertical progress divider that joins its top and bottom edges.
- bar: one repeat definition, a rounded rectangle (corner radius 2, Lucide
  `rect rx=2` construction) 28 wide and 12 tall on centerlines, so the
  interior is 8 tall; its top and bottom edges are split at the divider so the
  divider shares both endpoints (declared with relate("connect")).
- rows: two bars, staggered from upper left to lower right by 12, with a
  row gap of 8 on centerlines (4 ink): bar 1 x 4-32 y 8-20, bar 2 x 16-44
  y 28-40. Progress advances down the chart: divider at x 14 on bar 1
  (early, left cell 10 wide) and x 34 on bar 2 (late, right cell 10 wide),
  following the generated image (left divider on top, right divider below).
- keyshape: HRECT_L (centerline box (4,8)-(44,40)), not the suggested
  HRECT_M. Two 12-tall bars and an 8 gap need 32 of height; HRECT_M has 28.
  All four extremes sit exactly on the box.
- dropped: the third (middle) task bar. Three separate hollow bars need
  3 x 10 (6-unit hole + stroke) + 2 x 8 (row gap) = 46 of height, and the
  tallest SOLO48 box is 40. Other layouts tried: bars sharing edges turn into
  a brick stair with every divider pinned to the middle; three single-stroke
  bars with crossing ticks passed validation but read as a "sliders" control.
  Two hollow bars keep the hollow bars and dividers that identify the chart.

Metric issues:
- fixed: stroke-width (info; drawn at stroke 4), keyshape-short-axis (moved
  to HRECT_L, where the drawing touches all four box edges with no stretch),
  all six clearance errors (e0/e2, e0/e3, e1/e2, e2/e4, e2/e5, e3/e5: the
  traced bar edges were 3.2-4.6 apart; rows are now 8 apart and every divider
  is a connected part of its bar), and all six hole errors at [6.8,15.0],
  [13.0,15.0], [15.6,24.0], [26.2,24.0], [24.9,32.9], [40.0,32.8] (trace
  holes 1.6-1.8 wide; the smallest cell is now 10 x 12 on centerlines, a
  6 x 8 hole).
- not fixed: none. The only compromise is the dropped third row, required by
  the 46 > 40 height budget.
Lucide: `rect` with rx=2 for the bar corners; Lucide chart-gantt (single
stroke bars) was tried and rejected because it reads as sliders.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = "c6f9a1df-2dbc-4ed6-a75b-2dbdfa9e9de1"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1303-gantt-chart-with-progress-dividers/gantt-chart-with-progress-dividers_raw.svg"
AUTHOR = "claude-opus-5-5"

BAR_W, BAR_H, RADIUS = 28, 12, 2
# (left x, top y, divider x) for each task bar, upper left to lower right
BARS = ((4, 8, 14), (16, 28, 34))


class GanttChartWithProgressDividersRedraw(Solo48):
    icon_id = "gantt-chart-with-progress-dividers-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/chart"
    aliases = ("gantt-chart", "project-timeline", "task-schedule")
    keywords = ("gantt", "chart", "timeline", "schedule", "project", "tasks", "progress", "planning")

    def build(self) -> None:
        r = RADIUS
        for index, (x0, y0, d) in enumerate(BARS, 1):
            x1, y1 = x0 + BAR_W, y0 + BAR_H
            p = f"bar{index}"
            self.add_line(f"{p}-top-done", (x0 + r, y0), (d, y0))
            self.add_line(f"{p}-top-left", (d, y0), (x1 - r, y0))
            self.add_arc(f"{p}-corner-tr", (x1 - r, y0), (x1, y0 + r), radius_x=r)
            self.add_line(f"{p}-right", (x1, y0 + r), (x1, y1 - r))
            self.add_arc(f"{p}-corner-br", (x1, y1 - r), (x1 - r, y1), radius_x=r)
            self.add_line(f"{p}-bottom-left", (x1 - r, y1), (d, y1))
            self.add_line(f"{p}-bottom-done", (d, y1), (x0 + r, y1))
            self.add_arc(f"{p}-corner-bl", (x0 + r, y1), (x0, y1 - r), radius_x=r)
            self.add_line(f"{p}-left", (x0, y1 - r), (x0, y0 + r))
            self.add_arc(f"{p}-corner-tl", (x0, y0 + r), (x0 + r, y0), radius_x=r)
            self.add_contour(
                p,
                *(f"{p}-{k}" for k in (
                    "top-done", "top-left", "corner-tr", "right", "corner-br",
                    "bottom-left", "bottom-done", "corner-bl", "left", "corner-tl",
                )),
                closed=True,
            )
            # The progress divider joins the split top and bottom edges.
            self.add_line(f"{p}-divider", (d, y0), (d, y1))
            for edge in ("top-done", "top-left", "bottom-left", "bottom-done"):
                self.relate("connect", f"{p}-{edge}", f"{p}-divider")


if __name__ == "__main__":
    from pathlib import Path

    import cairosvg

    icon = GanttChartWithProgressDividersRedraw()
    print(icon.validate_icon().describe())
    here = Path(__file__).resolve().parent
    stem = "gantt-chart-with-progress-dividers_redraw"
    svg = icon.to_svg()
    (here / f"{stem}.svg").write_text(svg, encoding="utf-8")
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(here / f"{stem}.png"),
                     output_width=512, output_height=512, background_color="white")
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(here / f"{stem}-48.png"),
                     output_width=48, output_height=48, background_color="white")
