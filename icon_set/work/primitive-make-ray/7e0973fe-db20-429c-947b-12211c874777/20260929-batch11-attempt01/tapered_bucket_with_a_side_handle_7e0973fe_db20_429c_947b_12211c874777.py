"""Rejected bucket looks like a mug with a rigid side loop. Restore broad tapered pail and a swinging handle attached to a visible pivot.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7e0973fe-db20-429c-947b-12211c874777'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tapered-bucket-with-a-side-handle/20260929T130116Z-thuan-mac/reference/amazon s3 storage_7e0973fe-db20-429c-947b-12211c874777.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tapered-bucket-with-a-side-handle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('amazon', 's3', 'storage')
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

        path('rim',(6,12),[('A',(38,12),16,6,True),('A',(6,12),16,6,True)],True)
        path('body',(6,12),[('L',(10,36)),('C',(22,42),(10,40),(16,42)),('C',(34,36),(28,42),(34,40)),('L',(38,12))]);join('body','rim')
        circle('pivot',23,27,2)
        path('handle',(25,27),[('L',(38,32)),('A',(42,28),4,4,False),('L',(36,22))]);join('handle','pivot');join('handle','body')
