"""Zipped File Folder."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0969fca0-82ca-4fc8-9ddd-639a72983173'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/folders/file zip_0969fca0-82ca-4fc8-9ddd-639a72983173.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'zipped-folder-tall'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/files'
    aliases = ()
    keywords = ('folder', 'zip', 'zipper', 'archive', 'file', 'storage', 'document')

    def build(self):
        # Plan: Upright tabbed folder, attached pull, shortened zipper run. Lucide folder-archive. Bounds (8,4)-(40,44).
        left,right,top,bottom,tab,shoulder,r = 8,40,4,44,14,12,4
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

        self.add_line('pull-left',(24,shoulder),(24,shoulder+6))
        self.add_arc('pull-bottom',(24,shoulder+6),(32,shoulder+6),radius_x=4,sweep=False)
        self.add_line('pull-right',(32,shoulder+6),(32,shoulder))
        self.add_contour('pull','pull-left','pull-bottom','pull-right')
        self.relate('connect','pull','folder')
        self.add_line('zip-teeth',(28,shoulder+19),(28,shoulder+20))
