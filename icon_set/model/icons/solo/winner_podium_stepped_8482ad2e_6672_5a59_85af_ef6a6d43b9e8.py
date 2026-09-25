"""An angular winner podium with a tall middle, medium left block and low right block. Retain its unequal step heights and first-place numeral."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8482ad2e-6672-5a59-85af-ef6a6d43b9e8'
SOURCE_PATH = 'pictographic-primitives/rating/ranking winner_8482ad2e-6672-5a59-85af-ef6a6d43b9e8.svg'
AUTHOR = 'gpt-6'

class WinnerPodiumStepped(Solo48):
    icon_id = 'winner-podium-stepped'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "rating"
    aliases = ()
    keywords = ('podium', 'winner', 'ranking', 'first', 'competition', 'leaderboard', 'award', 'victory')

    def circle(self,name,cx,cy,r):
        points=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        for i in range(4):self.add_arc(name+'-'+str(i),points[i],points[i+1],radius_x=r)
        self.add_contour(name,*(name+'-'+str(i) for i in range(4)),closed=True)

    def build(self) -> None:
        # Centerline envelope (4,8)-(44,40); left and right heights differ deliberately.
        self.add_polyline('outline',(4,24),(13,24),(13,8),(35,8),(35,30),(44,30),(44,40),(35,40),(13,40),(4,40),closed=True)
        self.add_line('divider-left',(13,24),(13,40))
        self.add_line('divider-right',(35,30),(35,40))
        self.relate('connect','outline','divider-left');self.relate('connect','outline','divider-right')
        self.add_polyline('one',(22,20),(25,17),(25,30))
