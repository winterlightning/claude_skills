"""A diagonal flared horn curves into a short neck on a rectangular plinth. Omit fine platter, tonearm and feet to preserve the horn silhouette. Extremes (8,4)-(40,44). Lucide megaphone flare principle."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='39999dfa-8760-4f0c-a5ad-a695e7e50318'
SOURCE_PATH='pictographic-primitives/music/vinyl record gramophone_39999dfa-8760-4f0c-a5ad-a695e7e50318.svg'
AUTHOR='gpt-6'

class Gramophone(Solo48):
    icon_id='gramophone'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('gramophone', 'phonograph', 'record', 'vinyl', 'vintage', 'horn', 'music', 'player')

    def build(self):
        self.add_line('horn-mouth',(8,24),(28,4))
        self.add_bezier('horn-back',(28,4),((28,18),(40,20),(38,34)))
        self.add_line('horn-foot',(38,34),(26,34))
        self.add_bezier('horn-front',(26,34),((34,26),(18,20),(8,24)))
        self.add_contour('horn','horn-mouth','horn-back','horn-foot','horn-front',closed=True)
        self.add_polyline('base',(8,34),(26,34),(38,34),(40,34),(40,44),(8,44),closed=True)
        self.relate('connect','horn','base')
