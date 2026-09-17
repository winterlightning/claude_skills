"""Hair Dryer with Airflow.

Plan: Rounded motor housing with right nozzle, slanted handle and three airflow strokes. Bounds (4,8)-(44,40).
Construction: Source hair dryer; no useful exact local Lucide match.
Reduction: Plain housing omits tiny rear grille and nozzle collar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '81215f58-3304-53f6-95b4-3ac86ae85327'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom hair dryer_81215f58-3304-53f6-95b4-3ac86ae85327.svg'
AUTHOR = 'gpt-6'


class IconHairDryerWithAirflow(Solo48):
    icon_id = 'hair-dryer-with-airflow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('hair', 'dryer', 'with', 'airflow')

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
        path('dryer',(14,8),[('L',(28,8)),('L',(28,24)),('L',(20,24)),('L',(16,40)),('L',(7,40)),('L',(11,24)),('C',(4,16),(7,24),(4,20)),('C',(14,8),(4,11),(8,8))],True)
        for y in [8,16,24]:self.add_line('air'+str(y),(37,y),(44,y))
