<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
  import Plate from "$lib/blockons/Plate.svelte";
</script>

<Blockon id="webdev">
  <h1>Développement Web</h1>

  <div class="icons">
    <a href="https://svelte.dev">
      <img src="/images/svelte-logo.png" alt="Svelte"/>
    </a>
    <a href="https://www.markdownguide.org/">
      <img src="/images/markdown-logo.webp" alt="Markdown"/>
    </a>
    <a href="https://developer.mozilla.org/fr/docs/Web/HTML">
      <img src="/images/html-logo.png" alt="HTML"/>
    </a>
    <a href="https://developer.mozilla.org/fr/docs/Web/CSS">
      <img src="/images/css-logo.png" alt="CSS"/>
    </a>
    <a href="https://www.sass-lang.com/">
      <img src="/images/sass-logo.png" alt="Sass (SCSS)"/>
    </a>
    <a href="https://typescriptlang.org">
      <img src="/images/typescript-logo.png" alt="Typescript"/>
    </a>
    <a href="https://vercel.com">
      <img src="/images/vercel-logo.png" alt="Vercel"/>
    </a>
    <a href="https://pocketbase.io">
      <img src="/images/pocketbase-logo.svg" alt="Pocketbase"/>
    </a>
  </div>

  <hr/>
  <p>
    Je manie les technologies modernes nécessaires à la création d'une application web&nbsp;:
  </p>

  <div class="plates">

    <Plate
        imgsrc="/images/framework.png"
        imgalt="Illustration framework"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Framework</h2>
      <p class="desc">
        <a href="https://kit.svelte.dev">SvelteKit</a> est un framework simpliste et intuitif, à rendu côté serveur (SSR).
        Ce site est écrit avec Svelte.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/contenu.png"
        imgalt="Illustration fichier"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Contenu</h2>
      <p class="desc">
        Des outils tels que <a href="https://www.markdownguide.org/">Markdown</a>
        ou <a href="https://www.sass-lang.com/">Sass</a>
        facilitent le maniement et la mise en page des langages
        <a href="https://developer.mozilla.org/fr/docs/Web/HTML">HTML</a> et
        <a href="https://developer.mozilla.org/fr/docs/Web/CSS">CSS</a>.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/logique.png"
        imgalt="Illustration engrenages"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Partie logique</h2>
      <p class="desc">
        La syntaxe <a href="https://typescriptlang.org">Typescript</a>
        assure le typage et avorte de nombreuses erreurs d'incohérence.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/backend.png"
        imgalt="Illustration serveur"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Backend</h2>
      <p class="desc">
        Des librairies diverses permettent aux applications de parfaire leurs tâches,
        comme la base de donnée <a href="https://pocketbase.io">PocketBase</a>.
      </p>
    </Plate>
  </div>

  <p>
    Toutes ces technologies peuvent être utilisées également dans d'autres optiques,
    comme la gestion de l'interface graphique (GUI) via des interfaces comme
    <a href="https://tauri.app">Tauri</a> en langage <a href="https://rust-lang.org">Rust</a>.
  </p>
</Blockon>

<style>
  .icons {
    width: 100%;
    height: 3rem;

    display: flex;
    /*** below buggy => using before/after auto margins ***/
    /* justify-content: space-around; */
    align-items: center;
    overflow-x: scroll;

    scrollbar-width: none;
    -ms-overflow-style: none;
  }
  .icons::-webkit-scrollbar {
    display: none;
  }
  .icons::before,
  .icons::after {
    content: "";
    margin: auto;
  }

  .icons a {
    margin: 0 auto;

    display: flex;
    justify-content: center;
    align-items: center;

    height: 2em;
    padding: 0.5em 0.8em;
    border-radius: 0.5em;
    transition: background-color 300ms;
  }
  .icons a:hover,
  .icons a:focus-visible {
    background-color: #d7dde4;
  }
  .icons img {
    height: 75%;
  }

  hr {
    width: 85%;
    border-top: 2px solid black;
  }

  .plates {
    display: grid;
    grid: repeat(4, 1fr);
    gap: 1em;
  }

  .plate {
    width: calc(100% - 2em);
    height: auto;
    min-height: 6em;
    padding: 1em;

    background-color: #fcfcfd;
    border-radius: 1.5em;

    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1em;
  }
  .plate-left {
    flex: 1;
    height: 100%;
    aspect-ratio: 1 / 1;

    display: none;
  }
  .plate-right {
    flex: 3;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .plate img {
    height: 7em;
  }
  .plate-right h2 {
    margin: 0;
    font-weight: lighter;
  }
  .plate-right p {
    margin: 0.5em 0 0 0;
    font-size: 1em;
    text-align: center;
  }

  @media screen and (min-width: 550px) {
    .plate {
      height: 8em;
    }
    .plate-left {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .plate-right {
      align-items: flex-start;
    }
    .plate-right p {
      text-align: left;
    }
  }

  @media screen and (min-width: 960px) {
    .plates { grid: 1fr 1fr / 1fr 1fr; }
    .plate { height: 6em }
    .plate img { height: 5em; }
  }
</style>
