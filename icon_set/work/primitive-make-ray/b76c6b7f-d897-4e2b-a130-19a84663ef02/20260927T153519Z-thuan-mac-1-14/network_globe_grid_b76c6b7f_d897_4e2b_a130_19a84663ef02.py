"""Network Globe. Authored from the supplied visual brief."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b76c6b7f-d897-4e2b-a130-19a84663ef02'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__network-globe-grid/20260927T153322Z-thuan-mac-1/reference/network globe_b76c6b7f-d897-4e2b-a130-19a84663ef02.svg'
AUTHOR = "gpt-6"

class NetworkGlobeGrid(Solo48):
    icon_id = 'network-globe-grid'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    categories = ("websites", "primitives")
    aliases = ()
    keywords = ('globe', 'network', 'world', 'internet', 'sphere', 'grid', 'web')

    def build(self):
        # True circular globe with three straight parallels and one central meridian.
        cardinal=((24,4),(44,24),(24,44),(4,24))
        for n,start in enumerate(cardinal):
            self.add_arc(f'outline-{n}', start, cardinal[(n+1)%4], radius_x=20, sweep=True)
        self.add_contour('globe', *(f'outline-{n}' for n in range(4)), closed=True)
        self.add_line('meridian', (24,4), (24,44))
        self.relate('connect','globe','meridian')
        for y,x0,x1 in ((16,16,32),(24,4,44),(32,16,32)):
            self.add_line(f'parallel-{y}', (x0,y), (x1,y))
            if y==24: self.relate('connect','globe',f'parallel-{y}')
            self.relate('connect','meridian',f'parallel-{y}')
