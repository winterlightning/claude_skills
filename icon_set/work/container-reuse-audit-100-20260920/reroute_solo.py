"""Persist the user's standalone-solo routing, with duplicate-generation holds."""
import collections
import html
import json
from pathlib import Path
import sqlite3
import sys

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_status import load_status, set_status
from icon_set.scripts.primitive_briefs import load_primitive_briefs, save_primitive_brief
from icon_set.scripts.deploy import record_activity

audit=json.loads((OUT/'audit.json').read_text())['rows']
original=json.loads((OUT/'sources.json').read_text())
solo_evidence={r['icon_id']:r for r in json.loads((OUT/'solo-candidate-evidence.json').read_text())}
direct=json.loads((OUT/'solo-match-candidates.json').read_text())
matches={r['number']:r['matches'][-1]['icon_id'] for r in direct if r['matches']}
matches.update({4:'layout-with-left-sidebar-batch-001-r3',27:'blank-folded-corner-page',32:'desktop-monitor-centre-post-stand',33:'desktop-monitor-bezel-splayed-stand',34:'desktop-monitor-bezel-splayed-stand',35:'desktop-monitor-curved-pedestal',36:'desktop-monitor-curved-pedestal',37:'desktop-monitor-splayed-stand',38:'desktop-monitor-bezel-splayed-stand',40:'film-strip-frame',43:'monitor-with-desk-keyboard',45:'desktop-monitor-centre-post-stand',46:'desktop-monitor-centre-post-stand',47:'desktop-monitor-curved-pedestal',50:'battery-1',53:'hanging-shop-sign-solo',61:'smartphone-bottom-bezel-solo-08a24aa4',65:'open-envelope-with-letter-solo',67:'square-brackets',68:'square-brackets',69:'double-bordered-rectangle',70:'retro-television-antenna',71:'retro-television-antenna',77:'rectangle-frame',78:'square-brackets',79:'plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32',80:'plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32',86:'square-selection-corner-handles',87:'square-selection-corner-handles',88:'square-face-smartwatch',92:'mobile-phone-with-speaker-slot',93:'plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32',94:'ticket-1',95:'ticket-1',96:'ticket-1',97:'browser-header-window-solo-dd2e4d0c',98:'browser-header-window-solo-dd2e4d0c'})
adapt={23:'Existing solo has a reduced table grid; restore the source three-column, two-row grid.',35:'Add the lower bezel divider to the existing curved-pedestal solo monitor.',36:'Same bezel addition as source 35; share one adapted solo asset.'}
notes={4:'Use the earlier batch-001-r3 version: its dashed divider is correctly on the left; the newer solo-b001-04 version incorrectly centers two dots.',5:'Existing solo uses two navigation marks rather than three; reuse the standard layout.',6:'Existing solo uses two navigation marks rather than three; reuse the standard layout.',40:'Existing solo uses connected perforation boxes rather than small separated slots; same film-frame concept.',43:'Existing solo adds a monitor stem; same blank monitor-and-keyboard subject.',69:'Existing solo differs in proportions but preserves the double-bordered empty frame.',70:'Existing solo has an extra inset screen border; same empty retro television subject.',71:'Reuse the same retro television as source 70.',88:'Reuse the existing square smartwatch with open curved wrist strap.',93:'Same pointed-top empty silhouette as the existing plain house outline; reuse the geometry with tag terminology rather than draw a duplicate.',94:'Rotate the existing ticket 90 degrees to place notches at top and bottom.',95:'Same rotated ticket asset as source 94.',96:'Same rotated ticket asset as source 94.',92:'Use the complete phone with speaker slot for the cropped upper-phone reference.'}
rows=[]
for r in audit:
    if r['content']['status']!='not_needed':continue
    n=r['number']
    if n in matches:
        candidate=solo_evidence[matches[n]]
        action='adapt_existing_solo' if n in adapt else 'reuse_existing_solo'
        note=adapt.get(n,notes.get(n,'Existing solo artwork matches this standalone subject; reuse it.'))
    else:
        candidate=r['container']['candidate']
        assert candidate is not None,(n,'Missing reuse starting point')
        action='convert_existing_artwork_to_solo'
        note='Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate.'
        if r['container']['status']=='adapt_existing':note+=' '+r['container']['note']
    assert Path(candidate['path']).is_file()
    assert candidate['validation']['status']=='valid'
    description=r['container']['brief']['description']
    row={'number':n,'source_uuid':r['source_uuid'],'name':r['source_name'],'reference_path':r['reference_path'],'target_family':'solo','action':action,'reuse_icon_id':candidate['icon_id'],'reuse_current_family':candidate['family'],'reuse_svg_path':candidate['path'],'description':description,'note':note,'new_generation_allowed':False}
    rows.append(row)

assert len(rows)==76
counts=dict(collections.Counter(r['action'] for r in rows))
summary={'rerouted_to_solo':76,'actions':counts,'new_generation_jobs':0,'unique_existing_artwork_targets':len({r['reuse_icon_id'] for r in rows}),'scope':'Only the 76 content-free sources from the 100-source audit. The other 24 are unchanged.','meaning':'Source routing/reference briefs changed. Existing icon model families and artwork are not migrated by this operation.'}
(OUT/'solo-routing.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2))

db=ROOT/'icon_set/.local/state/feedback.sqlite3'
connection=sqlite3.connect(db,timeout=10)
before_status=load_status(connection)
before_briefs=load_primitive_briefs(connection)
known={r['uuid'] for r in original}
affected={r['source_uuid'] for r in rows}
for r in rows:
    uid=r['source_uuid']
    assert before_status[uid]==original[r['number']-1]['decision'],f'Concurrent decision change: {uid}'
    assert uid not in before_briefs,f'New reference brief needs reconciliation: {uid}'
backup={uid:{'status':before_status.get(uid),'reference_brief':before_briefs.get(uid)} for uid in known}
(OUT/'before-solo-routing.json').write_text(json.dumps(backup,indent=2))
with connection:
    connection.execute('BEGIN IMMEDIATE')
    assert load_status(connection)==before_status,'Concurrent status update'
    assert load_primitive_briefs(connection)==before_briefs,'Concurrent brief update'
    for r in rows:
        uid=r['source_uuid']
        brief=f'''# Standalone solo route: {r['name']}

Target family: solo (SOLO48).
Source UUID: {uid}
Reference path: {r['reference_path']}

User decision: this empty frame or device is a standalone solo subject, not a container combination. No inner/sub icon is required. Do not split it into components.

Visual description: {r['description']}

Reuse action: {r['action']}
Existing icon ID: {r['reuse_icon_id']}
Existing family: {r['reuse_current_family']}
Existing artwork: {r['reuse_svg_path']}

{r['note']}

Duplicate-prevention hold: do not queue fresh generation. Reuse the existing solo, or adapt/convert the specified existing artwork to SOLO48 and validate it. Sources sharing the same target must share the result. Recheck the library before any new asset is created.
'''
        save_primitive_brief(connection,uid,'solo',brief,known=known,user='agent',record=record_activity)
        note=f"User rerouted empty standalone source to solo. Duplicate-generation hold: {r['action']} — {r['reuse_icon_id']}. See the saved solo reference brief."
        # 'other' is the existing store's duplicate/reuse hold; it is not a family.
        # It prevents a TODO generator from treating a reused reference as new work.
        set_status(connection,[uid],'skip','other',note,user='agent',record=record_activity,known=known)
after_status=load_status(connection)
after_briefs=load_primitive_briefs(connection)
for r in rows:
    uid=r['source_uuid']
    assert after_briefs[uid]['family']=='solo'
    assert r['reuse_icon_id'] in after_briefs[uid]['brief']
    assert after_status[uid]['reason']=='other'
    assert after_status[uid]['main_brief'] is None and after_status[uid]['sub_brief'] is None
assert all(after_status.get(uid)==before_status.get(uid) for uid in before_status.keys()-affected)
assert all(after_briefs.get(uid)==before_briefs.get(uid) for uid in before_briefs.keys()-affected)
connection.close()

report=f'''# Solo rerouting — 76 empty frames/devices

All **76** source reference briefs now route to **solo** in the local gallery database.

'''+''.join(f'- {key}: **{value}** sources\n' for key,value in counts.items())+f'''
**0** fresh-generation jobs were created. The 24 sources with inner content are unchanged.

These are source-routing changes, not completed geometry/family migrations. Existing solo assets can be reused. Other existing artwork is explicitly held for adaptation or SOLO48 conversion. Matching uses the standard-library subject, not pixel identity; meaningful differences are noted below. All candidates were visually inspected and their SVG files verified.

To prevent duplicate generation, these sources remain SKIP with reason `other` and a reuse explanation, instead of being returned to TODO. Their saved reference brief family is `solo`. Obsolete container component fields were cleared; complete previous values are retained in `before-solo-routing.json`.

The original 100-source audit is historical; this routing supersedes its treatment of these 76 sources. Existing model families, artwork, and the production gallery were not changed.

| # | Source | Action | Existing icon | Note |
|---|---|---|---|---|
'''
for r in rows:report+=f"| {r['number']} | {r['name']} | {r['action']} | {r['reuse_icon_id']} | {r['note']} |\n"
(OUT/'solo-routing-report.md').write_text(report)
old=OUT/'report.md'
old.write_text('> **Updated routing:** The 76 empty frames/devices now route to solo. See [solo-routing-report.md](solo-routing-report.md) for reuse targets and remaining conversion work. The audit below records the earlier container interpretation.\n\n'+old.read_text())
page=OUT/'index.html'
page.write_text(page.read_text().replace('<h1>100 container reuse checks</h1>','<h1>100 container reuse checks</h1><p><strong>Updated:</strong> the 76 empty sources now route to solo. See <a href="solo-routing-report.md">solo routing and reuse targets</a>. Comparisons below preserve the original audit.</p>'))
(OUT/'solo-routing-verification.json').write_text(json.dumps({'summary':summary,'persisted_solo_reference_briefs':76,'persisted_reuse_holds':76,'unrelated_decisions_unchanged':True,'unrelated_briefs_unchanged':True,'candidate_files_verified':True},indent=2))
print(json.dumps(summary,indent=2))
