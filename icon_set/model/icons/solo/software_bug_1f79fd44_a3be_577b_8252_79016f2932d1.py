"""A beetle with a divided body, rounded head, two antennae and six legs. Lucide bug informs the paired construction and smooth body. Every leg and antenna remains; anatomy mirrors around x=24.
SOLO48 SQUARE; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='1f79fd44-a3be-577b-8252-79016f2932d1'
SOURCE_PATH='pictographic-primitives/programing/computer bug_1f79fd44-a3be-577b-8252-79016f2932d1.svg'
AUTHOR='gpt-6'

class SoftwareBug(Solo48):
    icon_id='software-bug'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('bug', 'beetle', 'debug', 'error', 'insect', 'software', 'defect', 'issue')

    def build(self) -> None:
        self.add_line('shoulder',(14,20),(24,20))
        self.add_line('shoulder-right',(24,20),(34,20))
        self.add_line('right-upper',(34,20),(34,30))
        self.add_line('right-lower',(34,30),(34,32))
        self.add_arc('body-lower-right',(34,32),(32,38),radius_x=10)
        self.add_arc('body-tip-right',(32,38),(24,42),radius_x=10)
        self.add_arc('body-tip-left',(24,42),(16,38),radius_x=10)
        self.add_arc('body-lower-left',(16,38),(14,32),radius_x=10)
        self.add_line('left-lower',(14,32),(14,30))
        self.add_line('left-upper',(14,30),(14,20))
        self.add_contour('body','shoulder','shoulder-right','right-upper','right-lower','body-lower-right','body-tip-right','body-tip-left','body-lower-left','left-lower','left-upper',closed=True)
        self.add_arc('head-left',(14,20),(18,12),radius_x=10)
        self.add_arc('head-top',(18,12),(30,12),radius_x=10)
        self.add_arc('head-right',(30,12),(34,20),radius_x=10)
        self.add_contour('head','head-left','head-top','head-right')
        self.relate('connect','body','head')
        self.add_line('wing-seam',(24,20),(24,42))
        self.relate('connect','body','wing-seam')
        for side,mirror in (('left',False),('right',True)):
            def p(x,y): return (48-x if mirror else x,y)
            self.add_line(side+'-antenna',p(18,12),p(14,6))
            self.relate('connect',side+'-antenna','head')
            self.add_polyline(side+'-front-leg',p(14,20),p(6,16),p(6,12))
            self.add_line(side+'-middle-leg',p(14,30),p(6,30))
            self.add_line(side+'-rear-leg',p(16,38),p(6,42))
            for leg in ('front','middle','rear'):
                self.relate('connect',side+'-'+leg+'-leg','body')
            self.relate('connect',side+'-front-leg','head')
