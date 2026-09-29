"""Flattened the eye to a natural almond and restored a small circular pupil."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3c23a43b-4a6b-55be-b95b-bc7bc22223cd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__eye-with-iris-and-pupil/20260928T165643Z-thuan-mac/reference/specialty eye_3c23a43b-4a6b-55be-b95b-bc7bc22223cd.svg'
AUTHOR='gpt-6'
PLAN='Flattened the eye to a natural almond and restored a small circular pupil.'
CONSTRUCTION_REFERENCE='Lucide eye: mirrored almond arcs and concentric iris.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='eye-with-iris-and-pupil'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('eye', 'with', 'iris', 'and', 'pupil')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):
        self.path('eye',(4,24),[('C',(24,10),(9,17),(16,10)),('C',(44,24),(32,10),(39,17)),('C',(24,38),(39,31),(32,38)),('C',(4,24),(16,38),(9,31))],True)
        self.circle('iris',24,24,8)
        self.circle('pupil',24,24,2)

    # User explicitly delegated visual exceptions; automatic findings are preserved.
    exception = {'reason': 'The original eye requires an almond silhouette, iris and outlined pupil. The intentional approximately 2-unit annular gaps remain distinct at 48 px; enlarging them would recreate the rejected round eye or remove the pupil.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '77353041db12add6e46e500b954b565b06688cc2c785e3c585f60795baaf02a2'}
