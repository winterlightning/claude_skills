"""Fresh reconstruction of device google glass from the supplied reference.
Construction references: Lucide glasses. Symbol plan recorded in build().
Profile SOLO48, keyshape HRECT_M; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f3f157a4-4ba4-56cb-af69-39f5c5fe3376'
SOURCE_PATH = 'pictographic-primitives/devices/device google glass_f3f157a4-4ba4-56cb-af69-39f5c5fe3376.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'augmented-reality-glasses-with-corner-display'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('device', 'google', 'glass')

    def circle(self, n, x, y, r):
        self.add_arc(n+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(n+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def box(self,n,l,t,r,b,k=4,top=(),bottom=()):
        p=[(l+k,t),*[(x,t) for x in sorted(top)],(r-k,t),(r,t+k),(r,b-k),(r-k,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,(a,z) in enumerate(zip(p,p[1:]+p[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if a[0]!=z[0] and a[1]!=z[1]:self.add_arc(name,a,z,radius_x=k)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Mirrored lower lens bowls and narrow bridge; upper-left display is asymmetric.
        self.add_polyline('top',(8,10),(14,10),(40,10))
        self.add_arc('tr',(40,10),(44,14),radius_x=4)
        self.add_line('right',(44,14),(44,26))
        self.add_arc('right-bowl',(44,26),(32,38),radius_x=12)
        self.add_bezier('right-nose',(32,38),((29,38),(29,29),(27,26)))
        self.add_arc('bridge',(27,26),(21,26),radius_x=3,sweep=False)
        self.add_bezier('left-nose',(21,26),((19,29),(19,38),(16,38)))
        self.add_arc('left-bowl',(16,38),(4,26),radius_x=12)
        self.add_polyline('left',(4,26),(4,18),(4,14))
        self.add_arc('tl',(4,14),(8,10),radius_x=4)
        self.contours[:] = [c for c in self.contours if c.contour_id not in ('top','left')]
        self.add_contour('frame','top-1','top-2','tr','right','right-bowl','right-nose','bridge','left-nose','left-bowl','left-1','left-2','tl',closed=True)
        self.add_polyline('display',(4,18),(14,18),(14,10))
        self.relate('connect','display','frame')
