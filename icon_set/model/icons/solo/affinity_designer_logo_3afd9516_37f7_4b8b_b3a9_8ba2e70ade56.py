"""affinity-designer-logo: Clean angular designer emblem; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3afd9516-37f7-4b8b-b3a9-8ba2e70ade56'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/affinity designer logo_3afd9516-37f7-4b8b-b3a9-8ba2e70ade56.svg'
AUTHOR = 'gpt-6'

class AffinityDesignerLogo(Solo48):
    icon_id = 'affinity-designer-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('solo-ai-full-set', 'affinity-designer-logo')

    def build(self):
        # Plan: Preserve the triangular partition and diagonal band; widen the narrow outer band and share every facet node.
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
        path('outline',(4,30),[('L',(17,8)),('L',(28,8)),('L',(44,8)),('L',(44,29)),('L',(44,40)),('L',(21,40)),('L',(4,40)),('L',(4,30))],True)
        path('band',(28,8),[('L',(21,18)),('L',(14,29)),('L',(21,40))]);join('band','outline')
        path('facet',(14,29),[('L',(29,29)),('L',(44,29))]);line('diagonal',(21,18),(29,29));join('facet','outline');join('facet','band');join('diagonal','facet');join('diagonal','band')
