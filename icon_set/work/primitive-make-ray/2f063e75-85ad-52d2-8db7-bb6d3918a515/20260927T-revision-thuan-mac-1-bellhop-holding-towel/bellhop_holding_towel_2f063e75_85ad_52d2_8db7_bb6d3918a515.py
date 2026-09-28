"""Bellhop Holding Towel.

Plan: Capped attendant with towel over extended left forearm. Bounds (6,6)-(42,42).
Construction: human_ref/full_body_ref.png round head and articulated limbs, exact detached neck gap.
Reduction: Cap reduced to flat upper head silhouette; single-stroke uniform and limbs preserve towel-over-forearm pose.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2f063e75-85ad-52d2-8db7-bb6d3918a515'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bellhop-holding-towel/20260927T152212Z-thuan-mac-1/reference/staff_2f063e75-85ad-52d2-8db7-bb6d3918a515.svg'
AUTHOR = "gpt-6"


class IconBellhopHoldingTowel(Solo48):
    icon_id = 'bellhop-holding-towel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
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
        # Long coat and a hanging towel give the attendant a clear silhouette.
        self.add_polyline('coat',(24,28),(32,28),(36,28),(40,32),(40,42),(32,42),(24,42),closed=True)
        self.add_line('torso',(32,28),(32,42))
        self.relate('connect','torso','coat')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_line('arm-left',(24,28),(14,30))
        self.relate('connect','arm-left','coat')
        self.add_line('arm-right',(36,28),(42,30))
        self.relate('connect','arm-right','coat')
        self.add_polyline('towel',(14,30),(6,30),(6,42),(14,42),closed=True)
        self.relate('connect','towel','arm-left')
