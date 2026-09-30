"""Rejected cow has a dog-like angular muzzle and blocky feet. Restore rounded hanging muzzle, sloped hock and a small ear while preserving the long back.
Plan: HRECT_L envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e86bdf40-e8f1-4d65-a5ae-e3b40658db61'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__standing-cow-profile/20260929T130116Z-thuan-mac/reference/heifer_e86bdf40-e8f1-4d65-a5ae-e3b40658db61.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='standing-cow-profile'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('heifer',)
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

        path('cow',(8,40),[('L',(8,22)),('A',(16,14),8,8,True),('L',(30,14)),('L',(32,8)),('L',(36,12)),('C',(44,23),(39,16),(44,19)),('A',(40,27),4,4,True),('L',(35,26)),('C',(31,31),(33,27),(32,30)),('L',(31,40)),('L',(23,40)),('L',(23,31)),('L',(16,31)),('L',(12,37)),('L',(14,40)),('L',(8,40))],True)
        path('tail',(8,22),[('C',(4,32),(6,23),(4,28))]);join('tail','cow')
