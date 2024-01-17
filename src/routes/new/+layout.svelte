<script lang="ts">
  import Navigation from "./Navigation.svelte";
  import ScrollUp from "./ScrollUp.svelte";
</script>

<Navigation prefix="new" />
<ScrollUp />

<main>
  <slot />
</main>

<style>
  main {
    padding-top: 5em;
  }
  main :global(*) {
    scroll-margin-top: 6em;
  }
</style>
