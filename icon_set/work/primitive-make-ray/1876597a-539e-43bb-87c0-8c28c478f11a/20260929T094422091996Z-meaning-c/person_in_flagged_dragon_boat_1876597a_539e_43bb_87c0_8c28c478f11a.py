from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1876597a-539e-43bb-87c0-8c28c478f11a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-in-flagged-dragon-boat/20260929T093326Z-thuan-mac/reference/dragon boat festival person_1876597a-539e-43bb-87c0-8c28c478f11a.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Dragon head at left; passenger and upright flag above a smooth bowl-like hull.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-in-flagged-dragon-boat'
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
        path('boat',(6,22),[('L',(10,22)),('L',(11,18)),('L',(15,15)),('L',(15,30)),('L',(19,34)),('L',(34,34)),('L',(42,30)),('B',(42,39),(35,42),(25,42)),('B',(14,42),(10,36),(9,29)),('L',(6,29)),('L',(6,22))],True)
        circle('head',24,13,4)
        path('bust',(18,33),[('B',(18,28),(20,25),(24,25)),('B',(28,25),(30,28),(30,34))])
        self.add_line('pole',(34,34),(34,6));self.add_polyline('flag',(34,6),(42,6),(42,14),(34,14))
        join('boat','bust');join('boat','pole');join('pole','flag')
