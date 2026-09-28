"""Three separated hexagonal nanobots retain the source's staggered swarm arrangement.
Plan: one upper bot and two lower bots; shared 12-unit hex definition and balanced pair. The tiny eyes and claws are omitted because their clearance is below SOLO48's minimum.
Keyshape HRECT_L reaches (4,8)-(44,40) on centerlines. Lucide bot informed the compact robot-unit silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "e264133e-8474-4b00-bda2-455eae35ae6d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__nanobot-swarm-e264133e/20260927T164305Z-thuan-mac-1/reference/nanobots_e264133e-8474-4b00-bda2-455eae35ae6d.svg"
AUTHOR = "gpt-6"
class NanobotSwarm(Solo48):
 icon_id = "nanobot-swarm-e264133e"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "health"
 aliases = ("nanobot-swarm",)
 keywords = ("nanobot", "swarm", "robot")
 def build(self):
  def bot(label,cx,top):
   points=((cx,top),(cx+6,top+2),(cx+6,top+8),(cx,top+10),(cx-6,top+8),(cx-6,top+2))
   self.add_polyline(label,*points,closed=True)
   self.add_line(label+"-stem",(cx,top+10),(cx,top+14))
   self.relate("connect",label,label+"-stem")
  bot("leader",24,8)
  bot("follower-left",10,26)
  bot("follower-right",38,26)
