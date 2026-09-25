"""Seasoning Shaker Bottle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e4214a4-294d-4acd-8c74-8255de965bc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/seasoning salt_5e4214a4-294d-4acd-8c74-8255de965bc5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seasoning-shaker-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('seasoning', 'shaker', 'bottle')

    def build(self):
        # Plan: Domed seasoning cap and bulbous tapered bottle with a lower band. Mirrored shoulders and base; cap and lower section each have adequate open height. No useful exact Lucide match.
        # Envelope: VRECT_M; visible ink (8, 2, 40, 46) on SOLO48.

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

        path('cap',(14,16),[('L',(14,14)),('A',(34,14),10,10,True),('L',(34,16)),('L',(14,16))],True)
        path('body',(14,16),[('C',(10,32),(12,22),(10,27)),('L',(10,36)),('A',(18,44),8,8,False),('L',(30,44)),('A',(38,36),8,8,False),('L',(38,32)),('C',(34,16),(38,27),(36,22))]);join('cap','body')
        line('band',(10,32),(38,32));join('band','body')
