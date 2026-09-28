"""Hand Ringing Service Bell.

Plan: Descending finger points onto the button above a broad bell dome. Bounds (6,6)-(42,42).
Construction: Lucide concierge-bell dome, button and rim; shared human hand reference for rounded fingertip.
Reduction: Single extended finger silhouette omits curled finger creases.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '03a6657e-e3c0-4963-bdc9-8955e695afe1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/reception bell call_03a6657e-e3c0-4963-bdc9-8955e695afe1.svg'
AUTHOR = 'gpt-6'


class IconHandRingingServiceBell(Solo48):
    icon_id = 'hand-ringing-service-bell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('hand', 'ringing', 'service', 'bell')

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
        path('bell',(6,42),[('C',(24,29),(6,35),(14,29)),('C',(42,42),(34,29),(42,35)),('L',(6,42))],True)
        path('hand',(6,6),[('L',(14,6)),('L',(28,12)),('C',(24,20),(32,16),(28,20)),('C',(20,18),(22,20),(21,19)),('L',(6,16))])
        self.add_line('button',(24,20),(24,29));self.relate('connect','button','hand');self.relate('connect','button','bell')
