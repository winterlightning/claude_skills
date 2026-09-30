"""Rejected lenses are deep bowls and the sun is centered with dot rays. Restore shallower sunglasses and an upper-right outlined sun with short line rays.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='81f3cdea-8b11-5ce2-be37-8b1a02812d9f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__glasses-sun/20260929T132937Z-thuan-mac/reference/glasses sun_81f3cdea-8b11-5ce2-be37-8b1a02812d9f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='glasses-sun'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('glasses', 'sun')
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

        for side,cx in [('left',13),('right',35)]:
            path('lens-'+side,(cx-7,32),[('L',(cx+7,32)),('A',(cx-7,32),7,10,True)],True)
        self.add_line('bridge',(20,32),(28,32));join('bridge','lens-left');join('bridge','lens-right')
        self.add_line('arm-left',(6,32),(12,24));join('arm-left','lens-left')
        self.add_line('arm-right',(42,32),(38,24));join('arm-right','lens-right')
        circle('sun',32,11,5)
        self.add_line('ray-upper-left',(17,6),(19,7));self.add_line('ray-left',(14,15),(18,15))
