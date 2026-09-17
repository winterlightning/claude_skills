"""Person under Shower Spray.

Plan: Centered detached head and rounded-shoulder body beneath three diverging water streams. Bounds (8,4)-(40,44).
Construction: Shared human_ref detached-head spacing; source overhead shower figure.
Reduction: One row of three streams, open-ended body and no inner arm seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ce7a49d0-bcbd-5c1c-bfa5-31baabdd658b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom person_ce7a49d0-bcbd-5c1c-bfa5-31baabdd658b.svg'
AUTHOR = 'gpt-6'


class IconPersonUnderShowerSpray(Solo48):
    icon_id = 'person-under-shower-spray'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('person', 'under', 'shower', 'spray')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        circle('head',24,21,5)
        path('torso',(24,34),[('C',(14,44),(18,34),(14,37))])
        path('right-body',(24,34),[('C',(34,44),(30,34),(34,37))]);self.relate('connect','torso','right-body')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
        for n,a,b in [('left',(12,4),(8,12)),('center',(24,4),(24,7)),('right',(36,4),(40,12))]:self.add_line('water-'+n,a,b)
