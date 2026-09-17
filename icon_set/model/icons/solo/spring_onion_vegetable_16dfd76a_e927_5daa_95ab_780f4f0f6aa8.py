"""Spring Onion Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16dfd76a-e927-5daa-95ab-780f4f0f6aa8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/scallion spring onion_16dfd76a-e927-5daa-95ab-780f4f0f6aa8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spring-onion-vegetable'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('spring', 'onion', 'vegetable')

    def build(self):
        # Plan: Spring onion with a rounded bulb, flaring pointed leaves and two rootlets. Two wide leaf blades replace the dense original overlap; natural slight asymmetry retained. Lucide leaf informs coherent tapered contours.
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

        path('onion',(24,40),[('C',(15,33),(17,40),(13,37)),('C',(17,27),(16,30),(17,29)),('C',(10,4),(17,20),(13,10)),('L',(21,8)),('L',(24,16)),('L',(27,8)),('L',(38,4)),('C',(31,27),(35,12),(31,20)),('C',(33,33),(31,29),(32,30)),('C',(24,40),(35,37),(31,40))],True)
        line('root-left',(24,40),(19,44));line('root-right',(24,40),(29,44));join('root-left','onion');join('root-right','onion')
