"""Election result: two candidate busts beside a vertical axis, each with a horizontal result bar.

Symbol plan: one bust definition used twice (series step 24 down): a circle head (r2)
and open half-ellipse shoulders (rx5, ry4) whose apex is exactly 8 below the head on
centerlines (4 units of ink), per the shared human reference (user.svg). The axis is one
vertical line the full height; each bar is an open outline hanging off the axis with a
square right end (r2 corners), 8 tall, aligned with its bust. The first bar is longer.
Lucide construction: 'bar-chart-horizontal' axis and bars; 'user' bust from user.svg.
Keyshape VRECT_L: centerline x 8..40 (shoulders, long bar end), y 4..44 (head, shoulders/axis).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ca129290-34cc-4ef3-b197-f88a3f462cd3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__candidate-bar-chart/20260926T034135Z-thuan-mac/reference/election result_ca129290-34cc-4ef3-b197-f88a3f462cd3.svg"
AUTHOR = "claude-opus-5-5"


class CandidateBarChart(Solo48):
    icon_id = "candidate-bar-chart"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "civic/election"
    aliases = ("election result", "poll result", "candidate ranking")
    keywords = ("election", "result", "candidates", "poll", "votes", "chart", "bar chart", "ranking")

    def build(self) -> None:
        bx, head_r, sh_rx, sh_ry = 13, 2, 5, 4
        axis_x, bar_h, cap = 27, 8, 2
        rows = (  # (head top y, bar top y, bar end x)
            (4, 8, 40),
            (28, 30, 35),
        )
        stops = [4] + [y for _, t, _ in rows for y in (t, t + bar_h)] + [44]
        axis = [f"axis-{k}" for k in range(len(stops) - 1)]
        for k, name in enumerate(axis):
            self.add_line(name, (axis_x, stops[k]), (axis_x, stops[k + 1]))
        self.add_contour("axis", *axis)
        for i, (top, bar_top, bar_end) in enumerate(rows, start=1):
            hy = top + head_r
            pts = [(bx - head_r, hy), (bx, hy - head_r), (bx + head_r, hy), (bx, hy + head_r)]
            names = [f"head{i}-{q}" for q in ("nw", "ne", "se", "sw")]
            for k, name in enumerate(names):
                self.add_arc(name, pts[k], pts[(k + 1) % 4], radius_x=head_r)
            self.add_contour(f"head{i}", *names, closed=True)
            apex_y = hy + head_r + 8
            base_y = apex_y + sh_ry
            self.add_arc(f"shoulders{i}-l", (bx - sh_rx, base_y), (bx, apex_y), radius_x=sh_rx, radius_y=sh_ry)
            self.add_arc(f"shoulders{i}-r", (bx, apex_y), (bx + sh_rx, base_y), radius_x=sh_rx, radius_y=sh_ry)
            self.add_contour(f"shoulders{i}", f"shoulders{i}-l", f"shoulders{i}-r")
            self.mark_human_figure(f"candidate{i}", head=f"head{i}", torso=f"shoulders{i}-r",
                                   torso_junction="start")
            # bar hanging off the axis
            bb = bar_top + bar_h
            self.add_line(f"bar{i}-top", (axis_x, bar_top), (bar_end - cap, bar_top))
            self.add_arc(f"bar{i}-corner-t", (bar_end - cap, bar_top), (bar_end, bar_top + cap), radius_x=cap)
            self.add_line(f"bar{i}-end", (bar_end, bar_top + cap), (bar_end, bb - cap))
            self.add_arc(f"bar{i}-corner-b", (bar_end, bb - cap), (bar_end - cap, bb), radius_x=cap)
            self.add_line(f"bar{i}-bottom", (bar_end - cap, bb), (axis_x, bb))
            self.add_contour(f"bar{i}", f"bar{i}-top", f"bar{i}-corner-t", f"bar{i}-end",
                             f"bar{i}-corner-b", f"bar{i}-bottom")
            self.relate("connect", "axis", f"bar{i}")
