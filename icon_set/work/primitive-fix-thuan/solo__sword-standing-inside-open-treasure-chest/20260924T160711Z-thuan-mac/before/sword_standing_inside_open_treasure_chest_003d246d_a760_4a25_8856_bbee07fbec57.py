"""Sword standing in an open treasure chest.
VRECT_L (8,4)-(40,44) holds a broad chest beneath an diagonal sword.
Sword and chest own shared receiving nodes; guard halves share one junction.
Reference supplies chest/pommel relationship; Lucide sword supplies a simple
crossguard construction. Omit double rim and reduce blade to a single stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '003d246d-a760-4a25-8856-bbee07fbec57'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/loot box treasure chest reward 2_003d246d-a760-4a25-8856-bbee07fbec57.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'sword-standing-inside-open-treasure-chest'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Treasure Chest with Sword',)
    keywords = ('sword','chest','treasure','blade','pommel','storage','loot')
    def build(self):
        self.add_arc('pommel-a',(33,4),(33,10),radius_x=3)
        self.add_arc('pommel-b',(33,10),(33,4),radius_x=3)
        self.add_contour('pommel','pommel-a','pommel-b',closed=True)
        self.add_line('grip',(33,10),(24,14))
        self.add_line('guard-left',(20,10),(24,14))
        self.add_line('guard-right',(24,14),(28,18))
        self.add_line('blade',(24,14),(16,28))
        self.add_line('rim-left',(8,28),(16,28))
        self.add_line('rim-right',(16,28),(40,28))
        self.add_line('side-right',(40,28),(40,40))
        self.add_arc('corner-right',(40,40),(36,44),radius_x=4)
        self.add_line('base',(36,44),(12,44))
        self.add_arc('corner-left',(12,44),(8,40),radius_x=4)
        self.add_line('side-left',(8,40),(8,28))
        self.add_contour('chest','rim-left','rim-right','side-right','corner-right','base','corner-left','side-left',closed=True)
        self.relate('connect','pommel','grip')
        for a in ('grip','guard-left','guard-right','blade'):
            for z in ('grip','guard-left','guard-right','blade'):
                if a<z:self.relate('connect',a,z)
        self.relate('connect','blade','chest')
