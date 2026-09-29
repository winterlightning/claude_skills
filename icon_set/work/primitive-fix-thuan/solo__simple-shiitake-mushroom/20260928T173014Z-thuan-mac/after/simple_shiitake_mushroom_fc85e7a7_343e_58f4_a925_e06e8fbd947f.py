"""Rejected stem is short and kinked. Restore a broad domed cap and longer gently curved open stem.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: No exact local Lucide match; bean smooth contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fc85e7a7-343e-58f4-a925-e06e8fbd947f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__simple-shiitake-mushroom/20260928T173014Z-thuan-mac/reference/mushroom shiitake_fc85e7a7-343e-58f4-a925-e06e8fbd947f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the broad low domed cap and longer curved stem of the shiitake reference. All spacing checks pass. Natural mushroom envelope is wider and lower than the square keyshape, with all ink at least 2px inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '13616ae02e7f7c10013bc51a037a8442dae613a81c209ac31bbfe497f7db6f11'}
    icon_id='simple-shiitake-mushroom'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('mushroom', 'shiitake')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('cap',(4,24),[('E',(24,8),20,16,True),('E',(44,24),20,16,True),('L',(28,24)),('L',(20,24)),('L',(4,24))],True)
        path('stem',(20,24),[('C',(17,39),(20,30),(19,35)),('C',(22,44),(16,42),(18,44)),('C',(29,38),(29,44),(29,43)),('L',(28,24))]);join('cap','stem')


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

