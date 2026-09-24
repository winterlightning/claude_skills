"""Right-facing smooth muzzle and belly, with three swept quills on the left and two short feet; intentional animal asymmetry.
Keyshape HRECT_L. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Extra quills and two hidden feet omitted; reference direction restored."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '089d2df6-f974-42a3-9741-489bc35e9055'
SOURCE_PATH = 'pictographic-primitives/animals/hedgehog_089d2df6-f974-42a3-9741-489bc35e9055.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hedgehog'
    keyshape = Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="animals"
    aliases=()
    keywords=('hedgehog',)

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(12,8),[('C',(44,28),(25,12),(39,18)),('C',(32,35),(44,32),(39,35)),('L',(16,35)),('L',(8,35))])
        for i,(a,b) in enumerate([((6,16),(14,18)),((4,26),(10,26))]):line(f'quill-{i}',a,b)
        line('front-foot',(32,35),(32,40));line('rear-foot',(16,35),(16,40));join('body','front-foot');join('body','rear-foot')

