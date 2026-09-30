"""Rejected large diamonds have equal sizes, losing the size hierarchy. Rebalance the upper-left diamond and retain a larger lower-right fleck with two smaller companions.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3153aa20-491b-49c7-935e-ead102198009'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__four-diamond-flecks/20260929T132613Z-thuan-mac/reference/fleck_3153aa20-491b-49c7-935e-ead102198009.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='four-diamond-flecks'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('fleck',)
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

        for name,x,y,r in [('upper-large',13,13,7),('lower-large',34,34,8),('upper-small',36,12,6),('lower-small',12,36,6)]:
            self.add_polyline(name,(x,y-r),(x+r,y),(x,y+r),(x-r,y),closed=True)
