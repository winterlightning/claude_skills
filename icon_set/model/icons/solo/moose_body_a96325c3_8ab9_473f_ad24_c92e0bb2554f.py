"""Moose side silhouette with long muzzle, joined antlers and two broad legs; curved antler tines retain its distinctive profile."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a96325c3-8ab9-473f-ad24-c92e0bb2554f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broad-antlered-moose/20260925T060624Z-thuan-mac/reference/moose body_a96325c3-8ab9-473f-ad24-c92e0bb2554f.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'broad-antlered-moose-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('moose body',)

    def build(self):
        # Plan: Moose side silhouette with long muzzle, joined antlers and two broad legs; curved antler tines retain its distinctive profile.
        # Construction reference: no useful Lucide match; coherent animal contour and shared antler beam

        def path(name, start, commands, closed=False):
            members=[]; here=start
            for index, command in enumerate(commands):
                ident=f'{name}-{index}'; kind,end,*args=command
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            path(name,(cx-r,cy),[('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(6,42),[('L',(6,29)),('A',(14,21),8,8,True),('L',(27,21)),('C',(35,15),(29,17),(32,15)),('C',(42,24),(40,15),(42,20)),('C',(36,26),(42,28),(39,28)),('L',(33,42)),('L',(25,42)),('L',(25,33)),('A',(22,30),3,3,False),('L',(17,30)),('A',(14,33),3,3,False),('L',(14,42)),('L',(6,42))],True)
        path('antler',(6,6),[('L',(6,9)),('A',(10,13),4,4,False),('L',(27,13)),('L',(32,17))]);join('antler','body')
        for n,x in [('one',15),('two',24)]:
         line('tine-'+n,(x,6),(x,13));join('tine-'+n,'antler')
