"""Rejected hourglass is a wide rigid block with a heavy central X and a short sand dash. Restore slender vertical rims, smooth tapering glass walls and a longer horizontal sand level.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: hourglass.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1873be1c-2600-5197-83a2-680121a9a499'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hourglass-with-sand-level-batch-016-15/20260928T171322Z-thuan-mac/reference/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the narrow hourglass rims, smooth crossed glass walls and horizontal sand level. The level has approximately 2px clearance to the walls, while the central hourglass crossing is intentional. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2e49ebb9d556aaa3decc1bf0e49eb02ef72a4077fd8342b9e55156df360da38a'}
    icon_id='hourglass-with-sand-level-batch-016-15'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('hourglass',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for n,y in [('top',4),('bottom',44)]:poly(n+'-rim',(10,y),(14,y),(34,y),(38,y))
        path('glass-left',(14,4),[('L',(14,12)),('C',(24,24),(14,18),(20,21)),('C',(34,36),(28,27),(34,30)),('L',(34,44))])
        path('glass-right',(34,4),[('L',(34,12)),('C',(24,24),(34,18),(28,21)),('C',(14,36),(20,27),(14,30)),('L',(14,44))])
        for g in ('glass-left','glass-right'):
            join(g,'top-rim');join(g,'bottom-rim')
        join('glass-left','glass-right')
        line('sand',(20,12),(28,12))


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

