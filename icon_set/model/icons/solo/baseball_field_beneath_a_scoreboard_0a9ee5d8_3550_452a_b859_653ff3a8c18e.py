"""Baseball Field Scoreboard.

Plan: Scoreboard above fan-shaped field; omit pennants and scoreboard text.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a9ee5d8-3550-452a-b859-653ff3a8c18e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baseball score_0a9ee5d8-3550-452a-b859-653ff3a8c18e.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'baseball-field-beneath-a-scoreboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baseball', 'field', 'scoreboard')

    def build(self):

        self.rect('scoreboard',14,6,20,8,2)
        self.add_line('post',(24,14),(24,17));self.relate('connect','scoreboard','post')
        self.arc('field',(6,38),(42,38),18,12)
        self.path('foul-lines',[(42,38),(24,42),(6,38)])
        # Merge the temporary runs into one continuous contour.
        self.contours = [c for c in self.contours if not set(c.members).issubset({'foul-lines-2', 'foul-lines-1', 'field'})]
        self.add_contour('ground','field','foul-lines-1','foul-lines-2',closed=True)

    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
