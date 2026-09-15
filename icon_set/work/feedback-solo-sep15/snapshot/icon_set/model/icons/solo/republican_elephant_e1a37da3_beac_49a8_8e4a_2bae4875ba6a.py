"""Broad back, divided body, block legs, and upturned trunk retained; no useful Lucide elephant match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1a37da3-beac-49a8-8e4a-2bae4875ba6a'
SOURCE_PATH = 'pictographic-primitives/school-learning/election republican_e1a37da3-beac-49a8-8e4a-2bae4875ba6a.svg'
AUTHOR = 'gpt-6'


class RepublicanElephant(Solo48):
    icon_id = 'republican-elephant'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('elephant', 'republican', 'election', 'animal', 'politics', 'symbol')

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name+'-head',x,y,r)
        self.add_arc(name+'-sl',(x-width,y+7),(x,y+r),radius_x=width,radius_y=7-r)
        self.add_arc(name+'-sr',(x,y+r),(x+width,y+7),radius_x=width,radius_y=7-r)
        self.add_contour(name+'-shoulders',name+'-sl',name+'-sr')
        self.relate('connect',name+'-head',name+'-shoulders')

    def build(self) -> None:
        # Bounds are derived from the live SOLO48 contract, not the stale skill table.

        self.add_arc('back-left',(4,20),(16,8),radius_x=12)
        self.add_line('back',(16,8),(24,8))
        self.add_arc('back-right',(24,8),(36,20),radius_x=12)
        self.add_line('trunk-inner',(36,20),(36,34))
        self.add_arc('trunk-turn',(36,34),(44,34),radius_x=4,sweep=False)
        self.add_line('trunk-tip',(44,34),(44,30))
        self.add_contour('back-trunk','back-left','back','back-right','trunk-inner','trunk-turn','trunk-tip')
        self.add_polyline('legs',(4,20),(4,40),(12,40),(12,30),(20,30),(20,40),(28,40),(28,28))
        self.relate('connect','legs','back-trunk')
        self.add_line('body-division',(4,20),(36,20))
        self.relate('connect','body-division','back-trunk')
        self.relate('connect','body-division','legs')
