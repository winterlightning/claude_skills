"""slab-serif-text-character: Regular slab-serif M; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '70038eef-85af-41f4-aad8-09e1441d60a0'
SOURCE_PATH = 'icons-json/interface-essential/slab serif text character_70038eef-85af-41f4-aad8-09e1441d60a0.json'
AUTHOR = 'gpt-6'

class SlabSerifTextCharacter(Solo48):
    icon_id = 'slab-serif-text-character'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'slab-serif-text-character')

    def build(self):
        # Plan: Preserve the broad M with four serif ends; consolidate the shared vertical stems and serif junctions.
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
        path('left',(8,4),[('L',(13,4)),('L',(13,44))]);path('right',(40,4),[('L',(35,4)),('L',(35,44))])
        path('middle',(13,4),[('L',(24,30)),('L',(35,4))]);join('middle','left');join('middle','right')
        for name,x in [('left',13),('right',35)]:path(f'base-{name}',(x-4,44),[('L',(x,44)),('L',(x+4,44))]);join(f'base-{name}',name)
