from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '36050eda-0953-5f1d-b828-3b3c917e1c94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-kneeling-beside-bowl/20260929T093326Z-thuan-mac/reference/party throw up_36050eda-0953-5f1d-b828-3b3c917e1c94.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Forward-bent kneeling figure at right with bucket at left; head-to-neck uses a 5-12-13 triangle.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-kneeling-beside-bowl'
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
        circle('head',17,11,5)
        path('torso',(29,16),[('B',(37,19),(38,24),(35,32))])
        self.add_polyline('arm',(29,16),(25,27),(18,31))
        self.add_polyline('leg',(35,32),(31,42),(42,42))
        path('bucket',(6,31),[('L',(18,31)),('L',(16,39)),('A',(8,39),4,3,True),('L',(6,31))],True)
        join('torso','arm');join('torso','leg')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')

        join('arm','bucket')
