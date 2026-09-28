"""Virtual Reality Goggles.

Symbol plan: VR goggles with broad empty visor, shallow central nose notch and two short single-stroke side straps. Shared x=24 axis and radius-6 outer corners. Lucide glasses informs paired contour balance. Drop hollow strap interiors.
Keyshape HRECT_M; exact visible bounds (2, 8, 46, 40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b855886b-3199-52ae-a327-5e124680a94d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-vr-goggles-with-short-side-straps/20260927T084430Z-thuan-mac-1/reference/device wearable vr goggles_b855886b-3199-52ae-a327-5e124680a94d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'virtual-reality-goggles'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('devices', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('virtual', 'reality', 'goggles')

    def build(self):
        self.add_line('top',(14,10),(34,10));self.add_arc('tr',(34,10),(40,16),radius_x=6)
        self.run('right',(40,16),(40,24),(40,32));self.add_arc('br',(40,32),(34,38),radius_x=6)
        self.add_line('bottom-r',(34,38),(32,38));self.add_arc('nose-r',(32,38),(29,34),radius_x=6)
        self.add_arc('nose',(29,34),(19,34),radius_x=6,sweep=False)
        self.add_arc('nose-l',(19,34),(16,38),radius_x=6);self.add_line('bottom-l',(16,38),(14,38))
        self.add_arc('bl',(14,38),(8,32),radius_x=6);self.run('left',(8,32),(8,24),(8,16));self.add_arc('tl',(8,16),(14,10),radius_x=6)
        self.add_contour('visor','top','tr','right-1','right-2','br','bottom-r','nose-r','nose','nose-l','bottom-l','bl','left-1','left-2','tl',closed=True)
        for i,(a,b) in enumerate([((4,24),(8,24)),((40,24),(44,24))]):
            self.add_line(f'strap-{i}',a,b);self.relate('connect',f'strap-{i}','visor')

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'{name}-{i}',a,b)
