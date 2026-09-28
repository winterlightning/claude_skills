# Repair: Focus the selecting hand on one clear avatar. Retain the pointing fingertip; remove the two redundant background people to open the composition.
"""A large hand reaches down toward the central head in a group of three people. Its curved thumb and finger frame the larger middle figure, with smaller busts on either side.
Lucide hand-grab rounded finger construction and user heads. One grasping finger and thumb replace individual fingers; central person and side busts retained. Deliberate asymmetric reaching hand.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5607651d-e737-4878-ba6b-f783c322a934'
SOURCE_PATH = 'pictographic-primitives/work/recruiting employee hand pick_5607651d-e737-4878-ba6b-f783c322a934.svg'
AUTHOR = 'gpt-6'


class HandSelectingPerson(Solo48):
    icon_id = 'hand-selecting-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('hand', 'person', 'selection', 'recruiting', 'team', 'employee')

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'hand',(42,6),('L',(30,6)),('L',(16,16)),('A',4,4,False,(22,22)),('L',(30,16)),('C',(34,16),(37,19),(40,14)))
        ellipse(self,'head',24,34,2)
        path(self,'shoulders',(6,42),('A',18,2,True,(24,40)),('A',18,2,True,(42,42)))
        self.relate('connect','head','shoulders')
