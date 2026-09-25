"""A large concave sparkle with two smaller glints to the right; preserve the staggered hierarchy.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide sparkles informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fc3d8d53-ffb0-4e83-b7c2-6bbda4286523'
SOURCE_PATH='pictographic-primitives/rewards/reward stars_fc3d8d53-ffb0-4e83-b7c2-6bbda4286523.svg'
AUTHOR='gpt-6'
class SparkleClusterRoundedGlints(Solo48):
    icon_id='sparkle-cluster-rounded-glints'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('reward','celebration','sparkle-cluster-rounded-glints')
    def build(self) -> None:
        def sparkle(name,x,y,r,curve):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=curve,sweep=False)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)
        sparkle('main',16,24,12,12)
        sparkle('upper',37,15,7,21)
        sparkle('lower',39,35,5,20)

