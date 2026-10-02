<script>
  // The combined icon: the pair's stored build, else composed here (two at a time). Clicking it opens the popup with
  // the main and sub bounds; a stored icon is composed for it on demand.
  import '../styles/row.css';
  import {dataURL} from '../lib/rules.js';
  import {combinedPopup} from '../lib/actions.js';
  let {store, pair, sub} = $props();
  const found = $derived((store.version, store.combined(pair, sub)));
  $effect(() => { if (!found) store.requestRender(pair, sub); });
  let note = $state('');
  async function open() {
    try { const c = await window.SideData.compose(pair.id);window.SideCombinationPopup?.open(pair.concept, {...c.result, svg: c.svg}); }
    catch (e) { note = e.message; }
  }
</script>

<div class="side-combined">
  {#if found?.error}<span class="side-combined-empty">{found.error}</span>
  {:else if !found}<span class="side-combined-empty">Rendering…</span>
  {:else if found.result}
    <img src={found.url || dataURL(found.result.svg)} alt={pair.concept + ' — combined'} width="128" height="128" use:combinedPopup={{concept: pair.concept, result: found.result}}>
  {:else}
    <img src={found.url} alt={pair.concept + ' — combined'} width="128" height="128" role="button" tabindex="0" aria-label={'Inspect ' + pair.concept} title={note}
         onclick={open} onkeydown={e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault();open(); } }}>
  {/if}
</div>
