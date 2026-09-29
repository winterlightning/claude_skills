from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b7134d6f-1d86-40a4-ba79-82ee018f9bfd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__statue-with-flag/20260929T093326Z-thuan-mac/reference/landmarks statue flag_b7134d6f-1d86-40a4-ba79-82ee018f9bfd.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Standing figure and trapezoid plinth; angled flag with shared pole attachment.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'statue-with-flag'
    keyshape = Keyshape.VRECT_L
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
        circle('head',14,7,4)
        path('statue',(8,36),[('L',(8,25)),('B',(8,21),(10,19),(14,19)),('B',(18,19),(20,21),(20,25)),('L',(20,36))])
        self.add_line('legs',(14,29),(14,36))
        self.add_polyline('plinth',(6,36),(27,36),(24,44),(9,44),closed=True)
        self.add_line('pole',(24,36),(32,4))
        self.add_polyline('flag',(32,4),(44,8),(41,18),(29,16))
        join('statue','plinth');join('legs','plinth');join('pole','plinth');join('pole','flag')
