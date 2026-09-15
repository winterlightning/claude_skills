"""Canonical quarter ellipses remove off-grid extremes; valve creases now attach at exact shell nodes.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a23c6ef9-fd90-57c7-ae12-5006686062cd'
SOURCE_PATH = 'pictographic-primitives/animals/shell_a23c6ef9-fd90-57c7-ae12-5006686062cd.svg'
AUTHOR = 'gpt-6'

class ClamShell(Solo48):
    icon_id = 'clam-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('shell', 'clam', 'mussel', 'oyster', 'sea', 'beach', 'bivalve', 'marine')

    def build(self) -> None:
        # SQUARE centerlines (6,6)-(42,42). Asymmetric shell with shared
        # upper/lower radii, one valve crease and a short hinge.
        axis_y, apex_x, left_x, right_x = 24, 14, 6, 42
        for name,a,b,rx in [
         ('top-left',(left_x,axis_y),(apex_x,6),8),
         ('top-right',(apex_x,6),(right_x,axis_y),28),
         ('bottom-right',(right_x,axis_y),(apex_x,42),28),
         ('bottom-left',(apex_x,42),(left_x,axis_y),8)]:
            self.add_arc(name,a,b,radius_x=rx,radius_y=18)
        self.add_contour('shell','top-left','top-right','bottom-right','bottom-left',closed=True)
        self.add_polyline('valve',(apex_x,6),(34,axis_y),(apex_x,42))
        self.add_line('hinge',(left_x,axis_y),(24,axis_y))
        self.relate('connect','valve','shell')
        self.relate('connect','hinge','shell')
