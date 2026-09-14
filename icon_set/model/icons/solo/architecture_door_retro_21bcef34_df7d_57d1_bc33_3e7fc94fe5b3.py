'Retro arched door: matching vertical walls and one true semicircle; handle moved inward. Lucide door-closed informs the structural sill.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21bcef34-df7d-57d1-bc33-3e7fc94fe5b3'
SOURCE_PATH = 'icons-json/building/architecture door retro_21bcef34-df7d-57d1-bc33-3e7fc94fe5b3.json'
AUTHOR = 'gpt-6'

class ArchitectureDoorRetro(Solo48):
    icon_id = 'architecture-door-retro'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('architecture', 'door', 'retro', 'building')

    def build(self) -> None:
        # VRECT_L extremes via sill and semicircular arch; exact bilateral construction.
        self.add_line('left',(12,44),(12,16))
        self.add_arc('arch',(12,16),(36,16),radius_x=12)
        self.add_line('right',(36,16),(36,44))
        self.add_contour('door','left','arch','right')
        self.add_polyline('sill',(8,44),(12,44),(36,44),(40,44))
        self.relate('connect','door','sill')
        self.add_line('handle',(27,27),(27,30))
