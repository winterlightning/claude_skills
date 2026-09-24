"""Revision for bad-stroke feedback. Lucide refresh-cw: two smooth rotational arcs with open right-angle heads.
Omissions: None; diagonal opposing arrow arrangement retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3012b212-ec5f-487b-935e-c18701a8601b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-circular-refresh-arrows-batch-020-02/20260924T092136Z-thuan-mac/reference/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-circular-refresh-arrows-batch-020-02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('arrows', 'spin')
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

        # Opposite halves derive by 180-degree rotation; shared radius and head length.
        for i in range(2):
            def p(x,y): return (x,y) if i==0 else (48-x,48-y)
            path(f'arc-{i}',p(6,24),[('A',p(24,6),18,18,True),('C',p(40,14),p(31,6),p(36,9))])
            poly(f'head-{i}',p(40,6),p(40,14),p(32,14))
            join(f'arc-{i}',f'head-{i}')
