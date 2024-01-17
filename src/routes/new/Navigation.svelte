<script lang="ts">
  export let title: string = "lp06b";
  export let prefix: string = "";

  let list = {
    "self": {
      "fr": "A propos",
    },
    "insa": {
      "fr": "INSA",
    },
  }

  let scrollY: number;

  let shrunk = false;
  let hashChanged = false;
  let lastChange = 0;
  const offset = 60; // px

  function handleScroll() {
    // shrink or grow the navbar wether scrolled up or down or at the top of the page

    setTimeout(() => {
        if (scrollY <= offset) {
          // at top
          shrunk = false;
          lastChange = scrollY;
        } else {
          if (hashChanged) {
            // hashchanged
            shrunk = false;
            lastChange = scrollY;
          } else if (lastChange - scrollY - offset > 0) {
            // scrolled up
            shrunk = false;
            lastChange = scrollY;
          } else if (scrollY - lastChange - offset > 0) {
            // scrolled down
            shrunk = true;
            lastChange = scrollY;
          }
        }
        hashChanged = false;
        console.log("scrollY", scrollY);
      }, 50); // lil' hack so hashchange is correctly set

  }
  function handle_hashchange() {
    hashChanged = true;
  }
</script>
<svelte:window
  on:hashchange={handle_hashchange}
  on:scroll={handleScroll}
  bind:scrollY={scrollY}
/>

<nav class="bar" class:shrunk>
  <a href="#" class="title bar-element">{title}</a>
  {#each Object.keys(list) as page}
    <a href={prefix + "/" + page} class="bar-element">{list[page]["fr"]}</a>
  {/each}
</nav>

<style>
  nav.bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 5em;

    background: linear-gradient(45deg, #e66465, #9198e5);
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    transition: height 0.3s;
    overflow-y: hidden;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
  nav.bar.shrunk:not(:hover) {
    height: 3.4em;
  }

  nav.bar a.bar-element {
    padding: 1em 0.8em;
    position: relative;

    font-size: 1.3em;
    color: black;
    background: transparent;
    text-decoration: none;
    transition: color 0.2s;
  }
  nav.bar a.bar-element:hover {
    color: #403838;
  }

  nav.bar a.title {
    font-size: 2.4em;
    font-style: italic;
    transition: font-size 0.3s, color 0.2s;
  }
  nav.bar.shrunk:not(:hover) a.title {
    font-size: 2em;
  }
  
</style>
