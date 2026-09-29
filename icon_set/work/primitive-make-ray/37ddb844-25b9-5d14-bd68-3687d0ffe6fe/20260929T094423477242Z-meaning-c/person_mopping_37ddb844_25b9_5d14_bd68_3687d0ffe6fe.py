from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '37ddb844-25b9-5d14-bd68-3687d0ffe6fe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-mopping/20260929T093326Z-thuan-mac/reference/cleanser moping_37ddb844-25b9-5d14-bd68-3687d0ffe6fe.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Large mop pad at lower left, long shaft to both hands, upright head over a leaning torso.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-mopping'
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
        circle('head',28,11,5)
        path('torso',(28,24),[('B',(28,27),(29,29),(32,32))])
        self.add_polyline('arm',(28,24),(21,29),(16,29))
        self.add_polyline('legs',(28,44),(32,32),(42,44))
        self.add_line('handle',(16,29),(9,36))
        rect('mop',6,36,20,44,4)
        join('torso','arm');join('torso','legs');join('arm','handle');join('handle','mop')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
