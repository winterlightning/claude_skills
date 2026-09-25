"""Three Different Writing Pens.

Symbol plan: Three parallel writing tools on shared 16-unit pitch, 8-unit body width; distinct broad, tapered and needle points. Omit small clips and nib slit to preserve spacing.
Keyshape: HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fda97562-f1db-4338-8a72-deba11736c45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pens_fda97562-f1db-4338-8a72-deba11736c45.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-writing-pens-with-distinct-nibs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('three', 'different', 'writing', 'pens')

    def build(self):
        for i in range(3):
            x=8+i*16; left=x-4; right=x+4
            end=(24,24,30)[i]
            if i==1:
                self.add_line('middle-left',(left,end),(left,12))
                self.add_arc('middle-cap',(left,12),(right,12),radius_x=4)
                self.add_line('middle-right',(right,12),(right,end))
                self.add_contour('body-1','middle-left','middle-cap','middle-right')
            else:
                self.add_polyline(f'body-{i}',(left,end),(left,8),(right,8),(right,end))
            if i==0:
                self.add_polyline('nib',(left,end),(left,32),(x,40),(right,32),(right,end))
                self.add_line('nib-collar',(left,end),(right,end))
                self.relate('connect','nib-collar','body-0')
                self.relate('connect','nib-collar','nib')
            elif i==1:
                self.add_polyline('taper',(left,end),(x,40),(right,end))
            else:
                self.add_line('end',(left,end),(right,end));self.relate('connect',f'body-{i}','end')
                self.add_line('needle',(x,end),(x,40));self.relate('connect','end','needle')
            if i<2: self.relate('connect',f'body-{i}',('nib','taper')[i])
