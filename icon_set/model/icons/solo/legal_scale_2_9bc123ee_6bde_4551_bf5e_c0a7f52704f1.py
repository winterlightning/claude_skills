"""legal-scale-2: Matching balance pans; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bc123ee-6bde-4551-bf5e-c0a7f52704f1'
SOURCE_PATH = 'pictographic-primitives/office/legal scale 2_9bc123ee-6bde-4551-bf5e-c0a7f52704f1.svg'
AUTHOR = 'gpt-6'

class LegalScale2(Solo48):
    icon_id = 'legal-scale-2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'legal-scale-2')

    def build(self):
        # Plan: Two equal semicircular pans share suspension lengths and a level beam; preserve the hanging-scale composition.
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
        path('beam',(7,12),[('L',(12,12)),('L',(24,12)),('L',(36,12)),('L',(41,12))]);path('pivot',(24,8),[('L',(24,12)),('L',(24,17))]);join('beam','pivot')
        for j,cx in enumerate([12,36]):
         path(f'pan-{j}',(cx-8,32),[('L',(cx+8,32)),('A',(cx-8,32),8,8,True)],True)
         path(f'cord-{j}',(cx-8,32),[('L',(cx,12)),('L',(cx+8,32))]);join(f'cord-{j}',f'pan-{j}');join(f'cord-{j}','beam')
