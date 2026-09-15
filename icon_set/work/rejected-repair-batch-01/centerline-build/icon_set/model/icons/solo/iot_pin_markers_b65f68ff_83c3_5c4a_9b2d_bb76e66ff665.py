"""A large IoT node stands above three smaller pin markers. Flattened diamond bases reduce to short pin stems to avoid tiny enclosed holes. Lucide network informs repeated rings and explicit connections; three markers and the large root remain. Bilateral symmetry.
SOLO48 CIRCLE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='b65f68ff-83c3-5c4a-9b2d-bb76e66ff665'
SOURCE_PATH='pictographic-primitives/programing/internet of thing analytics services_b65f68ff-83c3-5c4a-9b2d-bb76e66ff665.svg'
AUTHOR='gpt-6'

class IotPinMarkers(Solo48):
    icon_id='iot-pin-markers'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('iot', 'pins', 'location', 'devices', 'analytics', 'nodes', 'network', 'markers')

    def build(self) -> None:
        def ring(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)

        def node(name,x,y,w,h):
            self.add_polyline(name,(x,y),(x+w//2,y),(x+w,y),(x+w,y+h),(x+w//2,y+h),(x,y+h),closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        ring('root',24,12,8)
        self.add_line('root-stem',(24,20),(24,32))
        ring('central-marker',24,35,3)
        self.add_line('central-pin',(24,38),(24,44))
        join('root','root-stem')
        join('root-stem','central-marker')
        join('central-marker','central-pin')
        for name,x in (('left',10),('right',38)):
            ring(name+'-marker',x,33,3)
            self.add_line(name+'-pin',(x,36),(x,38))
            join(name+'-marker',name+'-pin')
