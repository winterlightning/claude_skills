"""A person strides right with a tied bundle carried on a shoulder stick. Lucide person-standing informs the stride. The knot and fingers are reduced; the bundle and carrying pole remain distinct physical parts."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cabc5985-10ec-4ff6-97df-f2868406a44f'
SOURCE_PATH = 'pictographic-primitives/users/user homeless poverty 1_cabc5985-10ec-4ff6-97df-f2868406a44f.svg'
AUTHOR = 'gpt-6'


class PersonWithBindle(Solo48):
    icon_id = 'person-with-bindle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('homeless', 'bindle', 'walking', 'traveller', 'person', 'bundle', 'poverty', 'wanderer')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)


    def build(self) -> None:
        # Portrait centerline extremes (8,6)-(40,42); forward-leaning walking posture.
        self.circle('head',34,10,6)
        self.add_line('bundle-left',(13,6),(8,16))
        self.add_arc('bundle-bottom',(8,16),(18,16),radius_x=5,sweep=False)
        self.add_line('bundle-right',(18,16),(13,6))
        self.add_contour('bundle','bundle-left','bundle-bottom','bundle-right',closed=True)
        self.add_line('pole',(13,6),(26,26))
        self.relate('connect','bundle','pole')
        self.add_line('torso',(26,26),(24,34))
        self.add_polyline('arm',(26,26),(33,31),(39,27))
        self.add_polyline('legs',(16,42),(24,34),(32,37),(40,42))
        self.relate('connect','pole','torso')
        self.relate('connect','pole','arm')
        self.relate('connect','torso','arm')
        self.relate('connect','torso','legs')
