"""A round laboratory flask containing a pointed leaf.
Plan: Symmetric flask with open neck and a centered diagonal leaf lens; neck and shoulders share endpoints.
Construction reference: leaf: pointed leaf silhouette; search: coherent circular lower bowl.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '37c9b2bf-2623-41e2-b321-1ce5634ee388'
SOURCE_PATH = 'pictographic-primitives/other/biology_37c9b2bf-2623-41e2-b321-1ce5634ee388.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'biology'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('biology',)
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, left, top, right, bottom, radius=4):
        r = radius
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members = []
        for i, start in enumerate(points):
            end = points[(i+1)%8]
            part = f'{name}-{i}'
            if i%2:
                self.add_arc(part,start,end,radius_x=r)
            else:
                self.add_line(part,start,end)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.add_line('neck-left',(20,4),(20,16))
        self.add_arc('shoulder-left',(20,16),(8,28),radius_x=12,sweep=False)
        self.add_arc('bowl',(8,28),(40,28),radius_x=16,sweep=False)
        self.add_arc('shoulder-right',(40,28),(28,16),radius_x=12,sweep=False)
        self.add_line('neck-right',(28,16),(28,4))
        self.add_contour('flask','neck-left','shoulder-left','bowl','shoulder-right','neck-right')
        for i,(a,b) in enumerate([(16,20),(20,28),(28,32)]):
            self.add_line(f'rim-{i}',(a,4),(b,4))
        for side,ids in [('left',(0,1)),('right',(1,2))]:
            for i in ids:
                self.relate('connect','neck-'+side,f'rim-{i}')
        self.add_bezier('leaf-upper',(19,33),((16,24),(22,24),(29,25)))
        self.add_bezier('leaf-lower',(29,25),((29,31),(26,35),(19,33)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)
