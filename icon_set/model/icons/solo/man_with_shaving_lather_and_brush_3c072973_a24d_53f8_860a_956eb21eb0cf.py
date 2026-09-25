"""Man with Shaving Lather and Brush.

Plan: HRECT centerlines (4,8)-(44,40); circular face and scalloped lather meet a flared shaving brush at the right cheek. Intentional asymmetry reserves space for the physical brush.
Construction references: Shared human_ref/user.svg: circular face and minimal anatomy; supplied source controls the shaving/lather/brush relationship.
Reduction: Omitted eyes, smile and neck to emphasize shaving; simplified brush handle to one rounded stroke. Isolated head: no head/body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '3c072973-a24d-53f8-860a-956eb21eb0cf'
SOURCE_PATH = 'pictographic-primitives/beauty/beard style shave_3c072973-a24d-53f8-860a-956eb21eb0cf.svg'
SOURCE_ICON_IDS = ('3c072973-a24d-53f8-860a-956eb21eb0cf',)
SOURCE_PATHS = ('pictographic-primitives/beauty/beard style shave_3c072973-a24d-53f8-860a-956eb21eb0cf.svg',)
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'


class ManWithShavingLatherAndBrush(Solo48):
    icon_id = 'man-with-shaving-lather-and-brush'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('man', 'with', 'shaving', 'lather', 'and', 'brush')

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

        path("face",(4,22),[("A",(32,22),14,14,True),("A",(4,22),14,14,True)],True)
        path("lather",(4,22),[("C",(12,26),(6,22),(8,30)),("C",(18,26),(14,24),(16,24)),("C",(24,26),(20,24),(22,24)),("C",(32,22),(28,30),(30,22))])
        self.relate("connect","face","lather")
        self.add_polyline("brush-bristles",(32,22),(34,32),(38,32),(42,32),(44,22))
        self.relate("connect","face","brush-bristles")
        self.relate("connect","lather","brush-bristles")
        self.add_line("brush-handle",(38,32),(38,40))
        self.relate("connect","brush-bristles","brush-handle")
