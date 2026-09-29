from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '74cd9635-1138-4c98-8a6c-b379d6f39c3c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-drinking-from-fountain/20260929T093326Z-thuan-mac/reference/water fountain drink_74cd9635-1138-4c98-8a6c-b379d6f39c3c.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Leaning person at left and wall-like pedestal fountain at right; head aligned to upper torso with 5-12-13 gap.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'person-drinking-from-fountain'
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
        circle('head',25,11,5)
        path('torso',(13,16),[('B',(8,18),(10,26),(10,31))])
        self.add_polyline('legs',(6,42),(10,31),(19,42))
        self.add_polyline('arm',(13,16),(17,29),(22,29))
        path('basin',(30,31),[('L',(42,31)),('L',(42,39)),('B',(34,39),(30,36),(30,31))],True)
        self.add_line('pedestal',(42,39),(42,42))
        path('water',(32,23),[('A',(42,23),5,5,True)])
        join('torso','legs');self.relate('connect','torso','arm');join('basin','pedestal')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
