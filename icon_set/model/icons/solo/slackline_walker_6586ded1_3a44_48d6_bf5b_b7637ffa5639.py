"""Slackline Walker. Figure balances with spread arms and one raised knee on a gently sagging slackline; retain the asymmetric balance pose.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6586ded1-3a44-48d6-bf5b-b7637ffa5639'
SOURCE_PATH = 'pictographic-primitives/recreation/sport slack lining_6586ded1-3a44-48d6-bf5b-b7637ffa5639.svg'
AUTHOR = 'gpt-6'


class SlacklineWalker(Solo48):
    icon_id = 'slackline-walker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('slackline', 'walker')

    def build(self) -> None:
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arms-1', (8, 18), (22, 22))
        self.add_line('arms-2', (22, 22), (38, 15))
        self.add_contour('arms', 'arms-1', 'arms-2', closed=False)
        self.add_line('torso-1', (22, 22), (24, 32))
        self.add_line('torso-2', (24, 32), (24, 42))
        self.add_contour('torso', 'torso-1', 'torso-2', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_line('raised-leg-1', (24, 32), (34, 30))
        self.add_line('raised-leg-2', (34, 30), (38, 36))
        self.add_contour('raised-leg', 'raised-leg-1', 'raised-leg-2', closed=False)
        self.relate("connect", 'raised-leg', 'torso')
        self.add_arc('line-left', (6, 38), (24, 42), radius_x=42, radius_y=42, sweep=True)
        self.add_arc('line-right', (24, 42), (42, 38), radius_x=42, radius_y=42, sweep=True)
        self.add_contour('slackline', 'line-left', 'line-right', closed=False)
        self.relate("connect", 'slackline', 'torso')
