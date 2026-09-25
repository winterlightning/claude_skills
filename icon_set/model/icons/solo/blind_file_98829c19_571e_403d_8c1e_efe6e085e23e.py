"""A document with a clipped upper corner and five braille-like dots.
Plan: One file enclosure; a two-column dot series with the lower-right cell intentionally absent.
Construction reference: file: clipped upper corner and coherent rounded lower corners; no added folded-corner line.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '98829c19-571e-403d-8c1e-efe6e085e23e'
SOURCE_PATH = 'icon_set/work/todo-references/blind file_98829c19-571e-403d-8c1e-efe6e085e23e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blind-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('blind', 'file')
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
        self.add_line('top',(12,4),(30,4))
        self.add_line('clip',(30,4),(40,14))
        self.add_line('right',(40,14),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('page','top','clip','right','br','bottom','bl','left','tl',closed=True)
        for row,count in enumerate((2,2,1)):
            for col in range(count):
                self.add_dot(f'dot-{row}-{col}',(18+col*10,14+row*10))
