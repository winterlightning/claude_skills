"""Person Sleeping in Bed.

Plan: Round sleeping head left and horizontal blanket on a bed with two posts. Bounds (4,8)-(44,40).
Construction: Shared human reference exact detached neck gap; Lucide bed post and rail.
Reduction: Single bed rail and broad blanket contour replace doubled mattress bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '65881da4-e2b5-4025-8419-8ee364d9b2ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/hotel bed_65881da4-e2b5-4025-8419-8ee364d9b2ba.svg'
AUTHOR = 'gpt-6'


class IconPersonSleepingInBed(Solo48):
    icon_id = 'person-sleeping-in-bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('person', 'sleeping', 'in', 'bed')

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
        circle('head',17,17,5)
        path('torso',(30,17),[('L',(34,17)),('C',(44,30),(40,17),(44,23))])
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
        path('bed',(4,30),[('L',(44,30))]);self.relate('connect','bed','torso')
        for x,top in [(4,8),(44,30)]:
         path('post'+str(x),(x,top),[('L',(x,30)),('L',(x,40))] if top!=30 else [('L',(x,40))]);self.relate('connect','post'+str(x),'bed')
