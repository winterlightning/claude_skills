"""cat-bed: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fc88911f-a19f-4219-a235-ea1c5db29485'
SOURCE_PATH = 'icons-json/pets/cat bed_fc88911f-a19f-4219-a235-ea1c5db29485.json'
AUTHOR = 'gpt-6'

class CatBed(Solo48):
    icon_id = 'cat-bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'bed', 'pets', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the oval pet bed and lowered front entry. A shared elliptical rim makes both ends equal without flattening the cushion.
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
        path('back',(4,20),[('A',(44,20),20,12,True)])
        path('front',(4,20),[('L',(4,30)),('A',(44,30),20,10,False),('L',(44,20)),('L',(34,24)),('L',(32,30)),('L',(16,30)),('L',(14,24)),('L',(4,20))],True);join('front','back')
