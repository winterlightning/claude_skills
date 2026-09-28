"""Folder with Bookmark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '930dd44e-6822-5bd4-aa80-2235589f118e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/folders/folder bookmark_930dd44e-6822-5bd4-aa80-2235589f118e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folder-with-hanging-bookmark'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    categories = ('folders', 'primitives')
    aliases = ()
    keywords = ('folder', 'bookmark', 'ribbon', 'file', 'save', 'storage', 'document')

    def build(self):
        # Plan: Folder owns an attached bookmark with centered V notch. Lucide folder-bookmark, with matched ribbon sides. Bounds (4,8)-(44,40).
        left,right,top,bottom,tab,shoulder,r = 4,44,8,40,14,14,4
        self.add_line('tab-top',(left+r,top),(tab,top))
        self.add_bezier('tab-step',(tab,top),((tab+3,top),(tab+3,shoulder),(tab+6,shoulder)))
        self.add_line('top-1',(tab+6,shoulder),(24,shoulder))
        self.add_line('top-2',(24,shoulder),(32,shoulder))
        self.add_line('top-3',(32,shoulder),(right-r,shoulder))
        self.add_arc('tr',(right-r,shoulder),(right,shoulder+r),radius_x=r)
        self.add_line('right',(right,shoulder+r),(right,bottom-r))
        self.add_arc('br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('base',(right-r,bottom),(left+r,bottom))
        self.add_arc('bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('left',(left,bottom-r),(left,top+r))
        self.add_arc('tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('folder','tab-top','tab-step','top-1','top-2','top-3','tr','right','br','base','bl','left','tl',closed=True)

        self.add_polyline('bookmark',(24,14),(24,29),(28,25),(32,29),(32,14))
        self.relate('connect','bookmark','folder')
