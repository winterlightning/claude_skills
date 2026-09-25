"""One solid outlined person beside a person with an interrupted outline. Bounds (6,6)-(42,42). Both circular heads radius4, body tops y22 give exact4-unit head/body ink clearance.
Construction reference: Human user.svg and full_body_ref.png: circular heads and coherent body outlines.
Omissions: Fine dash pattern simplified to a large clear interruption; heads remain outlined."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '58fce536-ad33-4c76-86df-d52bb405808c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety missing people_58fce536-ad33-4c76-86df-d52bb405808c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='missing-person-pair'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "wayfinding"
    aliases=()
    keywords=('safety', 'missing', 'people')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        for x in (12,36): oval('head-'+str(x),x,10,4,4)
        path('person',(6,32),[('L',(6,28)),('A',(12,22),6,6,True),('A',(18,28),6,6,True),('L',(18,32)),('L',(16,32)),('L',(16,38)),('A',(8,38),4,4,True),('L',(8,32)),('L',(6,32))],True)
        path('missing-top',(30,30),[('L',(30,28)),('A',(36,22),6,6,True),('A',(42,28),6,6,True),('L',(42,30))])
        path('missing-bottom',(32,38),[('A',(40,38),4,4,False)])
