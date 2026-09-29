"""Restore a visible mug body, rounded foam, a generous side handle and a separate rounded loaf with one scoring cut.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The mug left wall disappeared behind a large bread shape and the handle became a tiny loop.
Construction: beer.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beer-mug-with-bread/20260928T175901Z-thuan-mac/reference/tarvern shop restuarant_f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'beer-mug-with-bread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('tarvern', 'shop', 'restuarant')

    def build(self):

        def path(name,start,commands,closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(commands):
                if end==here and kind=='L':continue
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        L=lambda end:('L',end)
        C=lambda end,c1,c2:('C',end,c1,c2)
        A=lambda end,rx,ry,sweep:('A',end,rx,ry,sweep)
        line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('foam',(10,17),[C((8,9),(4,17),(4,10)),C((17,8),(11,6),(14,6)),C((29,8),(18,5),(28,5)),C((35,17),(39,5),(41,17)),L((10,17))],True)
        line('mug-left',(10,17),(10,27));join('foam','mug-left')
        path('mug-right',(35,17),[L((35,35)),C((29,42),(35,40),(33,42)),L((27,42))]);join('foam','mug-right')
        path('handle',(35,22),[L((39,22)),C((44,27),(44,22),(44,24)),L((44,31)),C((39,36),(44,34),(43,36)),L((35,36))])
        path('loaf',(4,42),[C((15,30),(4,35),(9,30)),C((26,42),(21,30),(26,35)),L((4,42))],True)
        line('score',(15,30),(15,35));join('score','loaf')


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'Retain the beer mug, foam, side handle and overlapping bread loaf. Their intentional overlap and natural bounds preserve the tavern subject. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ff7937c557debc4ecb1498bc2eccbbc25727d6b2c57fc26f91d50946deeecad6'}
