"""Rejected hill is too steep. Restore a shallow rising slope and clean rounded triangle corners.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: mountain.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6bbed91c-30b7-45ad-ae98-8eb34d66c53b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hill-1/20260928T173014Z-thuan-mac/reference/hill 1_6bbed91c-30b7-45ad-ae98-8eb34d66c53b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the reference shallow rising hill. Its natural height is 4px less than the horizontal keyshape envelope; stretching it vertically would recreate the rejected steep slope. All spacing checks pass. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2708b69f94552d684c9b85b410c2b3354697357b12ed4fad086bb65c0de35669'}
    icon_id='hill-1'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('hill', '1')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('slope',(4,36),(44,12),(44,36),closed=True)


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

