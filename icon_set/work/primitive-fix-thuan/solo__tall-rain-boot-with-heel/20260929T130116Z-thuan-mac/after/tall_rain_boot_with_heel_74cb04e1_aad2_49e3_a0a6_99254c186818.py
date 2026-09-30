"""Rejected boot has square cuff and oversized stepped heel. Round the cuff and toe, add a natural curved ankle and a smaller integrated heel.
Plan: VRECT_L envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='74cb04e1-aad2-49e3-a0a6-99254c186818'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tall-rain-boot-with-heel/20260929T130116Z-thuan-mac/reference/boot_74cb04e1-aad2-49e3-a0a6-99254c186818.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tall-rain-boot-with-heel'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('boot',)
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

        path('boot',(26,4),[('L',(38,4)),('A',(40,6),2,2,True),('L',(39,26)),('L',(40,40)),('A',(36,44),4,4,True),('L',(30,44)),('L',(30,39)),('C',(17,42),(26,41),(21,42)),('L',(8,42)),('L',(8,36)),('A',(16,28),8,8,True),('C',(24,17),(23,28),(24,23)),('L',(24,6)),('A',(26,4),2,2,True)],True)
