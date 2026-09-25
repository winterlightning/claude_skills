"""A person works behind a laptop beside a beach palm. Natural scene, no modifier split. HRECT_L 4..44 x 8..40 supports left tree and right person. Source supplies layout; human_ref/full_body_ref.png supplies round head, Lucide laptop supplies simple panel silhouette. Head r5 at33,14; torso starts33,27 for exact 8 centerline gap. Omit laptop logo, shoreline ripples and extra fronds; keep palm trunk and two arching fronds."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '6d4dd61f-6a26-4fe2-9153-8e53f8a73a5d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/digital nomad beach_6d4dd61f-6a26-4fe2-9153-8e53f8a73a5d.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'laptop-worker-beside-beach-palm'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Laptop Worker Beside Beach Palm']
    keywords = ['laptop', 'worker', 'beach', 'palm', 'person', 'computer', 'remote']
    def build(self):
        self.add_arc('head-a',(28,14),(38,14),radius_x=5)
        self.add_arc('head-b',(38,14),(28,14),radius_x=5)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_bezier('torso',(33,27),((39,27),(44,32),(44,40)))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('laptop',(4,30),(24,30),(28,40),(8,40),closed=True)
        self.add_bezier('palm-left',(4,8),((8,8),(10,8),(13,12)))
        self.add_bezier('palm-right',(13,12),((16,8),(18,8),(20,8)))
        self.add_bezier('trunk',(13,12),((10,16),(10,18),(10,22)))
        self.relate('connect','palm-left','palm-right','trunk')
