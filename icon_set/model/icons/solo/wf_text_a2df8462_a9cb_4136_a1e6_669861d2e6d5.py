"""A capital W and F sit beside each other on a shared baseline. The W combines four sloping strokes with rounded lower joins, and the F has a long top arm and a shorter middle arm."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2df8462-a9cb-4136-a1e6-669861d2e6d5'
SOURCE_PATH = 'pictographic-primitives/mobile/wifi network text_a2df8462-a9cb-4136-a1e6-669861d2e6d5.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'wf-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('wf', 'text', 'wireless', 'network', 'letters', 'mobile', 'typography')

    def build(self):
        # Lucide construction references: none.
        # Typed contours keep shared radii and continuous joins together.
        def path(name,start,commands,closed=False):
            here, members = start, []
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L':
                    self.add_line(ident,here,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(ident)
                here=end
            self.add_contour(name,*members,closed=closed)
        # HRECT_L extremes (4,8)-(44,40): symmetric W about x=16, F after an eight-unit gap.
        axis=16
        left=[(4,8),(10,40),(axis,20)]
        self.add_polyline('w',*left,*[(2*axis-x,y) for x,y in reversed(left[:-1])])
        self.add_polyline('f',(36,40),(36,24),(36,8),(44,8))
        self.add_line('f-middle',(36,24),(44,24))
        self.relate('connect','f','f-middle')
