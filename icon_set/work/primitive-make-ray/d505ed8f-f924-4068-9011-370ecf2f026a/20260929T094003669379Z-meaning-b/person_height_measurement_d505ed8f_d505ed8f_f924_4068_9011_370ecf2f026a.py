from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd505ed8f-f924-4068-9011-370ecf2f026a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-height-measurement-d505ed8f/20260929T093326Z-thuan-mac/reference/virtual measuring_d505ed8f-f924-4068-9011-370ecf2f026a.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Rectangular ruler with repeated inward ticks, larger head, shoulders and divided legs.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-height-measurement-d505ed8f'
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
        self.add_polyline('ruler',(6,6),(16,6),(16,42),(6,42),closed=True)
        for y in (14,22,30):
         self.add_line(f'tick-{y}',(6,y),(10,y));join('ruler',f'tick-{y}')
        circle('head',31,12,6)
        path('body',(31,26),[('B',(24,26),(23,29),(23,33)),('L',(26,33)),('L',(27,42)),('L',(35,42)),('L',(36,33)),('L',(39,33)),('B',(39,29),(38,26),(31,26))],True)
        self.add_line('legs',(31,35),(31,42));join('body','legs')
