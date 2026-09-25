"""Fresh reconstruction of usb type c from the supplied reference.
Construction references: No useful Lucide USB-port match; source capsule governs geometry. Symbol plan recorded in build().
Profile SOLO48, keyshape HRECT_M; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c0a14e2a-4419-5c4d-bceb-f564e7b8279f'
SOURCE_PATH = 'pictographic-primitives/electronics/usb type c_c0a14e2a-4419-5c4d-bceb-f564e7b8279f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'usb-type-c'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('usb', 'type', 'c')

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
        # True horizontal capsule: equal semicircular ends, straight top/bottom, centered tongue.
        self.add_line('top',(18,10),(30,10))
        self.add_arc('right',(30,10),(30,38),radius_x=14)
        self.add_line('bottom',(30,38),(18,38))
        self.add_arc('left',(18,38),(18,10),radius_x=14)
        self.add_contour('shell','top','right','bottom','left',closed=True)
        self.add_line('tongue',(16,24),(32,24))
