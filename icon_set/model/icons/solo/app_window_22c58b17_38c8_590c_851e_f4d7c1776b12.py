'Application window: enlarge the toolbar band to accommodate three evenly spaced app dots with clear margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22c58b17-38c8-590c-851e-f4d7c1776b12'
SOURCE_PATH = 'icons-json/apps/app window_22c58b17-38c8-590c-851e-f4d7c1776b12.json'
AUTHOR = 'gpt-6'

class AppWindowApps(Solo48):
    icon_id = 'app-window-apps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('app', 'window', 'apps')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 6, 6, 42, 42, 4
        self.add_line('frame-top', (left+radius,top), (right-radius,top))
        self.add_arc('frame-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('frame-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('frame-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('frame-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('frame-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('frame-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('frame-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('frame', *('frame-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_line('toolbar',(6,24),(42,24));self.relate('connect','toolbar','frame')
        for i,x in enumerate((15,24,33)):self.add_dot(f'app-{i}',(x,15))
