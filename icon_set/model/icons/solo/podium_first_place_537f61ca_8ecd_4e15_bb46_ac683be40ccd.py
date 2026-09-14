"""A rounded podium with equal-height side blocks and a number one. Keep the three blocks and first-place numeral; share rounded corners and symmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '537f61ca-8ecd-4e15-bb46-ac683be40ccd'
SOURCE_PATH = 'pictographic-primitives/rating/ranking first_537f61ca-8ecd-4e15-bb46-ac683be40ccd.svg'
AUTHOR = 'gpt-6'

class PodiumFirstPlace(Solo48):
    icon_id = 'podium-first-place'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/rating"
    aliases = ()
    keywords = ('podium', 'ranking', 'first', 'winner', 'number-one', 'competition', 'leaderboard', 'award')

    def circle(self,name,cx,cy,r):
        points=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        for i in range(4):self.add_arc(name+'-'+str(i),points[i],points[i+1],radius_x=r)
        self.add_contour(name,*(name+'-'+str(i) for i in range(4)),closed=True)

    def build(self) -> None:
        # Centerline envelope (4,8)-(44,40), central block width20.
        self.add_line('upper-left',(13,26),(13,11))
        self.add_arc('top-left',(13,11),(16,8),radius_x=3)
        self.add_line('top',(16,8),(32,8))
        self.add_arc('top-right',(32,8),(35,11),radius_x=3)
        self.add_line('upper-right',(35,11),(35,26))
        self.add_line('step-right',(35,26),(41,26))
        self.add_arc('outer-right-top',(41,26),(44,29),radius_x=3)
        self.add_line('right',(44,29),(44,37))
        self.add_arc('outer-right-bottom',(44,37),(41,40),radius_x=3)
        self.add_line('bottom-r',(41,40),(35,40))
        self.add_line('bottom-c',(35,40),(13,40))
        self.add_line('bottom-l',(13,40),(7,40))
        self.add_arc('outer-left-bottom',(7,40),(4,37),radius_x=3)
        self.add_line('left',(4,37),(4,29))
        self.add_arc('outer-left-top',(4,29),(7,26),radius_x=3)
        self.add_line('step-left',(7,26),(13,26))
        self.add_contour('outline','upper-left','top-left','top','top-right','upper-right','step-right','outer-right-top','right','outer-right-bottom','bottom-r','bottom-c','bottom-l','outer-left-bottom','left','outer-left-top','step-left',closed=True)
        for x in (13,34):
         self.add_line('divider-'+str(x),(x,26),(x,40));self.relate('connect','outline','divider-'+str(x))
        self.add_polyline('one',(22,20),(25,17),(25,30))
