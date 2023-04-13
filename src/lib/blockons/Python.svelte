<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
  import Plate from "$lib/blockons/Plate.svelte";
</script>

<Blockon id="python">
  <h1>Scripts python</h1>

  <p>
    <a href="https://python.org/">Python</a> est un langage de programmation interprété très populaire.
    Je m'en suis servis pour différents projets&nbsp;:
  </p>

  <ul class="first-hand">
    <li>
      Le compilateur de <a href="#bits-asm">l'assembleur x800</a> est écrit en python.
    </li>

    <li>
      Projets en spécialité NSI (classe de première)&nbsp;:
      <ul>
        <li>
          <a href="/python/steno.py">Steno</a>
          est un module de sténographie graphique très minimaliste mais d'autant plus fonctionnel.
        </li>
        <li>
          <a href="/python/cov.py">Cov</a>
          est une interface en ligne de commande interactive permettant de faire des conversions de
          bases numérales (base N vers 10 ou base 10 vers N).
        </li>
      </ul>
    </li>

    <li>
      Scripts utiles sur la calculatrice <a href="https://numworks.com/fr">Numworks</a>&nbsp;:
      <ul>
        <li>
          <a href="https://my.numworks.com/python/polettielio/cb_lin_v001">Cb_lin</a>
          est un script utile en maths expertes pour vérifier ou non les solutions possibles x de a(x)|b(x).
        </li>
        <li>
          <a href="https://my.numworks.com/python/polettielio/pgcd">Pgcd</a>
          applique l'algorithme d'Euclide sur deux nombres a et b afin d'en trouver le PGCD.
        </li>
        <li>
          <a href="https://my.numworks.com/python/polettielio/cov">Cov</a>
          est un portage du programme cov.py précédent sur calculatrice : convertisseur de bases numérales.
        </li>
        <li>
          <a href="https://my.numworks.com/python/polettielio/mask">Mask</a>
          est calculateur d'addresse ip de réseau pour une addresse ip locale et un masque donnés.
        </li>
      </ul>
    </li>

    <li>
      Scripts secondaires et jeux sur la calculatrice <a href="https://numworks.com/fr">Numworks</a>&nbsp;;
      derrière l'aspect grossier que peut avoir tout jeu vidéo, on retrouve forcément de la programmation.
      Beaucoup d'éléments nécessitent une importante réflexion quant à leur mise en place,
      en particulier au vu de l'espace mémoire RAM alloué autant que de stockage tous deux très limités
      sur la Numworks. Résoudre ces problèmes est un exercice de programmation très instructif.
      <ul>
        <li>
          <a href="https://my.numworks.com/python/polettielio/draw_v3">Draw</a>
          apporte une interface de création graphique très précise et relativement complète pour la calculatrice.
        </li>
        <li>
          <a href="https://my.numworks.com/python/polettielio/floppy_v35">Floppy</a>
          est un jeu du genre "flappy-bird", le but est de passer des obstacles verticaux défilant sur l'écrant
          en faisant sauter un petit personnage. Ce script atteint les limites de la calculatrice
          concernant la mémoire allouable.
        </li>
        <li>
          <a href="https://my.numworks.com/python/polettielio/write_v3">Write</a>
          dessine du texte à l'écran à partir d'une chaîne de caractères. Différents paramètres peuvent être
          ajustés, les functionnalités sont compressées à outrance pour tenir dans les limites de mémoire.
        </li>
        <li>
          <a href="https://my.numworks.com/python/polettielio/crates">Crates</a>
          est un jeu de réactivité dont le but est d'appuyer au bon moment sur la bonne touche
          suivant la "boîte" (crate) qui s'affiche à l'écran.
        </li>
      </ul>

    </li>
    <li>
      J'utilise également quelques logiciels dont la configuration s'effectue en python,
      par exemple le gestionnaire de fenêtres <a href="http://www.qtile.org/">Qtile</a>
      ou le navigateur web <a href="https://qutebrowser.org/">Qutebrowser</a>.
    </li>
  </ul>

  <hr/>

  <p>
    Python n'est de loin pas mon langage préféré&nbsp;: selon moi, sa syntaxe à indentation facilite les erreurs,
    les variables ne sont pas typées, l'absence de normes de nomination des objets apporte une
    hétérogénéité oppressante lors de l'utilisation simultanée de plusieurs modules,
    les rapports d'erreur sont peu clairs et l'interprétation très lente...
  </p>
  <p>
    On ne peut cependant pas nier sa renommée et sa simplicité&nbsp;: il reste l'un des langages les
    plus utilisés dans le monde.
  </p>

</Blockon>

<style>
  hr {
    width: 85%;
    border-top: 2px solid black;
  }

  .first-hand > li:not(:last-child) {
    margin-bottom: 1em;
  }
  ul {
    padding-inline-start: 20px;
  }

  @media screen and (min-width: 550px) {
    ul {
      padding-inline-start: 40px;
    }
  }
</style>
