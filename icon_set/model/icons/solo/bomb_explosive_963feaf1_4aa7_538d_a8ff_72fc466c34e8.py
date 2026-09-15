"""bomb-explosive: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '963feaf1-4aa7-538d-a8ff-72fc466c34e8'
SOURCE_PATH = 'icons-json/war/bomb explosive_963feaf1-4aa7-538d-a8ff-72fc466c34e8.json'
AUTHOR = 'gpt-6'

class BombExplosive(Solo48):
    icon_id = 'bomb-explosive'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('bomb', 'explosive', 'war', 'solo-ai-next50')

    def build(self):
        # Plan: The source is a tied cylindrical explosive charge: a rounded canister and central strap with a short curved fuse. Kept that subject rather than substituting a spherical bomb.
        # Reference: Lucide bomb original and atomic-debug construction.

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
        path('case',(12,16),[('L',(18,16)),('L',(30,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(30,44)),('L',(18,44)),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,20)),('A',(12,16),4,4,True)],True)
        for x in (18,30):
         line(f'band-{x}',(x,16),(x,44));join(f'band-{x}','case')
        path('fuse',(24,16),[('C',(30,4),(24,8),(24,4)),('C',(40,8),(36,4),(36,8))]);join('fuse','case')
