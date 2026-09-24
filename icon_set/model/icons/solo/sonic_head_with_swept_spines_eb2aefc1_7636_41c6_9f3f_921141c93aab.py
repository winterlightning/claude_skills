"""A Sonic head with swept spines and rounded muzzle.
Plan: SQUARE gives the head and rightward spines room.
Reduction: Tiny brow and ear detail omitted; eye retained as a dot. Widened the valleys between three swept spines.
Construction: No useful exact Lucide match; source character silhouette governs construction.
Layout: Left-facing muzzle and right-facing spines deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb2aefc1-7636-41c6-9f3f-921141c93aab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/sonic 1_eb2aefc1-7636-41c6-9f3f-921141c93aab.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'sonic-head-with-swept-spines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sonic', 'hedgehog', 'character', 'head', 'spines', 'profile')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('head',(8,32),[('C',(32,6),(7,14),(18,6)),('L',(37,6)),('L',(28,15)),('C',(42,24),(38,15),(42,20)),('L',(30,24)),('C',(37,39),(36,30),(40,34)),('L',(31,35)),('C',(21,42),(27,39),(24,42)),('C',(6,32),(11,42),(6,38)),('L',(8,32))],True)
        path('muzzle',(6,32),[('C',(25,36),(15,33),(24,29)),('C',(21,42),(25,39),(24,41))]);self.relate('connect','muzzle','head')
        self.add_dot('eye',(20,23))
