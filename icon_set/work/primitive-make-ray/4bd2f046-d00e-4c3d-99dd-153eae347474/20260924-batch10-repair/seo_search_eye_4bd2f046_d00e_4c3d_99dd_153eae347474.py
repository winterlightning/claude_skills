from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bd2f046-d00e-4c3d-99dd-153eae347474'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/seo search eye_4bd2f046-d00e-4c3d-99dd-153eae347474.svg'
AUTHOR='gpt-6'
PLAN='Wider horizontal eye inside circular magnifier; exact8-15-17 handle attachment. Iris omitted for an open eye interior. SQUARE6,6–42,42. Lucide eye symmetry and round lens, directional handle.'
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
        pts=[(6,23),(23,6),(40,23),(31,38),(6,23)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'lens-{i}',a,b,radius_x=17)
        self.add_contour('lens',*(f'lens-{i}' for i in range(4)),closed=True)
        self.add_line('handle',(31,38),(42,42));self.relate('connect','lens','handle')
        self.add_bezier('eye',(15,23),((19,14),(27,14),(31,23)),((27,32),(19,32),(15,23)))
