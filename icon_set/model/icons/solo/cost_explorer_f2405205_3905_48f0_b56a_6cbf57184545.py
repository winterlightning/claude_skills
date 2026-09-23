"""cost explorer. Reconstructed whole reference on SOLO48.
Plan: SQUARE visible bounds (4, 4, 44, 44).
Construction: chart-line and search. Shared dimensions and relationships are recorded in build.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f2405205-3905-48f0-b56a-6cbf57184545'
SOURCE_PATH = 'icon_set/work/todo-references/cost explorer_f2405205-3905-48f0-b56a-6cbf57184545.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cost-explorer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('cost', 'explorer')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Three circular data nodes, joined outside their outlines, and a magnifier.
        self.add_polyline('axes',(6,6),(6,42),(14,42))
        nodes=((16,18),(26,10),(38,8))
        for i,(x,y) in enumerate(nodes):self.circle(f'point-{i}',x,y,2)
        links=[((6,32),(16,20)),((18,18),(24,10)),((28,10),(36,8))]
        for i,(a,b) in enumerate(links):
            self.add_line(f'series-{i}',a,b)
            self.relate('connect',f'series-{i}',f'point-{i}')
            if i:self.relate('connect',f'series-{i}',f'point-{i-1}')
        self.relate('connect','axes','series-0')
        # Exact 6-8-10 attachment locates the diagonal handle on the circular lens.
        self.add_arc('lens-a',(38,40),(26,24),radius_x=10)
        self.add_arc('lens-b',(26,24),(38,40),radius_x=10)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',(38,40),(42,42))
        self.relate('connect','lens','handle')
