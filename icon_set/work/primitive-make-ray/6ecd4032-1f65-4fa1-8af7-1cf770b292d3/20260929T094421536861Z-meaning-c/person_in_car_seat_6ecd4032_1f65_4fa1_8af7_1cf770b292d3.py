from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6ecd4032-1f65-4fa1-8af7-1cf770b292d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-in-car-seat/20260929T093326Z-thuan-mac/reference/person with seat_6ecd4032-1f65-4fa1-8af7-1cf770b292d3.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Rounded seat below a round head and bent torso; deliberate seated side view.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-in-car-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ()

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                eid=f"{name}-{j}"; kind=cmd[0]
                if kind=='L': self.add_line(eid,here,cmd[1]); end=cmd[1]
                elif kind=='B': self.add_bezier(eid,here,(cmd[1],cmd[2],cmd[3])); end=cmd[3]
                elif kind=='A':
                    end,rx,ry,sweep=cmd[1:];self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(eid);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x1,y1,x2,y2,r):
            path(name,(x1+r,y1),[('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True),('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True),('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True),('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)],True)
        def join(*names):
            for i,a in enumerate(names):
                for b in names[i+1:]:self.relate('connect',a,b)
        circle('head',23,12,6)
        self.add_polyline('torso',(23,26),(23,32),(33,32),(42,40))
        self.add_polyline('arm',(23,26),(31,26),(39,20))
        path('seat',(6,21),[('L',(8,32)),('B',(9,40),(15,42),(23,42)),('L',(32,42))])
        join('torso','arm')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
