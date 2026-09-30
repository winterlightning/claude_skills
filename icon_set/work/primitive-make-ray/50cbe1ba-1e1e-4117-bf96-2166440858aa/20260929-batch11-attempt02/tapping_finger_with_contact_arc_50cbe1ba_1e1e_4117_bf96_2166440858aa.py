"""Rejected hand has a stubby index finger and a single short halo. Lengthen the upright finger and carry the outer contact arc farther around it; keep the open wrist.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='50cbe1ba-1e1e-4117-bf96-2166440858aa'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tapping-finger-with-contact-arc/20260929T130116Z-thuan-mac/reference/gesture tap 1_50cbe1ba-1e1e-4117-bf96-2166440858aa.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tapping-finger-with-contact-arc'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('gesture', 'tap', '1')
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

        path('contact-outer',(4,24),[('A',(24,4),20,20,True),('A',(44,24),20,20,True)])
        path('contact-inner',(13,24),[('A',(24,13),11,11,True),('A',(35,24),11,11,True)])
        path('hand',(16,42),[('L',(10,36)),('A',(16,32),5,5,True),('L',(20,36)),('L',(20,28)),('A',(28,28),4,4,True),('L',(28,36)),('L',(32,38)),('L',(32,42))])
