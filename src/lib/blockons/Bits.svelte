<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
</script>

<Blockon id="bits">
  <h1>Élaboration d'un ordinateur 8-bits</h1>
  <p>
    Quoi de mieux pour comprendre le fonctionnement d'un ordinateur que d'en créer un soi-même, à partir de vraiment rien ?
    C'est ainsi que, en m'aidant des différents travaux de <a href="https://eater.net">Ben Eeater</a>,
    j'ai théorisé, élaboré et simulé un ordinateur 8-bits à partir de composants électroniques de base.
    Afin de simplifier l'affichage, ces derniers sont regroupés en modules (voir ci-dessous).
  </p>

  <div class="bits-img-1">
    <img src="/8bits/screenshot1.png" alt="Capture de l'émulation dans Logisim-Evolution"/>
  </div>

  <p>
    J'ai d'abord émulé le système dans le logiciel
    <a href="https://github.com/logisim-evolution/logisim-evolution">Logisim-Evolution</a>
    en le programmant à la main, avant de créer un langage assembleur et son compilateur spécifiques,
    dont les explications sont accessibles dans les fichiers exposés plus bas.
  </p>

  <p id="bits-asm">
    Je me suis inspiré du langage assembleur du
    <a href="https://www.masswerk.at/6502/6502_instruction_set.html">processeur 6502</a>
    pour faciliter l'écriture de programmes pour mon ordinateur émulé,
    et j'ai écrit un compilateur fonctionnel en <a href="https://python.org">python</a>
    pour traduire les scripts en instructions.

    Voici les programmes équivalents qui calculent et affichent les nombres (inférieurs à 255)
    de la suite de Fibonacci en python en assembleur X800&nbsp;:
  </p>

  <div class="bits-table-around">
    <div class="bits-table">
      <div class="code-title">Python</div>
      <div class="code-title">Assembly X800</div>

      <div class="code-area">
        <pre><code class="block-code"><span class="hl-gray1">#!/bin/env python</span>

<span class="hl-red">while</span> <span class="hl-orange">True</span>:
  x<span class="hl-red">=</span><span class="hl-blue">0</span>
  y<span class="hl-red">=</span><span class="hl-blue">1</span>
  <span class="hl-red">while</span> <span class="hl-orange">True</span>:
    <span class="hl-green">print</span>(x)
    z<span class="hl-red">=</span>x<span class="hl-red">+</span>y
    x<span class="hl-red">=</span>y
    y<span class="hl-red">=</span>z
    <span class="hl-red">if</span> x<span class="hl-red">&gt;</span><span class="hl-blue">255</span>:
      <span class="hl-red">break</span></code></pre>
      </div>

      <div class="code-area">
        <pre><code class="clock-code"><span class="hl-gray1">;<span class="hl-purple">!LP</span> x800</span>

<span class="hl-gray1">;<span class="hl-purple">!sec beg</span> fibonacci</span>
<span class="hl-green">orig:</span>
<span class="hl-red">lia</span> <span class="hl-blue">1</span>
<span class="hl-red">sta</span> <span class="hl-blue">.valuey</span><span class="hl-gray1 italic"> ; y</span>
<span class="hl-red">lia</span> <span class="hl-blue">0</span>
<span class="hl-red">sta</span> <span class="hl-blue">.valuex</span><span class="hl-gray1 italic"> ; x</span>
<span class="hl-green">loop:</span>
<span class="hl-red">ldb</span> <span class="hl-blue">.valuey</span><span class="hl-gray1 italic"> ; z=x+y</span>
<span class="hl-red">add</span>
<span class="hl-red">brc</span> <span class="hl-blue">.orig</span>
<span class="hl-red">sta</span> <span class="hl-blue">.valuez</span>
<span class="hl-red">lda</span> <span class="hl-blue">.valuey</span><span class="hl-gray1 italic"> ; x=y</span>
<span class="hl-red">sta</span> <span class="hl-blue">.valuex</span>
<span class="hl-red">lda</span> <span class="hl-blue">.valuez</span><span class="hl-gray1 italic"> ; y=z</span>
<span class="hl-red">sta</span> <span class="hl-blue">.valuey</span>
<span class="hl-red">lda</span> <span class="hl-blue">.valuex</span>
<span class="hl-red">jmp</span> <span class="hl-blue">.loop</span>
<span class="hl-green">valuex:</span><span class="hl-gray1 italic"> ; espace variable x</span>
<span class="hl-orange">.word</span> <span class="hl-blue">00</span>
<span class="hl-green">valuey:</span><span class="hl-gray1 italic"> ; espace variable y</span>
<span class="hl-orange">.word</span> <span class="hl-blue">00</span>
<span class="hl-green">valuez:</span><span class="hl-gray1 italic"> ; espace variable y</span>
<span class="hl-gray1">;<span class="hl-purple">!sec end</span> fibonacci</span></code></pre>
      </div>
    </div>
  </div>

  <p>
    Une capture vidéo de la compilation et de l'exécution de ce code se trouve à
    <a href="/8bits/compile_then_fibonacci.mp4">cette adresse</a>.
  </p>
</Blockon>

<style>
  .bits-img-1 {
    max-width: 100%;
    max-height: 100%;

    display: flex;
    justify-content: center;
  }
  .bits-img-1 img {
    max-height: 20em;
    max-width: 100%;
  }

  .bits-table-around {
    display: flex;
    width: 100%;
    /* justify-content: center; */
    align-content: center;
    overflow-x: auto;
    padding: 3px
  }
  .bits-table-around::before,
  .bits-table-around::after {
    content: "";
    margin: auto;
  }
  .bits-table {
    display: grid;
    width: min(100%, 40em);
    min-width: 35em;

    grid-template: auto auto / 1fr 1fr;
    gap: 3px;
  }

  .bits-table > * {
    padding: 0.5em 0.7em;
    box-shadow: 0 0 0 3px var(--hl-black);
  }
  .bits-table .code-title {
    background-color: #f1f4f5;
  }
  .bits-table .code-area {
    background-color: var(--hl-bg1);
  }
  .bits-table .code-area code {
    font-size: 1rem;
  }
  .code-area pre {
    margin: 0;
  }
</style>
