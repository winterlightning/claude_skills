from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7fd9f0d0-c938-40e5-aa02-cf196a735373'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-holding-a-bottle/20260929T093326Z-thuan-mac/reference/drinking bottle_7fd9f0d0-c938-40e5-aa02-cf196a735373.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Bust at left, bottle at right; rounded shoulder owns the arm that reaches the bottle.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-holding-a-bottle'
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
        circle('head',15,14,7)
        path('bust',(6,42),[('L',(6,36)),('B',(6,31),(10,29),(15,29)),('B',(21,29),(23,32),(24,36)),('L',(31,36))])
        path('arm',(17,35),[('B',(17,41),(24,42),(31,40))])
        path('bottle',(34,6),[('L',(40,6)),('L',(40,15)),('B',(40,19),(42,20),(42,24)),('L',(42,40)),('L',(32,40)),('L',(32,24)),('B',(32,20),(34,19),(34,15)),('L',(34,6))],True)
        self.add_line('cap',(34,10),(40,10));join('bottle','cap')
