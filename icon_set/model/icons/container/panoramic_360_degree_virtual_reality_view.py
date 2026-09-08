"""A cylindrical panorama frame curves around an immersive view.
Centerline extremes (2,6)-(62,58); near-square landscape fit preserves depth.
No useful direct Lucide match; mirrored ellipse segments and straight side
panels recompose the supplied reference. No features dropped.

Keyshape HRECT_XL; authored directly on CONTAINER64. Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class Panoramic360DegreeVirtualRealityView(Container64):
    icon_id = 'panoramic-360-degree-virtual-reality-view'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('panorama-frame',)
    keywords = ('panoramic', '360', 'degree', 'virtual', 'reality', 'view')

    def build(self) -> None:
        self.add_arc('top',(2,16),(62,16),radius_x=30,radius_y=10)
        self.add_line('right',(62,16),(62,48))
        self.add_arc('bottom-right',(62,48),(50,56),radius_x=30,radius_y=10)
        self.add_arc('bottom-middle',(50,56),(14,56),radius_x=30,radius_y=10)
        self.add_arc('bottom-left',(14,56),(2,48),radius_x=30,radius_y=10)
        self.add_line('left',(2,48),(2,16))
        self.add_contour('outline','top','right','bottom-right','bottom-middle','bottom-left','left',closed=True)
        self.add_polyline('panel-left',(2,16),(14,22),(14,56))
        self.add_polyline('panel-right',(62,16),(50,22),(50,56))
        self.relate('connect','panel-left','outline')
        self.relate('connect','panel-right','outline')
