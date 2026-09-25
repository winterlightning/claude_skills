"""death-coffin: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be911cd7-5766-5839-916f-fd3eb87581c6'
SOURCE_PATH = 'pictographic-primitives/religion/death coffin_be911cd7-5766-5839-916f-fd3eb87581c6.svg'
AUTHOR = 'gpt-6'

class DeathCoffin(Solo48):
    icon_id = 'death-coffin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    categories = ('primitives', 'religion')
    aliases = ()
    keywords = ('death', 'coffin', 'religion', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the tapered coffin and central cross; the six straight sides use paired coordinates and generous inner space.
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
        poly('coffin',(16,4),(32,4),(40,16),(34,44),(14,44),(8,16),closed=True)
        poly('cross',(24,15),(24,20),(24,31));poly('arms',(18,20),(24,20),(30,20));join('cross','arms')
