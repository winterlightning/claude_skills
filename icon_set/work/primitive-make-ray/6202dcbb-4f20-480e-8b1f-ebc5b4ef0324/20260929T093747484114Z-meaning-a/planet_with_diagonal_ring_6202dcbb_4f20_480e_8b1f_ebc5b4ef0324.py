from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6202dcbb-4f20-480e-8b1f-ebc5b4ef0324'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__planet-with-diagonal-ring/20260929T093326Z-thuan-mac/reference/planet ringed_6202dcbb-4f20-480e-8b1f-ebc5b4ef0324.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Two globe arcs and a continuous tilted orbital band; asymmetry follows the source perspective.
# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.

class Drawing(Solo48):
    icon_id = 'planet-with-diagonal-ring'
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
        path('globe-upper',(10,29),[('B',(4,18),(13,7),(24,7)),('B',(31,7),(36,11),(38,17))])
        path('globe-lower',(17,39),[('B',(28,45),(40,34),(39,24))])
        path('ring',(10,26),[('B',(6,29),(6,32),(6,35)),('B',(6,42),(26,32),(35,23)),('B',(42,16),(44,10),(40,9)),('B',(38,8),(35,9),(33,10))])
