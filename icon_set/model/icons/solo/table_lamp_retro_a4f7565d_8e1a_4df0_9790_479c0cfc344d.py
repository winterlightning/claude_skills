"""table-lamp-retro: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4f7565d-8e1a-4df0-9790-479c0cfc344d'
SOURCE_PATH = 'pictographic-primitives/outdoors/table lamp retro_a4f7565d-8e1a-4df0-9790-479c0cfc344d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TableLampRetro(Solo48):
    icon_id = 'table-lamp-retro'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('table', 'lamp', 'retro', 'outdoors')

    def build(self):
        # Plan: VRECT_L; elliptical dome, reflected scallops and centered stem; preserve the decorative rim.
        # Reference: Geometric dome and mirrored rim waves.
        self.add_arc('dome-left',(8,24),(24,6),radius_x=16,radius_y=18)
        self.add_arc('dome-right',(24,6),(40,24),radius_x=16,radius_y=18)
        self.add_bezier('rim-right',(40,24),((37,20),(35,20),(32,24)),((29,28),(27,24),(24,22)))
        self.add_bezier('rim-left',(24,22),((21,24),(19,28),(16,24)),((13,20),(11,20),(8,24)))
        self.add_contour('shade','dome-left','dome-right','rim-right','rim-left',closed=True)
        self.add_line('finial',(24,4),(24,6))
        self.add_line('stem',(24,22),(24,44))
        self.add_line('foot',(16,44),(32,44))
        self.relate('connect','finial','shade')
        self.relate('connect','stem','shade')
        self.relate('connect','stem','foot')
