"""A large concave sparkle with two smaller glints to the right; preserve the staggered hierarchy.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide sparkles informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5cd9611b-d11a-43b9-a5aa-fec776fd9805'
SOURCE_PATH='pictographic-primitives/rewards/reward stars_5cd9611b-d11a-43b9-a5aa-fec776fd9805.svg'
AUTHOR='gpt-6'
class SparkleClusterCrossGlint(Solo48):
    icon_id='sparkle-cluster-cross-glint'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('reward','celebration','sparkle-cluster-cross-glint')
    def build(self) -> None:
        def sparkle(name,x,y,r,curve):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=curve,sweep=False)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)
        sparkle('main',18,24,14,14)
        self.add_line('glint-v',(39,8),(39,18))
        self.add_line('glint-h',(34,13),(44,13))
        self.relate('connect','glint-v','glint-h')
        sparkle('lower',39,35,5,30)

