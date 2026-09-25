"""Model Sailboat on Stand.

Plan: Two triangular sails above hull and pedestal. Shared mast-to-hull attachment nodes; simplify curved support to single stem. Bounds (6,6)-(42,42). Lucide sailboat informed the subject; the final hull has broad flat-bottomed geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd27157ac-e2d0-460e-b37b-062f54952f22'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/model building_d27157ac-e2d0-460e-b37b-062f54952f22.svg'
AUTHOR = 'gpt-6'

class ModelSailboatOnStand(Solo48):
    icon_id = 'model-sailboat-on-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('model', 'sailboat', 'on', 'stand')

    def build(self):
        self.add_polyline('sail-left',(12,6),(12,18),(24,18),closed=True)
        self.add_polyline('sail-right',(32,6),(32,18),(42,18),closed=True)
        self.add_line('mast-left',(12,18),(12,26));self.add_line('mast-right',(32,18),(32,26))
        self.add_polyline('hull-rim',(6,26),(12,26),(32,26),(42,26))
        self.add_polyline('hull-r',(42,26),(34,34),(24,34))
        self.add_polyline('hull-l',(24,34),(14,34),(6,26))
        self.add_contour('boat','hull-rim-1','hull-rim-2','hull-rim-3','hull-r-1','hull-r-2','hull-l-1','hull-l-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['hull-rim','hull-r','hull-l']]
        self.add_line('stand',(24,34),(24,42));self.add_polyline('foot',(10,42),(24,42),(38,42))
        for a,b in [('sail-left','mast-left'),('sail-right','mast-right'),('mast-left','boat'),('mast-right','boat'),('boat','stand'),('stand','foot')]:self.relate('connect',a,b)
