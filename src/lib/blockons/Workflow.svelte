<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
  import Plate from "$lib/blockons/Plate.svelte";
</script>

<Blockon id="workflow">
  <h1>
    <span>Workflow</span>
    <span class="sub">Linux, Neovim, scripts shell et environnement de travail</span>
  </h1>

  <div class="plates">
    <Plate
        imgsrc="/workflow/tux.png"
        imgalt="Neovim logo"
        rightRatio="4"
        padding="2em"
      >
      <h2 class="title">GNU/Linux</h2>
      <p class="desc">
        J'utilise diverses distributions <a href="https://fr.wikipedia.org/wiki/Linux">GNU/Linux</a>
        depuis l'été 2018&nbsp;:
        l'ancienne <a href="https://fr.wikipedia.org/wiki/Raspberry_Pi_OS">Raspbian</a>,
        <a href="https://ubuntu-fr.org">Ubuntu</a>,
        <a href="https://manjaro.org">Manjaro</a> (avant le virage de l'administration),
        et aujourd'hui <a href="https://archlinux.fr">Archlinux</a> ("à la main").
        J'ai acquis des notions d'<a href="https://fr.wikipedia.org/wiki/Administrateur_syst%C3%A8me">
        administration de système</a> en explorant les multiples possibilités et en réparant
        les accidents d'Archlinux (cette distribution étant par définition très instable).
      </p>
    </Plate>
    <Plate
        imgsrc="/workflow/neovim.png"
        imgalt="Neovim logo"
        rightRatio="4"
        padding="2em"
      >
      <h2 class="title">Neovim</h2>
      <p class="desc">
        <a href="https://neovim.io/">Neovim</a> est un éditeur de text à interface
        <a href="https://fr.wikipedia.org/wiki/Environnement_en_mode_texte">semi-graphique (TUI)</a>
        ultra modulable, personnalisable et extensible.
        Il s'agit d'une belle suite de forks&nbsp;: neovim est issu de
        <a href="https://www.vim.org/">Vim 8</a>, qui est une extension de
        <a href="https://fr.wikipedia.org/wiki/Vi">vi</a>, lui-même reprise
        <a href="https://fr.wikipedia.org/wiki/Ed_(logiciel)">ed</a>.
        La configuration se fait en <a href="https://www.lua.org/">lua</a>, par l'ajout voire l'écriture
        de nombreux plugins <a href="https://github.com/topics/nvim-plugin">neovim</a>
        ou <a href="https://github.com/topics/vim-plugin">vim 8</a>.
      </p>
    </Plate>
    <Plate
        imgsrc="/workflow/bash-logo.png"
        imgalt="Neovim logo"
        rightRatio="4"
        padding="2em"
      >
      <h2 class="title">Scripts Shell</h2>
      <p class="desc">
        En utilisant Linux, j'ai rapidement appris à écrire des scripts shell&nbsp;: il s'agit du premier
        vrai langage de programmation que j'ai appris. Je m'en servais en particulier pour automatiser des actions
        répétitives, personnaliser et optimiser mon environnement, et même pour écrire des logiciels simples
        en ligne de commandes (dans les faits, bash n'est pas du tout dédié à ce dernier usage).
        Quelques uns sont exposés sur mon <a href="https://github.com/lapingenieur">GitHub</a>.
      </p>
    </Plate>
    <Plate
        imgsrc="/workflow/computer.png"
        imgalt="Neovim logo"
        rightRatio="4"
        padding="2em"
      >
      <h2 class="title">Workflow</h2>
      <p class="desc">
        Mon environnement de travail est assez exotique&nbsp;: j'utilise beaucoup de logiciels open-source
        donc facilement modifiable et configurable, afin de me forger l'environnement le plus plaisant
        et le plus optimisé possible. En mode graphique, j'utilise des gestionnaires de fenêtre
        <a href="https://fr.wikipedia.org/wiki/Gestionnaire_de_fen%C3%AAtres_par_pavage">par pavage (tiling)</a>
        comme <a href="http://www.qtile.org/">qtile</a>.
        Je me sers beaucoup de logiciels textuels et gère mes systèmes dans un terminal&nbsp;; la console ne me
        fait pas peur, je l'apprécie.
      </p>
    </Plate>
  </div>
</Blockon>

<style>
  h1 {
    display: flex;
    flex-direction: column;
  }
  h1 .sub {
    font-size: 0.4em;
    font-weight: normal;
    font-style: italic;
  }

  .plates {
    display: grid;
    grid: auto auto auto auto;
    gap: 1em;
  }
</style>
