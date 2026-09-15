"""Text flow rows (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a13af5c-a9a7-5fa9-9d87-28150cd3e8a0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text flow rows_8a13af5c-a9a7-5fa9-9d87-28150cd3e8a0.svg'
AUTHOR = 'gpt-6'

class TextFlowRows(Solo48):
    icon_id = 'text-flow-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'flow', 'rows', 'interface-essential')

    def build(self):
        # Plan: Three equal rounded text nodes and a clear stepped flow; all links meet explicit nodes, with separated turns and one output arrow.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        def node(n,l,t):
         path(n,(l+2,t), [('L',(l+6,t)),('L',(l+10,t)),('A',(l+12,t+2),2,2,True),('L',(l+12,t+4)),('L',(l+12,t+6)),('A',(l+10,t+8),2,2,True),('L',(l+6,t+8)),('L',(l+2,t+8)),('A',(l,t+6),2,2,True),('L',(l,t+4)),('L',(l,t+2)),('A',(l+2,t),2,2,True)],True)
        node('first',6,6);node('second',30,6);node('third',6,34)
        line('first-link',(18,10),(30,10));join('first-link','first');join('first-link','second')
        poly('return-link',(36,14),(36,24),(12,24),(12,34));join('return-link','second');join('return-link','third')
        line('output',(18,38),(42,38));poly('arrow',(36,34),(42,38),(36,42));join('output','third');join('output','arrow')
