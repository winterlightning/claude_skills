"""Rejected bell is a narrow crescent. Restore a broad rounded dome above the diagonal rim and three smooth trailing tentacles.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ef0702b0-d65f-5955-8954-f383064a984c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__drifting-jellyfish/20260929T132613Z-thuan-mac/reference/jellyfish_ef0702b0-d65f-5955-8954-f383064a984c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='drifting-jellyfish'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('jellyfish',)
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
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('bell',(14,18),[('C',(30,6),(16,10),(22,6)),('C',(42,18),(37,6),(42,11)),('C',(34,38),(42,28),(42,34)),('L',(28,32)),('L',(22,26)),('L',(16,20)),('L',(14,18))],True)
        path('tentacle-0',(16,20),[('C',(6,30),(14,24),(10,27))]);join('tentacle-0','bell')
        path('tentacle-1',(22,26),[('C',(10,38),(20,30),(15,36))]);join('tentacle-1','bell')
        path('tentacle-2',(28,32),[('C',(20,42),(26,36),(23,40))]);join('tentacle-2','bell')
