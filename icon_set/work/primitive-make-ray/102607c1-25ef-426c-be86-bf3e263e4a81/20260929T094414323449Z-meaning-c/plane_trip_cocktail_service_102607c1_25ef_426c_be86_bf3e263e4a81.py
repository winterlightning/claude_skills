from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '102607c1-25ef-426c-be86-bf3e263e4a81'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plane-trip-cocktail-service/20260929T093326Z-thuan-mac/reference/plane trip cocktail service_102607c1-25ef-426c-be86-bf3e263e4a81.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Outlined swept-wing plane and wide bowl on a centered stem; omit divider and garnish to protect clarity.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'plane-trip-cocktail-service'
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
        path('plane',(6,14),[('L',(10,21)),('L',(23,17)),('L',(20,24)),('L',(27,22)),('L',(32,16)),('L',(40,13)),('B',(46,11),(44,4),(39,6)),('L',(30,9)),('L',(20,4)),('L',(14,6)),('L',(22,12)),('L',(12,15)),('L',(9,11)),('L',(6,14))],True)

        path('glass',(14,32),[('L',(34,32)),('A',(24,40),10,8,True),('A',(14,32),10,8,True)],True)
        self.add_line('stem',(24,40),(24,46));self.add_line('foot',(18,46),(30,46));join('glass','stem');join('stem','foot')
