"""code build: complete reference reconstructed on SOLO48.
Keyshape: HRECT_L, visible bounds (2, 6, 46, 42).
Construction reference: construction and code. See build comments for symbols and relationships.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d435341-042f-470f-9af2-453657b4c06a'
SOURCE_PATH = 'icon_set/work/todo-references/code build_8d435341-042f-470f-9af2-453657b4c06a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'code-build'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('code', 'build')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8]; eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Crane frame with two truss bays suspends a code window at the right.
        self.add_polyline('crane',(4,40),(4,8),(32,8),(44,20),(4,20))
        self.add_polyline('truss',(8,20),(16,8),(24,20),(32,8))
        self.relate('connect','crane','truss')
        self.add_line('mast',(12,20),(12,40))
        self.add_line('foot',(4,40),(20,40))
        self.relate('connect','crane','mast')
        self.relate('connect','crane','foot')
        self.relate('connect','mast','foot')
        self.add_polyline('hanger',(32,20),(32,24),(28,28))
        self.add_line('hanger-right',(32,24),(36,28))
        self.relate('connect','crane','hanger')
        self.relate('connect','hanger','hanger-right')
        self.rounded_rect('window',22,28,22,12,2)
        self.relate('connect','window','hanger')
        self.relate('connect','window','hanger-right')
        self.add_polyline('left-code',(28,32),(26,34),(28,36))
        self.add_line('slash',(34,31),(31,37))
        self.add_polyline('right-code',(38,32),(40,34),(38,36))

