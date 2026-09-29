from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '07568706-6580-4938-9b1c-46841b6e4e23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-f/20260929T093326Z-thuan-mac/reference/square f_07568706-6580-4938-9b1c-46841b6e4e23.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Concentric rounded square and speech bubble, with one intentional tail.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'square-f'
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
        rect('frame',6,6,42,42,6)
        path('bubble',(19,15),[('L',(29,15)),('A',(33,19),4,4,True),('L',(33,23)),('A',(29,27),4,4,True),('L',(26,27)),('L',(21,33)),('L',(21,27)),('L',(19,27)),('A',(15,23),4,4,True),('L',(15,19)),('A',(19,15),4,4,True)],True)
