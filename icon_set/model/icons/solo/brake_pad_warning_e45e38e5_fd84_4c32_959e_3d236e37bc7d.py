"""brake-pad-warning: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e45e38e5-fd84-4c32-959e-3d236e37bc7d'
SOURCE_PATH = 'pictographic-primitives/transportation/worn brake pads warning_e45e38e5-fd84-4c32-959e-3d236e37bc7d.svg'
AUTHOR = 'gpt-6'


class BrakePadWarning(Solo48):
    icon_id = 'brake-pad-warning'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('brake pads', 'brake', 'worn', 'warning', 'dashboard', 'car', 'disc brake', 'maintenance')

    def build(self) -> None:

        # Concentric disc and four diagonal pad arcs; all share the centre (24,24).
        self.add_arc('disc-top',(13,24),(35,24),radius_x=11)
        self.add_arc('disc-bottom',(35,24),(13,24),radius_x=11)
        self.add_contour('disc','disc-top','disc-bottom',closed=True)
        pads=[((8,12),(12,8)),((36,8),(40,12)),((40,36),(36,40)),((12,40),(8,36))]
        for i,(start,end) in enumerate(pads): self.add_arc(f'pad-{i}',start,end,radius_x=20)
        # Declare only true junctions, where endpoint coordinates match exactly.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
