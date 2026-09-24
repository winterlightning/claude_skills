from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bd2f046-d00e-4c3d-99dd-153eae347474'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/seo search eye_4bd2f046-d00e-4c3d-99dd-153eae347474.svg'
AUTHOR='gpt-6'
PLAN='Nested eye inside magnifier; iris omitted to open eye interior. SQUARE extremes6,6–42,42. Lucide eye/search principles: mirrored eye and round search lens; handle intentionally diagonal.'
class Drawing(Solo48):
    icon_id='seo-search-eye'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        self.add_arc('lens-top',(6,22),(38,22),radius_x=16)
        self.add_arc('lens-bottom',(38,22),(6,22),radius_x=16)
        self.add_contour('lens','lens-top','lens-bottom',closed=True)
        self.add_line('handle',(34,34),(42,42));self.relate('connect','lens','handle')
        self.add_bezier('eye',(15,22),((19,13),(25,13),(29,22)),((25,31),(19,31),(15,22)))
