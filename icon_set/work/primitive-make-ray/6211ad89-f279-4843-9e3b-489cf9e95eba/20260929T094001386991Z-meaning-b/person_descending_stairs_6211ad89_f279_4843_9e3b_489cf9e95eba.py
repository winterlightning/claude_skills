from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6211ad89-f279-4843-9e3b-489cf9e95eba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-descending-stairs/20260929T093326Z-thuan-mac/reference/stairs person decend_6211ad89-f279-4843-9e3b-489cf9e95eba.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Stepped baseline with a leaning walker; bent rear leg and extended lower foot.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-descending-stairs'
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
        circle('head',19,11,5)
        path('torso',(19,24),[('B',(19,27),(22,28),(23,31))])
        self.add_polyline('arm-left',(19,24),(13,28),(9,28))
        self.add_polyline('arm-right',(19,24),(28,26),(30,30))
        self.add_polyline('leg-left',(23,31),(16,34),(14,42))
        self.add_polyline('leg-right',(23,31),(28,31),(30,36))
        self.add_polyline('stairs',(6,42),(18,42),(18,36),(30,36),(30,30),(42,30))
        join('torso','arm-left');join('torso','arm-right');join('arm-left','arm-right');join('torso','leg-left');join('torso','leg-right');join('leg-left','leg-right');join('leg-left','stairs');join('leg-right','stairs');join('arm-right','stairs')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
