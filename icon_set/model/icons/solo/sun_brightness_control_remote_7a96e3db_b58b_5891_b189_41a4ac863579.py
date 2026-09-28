"""Sun Brightness Control Remote.

Symbol plan: Mirrored rounded remote, header divider and an eight-point solar corona. Centerline extremes (8,4)-(40,44). Radius4 shell corners; x24 axis. A single solar corona replaces the separate center disk and detached rays; the broad central opening stays clear. Header y12 reserves space for the sun.
Source reference: SOURCE_PATH. Lucide originals and atomic-debug layers-2 and
sun informed the layer silhouette and radial brightness mark respectively.
No human or text elements. Preserve this integrated subject from its brief.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a96e3db-b58b-5891-b189-41a4ac863579'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/settings brightness_7a96e3db-b58b-5891-b189-41a4ac863579.svg'
AUTHOR = 'gpt-6'

class SunBrightnessControlRemote(Solo48):
    icon_id = 'sun-brightness-control-remote'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('sun', 'brightness', 'control', 'remote')

    def build(self):
        left,right,top,bottom,r,axis=8,40,4,44,4,24
        self.add_line('top',(left+r,top),(right-r,top))
        self.add_arc('tr',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('right-header',(right,top+r),(right,12))
        self.add_line('right-body',(right,12),(right,bottom-r))
        self.add_arc('br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('bottom',(right-r,bottom),(left+r,bottom))
        self.add_arc('bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('left-body',(left,bottom-r),(left,12))
        self.add_line('left-header',(left,12),(left,top+r))
        self.add_arc('tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('remote','top','tr','right-header','right-body','br','bottom','bl','left-body','left-header','tl',closed=True)
        self.add_line('header',(left,12),(right,12))
        self.relate('connect','remote','header')
        cy=28
        corona=((0,-7),(2,-5),(5,-5),(5,-2),(7,0),(5,2),(5,5),(2,5),
                (0,7),(-2,5),(-5,5),(-5,2),(-7,0),(-5,-2),(-5,-5),(-2,-5))
        self.add_polyline('sun-corona',*((axis+x,cy+y) for x,y in corona),closed=True)
