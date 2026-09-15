"""wave-e3459233: Two matching wave strokes; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3459233-4acf-5488-8964-ea188d1b0ae9'
SOURCE_PATH = 'icons-json/wayfinding/wave_e3459233-4acf-5488-8964-ea188d1b0ae9.json'
AUTHOR = 'gpt-6'

class WaveE3459233(Solo48):
    icon_id = 'wave-e3459233'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('solo-ai-full-set', 'wave-e3459233')

    def build(self):
        # Plan: Repeat the same smooth horizontal wave; preserve the broad two-line sign.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        for j,dy in enumerate([0,20]):
         path(f'wave-{j}',(4,15+dy),[('C',(14,8+dy),(8,10+dy),(10,8+dy)),('C',(34,20+dy),(22,8+dy),(26,20+dy)),('C',(44,13+dy),(38,20+dy),(42,16+dy))])
