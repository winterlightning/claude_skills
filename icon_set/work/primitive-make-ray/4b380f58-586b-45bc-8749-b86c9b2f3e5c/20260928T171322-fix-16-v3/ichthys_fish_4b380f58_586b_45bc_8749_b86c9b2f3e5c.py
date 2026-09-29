"""Rejected fish changes the reference to an open crossed tail and an eye dot. Restore the closed triangular tail and curved gill inside a natural horizontal fish body.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: fish.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4b380f58-586b-45bc-8749-b86c9b2f3e5c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ichthys-fish/20260928T171322Z-thuan-mac/reference/fish_4b380f58-586b-45bc-8749-b86c9b2f3e5c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the reference slender horizontal fish body, closed triangular tail and short curved gill. Natural height is smaller than the standard horizontal keyshape; gill clearance is about 1.77px and remains visible in both themes. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '848b854abafa14b6d763da55ee7fe4fc6faf59a659f173a5a2facb93fb6fb5fd'}
    icon_id='ichthys-fish'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('fish',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(12,24),[('C',(28,16),(16,20),(22,16)),('C',(44,24),(34,16),(40,20)),('C',(28,32),(40,28),(34,32)),('C',(12,24),(22,32),(16,28))],True)
        poly('tail',(12,24),(4,16),(4,32),closed=True);join('tail','body')
        path('gill',(30,22),[('C',(30,26),(29,23),(29,25))])


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

