"""atom-other: Balanced orbits · nucleus; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1360ae7-7838-4ce4-ab4c-2158d5dcbebb'
SOURCE_PATH = 'icons-json/other/atom_e1360ae7-7838-4ce4-ab4c-2158d5dcbebb.json'
AUTHOR = 'gpt-6'

class AtomOther(Solo48):
    icon_id = 'atom-other'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'atom-other')

    def build(self):
        # Plan: Two rounded diagonal orbits mirror around x=24 and y=24, with a restored central nucleus. Shared crossing nodes and wider central space preserve the atom reading; square bounds balance both loops.
        # Reference: Lucide atom: original and atomic-debug geometry.

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
        commands=[('A',(12,6),6,6,True),('C',(24,12),(16,6),(20,8)),('L',(36,24)),('C',(42,36),(40,28),(42,32)),('A',(36,42),6,6,True),('C',(24,36),(32,42),(28,40)),('L',(12,24)),('C',(6,12),(8,20),(6,16))]
        path('orbit-a',(6,12),commands,True)
        mirror=lambda p:(48-p[0],p[1])
        mirrored=[]
        for kind,end,*args in commands:
         if kind=='A': mirrored.append((kind,mirror(end),args[0],args[1],not args[2]))
         elif kind=='C':mirrored.append((kind,mirror(end),mirror(args[0]),mirror(args[1])))
         else:mirrored.append((kind,mirror(end)))
        path('orbit-b',mirror((6,12)),mirrored,True)
        self.add_dot('nucleus',(24,24));join('orbit-a','orbit-b')
