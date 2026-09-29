from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8ad981a5-b816-4b7b-adb5-407875ecdf55'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-enjoying-sunny-day/20260929T093326Z-thuan-mac/reference/virtual environment day_8ad981a5-b816-4b7b-adb5-407875ecdf55.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Cloud at upper left, sun at upper right, centered round head and open bust; no horizon clutter.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-enjoying-sunny-day'
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
        path('cloud',(8,15),[('B',(2,15),(2,8),(7,8)),('B',(8,2),(16,3),(17,9)),('B',(23,9),(22,15),(18,15)),('L',(8,15))],True)
        circle('sun',34,12,4)
        for name,a,b in [('top',(34,2),(34,3)),('right',(43,12),(44,12)),('lower',(34,21),(34,22))]:self.add_line(name,a,b)
        circle('head',24,28,5)
        path('bust',(12,46),[('B',(12,41),(18,41),(24,41)),('B',(30,41),(36,41),(36,46))])
