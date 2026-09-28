"""traction-control-skid: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81496b35-55f6-45f3-ab52-1d6bafb98ffc'
SOURCE_PATH = 'pictographic-primitives/transportation/traction control_81496b35-55f6-45f3-ab52-1d6bafb98ffc.svg'
AUTHOR = 'gpt-6'


class TractionControlSkid(Solo48):
    icon_id = 'traction-control-skid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('traction control', 'skid', 'slippery', 'esp', 'stability', 'dashboard', 'car', 'warning')

    def build(self) -> None:

        # Shared front-view cabin and body; motion context is detached below.
        self.add_polyline('cabin',(12,14),(16,6),(32,6),(36,14))
        self.add_polyline('body',(6,14),(12,14),(36,14),(42,14),(42,22),(34,22),(14,22),(6,22),closed=True)

        # Two identical S-shaped tracks with shared radii and vertical spacing.
        for i,x in enumerate([14,34]):
            self.add_arc(f'skid-{i}-upper',(x,33),(x,37),radius_x=2,radius_y=2)
            self.add_arc(f'skid-{i}-lower-a',(x,37),(x-2,39),radius_x=2,sweep=False)
            self.add_arc(f'skid-{i}-lower-b',(x-2,39),(x,42),radius_x=2,radius_y=3,sweep=False)
            self.add_contour(f'skid-{i}',f'skid-{i}-upper',f'skid-{i}-lower-a',f'skid-{i}-lower-b')
        for i,x in enumerate([14,34]): self.add_line(f'tyre-{i}',(x,22),(x,24))
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
