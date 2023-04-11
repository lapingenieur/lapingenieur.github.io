<script lang="ts">
  type Color = "auto" | "red" | "blue" | "green" | "null";

  export let id: string="";
  export let color: Color = "auto";
</script>

<div class="blockon color-{color}" id={id}>
  <slot />
</div>

<style>
  .blockon {
    --padding: 1em;
    --color-border-left-size: 12px;
    --background-color: #e4e9ec;

    width: calc(100% - 2*var(--padding) - var(--color-border-left-size));
    padding: var(--padding);

    /* background: linear-gradient(45deg, #e66465, #9198e5); */
    background-color: var(--background-color);
  }
  .blockon > :global(h1) {
    font-size: 2.5em;
    font-weight: lighter;
    font-style: italic;
  }
  .blockon > :global(:first-child) {
    margin-top: 0;
  }
  .blockon > :global(:last-child) {
    margin-bottom: 0;
  }

  .color-blue,
  .color-auto:nth-child(3n+1) {
    border-left: 3px solid #92b2dc;
    border-bottom: 3px solid #92b2dc;
  }
  .color-red,
  .color-auto:nth-child(3n+2) {
    border-left: 3px solid #dc92b2;
    border-bottom: 3px solid #dc92b2;
  }
  .color-green,
  .color-auto:nth-child(3n+3) {
    border-left: 3px solid #b2dc92;
    border-bottom: 3px solid #b2dc92;
  }
  
  @media screen and (min-width: 550px) {
    .blockon {
      --padding: 2em;
    }

    .color-null {
      border-left: calc(var(--color-border-left-size) / 2) solid var(--background-color);
      border-right: calc(var(--color-border-left-size) / 2) solid var(--background-color);
    }
    .color-blue,
    .color-auto:nth-child(3n+1) {
      border-left: var(--color-border-left-size) solid #92b2dc;
      border-bottom: 3px solid #92b2dc;
    }
    .color-red,
    .color-auto:nth-child(3n+2) {
      border-left: var(--color-border-left-size) solid #dc92b2;
      border-bottom: 3px solid #dc92b2;
    }
    .color-green,
    .color-auto:nth-child(3n+3) {
      border-left: var(--color-border-left-size) solid #b2dc92;
      border-bottom: 3px solid #b2dc92;
    }
  }
</style>
