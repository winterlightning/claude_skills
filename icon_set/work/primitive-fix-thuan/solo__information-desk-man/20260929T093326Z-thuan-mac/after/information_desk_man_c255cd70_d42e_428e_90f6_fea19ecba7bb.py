from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c255cd70-d42e-428e-90f6-fea19ecba7bb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__information-desk-man/20260929T093326Z-thuan-mac/reference/information desk man_c255cd70-d42e-428e-90f6-fea19ecba7bb.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Centered round head, smooth shoulders and rounded desk; symmetric geometry.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'information-desk-man'
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
        circle('head',24,10,6)
        path('shoulders',(12,32),[('B',(12,28),(17,24),(24,24)),('B',(31,24),(36,28),(36,32))])
        rect('desk',8,32,40,40,2)
        self.add_line('left-leg',(12,40),(12,44));self.add_line('right-leg',(36,40),(36,44))
        join('shoulders','desk');join('desk','left-leg');join('desk','right-leg')

# User-authorized visual exception, bound to this reviewed SVG; automatic findings remain recorded.
Drawing.exception = {'reason': 'The shoulder arcs intentionally converge into the counter; the broad shoulder opening and full counter remain legible at 48px despite internal-spacing advisories near their joins.', 'approved_by': 'user (exception discretion explicitly delegated); visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '766936bc9f352548fcb97bdb426c6d8f83236ff5c5d76888f732168c5cbb3e0e'}
