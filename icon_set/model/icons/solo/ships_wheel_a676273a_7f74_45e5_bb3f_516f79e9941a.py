"""ships-wheel: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a676273a-7f74-45e5-bb3f-516f79e9941a'
SOURCE_PATH = 'pictographic-primitives/transportation/wheel boat_a676273a-7f74-45e5-bb3f-516f79e9941a.svg'
AUTHOR = 'gpt-6'


class ShipsWheel(Solo48):
    icon_id = 'ships-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('ship wheel', 'helm', 'steering', 'nautical', 'boat', 'captain', 'sailing', 'marine', 'sub icon')

    def build(self) -> None:

        # Exact integer points on a radius-15 rim, with radius-20 handle tips.
        # Spoke angles alternate 36.87 and 53.13 degrees, preserving quarter-turn symmetry.
        rim=[(24,9),(33,12),(39,24),(36,33),(24,39),(15,36),(9,24),(12,15)]
        tips=[(24,6),(36,8),(42,24),(40,36),(24,42),(12,40),(6,24),(8,12)]
        for i,(p,tip) in enumerate(zip(rim,tips)):
            self.add_arc(f'rim-{i}',p,rim[(i+1)%8],radius_x=15)
            self.add_polyline(f'spoke-{i}',(24,24),p,tip)
        self.add_contour('rim',*[f'rim-{i}' for i in range(8)],closed=True)
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('2ff122ea-615a-43a4-98d6-4efda67be0a5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/bacteria_2ff122ea-615a-43a4-98d6-4efda67be0a5.svg')]
