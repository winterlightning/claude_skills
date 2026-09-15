"""megaphone-9e81b14e: Flowing megaphone bell; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9e81b14e-7968-4119-8d29-69479a774ba8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/megaphone_9e81b14e-7968-4119-8d29-69479a774ba8.svg'
AUTHOR = 'gpt-6'

class Megaphone9e81b14e(Solo48):
    icon_id = 'megaphone-9e81b14e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'megaphone-9e81b14e')

    def build(self):
        # Plan: Preserve the angled bell and hanging handle; smooth the bell curves around a clear, regular neck.
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
        path('body',(9,22),[('L',(18,22)),('C',(40,8),(26,20),(32,13)),('L',(44,32)),('C',(18,32),(35,29),(26,30)),('L',(14,32)),('L',(9,32)),('A',(9,22),5,5,True)],True)
        line('neck',(18,22),(18,32));join('neck','body')
        path('handle',(14,32),[('C',(21,40),(16,35),(18,40)),('L',(26,38))]);join('handle','body')
