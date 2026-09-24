"""A left-facing head and neck with circular crown, rounded jaw and two sore-throat ticks in the open neck. Bounds (8,4)-(40,44). Human user reference informs rounded skull; natural continuous neck retained.
Construction reference: Shared human user.svg: rounded head vocabulary; reference profile owns continuous neck.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '05f181ec-ad67-401f-a703-51e76d1605f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/sore throat_05f181ec-ad67-401f-a703-51e76d1605f7.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sore-throat-profile'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/health"
    aliases=()
    keywords=('sore', 'throat')
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
        path('profile',(40,44),[('L',(40,28)),('L',(40,20)),('A',(24,4),16,16,False),('C',(12,17),(16,4),(12,10)),('L',(8,25)),('L',(14,25)),('L',(14,31)),('A',(18,35),4,4,False),('L',(20,35)),('L',(20,44))])
        line('pain-one',(27,26),(31,29))
        line('pain-two',(29,38),(31,40))
