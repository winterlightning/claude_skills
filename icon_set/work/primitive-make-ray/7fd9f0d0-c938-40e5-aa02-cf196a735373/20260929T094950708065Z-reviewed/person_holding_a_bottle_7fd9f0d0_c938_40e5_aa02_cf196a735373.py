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
        circle('head',16,12,5)
        path('bust',(6,44),[('L',(6,34)),('B',(6,28),(12,25),(16,25)),('B',(22,25),(24,29),(24,33)),('L',(32,33))])
        path('arm',(16,34),[('B',(16,40),(24,41),(32,41))])
        path('bottle',(34,4),[('L',(42,4)),('L',(42,15)),('B',(42,19),(44,20),(44,24)),('L',(44,41)),('L',(32,41)),('L',(32,24)),('B',(32,20),(34,19),(34,15)),('L',(34,4))],True)
        join('bust','bottle');join('arm','bottle')

# User-authorized visual exception, bound to this reviewed SVG; automatic findings remain recorded.
Drawing.exception = {'reason': 'Preserve the larger bust, bent holding sleeve and slender capped bottle silhouette. Natural scene envelope and the sleeve opening are intentional.', 'approved_by': 'user (exception discretion explicitly delegated); visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b83f4583dbe6dc70884e47c66350d1c255d3828af81988cd46e89c6b57aafdda'}
