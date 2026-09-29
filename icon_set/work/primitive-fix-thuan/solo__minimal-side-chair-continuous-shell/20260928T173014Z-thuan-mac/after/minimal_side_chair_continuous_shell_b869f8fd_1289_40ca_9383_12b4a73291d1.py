"""Rejected chair lacks a crossbar and its shell has a sharp elbow. Restore a smooth continuous shell with splayed legs and crossbar.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: armchair.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b869f8fd-1289-40ca-9383-12b4a73291d1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__minimal-side-chair-continuous-shell/20260928T173014Z-thuan-mac/reference/chair modern_b869f8fd-1289-40ca-9383-12b4a73291d1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the continuous curved chair shell, splayed legs and crossbar. The seat has a deliberate 2px open channel, readable at native size. Natural shell proportions extend slightly outside the standard keyshape but stay inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '7d29343f00a52e34d2c0d69f687fd2079774717dc7a830eafd038c17fd28578a'}
    icon_id='minimal-side-chair-continuous-shell'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('chair', 'modern')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('shell',(12,4),[('L',(14,4)),('C',(20,18),(18,4),(18,8)),('C',(30,26),(22,25),(24,26)),('L',(40,26)),('C',(40,32),(44,26),(44,32)),('L',(34,32)),('L',(20,32)),('L',(18,32)),('C',(9,22),(12,32),(10,29)),('L',(7,8)),('C',(12,4),(6,4),(8,4))],True)
        poly('left-leg',(18,32),(14,40),(12,44));poly('right-leg',(34,32),(38,40),(40,44))
        line('crossbar',(14,40),(38,40))
        for n in ('left-leg','right-leg'):join(n,'shell');join(n,'crossbar')


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

