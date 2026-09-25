"""Raised child above mirrored supporting hands. Human full_body_ref: radius5 head at (24,11), torso starts (24,24), exact8 centerline gap. Lucide hand informs round palms. Finger divisions omitted.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de2a447f-9464-4dd2-8a82-6bf0842bf389'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/child care_de2a447f-9464-4dd2-8a82-6bf0842bf389.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-supporting-child'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('hands', 'supporting', 'child')

    def build(self):
        self.circle('head',24,11,5)
        self.add_polyline('arms',(10,16),(18,24),(24,24),(30,24),(38,16))
        self.add_line('torso',(24,24),(24,30))
        self.relate('connect','arms','torso')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
        self.cups()

    def path(self, name, start, steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            eid=f'{name}-{j}'
            if len(step)==2:
                self.add_line(eid,here,step); end=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

    def cups(self):
        # Mirrored hands about x24; equal fingertip radii and tangent S-curves into the wrists.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-hand',p(10,42),[(p(6,34),10,10,s>0),p(6,33),(p(14,33),4,4,s>0),(p(16,35),2,2,s<0),(p(18,37),2,2,s>0),p(18,42)])
