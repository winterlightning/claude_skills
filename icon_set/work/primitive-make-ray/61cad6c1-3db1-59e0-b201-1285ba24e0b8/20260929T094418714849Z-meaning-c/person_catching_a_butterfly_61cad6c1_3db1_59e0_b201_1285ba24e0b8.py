from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '61cad6c1-3db1-59e0-b201-1285ba24e0b8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-catching-a-butterfly/20260929T093326Z-thuan-mac/reference/catch bug_61cad6c1-3db1-59e0-b201-1285ba24e0b8.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Asymmetric catcher bust at right, oval net above, butterfly at upper left.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-catching-a-butterfly'
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
        circle('head',35,25,4)
        path('torso',(35,37),[('B',(40,37),(42,39),(42,44))])
        self.add_polyline('arm',(35,37),(26,37),(20,30),(20,24))
        self.add_line('handle',(20,24),(29,15))
        path('hoop',(25,9),[('A',(33,9),4,6,True),('A',(25,9),4,6,True)],True)
        path('net-bag',(29,3),[('L',(42,9)),('B',(40,14),(35,17),(29,15))])
        path('butterfly',(11,14),[('B',(5,6),(3,6),(3,10)),('B',(3,16),(7,19),(11,14)),('B',(17,6),(19,6),(19,10)),('B',(19,16),(15,19),(11,14))])
        self.add_line('butterfly-body',(11,14),(11,20))
        join('torso','arm');join('arm','handle');join('hoop','handle');join('hoop','net-bag');join('handle','net-bag');join('butterfly','butterfly-body')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
