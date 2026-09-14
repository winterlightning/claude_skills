"""A six-lobed gear branches to three circular nodes. Lucide workflow informs repeated nodes and the connecting bus. Gear lobes are broadened; the solid hub and all three children remain.
Fresh SOLO48 geometry. Keyshape VRECT_L; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d0f8813-4319-5220-8dfd-6e257aa659af'
SOURCE_PATH = 'pictographic-primitives/programing/amazon web service obs works circle_9d0f8813-4319-5220-8dfd-6e257aa659af.svg'
AUTHOR = 'gpt-6'

class GearHierarchySolidHub(Solo48):
    icon_id = 'gear-hierarchy-solid-hub'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/programming"
    aliases = ()
    keywords = ('gear', 'hierarchy', 'tree', 'settings', 'operations', 'nodes', 'automation', 'structure')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.add_polyline('gear',(24,4),(28,7),(34,9),(32,15),(34,21),(28,23),(24,26),(20,23),(14,21),(16,15),(14,9),(20,7),closed=True)
        self.add_dot('hub',(24,15))
        self.add_line('root-stem',(24,26),(24,29))
        self.add_line('bus-left',(11,29),(24,29))
        self.add_line('bus-right',(24,29),(37,29))
        self.relate('connect','gear','root-stem')
        for a,b in (('root-stem','bus-left'),('root-stem','bus-right'),('bus-left','bus-right')):
            self.relate('connect',a,b)
        for name,x in (('left',11),('middle',24),('right',37)):
            self.add_line(name+'-stem',(x,29),(x,38))
            self.add_arc(name+'-right',(x,38),(x,44),radius_x=3)
            self.add_arc(name+'-left',(x,44),(x,38),radius_x=3)
            self.add_contour(name+'-node',name+'-right',name+'-left',closed=True)
            self.relate('connect',name+'-stem',name+'-node')
            for bus in (('bus-left',) if name=='left' else ('bus-right',) if name=='right' else ('bus-left','bus-right','root-stem')):
                self.relate('connect',name+'-stem',bus)
