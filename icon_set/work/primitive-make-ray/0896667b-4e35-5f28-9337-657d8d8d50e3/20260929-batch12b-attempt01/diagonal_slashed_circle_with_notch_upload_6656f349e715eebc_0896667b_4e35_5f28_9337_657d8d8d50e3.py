"""Only the rejected SVG is available. Rebalance its diagonal stroke over a round ring and retain the short upper-right protrusion with cleaner joins.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0896667b-4e35-5f28-9337-657d8d8d50e3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-slashed-circle-with-notch-upload-6656f349e715eebc/20260929T132613Z-thuan-mac/reference/diagonal-slashed-circle-with-notch-upload-6656f349e715eebc_0896667b-4e35-5f28-9337-657d8d8d50e3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='diagonal-slashed-circle-with-notch-upload-6656f349e715eebc'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('diagonal-slashed-circle-with-notch-upload-6656f349e715eebc',)
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

        circle('ring',24,24,15)
        self.add_line('slash',(6,6),(42,42));join('slash','ring')
        self.add_line('notch',(33,12),(39,6));join('notch','ring')
