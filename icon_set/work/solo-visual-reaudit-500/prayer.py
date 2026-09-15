from humans import *
r=next(r for r in records if r['number']==45);d=create(r['icon_id']).draw();save(45,emit(d,{}, {'carrier-1':Bezier('carrier-1',Point(18,22),Point(24,32),(((18,26),(23,29),(24,32)),))}),r['reason']+' Curve the carrier upper torso so its tangent aligns with its own head.')
save(432,"""self.ring('head',24,8,4)
self.branches([('torso',[(24,20),(24,26),(24,40)]),('left-arm',[(24,20),(8,26),(18,30),(24,26)]),('right-arm',[(24,20),(40,26),(30,30),(24,26)]),('left-leg',[(8,36),(24,40),(40,44)]),('right-leg',[(40,36),(24,40),(8,44)])])
""",'Seated prayer: draw a real shoulder junction and torso behind two bent arms whose palms meet at(24,26). Radius4 head(24,8), actual shoulder(24,20), exact4 painted clearance; the palms do not substitute for the shoulder. VRECT_L gives both arm counters room above the crossed legs. Original prayer source and full_body_ref.png inspected.','VRECT_L')
