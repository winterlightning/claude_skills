"""cloud-internet: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75d3488a-6912-4de5-b1c9-1505730ec0ac'
SOURCE_PATH = 'pictographic-primitives/internet/cloud_75d3488a-6912-4de5-b1c9-1505730ec0ac.svg'
AUTHOR = 'gpt-6'

class CloudInternet(Solo48):
    icon_id = 'cloud-internet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('cloud', 'internet', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the source cloud as a single lobed outline. A high central dome and matched lower corners preserve a soft cloud silhouette.
        # Reference: Lucide cloud original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        path('cloud',(14,40),[('C',(4,29),(8,40),(4,35)),('C',(12,19),(4,23),(7,19)),('C',(23,8),(13,12),(17,8)),('C',(36,21),(31,8),(36,13)),('C',(44,30),(41,21),(44,24)),('C',(34,40),(44,36),(40,40)),('L',(14,40))],True)
