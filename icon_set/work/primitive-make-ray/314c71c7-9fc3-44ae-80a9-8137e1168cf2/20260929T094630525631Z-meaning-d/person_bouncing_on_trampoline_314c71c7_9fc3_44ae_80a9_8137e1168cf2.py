from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '314c71c7-9fc3-44ae-80a9-8137e1168cf2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-bouncing-on-trampoline/20260929T093326Z-thuan-mac/reference/trampoline playing_314c71c7-9fc3-44ae-80a9-8137e1168cf2.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Round head, airborne torso and two bent legs above a broad elliptical trampoline.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-bouncing-on-trampoline'
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
        circle('head',24,8,4)
        self.add_line('torso',(24,20),(24,26))
        self.add_polyline('arms',(10,10),(16,20),(24,20),(33,21),(38,17))
        self.add_polyline('leg-left',(24,26),(18,31),(13,29))
        self.add_polyline('leg-right',(24,26),(30,32),(34,27))
        path('trampoline',(6,40),[('A',(42,40),18,3,True),('A',(6,40),18,3,True)],True)
        self.add_line('left-support',(6,40),(6,44));self.add_line('right-support',(42,40),(42,44))
        join('torso','arms');join('torso','leg-left');join('torso','leg-right');join('leg-left','leg-right');join('trampoline','left-support');join('trampoline','right-support')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
