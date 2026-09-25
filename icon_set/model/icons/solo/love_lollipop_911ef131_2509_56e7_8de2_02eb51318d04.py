'love-lollipop: independent smooth-curve repair.\n\nConstruction: Heart lollipop with two flowing lobes and a centered stick. Each lobe and shoulder shares tangents.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/heart.svg and atomic-debug/heart.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '911ef131-2509-56e7-8de2-02eb51318d04'
SOURCE_PATH = 'pictographic-primitives/romance/love lollipop_911ef131-2509-56e7-8de2-02eb51318d04.svg'
AUTHOR = 'gpt-6'


class LoveLollipop(Solo48):
    icon_id = 'love-lollipop'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('love', 'lollipop', 'romance')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'heart',(24,30),('C',(18,26),(8,20),(8,13)),('C',(8,8),(12,4),(17,4)),('C',(21,4),(23,7),(24,8)),('C',(25,7),(27,4),(31,4)),('C',(36,4),(40,8),(40,13)),('C',(40,20),(30,26),(24,30)),closed=True)
        line(self,'stick',(24,30),(24,44))
        contacts(self)
