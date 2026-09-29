"""Rejected cap has a flattened top and angular shoulders. Restore a gently rounded triangular cap and a flared stem.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: No exact local Lucide match; mountain rounded silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='150f41be-4611-55ec-af11-7f0c3d5c744a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__simple-triangular-mushroom/20260928T173014Z-thuan-mac/reference/mushroom_150f41be-4611-55ec-af11-7f0c3d5c744a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the smoothly rounded triangular mushroom cap and flared stem. All spacing checks pass. The natural 44px-square ink envelope stays 2px inside the canvas; reducing the envelope would weaken the open stem. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '532951909bccdefe977a94d96a7b867a63b5cade052b4814dd568efc1138bcd4'}
    icon_id='simple-triangular-mushroom'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('mushroom',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('cap',(4,28),[('L',(18,8)),('C',(24,4),(20,5),(22,4)),('C',(30,8),(26,4),(28,5)),('L',(44,28)),('C',(40,32),(44,31),(43,32)),('L',(28,32)),('L',(20,32)),('L',(8,32)),('C',(4,28),(5,32),(4,31))],True)
        path('stem',(20,32),[('L',(19,41)),('C',(29,41),(18,45),(30,45)),('L',(28,32))]);join('stem','cap')


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

