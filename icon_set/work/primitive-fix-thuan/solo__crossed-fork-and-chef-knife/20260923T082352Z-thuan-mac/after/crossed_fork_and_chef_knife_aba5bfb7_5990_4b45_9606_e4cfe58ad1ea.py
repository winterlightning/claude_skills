"""Crossed Fork and Knife."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba5bfb7-5990-4b45-9606-e4cfe58ad1ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/symbol fork cross knife_aba5bfb7-5990-4b45-9606-e4cfe58ad1ea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-fork-and-chef-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('fork', 'knife', 'cutlery', 'utensil', 'crossed', 'dining', 'kitchen')

    def build(self):
        # Plan: three parallel fork tines and straight diagonal shafts sharing
        # (24,24). SQUARE centerline extremes (6,6)-(42,42).
        # Lucide utensils-crossed: coherent U-shaped fork and a shared crossing.
        # The different utensil heads deliberately remain asymmetric.
        self.add_line('fork-left-tine',(6,18),(10,22))
        self.add_bezier('fork-left-curve',(10,22),((13,25),(17,23),(20,20)))
        self.add_bezier('fork-right-curve',(20,20),((23,17),(25,13),(22,10)))
        self.add_line('fork-right-tine',(22,10),(18,6))
        self.add_contour('fork-head','fork-left-tine','fork-left-curve',
                         'fork-right-curve','fork-right-tine')
        self.add_line('fork-middle-tine',(12,12),(20,20))
        self.add_polyline('fork-handle',(20,20),(24,24),(42,42))
        self.relate('connect','fork-head','fork-middle-tine')
        self.relate('connect','fork-head','fork-handle')
        self.relate('connect','fork-middle-tine','fork-handle')

        self.add_polyline('knife-handle',(6,42),(24,24),(30,18))
        self.add_line('knife-spine',(30,18),(42,6))
        self.add_bezier('knife-edge',(42,6),((42,14),(42,18),(36,24)))
        self.add_line('knife-heel',(36,24),(30,18))
        self.add_contour('knife-blade','knife-spine','knife-edge','knife-heel',closed=True)
        self.relate('connect','knife-handle','knife-blade')
        self.relate('connect','knife-handle','fork-handle')
