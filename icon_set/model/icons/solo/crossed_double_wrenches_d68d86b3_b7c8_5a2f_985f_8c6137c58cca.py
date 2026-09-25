"""Revision for bad-stroke feedback. Lucide wrench: rounded open jaws and broad diagonal shafts.
Omissions: Double shaft outlines reduced to open strokes; all four jaws retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd68d86b3-b7c8-5a2f-985f-8c6137c58cca'
SOURCE_PATH = 'pictographic-primitives/tools/tools wrench_d68d86b3-b7c8-5a2f-985f-8c6137c58cca.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'crossed-double-wrenches'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('tools', 'wrench')
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Four open U-shaped jaws share one curved construction. The two slim
        # shafts meet at an explicit central crossing; remove double outlines
        # that made tiny wedges in the rejected drawing.
        for i,(sx,sy) in enumerate([(-1,-1),(1,-1),(1,1),(-1,1)]):
            def p(x,y): return (24+sx*(24-x),24+sy*(24-y))
            path(f'jaw-{i}',p(6,14),[('C',p(18,18),p(8,20),p(14,22)),('C',p(14,6),p(22,14),p(20,8))])
            line(f'shaft-{i}',p(18,18),(24,24))
            join(f'jaw-{i}',f'shaft-{i}')
        for i in range(4):
            for j in range(i): join(f'shaft-{i}',f'shaft-{j}')
