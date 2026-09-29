"""Rejected arrival clock uses an oval orbit and very short hands. Restore a circular return arrow with its upper-left opening and longer perpendicular clock hands.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: clock-arrow-up.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7420a5ad-20b8-4125-a020-7f6c31b74aac'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__clock-with-counterclockwise-arrival-arrow/20260928T171322Z-thuan-mac/reference/shipping logistic estimate time arrival 1_7420a5ad-20b8-4125-a020-7f6c31b74aac.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Keep a truly circular return orbit and a tangent arrowhead with readable clock hands. The head extends 2px beyond the square keyshape but stays inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e330eb3d1af15d4a60630f8af37dbbb052578275d7e8ce426ad6bfb06a4136b8'}
    icon_id='clock-with-counterclockwise-arrival-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('shipping', 'logistic', 'estimate', 'time', 'arrival', '1')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('orbit',(12,11),[('C',(24,6),(15,8),(19,6)),('A',(42,24),18,True),('A',(24,42),18,True),('A',(6,24),18,True)])
        poly('head',(4,29),(6,24),(11,29));join('orbit','head')
        poly('hands',(24,15),(24,25),(32,25))


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

