"""lead-nuturing-plant: Smooth paired seedling; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4f10974a-d5b4-43a2-b15c-1c1fd7f01497'
SOURCE_PATH = 'pictographic-primitives/nature/lead nuturing plant_4f10974a-d5b4-43a2-b15c-1c1fd7f01497.svg'
AUTHOR = 'gpt-6'

class LeadNuturingPlant(Solo48):
    icon_id = 'lead-nuturing-plant'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('solo-ai-full-set', 'lead-nuturing-plant')

    def build(self):
        # Plan: Preserve two cupped leaves and curved soil line. Mirror broad leaf contours around a shared central stem.
        # Reference: Lucide leaf: original and atomic-debug geometry.

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
        path('left',(24,29),[('C',(6,6),(8,29),(6,18)),('C',(24,29),(22,8),(24,15))],True)
        path('right',(24,29),[('C',(42,6),(24,15),(26,8)),('C',(24,29),(42,18),(40,29))],True)
        join('left','right');line('stem',(24,29),(24,38));join('stem','left');join('stem','right')
        path('soil',(8,42),[('C',(24,38),(13,40),(19,38)),('C',(40,42),(29,38),(35,40))]);join('soil','stem')
