"""Restore the flared tricorn silhouette, readable crossed mark, rounded face sides and pointed full beard.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The broad pirate hat became a domed helmet, the cross collapsed, and the beard was narrow and angular.
Construction: skull.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '871b202b-58cd-4c8b-af66-2a006eddce86'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bearded-pirate-with-crossed-hat-mark/20260928T175901Z-thuan-mac/reference/pirate_871b202b-58cd-4c8b-af66-2a006eddce86.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'bearded-pirate-with-crossed-hat-mark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pirate',)

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

        path('hat',(4,22),[C((13,13),(4,17),(8,13)),C((24,6),(15,6),(19,6)),C((35,13),(29,6),(33,6)),C((44,22),(40,13),(44,17)),L((35,25)),C((13,25),(29,21),(19,21)),L((4,22))],True)
        poly('cross-a',(21,12),(27,18));poly('cross-b',(27,12),(21,18))
        path('face-left',(14,25),[C((17,34),(14,30),(15,32))])
        path('face-right',(34,25),[C((31,34),(34,30),(33,32))])
        path('beard',(24,30),[C((32,35),(29,30),(32,32)),C((24,44),(32,38),(27,42)),C((16,35),(21,42),(16,38)),C((24,30),(16,32),(19,30))],True)


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'Retain the full tricorn hat, crossed emblem, face and pointed beard. Their compact portrait spacing is needed for pirate recognition at 48px. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2f64a15515aad5602cedce3ce68a217ad58641131abef87c34f3f12bd55e5fd5'}
