from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eb4a3a21-81c2-4505-9136-3a3335da3b2e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-needing-toilet/20260929T093326Z-thuan-mac/reference/toilet need_eb4a3a21-81c2-4505-9136-3a3335da3b2e.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Symmetric round head and broad shoulders; hands converge centrally and long legs cross below.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-needing-toilet'
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
        circle('head',24,7,4)
        path('body-left',(24,19),[('L',(17,19)),('B',(9,19),(8,24),(11,29)),('B',(13,33),(17,34),(21,35))])
        path('body-right',(24,19),[('L',(31,19)),('B',(39,19),(40,24),(37,29)),('B',(35,33),(31,34),(27,35))])
        path('hands-left',(17,26),[('B',(17,30),(24,30),(24,35))])
        path('hands-right',(31,26),[('B',(31,30),(24,30),(24,35))])
        self.add_line('leg-left',(21,35),(30,44));self.add_line('leg-right',(27,35),(18,44))
        join('body-left','body-right');join('hands-left','hands-right');join('body-left','leg-left');join('body-right','leg-right');join('leg-left','leg-right')
