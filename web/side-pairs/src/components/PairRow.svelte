<script>
  // One side pair: Original → Main → Sub → Combined, its status and badges, and what can be done with it.
  import '../styles/row.css';
  import PartFigure from './PartFigure.svelte';
  import CombinedFigure from './CombinedFigure.svelte';
  import CombinedReview from './CombinedReview.svelte';
  import PairPicker from './PairPicker.svelte';
  import {POSITIONS, round, dataURL, parts, state as stateOf, subIsText, display, editableDrawing} from '../lib/rules.js';
  import {mountBefore} from '../lib/actions.js';
  import {forms, openForm} from '../lib/picker.svelte.js';
  let {store, row, editor} = $props();

  const view = $derived.by(() => {
    store.version;
    const p = parts(store, row, store.flagged), {pair, main, sub} = p;
    const [label, tone, hint] = stateOf(store, row, p);
    const changed = p.ready && store.previews[pair.id]?.built ? store.staleRoles(pair.id) : [];
    const shownMain = display(store, row, 'main', main), shownSub = display(store, row, 'sub', sub);
    return {p, pair, main, sub, label, tone, hint, changed, shownMain, shownSub, ref: store.catalog.references[row.id],
            adjusted: p.ready && !!store.handLayout(pair.id), text: subIsText(store, row, pair),
            mainDrawing: editableDrawing(store, row, 'main', main), subDrawing: editableDrawing(store, row, 'sub', sub)};
  });
  const sizes = $derived((store.version, store.sizes()));
  let message = $state(''), recombining = $state(false), editMessage = $state({main: '', sub: ''});

  async function recombine() {
    recombining = true;message = '';
    try {
      // Composed here from the current drawings with automatic placement, then stored.
      const done = await window.SideData.buildPairs([view.pair.id]), result = done.results[0];
      if (done.skipped.length) throw Error(done.skipped[0].error);
      if (!result.ok) throw Error(result.error);
      await store.refresh(view.pair.id);
    } catch (error) { message = error.message; }
    finally { recombining = false; }
  }
  async function editIcon(role, drawing) {
    editMessage[role] = '';
    try { await window.SideComponentEditor.open(drawing, `${role === 'main' ? 'Main' : 'Sub'} · ${drawing.icon_id}`); }
    catch (error) { editMessage[role] = error.message; }
  }
  // Change the main or sub of any pair here. A published pair opens with what it uses now; native text pairs keep
  // their typeface layout.
  const pickerRow = $derived.by(() => {
    const {pair, main, sub} = view;if (!pair || pair.native_text) return null;
    const current = (item, family) => { const key = item ? item.model_key || item.key || item.family + '/' + item.icon : '';
      return key?.startsWith(family + '/') ? {key, icon_id: item.icon, name: item.icon.replace(/-/g, ' '), preview_url: item.document ? dataURL(item.document) : item.preview_url} : null; };
    const published = !pair.custom || !!pair.published;
    return {uuid: row.id, concept: row.concept, published, position: pair.position,
            current: published && !pair.custom ? {main: current(main, 'solo'), sub: current(sub, 'sub')} : null};
  });
  // The review chip of a part with the drawing it shows (side-repair-flags.js).
  const reviewItem = (role, item) => { const d = editableDrawing(store, row, role, item);return d ? {...item, model_key: d.key, sha256: d.svg_sha256} : item; };
  const download = $derived((store.version, view.p.ready ? store.combined(view.pair, view.sub) : null));
</script>

<article class="side-row" data-pair-id={row.id}>
  <div class="side-row-head">
    <h3>{row.concept}</h3>
    <span class="side-meta">{POSITIONS[view.pair?.position] || view.pair?.position || 'Side'} · {view.pair?.native_text ? `${round(view.pair.canvas_width)}×${round(view.pair.canvas_height)}` : `${sizes.canvas}×${sizes.canvas}`}</span>
    <span class={'side-state ' + view.tone} title={view.hint}>{view.label}</span>
    {#if view.text}<span class="side-state info">Text sub</span>{/if}
    {#if view.pair?.published}<span class="side-state info" title={'The published main / sub was changed here: ' + row.main_id + ' + ' + row.sub_id + '.'}>Main / sub changed</span>
    {:else if view.pair?.custom}<span class="side-state info" title={'Made from a combination primitive on the review page: ' + row.main_id + ' + ' + row.sub_id + '.'}>From review</span>{/if}
    {#if view.pair?.mains.length > 1}<span class="side-state info">{view.pair.mains.length} mains · showing first</span>{/if}
    {#if view.adjusted}<span class="side-state info" title="Main / sub positions and sizes were set by hand.">Adjusted layout</span>{/if}
    <!-- A main or sub redrawn since this pair was combined: the combined icon still shows the old one. -->
    {#if view.p.ready && view.changed.length}
      <span class="side-state info" title={`The ${view.changed.join(' and ')} changed after this icon was combined. Use Recombine this icon (or Adjust layout) to rebuild it from the current drawings.`}>Outdated: recombine</span>
    {/if}
  </div>
  <div class="side-steps">
    <div class="side-step"><p class="side-step-label">Original</p>
      <div class="side-original">
        {#if view.ref?.reference_url}<img src={view.ref.reference_url} alt={row.concept + ' — original'} loading="lazy">
        {:else}<span class="side-combined-empty">Reference missing</span>{/if}
      </div>
    </div>
    {#each [['main', view.shownMain, view.mainDrawing, sizes.main], ['sub', view.shownSub, view.subDrawing, sizes.sub]] as [role, item, drawing, size] (role)}
      <div class="side-step">
        <p class="side-step-label">{role === 'sub' && view.sub?.native_text ? 'Sub · native' : (role === 'main' ? 'Main · ' : 'Sub · ') + size}</p>
        <PartFigure s={store} label={role === 'main' ? 'Main' : 'Sub'} {item} {size} isSub={role === 'sub'} {drawing} concept={row.concept} />
        {#if item?.icon}<p class="side-step-name">{item.icon}</p>{/if}
        <!-- A part with no icon yet can name the one still to draw (Change main / sub › None of these). -->
        {#if view.pair && !view.pair[role + 's'].length && view.pair[role + '_name']}<p class="side-step-name">To draw: {view.pair[role + '_name']}</p>{/if}
        {#if drawing && drawing.profile !== 'TEXT_NATIVE_V2' && window.SideComponentEditor}
          <div class="requires-login">
            <button type="button" class="side-edit-component" onclick={() => editIcon(role, drawing)}>Edit {role} icon</button>
            <p class="side-editor-message" role="status">{editMessage[role]}</p>
          </div>
        {/if}
      </div>
    {/each}
    <div class="side-step"><p class="side-step-label">{view.pair?.native_text ? 'Combined · native' : 'Combined · ' + sizes.canvas}</p>
      {#if view.p.ready}<CombinedFigure {store} pair={view.pair} sub={view.sub} />
      {:else}<div class="side-combined"><span class="side-combined-empty">Not combined yet</span></div>{/if}
      {#if view.p.ready && !view.pair.mapped_native}
        <div class="requires-login">
          <button type="button" class="side-edit-component" title="Use the latest saved main and sub with automatic placement" disabled={recombining} onclick={recombine}>
            {recombining ? 'Recombining…' : view.changed.length ? 'Recombine (outdated)' : 'Recombine this icon'}</button>
          <p class="side-editor-message" role="status">{message}</p>
        </div>
        <p class="login-prompt"><a href="login.html">Log in</a> to recombine this icon or adjust its layout.</p>
        <!-- Editing the layout sits right under the combined icon it changes. -->
        <button type="button" class="side-layout-open" title="Move and resize the main, the sub or chosen elements, snapped to the grid"
                onclick={() => editor.show(view.pair, view.main, view.sub, () => store.refresh(view.pair.id), store.handLayout(view.pair.id))}>Edit layout</button>
      {/if}
    </div>
  </div>
  {#if pickerRow}
    <div class="component-brief side-pair side-pair-editor">
      {#if forms.get(row.id)}<PairPicker row={pickerRow} onSaved={() => store.refresh(row.id)} />
      {:else}<button type="button" class="login-only" onclick={() => openForm(pickerRow)}>Change main / sub</button>{/if}
    </div>
  {/if}
  {#if view.p.ready}
    <div class="pair-card-actions">
      {#if download?.url || download?.result?.svg}
        <span hidden use:mountBefore={() => { const a = document.createElement('a');a.href = download.url || dataURL(download.result.svg);a.download = view.pair.id + '.svg';return window.SideRepairFlags?.download(a) || a; }}></span>
      {/if}
      {#if window.SideRepairFlags && !view.pair.native_text}
        <span hidden use:mountBefore={() => window.SideRepairFlags.button('main', reviewItem('main', view.main), view.pair)}></span>
        <span hidden use:mountBefore={() => window.SideRepairFlags.button('sub', reviewItem('sub', view.sub), view.pair)}></span>
      {/if}
      <CombinedReview {store} pair={view.pair} main={view.main} sub={view.sub} />
    </div>
  {/if}
</article>
