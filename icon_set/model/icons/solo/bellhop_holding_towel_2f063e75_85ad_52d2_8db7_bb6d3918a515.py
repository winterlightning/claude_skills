"""Bellhop Holding Towel.

Plan: Capped attendant with towel over extended left forearm. Bounds (6,6)-(42,42).
Construction: human_ref/full_body_ref.png round head and articulated limbs, exact detached neck gap.
Reduction: Cap reduced to flat upper head silhouette; single-stroke uniform and limbs preserve towel-over-forearm pose.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '2f063e75-85ad-52d2-8db7-bb6d3918a515'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/staff_2f063e75-85ad-52d2-8db7-bb6d3918a515.svg'
AUTHOR = 'gpt-6'


class IconBellhopHoldingTowel(Solo48):
    icon_id = 'bellhop-holding-towel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('bellhop', 'holding', 'towel')

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
        path('head',(26,14),[('L',(26,6)),('L',(38,6)),('L',(38,14)),('A',(32,20),6,6,True),('A',(26,14),6,6,True)],True)
        # Flat upper head edge preserves cap silhouette without a narrow internal band.
        self.add_line('torso',(32,28),(32,36));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('arm-left',(32,28),(24,30),(14,30));self.relate('connect','arm-left','torso')
        self.add_line('arm-right',(32,28),(42,30));self.relate('connect','arm-right','torso');self.relate('connect','arm-left','arm-right')
        for name,end in [('leg-left',(26,42)),('leg-right',(38,42))]:self.add_line(name,(32,36),end);self.relate('connect',name,'torso')
        self.relate('connect','leg-left','leg-right')
        path('towel',(14,30),[('L',(6,30)),('L',(6,42)),('L',(14,42)),('L',(14,30))],True);self.relate('connect','towel','arm-left')
