"""Taro Root with Leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8a9f392-1634-48a6-8c59-fa341d6c54cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/taro_d8a9f392-1634-48a6-8c59-fa341d6c54cb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'taro-root-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('taro', 'root', 'leaf')

    def build(self):
        # Plan: Taro root with a broad bulb, pointed top and a small shoulder leaf. Two broad ridges replace three tight cuts. Directional asymmetry retained; Lucide leaf informs the pointed leaf contour.
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

        path('root',(18,6),[('C',(30,22),(22,11),(27,17)),('C',(34,28),(32,25),(34,25)),('C',(20,42),(34,38),(27,42)),('C',(6,30),(11,42),(6,37)),('C',(10,18),(6,26),(8,22)),('C',(18,6),(12,14),(15,10))],True)
        path('leaf',(30,22),[('C',(42,8),(29,12),(36,8)),('C',(30,22),(42,17),(38,22))],True)
        join('leaf','root')
        path('ridge-top',(10,18),[('C',(18,20),(12,19),(15,20))]);join('ridge-top','root')
        path('ridge-bottom',(6,30),[('C',(23,32),(11,32),(17,33))]);join('ridge-bottom','root')
