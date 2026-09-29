from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6211ad89-f279-4843-9e3b-489cf9e95eba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-descending-stairs/20260929T093326Z-thuan-mac/reference/stairs person decend_6211ad89-f279-4843-9e3b-489cf9e95eba.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Stepped baseline with a leaning walker; bent rear leg and extended lower foot.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-descending-stairs'
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
        circle('head',18,8,4)
        path('torso',(18,20),[('B',(18,23),(20,26),(21,28))])
        self.add_polyline('arm',(18,20),(12,27),(8,26))
        self.add_polyline('leg-left',(21,28),(15,33),(14,44))
        self.add_polyline('leg-right',(21,28),(27,29),(28,38))
        self.add_polyline('stairs',(6,44),(18,44),(18,38),(30,38),(30,32),(42,32))
        join('torso','arm');join('torso','leg-left');join('torso','leg-right');join('leg-left','leg-right');join('leg-left','stairs');join('leg-right','stairs')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')

# User-authorized visual exception, bound to this reviewed SVG; automatic findings remain recorded.
Drawing.exception = {'reason': 'Preserve the descending step pose with three visible stair levels; natural scene envelope and compact bent knee/step junctions remain legible.', 'approved_by': 'user (exception discretion explicitly delegated); visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '69b20105f6d44e7c2ac74625e18b001102b8712780506333c3b5ff54d7227c80'}
