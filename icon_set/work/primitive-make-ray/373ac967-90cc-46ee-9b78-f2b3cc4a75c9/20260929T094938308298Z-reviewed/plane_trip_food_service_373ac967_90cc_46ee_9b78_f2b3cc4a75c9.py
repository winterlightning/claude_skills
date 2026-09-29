from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '373ac967-90cc-46ee-9b78-f2b3cc4a75c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plane-trip-food-service/20260929T093326Z-thuan-mac/reference/plane trip food service_373ac967-90cc-46ee-9b78-f2b3cc4a75c9.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Compact horizontal plane silhouette, then separated fork and knife; omit divider to give symbols breathing space.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'plane-trip-food-service'
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

        path('fork',(10,32),[('L',(10,36)),('A',(18,36),4,4,False),('L',(18,32))])
        self.add_line('fork-stem',(14,40),(14,44));join('fork','fork-stem')
        path('knife',(32,44),[('L',(32,32)),('B',(38,34),(38,37),(38,39)),('L',(32,39))])

# User-authorized visual exception, bound to this reviewed SVG; automatic findings remain recorded.
Drawing.exception = {'reason': 'Preserve a recognizable outlined airplane above separate fork and knife. Compact wing/tail openings and the natural scene envelope remain readable at 48px.', 'approved_by': 'user (exception discretion explicitly delegated); visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '8a58db3defbc05d4710628af2c2772537df0256b816f3f11ad9c14ab9f2852fb'}
