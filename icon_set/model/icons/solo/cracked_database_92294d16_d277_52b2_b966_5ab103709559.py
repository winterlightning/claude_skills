"""A database cylinder with a jagged structural fracture through its rim and band. Lucide database informs ellipse construction. Two source bands reduce to one; the crack shares exact top, rim and band points. The crack is intentionally asymmetric.
SOLO48 HRECT_L; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='92294d16-d277-52b2-b966-5ab103709559'
SOURCE_PATH='pictographic-primitives/programing/digital policies data breach broken_92294d16-d277-52b2-b966-5ab103709559.svg'
AUTHOR='gpt-6'

class CrackedDatabase(Solo48):
    icon_id='cracked-database'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('database', 'broken', 'crack', 'breach', 'data', 'failure', 'storage', 'damaged')

    def build(self) -> None:
        self.add_arc('rim-back-left',(4,13),(24,8),radius_x=20,radius_y=5)
        self.add_arc('rim-back-right',(24,8),(44,13),radius_x=20,radius_y=5)
        self.add_arc('rim-front-right',(44,13),(24,18),radius_x=20,radius_y=5)
        self.add_arc('rim-front-left',(24,18),(4,13),radius_x=20,radius_y=5)
        self.add_contour('rim','rim-back-left','rim-back-right','rim-front-right','rim-front-left',closed=True)
        self.add_line('right-wall-1',(44,13),(44,23))
        self.add_line('right-wall-2',(44,23),(44,35))
        self.add_arc('bottom',(44,35),(4,35),radius_x=20,radius_y=5)
        self.add_line('left-wall-1',(4,35),(4,23))
        self.add_line('left-wall-2',(4,23),(4,13))
        self.add_contour('body','right-wall-1','right-wall-2','bottom','left-wall-1','left-wall-2')
        self.add_arc('band-right',(44,23),(24,28),radius_x=20,radius_y=5)
        self.add_arc('band-left',(24,28),(4,23),radius_x=20,radius_y=5)
        self.add_contour('band','band-right','band-left')
        self.add_polyline('fracture',(24,8),(20,13),(24,18),(20,23),(24,28))
        for a,b in (('rim','body'),('band','body'),('fracture','rim'),('fracture','band')):
            self.relate('connect',a,b)
