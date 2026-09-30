"""Rejected pinafore has wide sloping shoulders and an hourglass bodice. Restore upright shoulder straps, squared neckline and a straight-sided bodice above the flared skirt.
Plan: VRECT_L envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='14d918d8-50d3-4ebe-98ee-fa95f856b6a2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__square-neck-pinafore-dress/20260929T130116Z-thuan-mac/reference/pinafore_14d918d8-50d3-4ebe-98ee-fa95f856b6a2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-neck-pinafore-dress'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pinafore',)
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        self.add_polyline('bodice',(10,4),(20,4),(20,13),(28,13),(28,4),(38,4),(33,24),(15,24),closed=True)
        path('skirt',(15,24),[('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(33,24))]);join('skirt','bodice')
