<script lang="ts">
  function scrollUp() {
    window.scrollTo({
      left: window.scrollX,
      top: 0,
      behavior: "smooth"
    });
  }

  let visible = ""; // adds a class
  let lastChange = 0;
  const offsetTop = 60; // px
  const offsetBottom = 120; // px
  const offsetUp = 200; // px

  function handleScroll() {
    // show or hide scrollup button wether scrolled up or down or at the top of the page
    const scroll = window.pageYOffset;

    const footer = document.getElementsByClassName("footer").item(0);
    let footerHeight;
    if (footer !== null) {
      footerHeight = footer.clientHeight;
    } else {
      footerHeight = 0;
    }

    if (scroll <= offsetTop) {
      // at the top
      visible = "";
    } else if (document.documentElement.scrollHeight - document.documentElement.clientHeight - footerHeight - scroll <= offsetBottom) {
      // at the bottom
      visible = "up";
    } else if (lastChange - scroll - offsetUp > 0) {
      // scrolled up
      visible = "up";
      lastChange = scroll;
    } else if (scroll - lastChange - offsetTop > 0) {
      // scrolled down
      visible = "down";
      lastChange = scroll;
    }
  }
</script>
<svelte:window on:scroll={handleScroll} />

<button on:click={scrollUp} class="{visible}">
  <div class="virtual">
    <svg viewBox="220 220 560 560">
      <path d="M549,780V402l168,168l63-70L500,220L220,500l63,70l168-168v378H549z"/>
    </svg>
  </div>
</button>

<style>
  button {
    --inner-width: 2em;

    position: fixed;
    right: 0;
    width: calc(var(--inner-width) + 3em);
    height: calc(var(--inner-width) + 3em);
    cursor: pointer;

    bottom: calc(-1 * var(--inner-width) - 3em - 10px );
    transition:
      bottom 0.5s ease;

    border: none;
    border-top-left-radius: 50%;
    padding: 0;
    background: none;
  }
  button.up {
    bottom: 0;
  }
  button.down:hover {
    bottom: 0;
  }

  .virtual {
    width: var(--inner-width);
    height: var(--inner-width);
    position: absolute;
    top: 0;
    left: 0;

    padding: 0.9em;
    border-radius: 100%;
    background: white;

    transition: background-color 0.2s;
    box-shadow: 1.5px 1.5px 5px 1px rgba(0,0,0,0.35);
  }
  .virtual:hover {
    background-color: #fffcfc;
  }

  path {
    fill: black;
    transition: fill 0.2s;
  }
  button:hover path {
    fill: black;
  }
  
  @media screen and (min-width: 1200px) {
    button.down {
      bottom: calc(-0.3833 * (var(--inner-width) + 3em));
    }

    path {
      fill: #909bb4;
    }
    button:hover path {
      fill: #2b2e36;
    }
  }
</style>
