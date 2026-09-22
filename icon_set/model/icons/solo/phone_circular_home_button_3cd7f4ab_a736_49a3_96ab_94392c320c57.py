"""Phone with circular home button. VRECT_M preserves the tall device.
Shared radius 4 corners, symmetric about x=24. The source provides the home
button; Lucide smartphone supplies the single rounded enclosure principle.
Omit bezel separators to preserve a large clear screen and an open button hole.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cd7f4ab-a736-49a3-96ab-94392c320c57'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/mobile_3cd7f4ab-a736-49a3-96ab-94392c320c57.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'phone-circular-home-button'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Smartphone with Home Button',)
    keywords = ('phone','smartphone','screen','mobile','device','button')
    def build(self):
        l,t,r,b,rad=10,4,38,44,4
        points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        for i,(a,z) in enumerate(zip(points,points[1:])):
            if i%2:self.add_arc(f'case-{i}',a,z,radius_x=rad)
            else:self.add_line(f'case-{i}',a,z)
        self.add_contour('case',*[f'case-{i}' for i in range(8)],closed=True)
        self.add_arc('button-a',(21,32),(27,32),radius_x=3)
        self.add_arc('button-b',(27,32),(21,32),radius_x=3)
        self.add_contour('button','button-a','button-b',closed=True)
