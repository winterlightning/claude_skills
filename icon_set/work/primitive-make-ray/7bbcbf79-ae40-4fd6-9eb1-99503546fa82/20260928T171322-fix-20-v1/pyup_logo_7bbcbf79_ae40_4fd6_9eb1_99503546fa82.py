"""Feedback explicitly says the logo is narrow. Widen both the outer hexagonal spiral and inner hexagon, preserving the open lower-right break and left vertical return.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: No useful local Lucide PyUp logo match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7bbcbf79-ae40-4fd6-9eb1-99503546fa82'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pyup-logo/20260928T171410Z-thuan-mac/reference/pyup logo_7bbcbf79-ae40-4fd6-9eb1-99503546fa82.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pyup-logo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pyup', 'logo')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('outer',(26,44),(44,34),(44,14),(24,4),(4,14),(4,34),(14,40),(14,29))
        poly('inner',(14,29),(14,19),(24,14),(34,19),(34,29),(24,34),closed=True)
        join('outer','inner')


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

