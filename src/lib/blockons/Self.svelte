<script lang="ts">
  import Blockon from "./Blockon.svelte";
  import PlateAlways from "./PlateAlways.svelte";
  import Plate from "./Plate.svelte";
    import { empty } from "svelte/internal";
</script>

<Blockon id="self">
  <h1>Présentation</h1>

  <div class="plates">
    <PlateAlways
        imgsrc="/images/self.jpg"
        imgalt="Photo de moi"
        rightRatio="3"
        padding="1em"
      >
      <h1 class="title">Bonjour&nbsp;!</h1>
      <p class="desc">
        étudiant en première année à l'<a class="emphase" href="https://www.insa-strasbourg.fr">INSA Strasbourg</a>.
      </p>
    </PlateAlways>

    <Plate
        imgsrc="/images/academic-hat.png"
        imgalt="Études postbac"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <h2 class="title">Études</h2>
      <p class="desc">
        Après une <a class="emphase" href="https://www.insa-strasbourg.fr/fr/ingenieur-premiere-annee">première année</a> très généraliste,
        je souhaite poursuivre mes études avec la spécialité <a class="emphase" href="https://www.insa-strasbourg.fr/fr/mecatronique/">Mécatronique</a>.
      </p>
      <p class="desc">
        Je fais partie de la section allemande <a class="emphase" href="https://www.insa-strasbourg.fr/fr/deutschinsa/">Deutsch'INSA Confirmé</a>,
        qui me prépare aux industries des deux côtés du Rhin.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/lightbulb-c.jpg"
        imgalt="Dessin d'une ampoule brillant dans une tête"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <h2 class="title">Aptitudes et qualités</h2>
      <p class="desc">
        <span class="emphase">Ouverture d'esprit</span>&nbsp;: je me plaît à apprendre de nouveaux savoirs,
        à découvrir de nouvelles disciplines, de nouveaux points de vus et de nouveaux avis. Je m'efforce
        de considérer la vision des autres à égale valeur avec la mienne.
      </p>
      <p class="desc">
        <span class="emphase">Langues</span>&nbsp;: francophone et hungarophone natifs,
        j'ai un niveau B2+ en Anglais et B1+ en Allemand.
        J'ai suivi la section Euro Anglais au lycée, et m'intéresse désormais au Deutsch'INSA (Allemand).
        Je souhaite aussi m'investir dans l'apprentissage de l'Espagnol, à la fin du parcours DI.
      </p>
      <p class="desc">
        <span class="emphase">Informatique</span>&nbsp;: comme le présente ce site internet,
        j'ai des connaissances dans de nombreuses disciplines l'informatiques.
      </p>
      <p class="desc">
        <span class="emphase">Autodidactie</span>&nbsp;: l'ensemble de mes connaissances en informatique
        et linguistique ont été acquises en autodidacte, par recherches numériques ou bibliographiques.
      </p>
      <p class="desc">
        <span class="emphase">Sérieux</span>&nbsp;: mes résultats, la quantité et qualité des enseignements optionnels
        que j'ai pu suivre, ainsi que mon établissement actuel, témoignent du sérieux
        que je tiens en mon travail, et de mon assiduité.
      </p>
      <p class="desc">
        <span class="emphase">Perfectionnisme</span>&nbsp;: j'ai appris à user de mon perfectionnisme
        pour m'investir à grande ampleur dans les projets qui me tiennent à cœur,
        sans pour autant confondre l'univers des possibles et celui de l'imagination.
        Ce site, dont le résultat m'est particulièrement satisfaisant, en fait office.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/logo-insa.jpg"
        imgalt="Logo INSA Strasbourg"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <h2 class="title">Pourquoi l'INSA Strasbourg&nbsp;?</h2>
      <p class="desc">
        J'ai choisi d'intégrer l'INSA de Strasbourg directement après mon baccalauréat pour plusieurs raisons :
      </p>
      <p class="desc">
        Tout d’abord, j’apprécie apprendre de nouvelles notions théoriques,
        mais j’aime encore plus les appliquer et expérimenter par moi-même des
        <span class="emphase">disciplines techniques</span> lors de projets,
        que l’on ne retrouve pas dans les classes préparatoires.
        On retrouve d'ailleurs cet attrait dans les notes du DS de dessin technique :
        <span class="emphase">19,6/20</span> pour une moyenne de promotion à 7,6/20.
      </p>
      <p class="desc">
        D’autre part, cet établissement propose la <span class="emphase">spécialité mécatronique</span>,
        qui allie de multiples notions d’ingénierie, et que je souhaite étudier dès l’année prochaine.
      </p>
      <p class="desc">
        L’école m’apporte en outre la possibilité de suivre un enseignement bilingue franco-allemand grâce à
        la <span class="emphase">section Deutsch’INSA</span>, et ainsi d’avoir une formation me préparant aux industries des deux côtés du Rhin.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/logo-mauriac.png"
        imgalt="Études prébac"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <h2 class="title">Lycée et Baccalauréat</h2>
      <p class="desc">
        J'ai présenté le Bacalauréat au lycée général <a href="https://mauriac-desgranges.ent.auvergnerhonealpes.fr">Mauriac</a>
        d'Andrézieux-Bouthéon&nbsp;:
      </p>
      <ul class="desc">
        <li>note finale de <span class="emphase">17,76/20</span></li>
        <li>spécialités <span class="emphase">mathématiques</span>, <span class="emphase">physique-chimie</span> et <span class="emphase">informatique</span> <i>(NSI)</i></li>
        <li>options <span class="emphase">DNL anglais</span> et <span class="emphase">mathématiques expertes</span></li>
        <li>mentions <span class="emphase">Très Bien</span> et <span class="emphase">Section Européenne</span> <i>(Anglais)</i></li>
      </ul>
      <p class="desc">
        J'ai également suivi des enseignements de <span class="emphase">latin</span> et de <span class="emphase">grec ancien</span> jusqu'en classe de première.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/academic-hat.png"
        imgalt="Coiffe académique"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <h2 class="title">Implication</h2>
      <p class="desc">
        Dès le collège, j'ai participé activement au <span class="emphase">Conseil de la Vie Collégienne</span>.
      </p>
      <p class="desc">
        Au lycée, j'ai été <span class="emphase">secrétaire de la Maison des Lycéens</span> durant les trois.
        Cela m'a permis de participer à l'organisation de la <span class="emphase">Fête des Talents</span>
        et du <span class="emphase">Journal</span> du Lycée.
      </p>
      <p class="desc">
        Dans un cadre plus personnel, j'ai apporté des modifications d'ordre de détails à quelques projets informatiques.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/puzzle-b.png"
        imgalt="Pièces de puzzle assemblées"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <h2 class="title">Points d'intérêt</h2>
      <p class="desc">
        J'ai découvert de nombreux pans de l'<span class="emphase">informatique</span>,
        comme la programmation, l'interface en ligne de commandes, le fonctionnement élémentaire
        des systèmes physiques et logiciels,
        dont <a class="emphase" href="https://lapingenieur.github.io">le site internet</a>
        que vous regardez actuellement est une parfaite illustration. Toutes ces connaissances
        ont été apprises en <span class="emphase">autodidacte</span>, en particulier pendant le premier confinement.
      </p>
      <p class="desc">
        La <span class="emphase">linguistique</span> est aussi une discipline que je porte en mon cœur&nbsp;:
        ouvre mon polyglottisme, j'apprécie étudier les langues, leur fonctionnement, les différentes
        solutions qu'elles présentent pour exprimer une même notion et leurs évolutions divergentes ou convergentes,
        et je m'investis même à leur création&nbsp;: l'idéolinguistique.
      </p>
      <p class="desc">
        Je porte aussi de l'admiration envers les sciences théoriques, bien que je n'aie ni les capacités
        ni les connaissances requises pour les étudier et les manipuler.
      </p>
      <p class="desc">
        J'ai en outre suivi des cours de <span class="emphase">musique</span> en classe de percussions 
        au conservatoire pendant 12 ans, et pratique
        l'<a class="emphase" href="https://fr.wikipedia.org/wiki/Ultimate_(sport)">ultimate</a> depuis 7 ans.
      </p>
    </Plate>
  </div>
</Blockon>

<style>
  .plates {
    display: flex;
    flex-direction: column;
    gap: 1em;
  }
</style>
