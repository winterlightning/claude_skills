"""An isometric box has an inset panel in its right face. Shared vertices own perspective edges. VRECT_L gives the roof a measurable opening and the inset panel 8-unit clearances. The right face is broadened while retaining all three faces and the inset panel. Lucide box supplies single silhouette and shared corner construction; source supplies inset side panel.
Plan: exact VRECT_L envelope; stroke 4, integer points, shared attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0243a57-ed91-4e54-aa5f-ad0799040a66'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon elastic container registry_b0243a57-ed91-4e54-aa5f-ad0799040a66.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'isometric-box-with-a-side-panel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = []
    keywords = ['isometric', 'box', 'with', 'a', 'side', 'panel']

    def build(self):
        points=[(8,10),(24,4),(40,10),(40,38),(16,44),(8,38)]
        for i,a in enumerate(points): self.add_line(f'outer-{i}',a,points[(i+1)%6])
        self.add_contour('outer',*[f'outer-{i}' for i in range(6)],closed=True)
        self.add_line('edge-left',(8,10),(16,16))
        self.add_line('edge-right',(16,16),(40,10))
        self.add_line('edge-down',(16,16),(16,44))
        self.relate('connect','edge-left','edge-right','edge-down')
        self.relate('connect','edge-left','outer-0','outer-5')
        self.relate('connect','edge-right','outer-1','outer-2')
        self.relate('connect','edge-down','outer-3','outer-4')
        self.add_polyline('panel',(24,23),(32,21),(32,30),(24,32),closed=True)
