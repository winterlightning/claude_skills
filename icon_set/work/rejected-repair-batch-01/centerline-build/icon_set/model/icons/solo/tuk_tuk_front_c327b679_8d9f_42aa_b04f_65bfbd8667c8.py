"""tuk-tuk-front: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c327b679-8d9f-42aa-b04f-65bfbd8667c8'
SOURCE_PATH = 'pictographic-primitives/transportation/tuk tuk 1_c327b679-8d9f-42aa-b04f-65bfbd8667c8.svg'
AUTHOR = 'gpt-6'


class TukTukFront(Solo48):
    icon_id = 'tuk-tuk-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('tuk tuk', 'auto rickshaw', 'rickshaw', 'three wheeler', 'taxi', 'asia', 'vehicle', 'front')

    def build(self) -> None:

        # Broad canopy, paired headlamps and three distinct tyre stubs about x=24.
        self.add_polyline('visor',(6,6),(16,6),(32,6),(42,6))
        self.add_line('canopy-left',(16,6),(12,20))
        self.add_line('canopy-right',(32,6),(36,20))
        self.add_polyline('body',(8,20),(12,20),(36,20),(40,20),(40,38),(24,38),(8,38),closed=True)
        self.add_dot('lamp-left',(17,29))
        self.add_dot('lamp-right',(31,29))
        self.add_line('tyre-left',(8,38),(8,40))
        self.add_line('tyre-right',(40,38),(40,40))
        self.add_line('tyre-front',(24,38),(24,42))
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
