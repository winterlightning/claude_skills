"""A large concave sparkle with two smaller glints to the right; preserve the staggered hierarchy.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide sparkles informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1072747a-1f2f-4cc0-9f6a-4d899ae345c7'
SOURCE_PATH='pictographic-primitives/rewards/reward stars 1_1072747a-1f2f-4cc0-9f6a-4d899ae345c7.svg'
AUTHOR='gpt-6'
class SparkleClusterThreeStars(Solo48):
    icon_id='sparkle-cluster-three-stars'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('reward','celebration','sparkle-cluster-three-stars')
    def build(self) -> None:
        def sparkle(name,x,y,r,curve):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=curve,sweep=False)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)
        sparkle('main',16,24,12,12)
        sparkle('upper',37,15,7,28)
        sparkle('lower',39,35,5,30)

