"""crane-hook: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40e56b92-93e6-4122-b70a-f6f602cc3011'
SOURCE_PATH = 'icons-json/shipping/crane hook_40e56b92-93e6-4122-b70a-f6f602cc3011.json'
AUTHOR = 'gpt-6'

class CraneHook(Solo48):
    icon_id = 'crane-hook'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('crane', 'hook', 'shipping', 'solo-ai-next100')

    def build(self):
        # Plan: A compact pulley block supports a smooth open hook. A diagonal block seam and spacious lower hook retain the original mechanism.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        poly('block',(8,4),(32,4),(40,4),(40,16),(32,23),(24,23),(16,23),(8,16),(8,4))
        line('diagonal',(8,16),(32,4));join('diagonal','block')
        path('hook',(24,23),[('L',(24,31)),('C',(16,36),(19,31),(16,32)),('C',(26,44),(16,42),(20,44)),('C',(36,36),(32,44),(36,41))]);join('hook','block')
