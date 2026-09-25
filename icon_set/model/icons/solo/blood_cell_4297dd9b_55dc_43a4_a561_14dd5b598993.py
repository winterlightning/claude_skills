"""blood-cell: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4297dd9b-55dc-43a4-a561-14dd5b598993'
SOURCE_PATH = 'pictographic-primitives/other/blood cell_4297dd9b-55dc-43a4-a561-14dd5b598993.svg'
AUTHOR = 'gpt-6'

class BloodCell(Solo48):
    icon_id = 'blood-cell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('blood', 'cell', 'other', 'solo-ai-next50')

    def build(self):
        # Plan: One softly lobed cell outline replaces the jagged conversion. Four identical quarters share their extrema and tangent directions; no decorative inner marks.
        # Reference: Lucide circle original and atomic-debug construction.

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
        quarter=[('C',(34,10),(29,6),(29,10)),('C',(38,16),(38,10),(38,12)),('C',(42,24),(38,20),(42,20))]
        turn=lambda p,n: p if n==0 else turn((48-p[1],p[0]),n-1)
        commands=[]
        for n in range(4):
         for kind,end,c1,c2 in quarter:commands.append((kind,turn(end,n),turn(c1,n),turn(c2,n)))
        path('cell',(24,6),commands,True)
