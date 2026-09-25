"""Head and shoulders with a shallow neckline dip. Lucide user-round informs separate circular head and coherent shoulder curves; paired geometry follows the vertical axis.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='b3632004-2acf-4d40-9c48-d33c4170d1d3'
SOURCE_PATH='pictographic-primitives/symbol/state person_b3632004-2acf-4d40-9c48-d33c4170d1d3.svg'
AUTHOR='gpt-6'

class UserBustSlopedShoulders(Solo48):
    icon_id='user-bust-sloped-shoulders'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('user', 'person', 'profile', 'account', 'avatar', 'member', 'contact', 'people')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.oval('head',24,14,8)
        self.add_line('left-edge',(6,42),(6,40))
        self.add_arc('left-shoulder',(6,40),(18,30),radius_x=12,radius_y=10)
        self.add_arc('neck',(18,30),(30,30),radius_x=10,sweep=False)
        self.add_arc('right-shoulder',(30,30),(42,40),radius_x=12,radius_y=10)
        self.add_line('right-edge',(42,40),(42,42))
        self.add_contour('shoulders','left-edge','left-shoulder','neck','right-shoulder','right-edge')
