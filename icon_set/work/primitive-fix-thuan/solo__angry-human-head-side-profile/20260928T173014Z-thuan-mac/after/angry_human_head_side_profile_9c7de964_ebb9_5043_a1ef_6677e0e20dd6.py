"""Rejected skull is kinked and mouth reads as a blob. Restore a circular cranium, open neck, slanted angry brow and attached curved mouth.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: brain; human profile reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9c7de964-ebb9-5043-a1ef-6677e0e20dd6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__angry-human-head-side-profile/20260928T173014Z-thuan-mac/reference/anger emotions_9c7de964-ebb9-5043-a1ef-6677e0e20dd6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the round cranium, projecting nose, angry brow, curved attached mouth and open neck. Brow-to-skull clearance is about 2.94px; the short nose return has about 1.65px local clearance. Both are visually distinct. Natural profile extends 2px outside the portrait keyshape on each side but remains inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '7dd10f738c3a2c65038bb4d1b5074d0a81ecb935421dc5c2f03da8343f5b470d'}
    icon_id='angry-human-head-side-profile'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('anger', 'emotions')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('profile',(14,44),[('L',(14,34)),('C',(6,20),(8,30),(6,25)),('A',(22,4),16,True),('A',(38,20),16,True),('L',(42,28)),('L',(36,28)),('L',(36,33)),('A',(28,41),8,True),('L',(28,44))])
        path('mouth',(36,33),[('C',(25,35),(30,32),(27,33))]);join('mouth','profile')
        line('brow',(25,16),(31,19))


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

