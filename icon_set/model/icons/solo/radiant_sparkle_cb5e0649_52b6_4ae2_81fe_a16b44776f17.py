"""A four-point sparkle surrounded by eight detached rays.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide sparkles and sun informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='cb5e0649-52b6-4ae2-81fe-a16b44776f17'
SOURCE_PATH='pictographic-primitives/rewards/reward stars_cb5e0649-52b6-4ae2-81fe-a16b44776f17.svg'
AUTHOR='gpt-6'
class RadiantSparkle(Solo48):
    icon_id='radiant-sparkle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('reward','celebration','radiant-sparkle')
    def build(self) -> None:
        def sparkle(name,x,y,r,curve):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=curve,sweep=False)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)
        sparkle('center',24,24,8,18)
        for name,a,b in [('n',(24,6),(24,7)),('s',(24,41),(24,42)),('w',(6,24),(7,24)),('e',(41,24),(42,24)),('nw',(8,8),(12,12)),('ne',(40,8),(36,12)),('sw',(8,40),(12,36)),('se',(40,40),(36,36))]:
            self.add_line(name,a,b)

