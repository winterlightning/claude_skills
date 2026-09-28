'Person with glasses.\n\nSymbol plan: Round-glasses avatar. The spectacle lenses replace the occluded upper face line; circular lower jaw and touching shoulders remain.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: glasses.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '70c73394-194d-461a-826d-fb778245dc72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-glasses-user-bust/20260927T171905Z-thuan-mac-1/reference/expert_70c73394-194d-461a-826d-fb778245dc72.svg'
AUTHOR = 'gpt-6'

class RoundGlassesUserBust(Solo48):
    icon_id = 'round-glasses-user-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('round', 'glasses', 'user', 'bust')

    def build(self):
        # The reference reads as a separate round head over broad shoulders.
        self.add_arc('head-upper',(12,16),(36,16),radius_x=12,sweep=True)
        self.add_arc('head-lower',(36,16),(12,16),radius_x=12,sweep=True)
        self.add_contour('head','head-upper','head-lower',closed=True)

        for label,left,right in (('left',12,24),('right',24,36)):
            self.add_arc(label+'-upper',(left,16),(right,16),radius_x=6,sweep=True)
            self.add_arc(label+'-lower',(right,16),(left,16),radius_x=6,sweep=True)
            self.add_contour(label+'-lens',label+'-upper',label+'-lower',closed=True)
        self.relate('connect','head','left-lens')
        self.relate('connect','head','right-lens')
        self.relate('connect','left-lens','right-lens')

        self.add_bezier('shoulder-left',(8,44),((8,39),(13,36),(20,36)))
        self.add_line('shoulder-top',(20,36),(28,36))
        self.add_bezier('shoulder-right',(28,36),((35,36),(40,39),(40,44)))
        self.add_line('shoulder-bottom',(40,44),(8,44))
        self.add_contour('shoulders','shoulder-left','shoulder-top',
                         'shoulder-right','shoulder-bottom',closed=True)
