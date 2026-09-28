"""Person Reaching in Shower.

Plan: Detached round head and raised arm beside upper-left shower pipe. Bounds (6,6)-(42,42).
Construction: Shared human_ref/full_body_ref.png detached head construction; Lucide shower-head pipe.
Reduction: One water stroke and single-stroke figure replace narrow body outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'fb62429d-4601-528d-8ec0-9b95660c475d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom shower person_fb62429d-4601-528d-8ec0-9b95660c475d.svg'
AUTHOR = 'gpt-6'


class IconPersonReachingInShower(Solo48):
    icon_id = 'person-reaching-in-shower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('person', 'reaching', 'in', 'shower')

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
        circle('head',24,16,5)
        self.add_line('torso',(24,29),(24,42));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        path('arm',(24,32),[('C',(42,12),(34,32),(42,22))]);self.relate('connect','arm','torso')
        path('shower',(6,6),[('L',(9,6)),('A',(12,9),3,3,True)])
        self.add_line('water',(7,19),(6,25))
