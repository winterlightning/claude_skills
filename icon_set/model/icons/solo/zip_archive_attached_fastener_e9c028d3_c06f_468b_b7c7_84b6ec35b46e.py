"""Compressed Zip Archive File.
Plan: Clipped-corner document owns an attached zipper pull and two separated teeth. Extrema (8,4)-(40,44).
Reference: Lucide file-archive: clipped sheet silhouette and separated zipper details.
Reduction: Three zipper marks reduced to two; fold seam omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9c028d3-c06f-468b-b7c7-84b6ec35b46e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/files/file zip_e9c028d3-c06f-468b-b7c7-84b6ec35b46e.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'zip-archive-attached-fastener'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "files"
    aliases = ()
    keywords = ('compressed', 'zip', 'archive', 'file')

    def build(self):

        self.add_polyline('paper',(8,4),(16,4),(24,4),(30,4),(40,14),(40,44),(8,44),(8,4))
        self.add_line('pull-1',(16, 4),(16, 12))
        self.add_arc('pull-end',(16,12),(24,12),radius_x=4,sweep=False)
        self.add_line('pull-right',(24,12),(24,4))
        self.add_contour('zipper','pull-1','pull-end','pull-right')
        self.relate('connect','paper','zipper')
        for i,y in enumerate((25,35)):self.add_line(f'tooth-{i}',(20,y),(20,y+1))
