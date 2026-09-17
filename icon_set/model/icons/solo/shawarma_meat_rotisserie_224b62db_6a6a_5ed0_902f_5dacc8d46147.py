"""Shawarma Meat Rotisserie."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '224b62db-6a6a-5ed0-902f-5dacc8d46147'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/exotic food kebab shred_224b62db-6a6a-5ed0-902f-5dacc8d46147.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shawarma-meat-rotisserie'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('shawarma', 'meat', 'rotisserie')

    def build(self):
        # Plan: Tapered meat stack on a hooked vertical skewer and flat stand. One attached side cut replaces multiple source cuts; shared meat, skewer and stand nodes. No useful exact Lucide match.
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

        path('meat',(24,12),[('C',(35,17),(30,12),(35,12)),('L',(33,26)),('L',(31,31)),('C',(24,35),(30,34),(27,35)),('C',(17,31),(21,35),(18,34)),('L',(13,17)),('C',(24,12),(13,12),(18,12))],True)
        path('hook',(24,12),[('L',(24,8)),('A',(28,4),4,4,True),('L',(32,4))]);join('hook','meat')
        line('spit-bottom',(24,35),(24,44));join('spit-bottom','meat')
        poly('stand',(10,44),(24,44),(38,44));join('stand','spit-bottom')
        line('meat-cut',(25,26),(33,26));join('meat-cut','meat')
