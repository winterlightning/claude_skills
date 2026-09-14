"""Fuse Compartment Panel, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd33320b-6dcb-5d9c-9cd5-4c06ab38a4fe'
SOURCE_PATH = 'pictographic-primitives/transportation/fuse compartment_bd33320b-6dcb-5d9c-9cd5-4c06ab38a4fe.svg'
AUTHOR = 'gpt-6'

class FuseCompartmentPanel(Solo48):
    icon_id = 'fuse-compartment-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fuse box', 'fuse', 'compartment', 'electrical', 'car', 'panel', 'circuit', 'maintenance')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('panel','top','tr','right','br','bottom','bl','left','tl',closed=True)
        for i,(x,y) in enumerate(((18,21),(30,27))):
            self.add_polyline(f'circuit-{i}',(x,15),(x,y),(x,33))
            self.add_polyline(f'fuse-{i}',(x-3,y),(x,y),(x+3,y))
            self.relate('connect',f'circuit-{i}',f'fuse-{i}')
