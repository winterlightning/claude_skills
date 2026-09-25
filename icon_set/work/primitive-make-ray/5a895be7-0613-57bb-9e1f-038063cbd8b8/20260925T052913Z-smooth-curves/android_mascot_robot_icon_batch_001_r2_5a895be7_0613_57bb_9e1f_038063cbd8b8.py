"""Fresh reconstruction of android from the supplied reference.
Construction references: Lucide bot. Symbol plan recorded in build().
Profile SOLO48, keyshape VRECT_L; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a895be7-0613-57bb-9e1f-038063cbd8b8'
SOURCE_PATH = 'pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'android-mascot-robot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
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
        # Smooth dome, symmetric short antennae, rounded shoulders and equal outlined legs.
        self.add_bezier('dome-left',(8,20),((8,15),(12,10),(16,8)),((20,6),(21,6),(24,6)))
        self.add_bezier('dome-right',(24,6),((27,6),(28,6),(32,8)),((36,10),(40,15),(40,20)))
        self.add_line('right-wall',(40,20),(40,30))
        self.add_arc('right-corner',(40,30),(36,34),radius_x=4)
        self.add_line('right-leg-outer',(36,34),(36,40))
        self.add_arc('right-foot',(36,40),(28,40),radius_x=4)
        self.add_line('right-leg-inner',(28,40),(28,34))
        self.add_line('crotch',(28,34),(20,34))
        self.add_line('left-leg-inner',(20,34),(20,40))
        self.add_arc('left-foot',(20,40),(12,40),radius_x=4)
        self.add_line('left-leg-outer',(12,40),(12,34))
        self.add_arc('left-corner',(12,34),(8,30),radius_x=4)
        self.add_line('left-wall',(8,30),(8,20))
        self.add_contour('outline','dome-left','dome-right','right-wall','right-corner','right-leg-outer','right-foot','right-leg-inner','crotch','left-leg-inner','left-foot','left-leg-outer','left-corner','left-wall',closed=True)
        self.add_line('seam',(8,20),(40,20));self.relate('connect','seam','outline')
        for n,x,tip in [('left',16,12),('right',32,36)]:
            self.add_line('antenna-'+n,(x,8),(tip,4));self.relate('connect','antenna-'+n,'outline')
