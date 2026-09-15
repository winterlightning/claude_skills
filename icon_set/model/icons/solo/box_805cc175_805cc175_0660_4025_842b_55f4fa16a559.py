"""box-805cc175: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '805cc175-0660-4025-842b-55f4fa16a559'
SOURCE_PATH = 'icons-json/shipping/box_805cc175-0660-4025-842b-55f4fa16a559.json'
AUTHOR = 'gpt-6'

class Box805cc175(Solo48):
    icon_id = 'box-805cc175'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping', 'solo-ai-next50')

    def build(self):
        # Plan: A wide lidded storage carton has a centered short lid seam and rounded lower corners. Horizontal format makes it distinct from the tall parcels.
        # Reference: Lucide package original and atomic-debug construction.

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
        path('carton',(8,8),[('L',(24,8)),('L',(40,8)),('A',(44,12),4,4,True),('L',(44,18)),('L',(44,34)),('A',(38,40),6,6,True),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,18)),('L',(4,12)),('A',(8,8),4,4,True)],True)
        poly('lid',(4,18),(24,18),(44,18));line('seam',(24,8),(24,18));join('lid','carton');join('seam','lid');join('seam','carton')
