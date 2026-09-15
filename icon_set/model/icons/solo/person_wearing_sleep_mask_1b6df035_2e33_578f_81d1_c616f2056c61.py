"""Person Wearing Sleep Mask.

Plan: SQUARE centerlines (6,6)-(42,42); radius-18 circular face centered at (24,24) with a broad two-lobed sleep mask. Mirror controls preserve the central nose notch.
Construction references: Shared human_ref/user.svg: circular outlined head; supplied source controls the mask lobes and nose notch.
Reduction: Omitted the short neck and shoulders to give the sleep mask and facial openings sufficient room; this is an isolated head, with no head/body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1b6df035-2e33-578f-81d1-c616f2056c61'
SOURCE_PATH = 'pictographic-primitives/beauty/body care eye mask_1b6df035-2e33-578f-81d1-c616f2056c61.svg'
SOURCE_ICON_IDS = ('1b6df035-2e33-578f-81d1-c616f2056c61',)
SOURCE_PATHS = ('pictographic-primitives/beauty/body care eye mask_1b6df035-2e33-578f-81d1-c616f2056c61.svg',)
AUTHOR = 'gpt-6'


class PersonWearingSleepMask(Solo48):
    icon_id = 'person-wearing-sleep-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('person', 'wearing', 'sleep', 'mask')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        axis,cy,radius=24,24,18
        path("face",(6,24),[("A",(42,24),radius,radius,True),("A",(6,24),radius,radius,True)],True)
        path("sleep-mask",(6,24),[("C",(42,24),(6,14),(42,14)),("C",(27,26),(42,34),(32,34)),("C",(21,26),(25,23),(23,23)),("C",(6,24),(16,34),(6,34))],True)
        self.relate("connect","face","sleep-mask")
