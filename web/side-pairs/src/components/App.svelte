<script>
  // Progression › Side combination: every side pair of the chosen size as Original → Main → Sub → Combined, with the
  // icon counts, Build all / Rebuild stale, search, filter, grouping and pages. `page` is Progression's own state
  // (search text, page number, its URL), shared with the rest of primitives.html.
  import {tick, untrack} from 'svelte';
  import '../styles/row.css';
  import Summary from './Summary.svelte';
  import PairRow from './PairRow.svelte';
  import GroupSection from './GroupSection.svelte';
  import PartInspect from './PartInspect.svelte';
  import LayoutEditorDialog from './LayoutEditorDialog.svelte';
  import {FILTERS, GROUPS, PAGE_SIZES, key, category, groups as groupRows, matches, currentSub, dataURL} from '../lib/rules.js';
  let {store, editor, page, params} = $props();

  let filter = $state(FILTERS[params.get('side')] ? params.get('side') : '');
  let groupBy = $state(GROUPS[params.get('group')] ? params.get('group') : '');
  let pageSize = $state(PAGE_SIZES.includes(Number(params.get('size'))) ? Number(params.get('size')) : 24);
  let query = $state(page.query());
  let current = $state(page.page());
  let host = $state(), searchBox = $state();
  const openGroups = new Set();

  const sizes = $derived((store.version, store.sizes()));
  // A copy each time: the store changes its rows in place.
  const all = $derived((store.version, store.ready ? [...store.catalog.rows] : []));
  const categories = $derived(new Map(all.map(r => [r.id, category(store, r, store.flagged, store.buildState(r.id))])));
  const rows = $derived((store.version, all.filter(r => (!filter || categories.get(r.id)?.[filter]) && matches(store, r, query))));
  const grouped = $derived((store.version, groupBy ? groupRows(store, rows, groupBy, store.flagged) : null));
  const items = $derived(grouped || rows);
  const pages = $derived(Math.max(1, Math.ceil(items.length / pageSize)));
  const visible = $derived(items.slice((Math.min(current, pages) - 1) * pageSize, Math.min(current, pages) * pageSize));

  // Build all: ready pairs not built yet or built from older drawings. Rebuild: stale pairs only.
  const buildable = $derived((store.version, store.ready ? all.filter(r => key(store, r, store.flagged) === 'ready' && (!store.previews[r.id]?.built || store.staleRoles(r.id).length)).map(r => r.id) : []));
  const stale = $derived((store.version, store.ready ? all.filter(r => store.buildState(r.id) === 'stale').map(r => r.id) : []));
  function rebuildStale() {
    if (stale.length && confirm(`Rebuild all ${stale.length} stale side pairs from their parts' current drawings?`)) store.buildPairs(stale, 'Rebuilding');
  }

  // The page's address keeps the search, page, filter, page size, grouping and pair size.
  $effect(() => {
    if (!store.ready) return;
    if (current > pages) current = pages;
    page.setQuery(query);page.setPage(current);page.writeURL();
    const u = new URL(location.href);
    for (const [name, value, fallback] of [['side', filter, ''], ['size', pageSize, 24], ['group', groupBy, ''], ['grid', store.size === 72 ? '72' : '', '']]) {
      if (value !== fallback) u.searchParams.set(name, value); else u.searchParams.delete(name);
    }
    history.replaceState(null, '', u);
  });
  // The review buttons (side-repair-flags.js) need every pair. Not on every redraw: setRows announces a flags change,
  // which redraws.
  $effect(() => { store.pairsVersion;if (store.ready) untrack(() => window.SideRepairFlags?.setRows([...store.pairs.values()])); });

  let timer;
  function search(e) { const value = e.currentTarget.value;clearTimeout(timer);timer = setTimeout(() => { query = value;current = 1; }, 180); }
  const restart = () => { current = 1; };
  function setSize(e) { current = 1;store.setSize(Number(e.currentTarget.value)); }
  function go(step) { current = Math.min(pages, Math.max(1, current + step));host?.scrollIntoView(); }

  // The layout editor lists the other pairs using the same main, so one fix can go to several of them.
  editor.pairsWithMain = (icon, exceptId) => [...store.pairs.values()]
    .filter(p => p.id !== exceptId && !p.mapped_native && p.subs.length && p.mains.some(m => m.icon === icon)).map(p => {
      const sub = currentSub(p), found = store.combined(p, sub);
      return {id: p.id, concept: p.concept, position: p.position, sub: sub.icon, adjusted: !!store.handLayout(p.id),
              preview: found?.url || (found?.result?.svg ? dataURL(found.result.svg) : null)};
    });
  // After an apply: every pair that took the layout is read again from D1.
  editor.applied = async results => { for (const r of results) if (r.ok) await store.refresh(r.pair_id); };

  // ?edit=<pair> opens the pair's layout editor; ?make=<primitive>[&position=] makes its side pair and opens its main /
  // sub picker (links from Combinations, Experiment and side-pairs.html). Once, read when the page loaded.
  let followed = false;
  $effect(() => { if (store.ready && !followed) { followed = true;follow(); } });
  async function follow() {
    const edit = params.get('edit'), make = params.get('make');
    const strip = () => { const u = new URL(location.href);for (const k of ['edit', 'make', 'position']) u.searchParams.delete(k);history.replaceState(null, '', u); };
    // Once the list shows the pair (tick: after the page updates).
    const click = (id, selector) => tick().then(() => document.querySelector(`.side-row[data-pair-id="${CSS.escape(id)}"] ${selector}`)?.click());
    if (make) {
      try {
        if (!store.pairs.has(make)) {
          const response = await fetch('/api/combinations/pair', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({reference_id: make, position: params.get('position') || 'br'})});
          const data = await response.json().catch(() => ({}));if (!response.ok) throw Error(data.error || 'Could not make the side pair.');
          await store.refresh(make);
        }
        query = make;current = 1;strip();click(make, '.side-pair-editor button');
      } catch (error) { store.status = 'Could not make the side pair: ' + error.message;strip(); }
      return;
    }
    if (edit && store.pairs.has(edit)) { query = edit;current = 1;strip();click(edit, '.side-layout-open'); }
  }
</script>

<div bind:this={host}>
  <h2>Side combination</h2>
  <p class="muted">Work on each pair as Original → Main → Sub → Combined: one {sizes.main}-unit main and one {sizes.sub}×{sizes.sub} sub. Group by main or sub to see where an icon is reused. Finished outputs live on Experiment › Side combination.</p>
  {#if !store.ready}
    <p class="muted">{store.error || 'Loading side pairs…'}</p>
    {#if store.error}<button type="button" onclick={() => { store.error = '';store.load(); }}>Retry</button>{/if}
  {:else}
    <Summary {store} pairCount={all.length} />
    <p class="muted">Pair badges: Waiting = main and sub are drawn but not combined yet. Lists: <a href="side-mains.html">Main icons →</a> · <a href="side-subs.html">Sub icons →</a></p>
    <div class="toolbar side-combine">
      <button type="button" class="requires-login" disabled={store.combine.status === 'running' || !buildable.length} onclick={() => store.buildPairs(buildable, 'Building')}>Build {buildable.length.toLocaleString()} side pair{buildable.length === 1 ? '' : 's'}</button>
      <button type="button" class="requires-login" title="Pairs built before a main or sub was redrawn" disabled={store.combine.status === 'running' || !stale.length} onclick={rebuildStale}>Rebuild {stale.length.toLocaleString()} stale pair{stale.length === 1 ? '' : 's'}</button>
      <span class="muted" role="status">{store.combine.status === 'running' ? store.combine.message : store.combine.status === 'error' ? store.combine.message + ' You can retry.'
        : `${buildable.length.toLocaleString()} ready side pairs not built yet or built from older drawings · ${(store.run?.count || 0).toLocaleString()} built`}</span>
    </div>
    <section id="pairGallery">
      {#if store.status}<p class="side-status" role="status">{store.status}</p>{/if}
      <div class="toolbar">
        <select aria-label="Pair size" value={String(store.size)} onchange={setSize}>
          <option value="64">64 · 48 main + 32 sub</option><option value="72">72 · 54 main + 36 sub</option>
        </select>
        <input type="search" placeholder="Search concept, component ID or icon name" aria-label="Search side pairs" value={query} oninput={search} bind:this={searchBox}>
        <select aria-label="Side pair filter" bind:value={filter} onchange={restart}>
          {#each Object.entries(FILTERS) as [k, v] (k)}<option value={k}>{v}</option>{/each}
        </select>
        <select aria-label="Group side pairs" bind:value={groupBy} onchange={restart}>
          {#each Object.entries(GROUPS) as [k, v] (k)}<option value={k}>{v}</option>{/each}
        </select>
        <select aria-label="Items per page" bind:value={pageSize} onchange={restart}>
          {#each PAGE_SIZES as n (n)}<option value={n}>{n}{groupBy ? ' groups' : ' pairs'} per page</option>{/each}
        </select>
      </div>
      {#snippet pager()}
        <div class="pager">
          <button type="button" disabled={current <= 1} onclick={() => go(-1)}>← Previous</button>
          <span class="muted">{rows.length.toLocaleString()} pairs{grouped ? ` · ${grouped.length.toLocaleString()} ${groupBy === 'main' ? 'main' : 'sub'} icons` : ''} · Page {Math.min(current, pages)} of {pages}</span>
          <button type="button" disabled={current >= pages} onclick={() => go(1)}>Next →</button>
        </div>
      {/snippet}
      {@render pager()}
      <div class="side-list">
        {#if grouped}
          {#each visible as group (groupBy + group.key)}<GroupSection {store} {group} by={groupBy} {editor} {openGroups} />{/each}
        {:else}
          {#each visible as row (row.id)}<PairRow {store} {row} {editor} />{/each}
        {/if}
        {#if !rows.length}<p class="muted">No side pairs match these filters.</p>{/if}
      </div>
      {@render pager()}
    </section>
  {/if}
</div>
<PartInspect />
<LayoutEditorDialog {editor} />
