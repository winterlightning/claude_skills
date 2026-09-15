'robot-e46fb630: independent smooth-curve repair.\n\nConstruction: Robot head with four coherent round corners, matched eye strokes and central antenna.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bot.svg and atomic-debug/bot.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e46fb630-ba38-428c-8b2e-adf342a25e31'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_e46fb630-ba38-428c-8b2e-adf342a25e31.svg'
AUTHOR = 'gpt-6'


class RobotE46fb630(Solo48):
    icon_id = 'robot-e46fb630'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'head',4,16,44,40,7,xs=(24,))
        line(self,'antenna',(24,8),(24,16))
        line(self,'eye-left',(17,25),(17,29));line(self,'eye-right',(31,25),(31,29))
        contacts(self)
