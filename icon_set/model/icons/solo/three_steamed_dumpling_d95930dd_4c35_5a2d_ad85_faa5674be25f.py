"""Three Steamed Dumplings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd95930dd-4c35-5a2d-ad85-faa5674be25f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear dumplings_d95930dd-4c35-5a2d-ad85-faa5674be25f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-steamed-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('three', 'steamed', 'dumpling')

    def build(self):
        # Plan: Three steamed dumplings arranged one above two. Shared plump pointed-bun definition; each carries one short top crease. Source overlap and second crease removed for separation; no useful exact Lucide match.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for j,(cx,top) in enumerate(((24,6),(12,28),(36,28))):
         path('bun-'+str(j),(cx,top),[('C',(cx+6,top+8),(cx+3,top+2),(cx+6,top+4)),('C',(cx,top+14),(cx+6,top+13),(cx+4,top+14)),('C',(cx-6,top+8),(cx-4,top+14),(cx-6,top+13)),('C',(cx,top),(cx-6,top+4),(cx-3,top+2))],True)
         line('crease-'+str(j),(cx,top),(cx,top+4));join('crease-'+str(j),'bun-'+str(j))
