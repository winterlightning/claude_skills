"""Three people cluster around a taller central figure. Lucide users informs repeated round heads and open shoulders; hidden rear shoulder segments are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19230a4b-c143-41cf-9599-572150251183'
SOURCE_PATH = 'pictographic-primitives/users/family_19230a4b-c143-41cf-9599-572150251183.svg'
AUTHOR = 'gpt-6'


class FamilyGroup(Solo48):
    icon_id = 'family-group'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
    aliases = ()
    keywords = ('family', 'group', 'people', 'parents', 'children', 'team', 'users', 'together')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-right', top, bottom, radius_x=radius)
        self.add_arc(name+'-left', bottom, top, radius_x=radius)
        self.add_contour(name, name+'-right', name+'-left', closed=True)

    def build(self) -> None:
        # Landscape extremes (6,8)-(42,40); mirrored side figures.
        axis_x, side_offset, side_radius = 24, 16, 3
        self.circle('head-center',axis_x,13,5)
        for side, direction in (('left', -1), ('right', 1)):
            self.circle('head-'+side,axis_x + direction*side_offset,22,side_radius)
        self.add_arc('center-shoulders',(16,36),(32,36),radius_x=8)
        self.add_line('center-left',(16,40),(16,36))
        self.add_line('center-right',(32,36),(32,40))
        self.add_contour('center-body','center-left','center-shoulders','center-right')
        self.add_arc('left-shoulder',(6,38),(8,34),radius_x=4)
        self.add_line('left-side',(6,40),(6,38))
        self.add_contour('left-body','left-side','left-shoulder')
        self.add_arc('right-shoulder',(40,34),(42,38),radius_x=4)
        self.add_line('right-side',(42,38),(42,40))
        self.add_contour('right-body','right-shoulder','right-side')
