"""Fresh reconstruction of android from the supplied reference.
Construction references: Lucide bot. Symbol plan recorded in build().
Profile SOLO48, keyshape HRECT_L; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb'
SOURCE_PATH = 'pictographic-primitives/apps/android_bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'android-mascot-with-arms'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('android',)

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
        # Arms are exactly 8 centerline / 4 ink units from straight body walls.
        self.add_bezier('dome-left',(12,20),((12,16),(13,14),(16,11)),((19,8),(21,8),(24,8)))
        self.add_bezier('dome-right',(24,8),((27,8),(29,8),(32,11)),((35,14),(36,16),(36,20)))
        self.add_line('right-wall',(36,20),(36,32))
        self.add_arc('right-corner',(36,32),(32,36),radius_x=4)
        self.add_polyline('bottom',(32,36),(30,36),(18,36),(16,36))
        self.add_arc('left-corner',(16,36),(12,32),radius_x=4)
        self.add_line('left-wall',(12,32),(12,20))
        self.contours[:] = [c for c in self.contours if c.contour_id != 'bottom']
        self.add_contour('body','dome-left','dome-right','right-wall','right-corner','bottom-1','bottom-2','bottom-3','left-corner','left-wall',closed=True)
        self.add_line('seam',(12,20),(36,20));self.relate('connect','seam','body')
        for n,x,tip in [('left',16,12),('right',32,36)]:
            self.add_line('antenna-'+n,(x,11),(tip,8));self.relate('connect','antenna-'+n,'body')
        for i,x in enumerate((18,30)):
            self.add_line(f'leg-{i}',(x,36),(x,40));self.relate('connect',f'leg-{i}','body')
        for i,x in enumerate((4,44)):self.add_line(f'arm-{i}',(x,24),(x,31))

    icon_id = 'android-mascot-with-arms'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('android', 'mascot', 'with', 'arms')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
