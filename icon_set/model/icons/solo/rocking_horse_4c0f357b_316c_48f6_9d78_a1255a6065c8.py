"""Corrected keyshape selection to match the existing square proportions.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c0f357b-316c-48f6-9d78-a1255a6065c8'
SOURCE_PATH = 'pictographic-primitives/babies/toys rocking horse_4c0f357b-316c-48f6-9d78-a1255a6065c8.svg'
AUTHOR = 'gpt-6'

class RockingHorse(Solo48):
    icon_id = 'rocking-horse'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ()
    keywords = ('rocking', 'horse', 'baby', 'nursery', 'toy')

    def build(self):
        # Plan: Trace a wider neck and rounded back into two legs, with a smooth belly and one continuous curved rocker.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('front',(18,6), [('L',(8,10)),('L',(6,17)),('A',(12,20),4,4,False),('L',(14,18)),('L',(16,28)),('L',(12,42))])
        path('back',(18,6), [('C',(30,20),(24,6),(24,20)),('L',(35,20)),('A',(40,25),5,5,True),('L',(36,42))]);join('front','back')
        path('belly',(12,42), [('A',(36,42),13,13,True)]);join('belly','front');join('belly','back')
        path('rocker',(6,33), [('A',(12,42),10,10,False),('L',(36,42)),('A',(42,33),10,10,False)]);join('rocker','front');join('rocker','back');join('rocker','belly')
