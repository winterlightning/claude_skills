<script>
  // Change main / sub: the form for one pair (or a primitive becoming one). `onSaved` runs after a save or a removal
  // on the Side pairs page; on a primitive's card the card shows a notice instead.
  import '../styles/picker.css';
  import {POSITIONS, ROLES, forms, notices, pairs, findCandidates, pairBody, send} from '../lib/picker.svelte.js';
  let {row, onSaved = null} = $props();
  const form = $derived(forms.get(row.uuid));
  let timers = {};

  function search(role, value) {
    form.queries[role] = value;clearTimeout(timers[role]);
    timers[role] = setTimeout(async () => {
      const query = value;
      try { const candidates = await findCandidates(role, query);if (form.queries[role] === query) form.candidates[role] = candidates; }
      catch (error) { form.message = error.message; }
    }, 250);
  }
  function choose(role, c) { form[role] = c.key;form.chosen[role] = c;form.draw[role] = null; }
  async function save() {
    const data = await send(row, form, pairBody(form), 'Saving…');
    if (!data) return;
    if (data.pair && !pairs.has(row.uuid)) pairs.set(row.uuid, {row: data.pair, status: data.status});
    forms.delete(row.uuid);
    // On the side page the row redraws itself from the saved pair.
    if (onSaved) { onSaved(data);return; }
    notices.set(row.uuid, data.status === 'waiting' ? 'Saved to Side combination. Combine it there. '
      : 'Saved to Side combination. It waits there until the ' + (data.status === 'needs_both' ? 'main and sub are' : data.status === 'needs_main' ? 'main is' : 'sub is') + ' drawn. ');
  }
  async function remove() {
    if (!await send(row, form, {remove: true}, 'Removing…')) return;
    pairs.delete(row.uuid);
    if (onSaved) { forms.delete(row.uuid);onSaved({removed: true});return; }
    form.message = 'Removed.';
  }
</script>

{#if form}
  <div class="side-pair-form">
    {#if !form.loaded}
      <p class="muted">Finding the main and sub icons…</p>
    {:else}
      {#each ['main', 'sub'] as role (role)}
        {@const info = ROLES[role]}
        <div class="side-pair-role">
          <strong>{info.label}</strong><span class="muted">{' · '}{info.hint}</span>
          {#if form.draw[role] !== null}
            <!-- No icon fits yet: the pair keeps the name of the one to draw, and waits for it. -->
            <div class="side-pair-chosen to-draw"><span>To draw:</span>
              <input maxlength="120" placeholder={'Name of the ' + role + ' icon to draw'} aria-label={'Name of the ' + role + ' icon to draw'} bind:value={form.draw[role]}>
            </div>
            <button type="button" onclick={() => { form.draw[role] = null; }}>Pick an existing icon instead</button>
          {:else}
            <!-- The chosen icon, shown as its picture and name: picked by clicking a result, never typed. -->
            <div class="side-pair-chosen" title={form.chosen[role]?.icon_id || ''}>
              {#if form.chosen[role]}
                {#if form.chosen[role].preview_url}<img src={form.chosen[role].preview_url} alt="">{/if}
                <span>{form.chosen[role].name || form.chosen[role].icon_id}</span>
              {:else}<span class="muted">Nothing chosen yet: click an icon below.</span>{/if}
            </div>
            <input type="search" value={form.queries[role]} placeholder={'Search by name, e.g. ' + info.example} aria-label={'Search ' + info.label.toLowerCase()}
                   oninput={e => search(role, e.currentTarget.value)}>
            <div class="side-pair-candidates">
              {#each form.candidates[role] || [] as c (c.key)}
                <button type="button" class={'side-pair-candidate' + (!form.draw[role] && form[role] === c.key ? ' chosen' : '')}
                        title={c.icon_id + (c.build_failed ? ' · fails the build check' : '') + (c.approved ? ' · approved' : '')} onclick={() => choose(role, c)}>
                  {#if c.preview_url}<img src={c.preview_url} alt="" loading="lazy">{/if}
                  <span>{c.name || c.icon_id}</span>
                  {#if c.approved}<span class="badge generated">Approved</span>{:else if c.build_failed}<span class="badge failed">Fails</span>{/if}
                </button>
              {:else}
                <span class="muted">{form.queries[role] ? 'No ' + info.family + ' icon matches “' + form.queries[role] + '”.' : 'Type a name to search.'}</span>
              {/each}
            </div>
            <button type="button" class="side-pair-none" onclick={() => { form.draw[role] = form.brief[role] || form.queries[role] || ''; }}>None of these: it needs drawing</button>
          {/if}
        </div>
      {/each}
      <label>Sub position <select bind:value={form.position}>
        <option value="">Choose…</option>
        {#each Object.entries(POSITIONS) as [k, v] (k)}<option value={k}>{v}</option>{/each}
      </select></label>
      {#if form.sub_position === 'center'}<p class="muted">Classified as center: a side pair needs one of the eight side positions.</p>{/if}
      <div class="side-pair-actions">
        <button type="button" class="primary" disabled={form.busy} onclick={save}>Save</button>
        <button type="button" onclick={() => forms.delete(row.uuid)}>Close</button>
        {#if pairs.has(row.uuid)}
          <!-- Removing a published pair's change brings back its published main / sub, icon and layout. -->
          <button type="button" disabled={form.busy} onclick={remove}>{row.published ? 'Use published main / sub' : 'Remove pair'}</button>
        {/if}
      </div>
    {/if}
  </div>
  {#if form.message}<p class="side-pair-message" role="status">{form.message}</p>{/if}
{/if}
