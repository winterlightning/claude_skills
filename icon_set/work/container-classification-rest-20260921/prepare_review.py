"""Materialize visual review decisions and independently reusable component briefs."""
import collections, copy, hashlib, html, json, re
from pathlib import Path
P=Path(__file__).resolve().parent
src=json.loads((P/'scope.json').read_text())
dec=json.loads((P/'visual-decisions.json').read_text())
reuse={x['number']:x for x in json.loads((P/'reuse-shortlist.json').read_text())}
assert dec['reviewed_through']==750
def b(name,description,family='sub'):
    return dict(name=name,description=description,family=family)
circle=b('Circle','A complete circular outline. Exclude all surrounding artwork.')
square=b('Rounded square','A complete rounded square outline. Exclude all surrounding artwork.')
triangle=b('Upright triangle','A complete upright triangular outline. Exclude all surrounding artwork.')
right=b('Right arrow','A horizontal shaft ending in an open right-pointing arrowhead. Exclude the enclosure.')
left=b('Left arrow','A horizontal shaft ending in an open left-pointing arrowhead. Exclude the enclosure.')
up=b('Up arrow','A vertical shaft ending in an open upward-pointing arrowhead. Exclude the enclosure and people.')
down=b('Down arrow','A vertical shaft ending in an open downward-pointing arrowhead. Exclude the enclosure and people.')
cross=b('Cross mark','Two diagonal strokes crossing as an X. Exclude the enclosure.')
check=b('Checkmark','A checkmark with a short descending left arm and longer ascending right arm. Exclude the enclosure.')
plus=b('Plus sign','Two equal perpendicular strokes crossing at the center. Exclude the enclosure and person.')
heart=b('Heart','A symmetrical outlined heart. Exclude the people and frame.')
lines2=b('Two writing lines','Two horizontal writing-like strokes, the lower shorter. No readable text; exclude the enclosure and portrait.')
lines3=b('Three writing lines','Three stacked horizontal writing-like strokes, the lowest shortest. No readable text; exclude the enclosure.')
portrait=b('User bust','A circular head above an open curved shoulder arc. Complete the shoulders independently; exclude the enclosure.')
content={
20:[b('Overlapping circle and square','A large circular outline partly overlapping a smaller rounded square at its upper-right. Complete both shapes without the artboard.'),b('Short horizontal stroke','A short straight horizontal stroke. Exclude the artboard.'),b('Angled brush-like mark','A shallow rounded rectangular bowl joined at its upper-left to a short diagonal handle. Complete its right edge independently of the artboard; preserve the visible ambiguous brush-like shape.')],
23:[right,left],
80:[b('Pie chart','A circular chart divided into three sectors by a vertical upper radius and diagonal lower-left radius from a shared center. Exclude the page.'),b('Two summary lines','Two horizontal lines stacked below one another, lower shorter; exclude the chart and page.')],
81:[b('Mountain and sun','Two adjoining mountain peaks, the left higher, beneath a circular sun at upper-right. Complete the landscape without a frame.'),b('Two summary lines','Two horizontal lines, upper shorter; exclude the image and page.')],
137:[b('Angular pulse trace','A horizontal signal trace with two upward peaks separated by a deep downward valley. Complete both ends without the screen.'),b('Flowing wave trace','An undulating horizontal line with two rounded peaks and three troughs; exclude the screen.')],
202:[b('Dollar sign','An S-shaped dollar glyph crossed by short vertical extensions. Exclude the page.'),b('Billing summary lines','Two short horizontal lines stacked at left and one longer line below; exclude the dollar sign and page.')],
215:[b('Connected portrait bust','A rounded head joining a neck and broad shoulders with a flat lower edge. Complete the bust without the card.'),lines2],
217:[b('Separated portrait bust','A circular head above a separate rounded shoulder block with a flat base. Exclude the card.'),lines2],
452:[b('Cloud','A complete cloud with rounded upper lobes and flat base; restore the left edge where it meets the phone bezel. Exclude both devices.'),b('Open circular trace','A C-shaped circular outline opening right, as seen on the laptop screen. Do not turn it into a second cloud; exclude both devices.')],
562:[b('Landscape image','A rising and falling mountain ridge with a small circular sun above-left. Complete it independently of the monitor.'),lines3],
662:[circle,triangle,square],
}
extra={
273:[heart],281:[heart],296:[plus],297:[plus],301:[cross],345:[check],
440:[lines2],441:[b('Progress arrows','Three separate right-pointing arrows in one horizontal row. Exclude the document.'),b('Progress field','A short horizontal dash at left and an outlined horizontal rectangular field to its right. Exclude the checkmark, arrows and page.')],
539:[b('Diamond suit','A complete upright rhombus. Exclude the cards and spade.')],
572:[b('Alert stroke','A short upright stroke visible in the smaller speech bubble. Keep the source stroke; exclude the bubbles and question mark.')],
587:[check],590:[cross],613:[cross],
615:[b('Checkbox frame','A complete empty rounded square outline. Exclude the clipboard and checkmark.','container'),lines3],
616:[b('Circular check frame','A complete empty circle. Exclude the page and checkmark.','container'),lines3],
631:[left,right],665:[lines2],694:[lines2],
704:[b('Trim timeline','Two horizontal timeline segments with upright end markers, separated by a short central dash. Exclude the video bubble and play triangle.')],
728:[up],729:[up,down],730:[up,down],737:[up,down],
}
main_edits={
23:b('Overlapping page frames','Two offset rounded rectangular page frames, upper-left in front of lower-right. Complete both outlines and leave their interiors empty; exclude both arrows.','container'),
562:b('Monitor with split content area','A desktop monitor with a lower bezel, central upright stand and flat foot. Its screen has a vertical center divider. Exclude the landscape and writing lines.','container'),
703:b('Video window with caption tail','A rounded rectangular screen above a narrow lower playback band with a horizontal slider track and short upright marker. A caption tail extends from the lower-left. Exclude the play triangle.','container'),
}
side={
611:[b('Envelope','A complete horizontal envelope with a folded triangular flap. Exclude the speech bubble and cross.','solo'),b('Empty medical-message bubble','A rounded rectangular bubble with a lower-right tail. Complete its outline; exclude the envelope and cross.','container'),b('Medical cross','An outlined equal-armed medical cross. Exclude the bubble and envelope.')],
746:[b('Person using laptop','A seated front-facing person with a round head and curved shoulders beside an open laptop resting on a horizontal baseline. Complete the person and laptop independently; exclude the floating video window and remote participant.','solo'),b('Empty video window','A rounded rectangular video window with a narrow top header. Complete its lower-right outline; exclude both people and laptop.','container'),portrait],
747:[b('Two people','Two front-facing busts side by side, each a circular head above an open curved shoulder arc. Exclude all speech bubbles and symbols.','solo'),b('Empty feedback bubble','A rounded rectangular speech bubble with a short downward central tail. Exclude people, checkmark and cross.','container'),check,cross],
}
# The gallery has two component slots. Additional components remain independent
# in the saved full reference brief and the per-source component export.
placements={611:'top-left',746:'top-left',747:'top-left'}
notes={452:'Laptop content is an open circular trace; the phone contains a cloud. The two screens do not contain the same glyph.',750:'Reuse the completed bust three times inside the panel grid and once as the larger foreground participant. Preserve the foreground position in later composition; do not omit that person.',20:'Brush-like lower-right content is visually ambiguous. Preserve its visible shallow bowl/angled handle draft and resolve its intended object before authoring.',640:'Name/concept needs editorial review: preserve the divided rectangle and central circle; no ant is visible.'}
solo_descriptions={
130:'A front-facing patient with a round head and shoulders behind a rectangular chest X-ray plate. The plate shows a central spine and curved ribs aligned with the patient; keep the whole examination scene together.',
619:'A circular outline crossed by a diagonal slash, with the small attached notch shown in the source. Keep this integrated mark together.',
640:'A rounded rectangular field divided horizontally through its center, with a circular center marking crossing the dividing line. Preserve this as one layout symbol; do not invent an ant or other content.',
651:'A rounded document outline with a folded upper-right corner whose seam extends into an inset rectangular loop. Preserve the connected page/logo construction.',
668:'A square outline whose left edge curves inward into a broad spiral, with a small separated triangular lower-left corner and open lower edge. Preserve the connected square-and-spiral construction.',
672:'A square land-plot outline with a gently rising terrain curve connecting its side boundaries near the bottom.',
712:'Two overlapping equilateral triangles form a six-pointed star inscribed in a circle, with the star tips meeting the circular boundary.',
718:'A rounded square map containing two opposing right triangles separated by a broad diagonal lane. Keep the complete integrated arena-map layout.',
}
def clean(s):
    return re.sub(r'(?:Exclude|Omit|Leave|Keep (?:the|its)|Complete .*? without)[^.]*\.', '',s,flags=re.I).strip()
out=[]
component_dir=P/'component-briefs';component_dir.mkdir(exist_ok=True)
for n,r in enumerate(src,1):
    d=r['decision'];route='container' if d.get('sub_brief') else 'solo'
    for k in ['solo','container','side','text']:
        if str(n) in dec[k+'_overrides']:route=k
    why=dec.get(route+'_overrides',{}).get(str(n))
    if not why:why=('No independently meaningful hosted content is visible; the enclosure, controls or layout are one standalone subject.' if route=='solo' else d['note'])
    row=dict(number=n,uuid=r['uuid'],name=r['concept'],reference_path=r['path'],category=r['category'],batch=r['batch'],route=route,visual_reason=why,notes=notes.get(n,dec['notes'].get(str(n),'')))
    if route=='solo':
        main=d.get('main_brief') or {};sub=d.get('sub_brief') or {}
        description=solo_descriptions.get(n,clean(main.get('description','')))
        if sub and n not in solo_descriptions:description+=' Intrinsic details to retain with the subject: '+clean(sub['description'])
        assert description
        row['components']=[b(r['concept'],description,'solo')]
        candidates=reuse[n]['candidates']
        linked=[c for c in candidates if c['source_linked']]
        # Only source-linked artwork was visually checked in this pass. Search
        # suggestions are kept separately and are never approval to reuse.
        row['reuse_candidates']=linked or [c for c in candidates if c['score']>=0.6]
        if linked:
            row['reuse_action']='reuse_existing_solo' if linked[0]['family']=='solo' else 'convert_existing_artwork_to_solo'
            row['status']='skip';row['reason']='other'
            row['reuse_note']='Source-linked artwork visually checked. Reuse its subject; retain source-specific details through adaptation if required. Container-family artwork still requires SOLO48 conversion and validation.'
        else:
            row['reuse_action']='check_library_before_generation';row['status']='todo';row['reason']=None
            row['reuse_note']='This is a solo routing decision, not evidence that new artwork is needed. Candidate names are search leads only. Check actual artwork and all other solo briefs before any generation; share one result for duplicate concepts.'
    else:
        cs=copy.deepcopy(side[n] if route=='side' else [main_edits.get(n,d['main_brief'])]+content.get(n,[d['sub_brief']])+extra.get(n,[]))
        assert all(cs),(n,cs)
        row['components']=cs;row['status']='skip';row['reason']='combination' if route=='side' else 'container'
        row['sub_position']=placements.get(n)
        row['reuse_action']='check_each_component_before_generation'
        row['reuse_note']='Search existing library artwork for each component independently. A source classification is not permission to redraw the combined icon or create duplicate components.'
    if route!='solo':
        row['main_brief']=row['components'][0]
        row['sub_brief']=next(c for c in row['components'][1:] if c['family']=='sub')
    row['component_fields_corrected']=[row['main_brief'],row['sub_brief']]!=[d.get('main_brief'),d.get('sub_brief')] if route!='solo' else False
    row['extra_components_added']=max(0,len(row['components'])-2)
    row['new_generation_allowed']=False
    brief=f"# {r['concept']} — {route} route\n\nSource UUID: {r['uuid']}\nReference path: {r['path']}\n\nVisual review: {why}\n\n"
    if row['notes']:brief+='Review note: '+row['notes']+'\n\n'
    if route=='solo':brief+='Target family: solo (SOLO48). Preserve the complete standalone subject. Do not split intrinsic parts into container/sub icons.\n\n'
    else:brief+='Prepare each component independently; never regenerate the combined source as one primitive. All component families below apply to their separate outputs.\n\n'
    for i,c in enumerate(row['components'],1):
        brief+=f"## Component {i}: {c['name']}\nFamily: {c['family']}\n{c['description']}\n\n"
        dest=component_dir/f'{n:03}-{i:02}.md'
        dest.write_text(f"# {c['name']}\n\nSource UUID: {r['uuid']}\nReference path: {r['path']}\nFamily: {c['family']}\n\n{c['description']}\n\nGenerate only this component after a library reuse check. Do not recreate the combined source.\n")
    if row.get('sub_position'):brief+='Sub icon position relative to main: '+row['sub_position']+'. The saved sub glyph appears within a separate bubble/window at this position.\n\n'
    if n==747:brief+='Use two copies of the empty feedback bubble: checkmark above the left person and cross above the right person. Each glyph and each empty bubble remains an independent component.\n\n'
    if len(row['components'])>2:brief+='The gallery fields show the main subject and the first sub-family component; additional container and sub components are independently listed here and in the component export.\n\n'
    brief+='Reuse / duplicate prevention: '+row['reuse_note']+'\n'
    for c in row.get('reuse_candidates',[]):brief+=f"\n{'Source-linked reuse target' if c['source_linked'] else 'Unverified search lead'}: {c['icon_id']} ({c['family']}). Artwork: {c['svg_path']}\n"
    brief+='\nNo generation job is authorized or queued by this classification review. Recheck the live library before authoring.\n'
    row['reference_brief']=brief
    out.append(row)
counts=dict(collections.Counter(x['route'] for x in out))
summary={'reviewed':750,'routes':counts,'original_850_routes':{'solo':counts['solo']+76,'container':counts['container']+24,'side':counts.get('side',0)},'classification_corrections':sum(x['route']!='container' for x in out),'component_field_corrections':sum(x['component_fields_corrected'] for x in out),'sources_with_extra_components':sum(x['extra_components_added']>0 for x in out),'component_briefs':sum(len(x['components']) for x in out),'solo_actions':dict(collections.Counter(x['reuse_action'] for x in out if x['route']=='solo')),'saved_statuses':dict(collections.Counter(x['status'] for x in out)),'new_generation_jobs':0,'scope':'Remaining 750 of the original 850; prior 100 are unchanged.'}
(P/'review.json').write_text(json.dumps({'summary':summary,'rows':out},indent=2))
(P/'components.json').write_text(json.dumps([dict(source_number=x['number'],source_uuid=x['uuid'],reference_path=x['reference_path'],components=x['components'],placement=x.get('sub_position')) for x in out],indent=2))
print(json.dumps(summary,indent=2))
