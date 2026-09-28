"""Network (networks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1e9f2473-7774-5d81-917a-5de0d098f445'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__network/20260927T153322Z-thuan-mac-1/reference/network_1e9f2473-7774-5d81-917a-5de0d098f445.svg'
AUTHOR = "gpt-6"

class Network(Solo48):
    icon_id = 'network'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    categories = ('primitives', 'networks')
    aliases = ()
    keywords = ('network', 'networks')

    def build(self):
        # One parent circle and three equal child circles on a shared bus.
        def ring(name, x, y):
            self.add_arc(name+'-a', (x,y-4), (x,y+4), radius_x=4, sweep=True)
            self.add_arc(name+'-b', (x,y+4), (x,y-4), radius_x=4, sweep=True)
            self.add_contour(name, name+'-a', name+'-b', closed=True)
        ring('parent',24,12)
        for name,x in (('child-left',8),('child-middle',24),('child-right',40)):
            ring(name,x,36)
        self.add_line('trunk', (24,16), (24,24))
        self.add_line('bus-left', (8,24), (24,24))
        self.add_line('bus-right', (24,24), (40,24))
        for name,x in (('left-drop',8),('middle-drop',24),('right-drop',40)):
            self.add_line(name, (x,24), (x,32))
        self.relate('connect','parent','trunk')
        self.relate('connect','trunk','bus-left','bus-right','middle-drop')
        self.relate('connect','bus-left','left-drop')
        self.relate('connect','bus-right','right-drop')
        self.relate('connect','child-left','left-drop')
        self.relate('connect','child-middle','middle-drop')
        self.relate('connect','child-right','right-drop')
