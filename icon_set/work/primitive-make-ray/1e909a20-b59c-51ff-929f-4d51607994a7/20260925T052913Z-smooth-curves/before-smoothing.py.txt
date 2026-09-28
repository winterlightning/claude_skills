"""Fresh reconstruction of man doctor from the supplied reference.
Construction references: human_ref/user.svg and Lucide stethoscope. Symbol plan recorded in build().
Profile SOLO48, keyshape SQUARE; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1e909a20-b59c-51ff-929f-4d51607994a7'
SOURCE_PATH = 'pictographic-primitives/avatars/man doctor_1e909a20-b59c-51ff-929f-4d51607994a7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'doctor-with-stethoscope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'doctor')

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
        # Shared human_ref bust: radius-8 head, tangent ink at y=24.
        self.add_arc('crown-left',(16,14),(24,6),radius_x=8)
        self.add_arc('crown-right',(24,6),(32,14),radius_x=8)
        self.add_arc('jaw',(32,14),(16,14),radius_x=8)
        self.add_contour('head','crown-left','crown-right','jaw',closed=True)
        self.add_line('left-side',(6,42),(6,36))
        self.add_arc('left-shoulder',(6,36),(16,26),radius_x=10)
        self.add_line('body-top',(16,26),(24,26))
        self.add_polyline('body-top-right',(24,26),(30,26),(32,26))
        self.contours[:] = [c for c in self.contours if c.contour_id != 'body-top-right']
        self.add_arc('right-shoulder',(32,26),(42,36),radius_x=10)
        self.add_line('right-side',(42,36),(42,42))
        self.add_contour('shoulders','left-side','left-shoulder','body-top','body-top-right-1','body-top-right-2','right-shoulder','right-side')
        self.relate('connect','head','shoulders')
        # Left chestpiece and right open earpiece restore the reference asymmetry.
        self.add_line('left-tube',(16,26),(16,36))
        self.add_arc('chestpiece-upper-right',(16,36),(18,38),radius_x=2)
        self.add_arc('chestpiece-lower-right',(18,38),(16,40),radius_x=2)
        self.add_arc('chestpiece-lower-left',(16,40),(14,38),radius_x=2)
        self.add_arc('chestpiece-upper-left',(14,38),(16,36),radius_x=2)
        self.add_contour('chestpiece','chestpiece-upper-right','chestpiece-lower-right','chestpiece-lower-left','chestpiece-upper-left',closed=True)
        self.relate('connect','left-tube','body-top','left-shoulder')
        self.relate('connect','left-tube','chestpiece')
        self.add_line('right-tube',(30,26),(30,34))
        self.add_arc('earpiece-cap-left',(26,38),(30,34),radius_x=4)
        self.add_arc('earpiece-cap-right',(30,34),(34,38),radius_x=4)
        self.add_contour('earpiece-top','earpiece-cap-left','earpiece-cap-right')
        self.add_line('earpiece-left',(26,38),(26,42))
        self.add_line('earpiece-right',(34,38),(34,42))
        self.add_contour('earpiece','earpiece-left')
        self.relate('connect','right-tube','shoulders')
        self.relate('connect','right-tube','earpiece-top')
        self.relate('connect','earpiece-top','earpiece-left')
        self.relate('connect','earpiece-top','earpiece-right')
