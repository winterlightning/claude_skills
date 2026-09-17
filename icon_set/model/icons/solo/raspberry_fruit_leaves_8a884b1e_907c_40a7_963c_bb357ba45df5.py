"""Raspberry Fruit with Leaves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a884b1e-907c-40a7-963c-bb357ba45df5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/raspberry pi_8a884b1e-907c-40a7-963c-bb357ba45df5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raspberry-fruit-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('raspberry', 'fruit', 'leaves')

    def build(self):
        # Plan: Supplied raspberry: paired pointed leaves and three large joined drupelets. Five crowded source lobes reduced to three clear berry chambers. Mirrored fruit and leaf geometry; no useful exact Lucide match.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

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

        path('fruit',(24,20),[('C',(8,24),(20,10),(8,14)),('C',(14,34),(8,30),(10,34)),('C',(24,44),(14,40),(18,44)),('C',(34,34),(30,44),(34,40)),('C',(40,24),(38,34),(40,30)),('C',(24,20),(40,14),(28,10))],True)
        for side in (-1,1):
         path('leaf'+str(side),(24,20),[('C',(24+side*14,4),(24+side*2,8),(24+side*8,4)),('C',(24+side*12,16),(24+side*14,9),(24+side*14,13))]);join('leaf'+str(side),'fruit')
        line('split',(24,20),(24,30));join('split','fruit')
        path('lobes',(14,34),[('C',(24,30),(18,34),(21,34)),('C',(34,34),(27,34),(30,34))]);join('lobes','fruit');join('lobes','split')
