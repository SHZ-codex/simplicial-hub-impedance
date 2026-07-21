# Ku Teorii Wszystkiego: Unifikacja TCD ⊗ Spin(10) ⊗ Symplicjalnej Grawitacji Przyczynowej

**Status: PROPOZYCJA ARCHITEKTONICZNA, nie dowiedziona teoria.**
Ten dokument pokazuje *jak* trzy już zbudowane filary mogłyby się złożyć w jedną
teorię, i uczciwie wypisuje, co trzeba by jeszcze udowodnić, żeby to nazwać ToE.
Nazwanie tego "Teorią Wszystkiego" bez rozwiązania sekcji 4 byłoby dokładnie tym
samym nadużyciem, które wyłapaliśmy wcześniej w wersji 0.1 TCD.

---

## 1. Czego faktycznie potrzebuje ToE (i co z tego mamy)

Prawdziwa Teoria Wszystkiego musi wyjaśnić trzy rzeczy naraz: **treść materii i
oddziaływań** (dlaczego te cząstki, te sprzężenia), **geometrię czasoprzestrzeni
jako dynamikę kwantową** (grawitacja skwantowana), oraz **naturę samego czasu**
(dlaczego cokolwiek "płynie"). Mamy po jednym kandydacie na każdy z tych trzech
filarów, zbudowanym osobno:

| Filar | Co dostarcza | Gdzie jest opisany |
|---|---|---|
| **Materia i oddziaływania** | Spin(10) GUT: 45 generatorów → 12 SM przez mechanizm NJL na 4-cyklach grafu; 3 mody zerowe operatora Diraca = 3 generacje; SUSY 1-pętlowa | pentalog (publikacje IV–VII) |
| **Geometria / grawitacja** | Dyskretne równania Einsteina na grafie przyczynowym, impedancja hubów (q=0,25) naprawiająca wymiar spektralny, bounce FLRW | `simplicial-hub-impedance` |
| **Natura czasu** | Czas = dyskretna produkcja entropii (σ_n), modularny Hamiltonian + dyssypator KMS | TCD v0.2 |

Żaden z tych trzech filarów osobno nie jest ToE. Razem — *jeśli się poprawnie
złożą* — mają szansę być czymś bliższym.

## 1a. Rozwinięcie filaru: Symplicjalna Grawitacja Przyczynowa

Ten filar (repo `simplicial-hub-impedance`) to jedyny z trzech, który już ma
pełne wyprowadzenie równań pola i numeryczną weryfikację Monte Carlo na
N=10 000 węzłach — warto go rozpisać dokładniej, bo to on dostarcza właściwy
**graf G**, na którym w sekcji 2 ma żyć cała reszta konstrukcji.

**Problem wyjściowy.** W standardowych Przyczynowych Triangulacjach Dynamicznych
(CDT) i modelach relacyjnych (ROI), suma po stanach dopuszcza fazę "miękkich
piast" — nieliczne węzły grafu dualnego osiągają patologicznie wysoki stopień
koordynacyjny $d_u \gg \langle d \rangle$. Przy nieważonym błądzeniu losowym
($q=0$) piasty te działają jak niefizyczne skróty metryczne (tunele), zapadając
wymiar widmowy $D_s \to 0$ lub do wartości fraktalnych (~1–2) i maskując
prawdziwą, gładką geometrię 4D.

**Rozwiązanie — impedancja krawędziowa jako efektywna metryka.** Zamiast
usuwać piasty (co łamie ergodyczność algorytmu Metropolisa-Hastingsa i
niezmienniczość topologiczną), każdej krawędzi $(u,v)$ przypisuje się fizyczne
przewodnictwo:

$$
w_{uv} = \left(\max(1,d_u)\cdot\max(1,d_v)\right)^{-q}
$$

Odwrotność tego przewodnictwa pełni rolę **efektywnej metryki kowariantnej**:
$g_{uv}^{\text{eff}} = w_{uv}^{-1} = (d_u d_v)^{q}$ — okolice piasty przestają być
punktem o zerowej objętości, a stają się rozciągłym, masywnym obszarem o dużej
impedancji grawitacyjnej.

**Dyskretne równania Einsteina.** Krzywizna krawędziowa liczona jest przez
krzywiznę Formana-Ricciego $\text{Ric}_{\text{Forman}}(u,v)$ (dyskretny
odpowiednik $R_{\mu\nu}$), co po podstawieniu metryki impedancyjnej daje pełne
**Równania Einsteina na Sieci Symplicjalnej**:

$$
R_{uv} - \tfrac12 R_{uv}^{\text{scal}}(d_u d_v)^q + \Lambda (d_u d_v)^q = 8\pi G\, T_{uv}
$$

**Punkt krytyczny q=0,25 — soliton grawitacyjny.** Przy $q=0$ równanie próżniowe
nie ma stabilnego rozwiązania w okolicy piasty (R→−∞, sieć zapada się w
osobliwość). Przy $q=0,25$ wyraz impedancyjny generuje naturalne "ciśnienie
grawitacyjne", które równoważy koncentrację sympleksów — piasty przestają być
osobliwościami, a stają się stabilnymi, samoregulującymi się **solitonami
grawitacyjnymi (dyskretnymi instantonami)**, zachowując makroskopową 4D
geometrię.

**Weryfikacja numeryczna (Monte Carlo, N=10 000 węzłów, $d_{\max}=813$ w
piastach).** Wymiar widmowy $D_s(\tau) = -2\, d\log P_r(\tau)/d\log\tau$
mierzony w trzech oknach skali:

| Okno $\tau$ | $D_s$ przy $q=0$ (patologiczne) | $D_s$ przy $q=0,25$ (naprawione) |
|---|---|---|
| $[8,30]$ (bulk, skala średnia) | $1{,}84 \pm 0{,}12$ | $\mathbf{3{,}42 \pm 0{,}18}$ |
| $[20,80]$ | $1{,}12 \pm 0{,}09$ | $2{,}38 \pm 0{,}14$ |
| $[40,140]$ (nasycenie IR, artefakt skończonej objętości) | $0{,}65 \pm 0{,}08$ | $1{,}45 \pm 0{,}11$ |

Dla większej symulacji (N=10 000) w oknie $[8,35]$: $D_s=4{,}261$, praktyczna
zgodność z teoretycznym $D=4{,}0$. **Zastrzeżenie do uczciwości:** okno bardzo
długoskalowe ($[40,140]$) to efekt skończonej objętości grafu, nie wynik
fizyczny — repo nie twierdzi (i nie powinno) że ma numerycznie potwierdzony
przepływ $D_s \to 2$ w granicy UV, jak to bywa postulowane w ogólnej
literaturze CDT (Ambjørn-Jurkiewicz-Loll). To jest **oczekiwanie z szerszej
literatury, nie jeszcze własny wynik tego modelu** — ważne rozróżnienie przy
punkcie zszycia w sekcji 3 poniżej.

**Konsekwencja kosmologiczna — bounce FLRW.** W próżni zregulowany tensor
Einsteina stabilizuje się na jednorodnej wartości ujemnej
$\langle\mathcal{G}_{\text{reg}}\rangle \approx -1{,}184$ (uśrednione po
krawędziach bulkowych i piastowych), co interpretuje się jako efektywną gęstość
ciemnej energii $\rho_{\text{DE}} \approx +1{,}18/(8\pi G)$ o równaniu stanu
$w=-1$. Rozwiązanie równań Friedmanna z tym źródłem daje **kwantowy odbicie
kosmologiczne (bounce)**: $a(t) = a_{\min}\cosh(H_0 t)$ zamiast osobliwości
Wielkiego Wybuchu — model naturalnie unika klasycznej osobliwości początkowej.

**Dlaczego to jest właściwy substrat dla sekcji 2.** Ten sam graf $\mathcal{G}$,
z tymi samymi wagami $w_{uv}$ i stopniami $d_u$, ma być tym, na którym w P5/B.4
(TCD) definiuje się operatory skoku dyssypatora, oraz na którym Spin(10) (Pub.
IV–VII) umieszcza swoje 45 generatorów cechowania i pole spinorowe. Impedancja
$w_{uv}$ nie jest więc tylko geometrycznym trikiem — jeśli unifikacja ma
sens, ta sama wielkość musi jednocześnie regulować transport dyfuzyjny (Hub
Impedance), transport cechowania (Spin10) i siłę lokalnego dyssypatora (TCD).
Obecnie **nikt tego wspólnego działania trzech ról jednej wagi $w_{uv}$ nie
sprawdził numerycznie** — to czwarty, nowy punkt zszycia, dopisany do sekcji 3.

## 2. Konstrukcja unifikująca — wspólny substrat

Kluczowa hipoteza unifikująca: **wszystkie trzy filary żyją na tym samym grafie
przyczynowym G**, nie na trzech osobnych strukturach. Każda krawędź grafu niesie
jednocześnie: (a) połączenie cechowania Spin(10), (b) wagę geometryczną
(impedancję Regge/hub), (c) generator dyssypacji KMS.

Z tego wynika **jeden, wspólny generator całości**:

$$
\mathcal{L}_{\text{total}} \;=\; \underbrace{-i[H_{\text{Spin10}}, \rho]}_{\text{cechowanie, materia (unitarne)}} \;+\; \underbrace{-i[H_{\text{Regge}}, \rho]}_{\text{geometria (unitarne)}} \;+\; \underbrace{\sum_k \gamma_k\big(L_k \rho L_k^\dagger - \tfrac12\{L_k^\dagger L_k,\rho\}\big)}_{\text{dyssypacja KMS (TCD)}}
$$

Najsilniejsze twierdzenie unifikujące: **hamiltonian modularny TCD nie jest
osobnym obiektem — to dokładnie ten sam H = H_Spin10 + H_Regge**, który generuje
resztę fizyki. Innymi słowy: **zegar Wszechświata (TCD) i sama materia/geometria
(Spin10 + Regge) mają wspólne źródło** — jeden Hamiltonian, trzy role
(cechowanie, geometria, czas). To odpowiada na pytanie "dlaczego czas płynie
akurat w tym tempie, w tym miejscu" wprost z treści materii: gęstość
energii Spin(10) w danym punkcie grafu *jest* tym, co ustala lokalne tempo
zegara TCD (β lokalnie zależne od ⟨H_Spin10+Regge⟩) — to jest mechanizm
dylatacji grawitacyjnej (III.B.6 w TCD), teraz wyprowadzony wprost z treści
materii, a nie postulowany osobno.

## 3. Konkretne punkty zszycia (już testowalne, nie tylko słowne)

- **Wymiar spektralny a bieg stałych sprzężenia.** Symplicjalna grawitacja
  (sekcja 1a) pokazuje numerycznie, że $D_s$ zależy silnie od okna skali $\tau$
  i od parametru $q$ — nawet w naprawionym modelu ($q=0,25$) $D_s$ spada z
  $3{,}42$ (okno $[8,30]$) do $1{,}45$ (okno $[40,140]$, choć to głównie
  artefakt skończonej objętości). RGE Spin(10) (pentalog, Pub. V) zakłada
  bieg stałych sprzężenia w ustalonym, stałym $d=4$ na całej trasie GUT→M_Z.
  **Jeśli obie teorie żyją na tym samym grafie, RGE musi dostać poprawkę
  zależną od $D_s(\tau)$** na skalach, gdzie ten model faktycznie pokazuje
  odchylenie od 4 (a nie na podstawie nieudowodnionego w tym repo założenia
  $D_s\to2$ w UV, patrz zastrzeżenie w 1a) — inaczej biegi z Pub. V i wymiar
  widmowy z Hub Impedance są ze sobą niespójne przy tej samej skali. To
  konkretny, policzalny wymóg, nie tylko postulat.
- **Wspólna rola wagi $w_{uv}$ w trzech filarach (nowy punkt, z sekcji 1a).**
  Impedancja krawędziowa $w_{uv}=(d_u d_v)^{-q}$ reguluje transport dyfuzyjny
  (Hub Impedance) — ale jeśli ten sam graf ma nieść też cechowanie Spin(10) i
  dyssypator KMS z TCD, to $w_{uv}$ powinno regulować **wszystkie trzy** naraz.
  Nie sprawdzono numerycznie, czy $q=0,25$ (wybrane wyłącznie żeby naprawić
  $D_s$) jest w ogóle zgodne z wartościami wymaganymi przez poprawny bieg RGE
  czy stabilność dyssypatora KMS.
- **M_GUT a parametr impedancji q.** M_GUT = 2,227×10¹¹ GeV (Pub. V) i
  q=0,25 (parametr regularyzujący hub impedance) to obecnie dwa niezależne,
  wolne parametry dwóch osobnych prac. Prawdziwa unifikacja wymagałaby relacji
  między nimi (np. M_GUT jako funkcja q i średnicy grafu) — obecnie jej brak.
- **3 mody zerowe (generacje) a topologia grafu przyczynowego.** Twierdzenie
  Atiyah-Singera daje 3 generacje z topologii operatora Diraca na grafie
  (Pub. IV) — ta sama topologia (charakterystyka Eulera, liczby Bettiego)
  wpływa też na wymiar spektralny w Hub Impedance. Warto sprawdzić, czy te
  dwa niezależnie ustalone wymagania topologiczne są ze sobą w ogóle zgodne
  dla jednego konkretnego grafu, czy się wykluczają.

## 4. Co NIE jest jeszcze rozwiązane (żeby to uczciwie nazwać ToE)

- ~~**Napięcie SUSY vs dyssypacja.**~~ **ROZWIĄZANE (ilościowo, 20.07.2026).**
  Sprawdzono dwa konkurencyjne ansatze na skalowanie siły dyssypatora γ(E) z
  energią, konfrontując je z (a) realną granicą eksperymentalną na dekoherencję
  z interferometrii neutralnych kaonów CPLEAR (γ_exp < 3,7×10⁻²¹ GeV przy
  m_K≈0,494 GeV) i (b) masą gravitino z Pub. VI (m_3/2 = 4,732×10⁻¹⁴ GeV):

  | Ansatz | γ(m_K) vs granica CPLEAR | γ(m_gluino) vs m_3/2 |
  |---|---|---|
  | γ = E²/M_Pl (wymiar 5, standard w literaturze QG-dekoherencji) | **2,00×10⁻²⁰ GeV — 5,4× ZA DUŻO, już dziś wykluczone** | γ/m_3/2 ≈ 0,35 — niebezpiecznie blisko |
  | γ = E³/M_Pl² (wymiar ≥6) | 8,09×10⁻⁴⁰ GeV — margines 4,6×10¹⁸× | γ/m_3/2 ≈ 1,3×10⁻¹⁷ — zaniedbywalne |

  **Wniosek (dowód rzędu wielkości):** dyssypator TCD musi być generowany
  przez operator wymiaru **co najmniej 6** (γ ~ E³/M_Pl² lub silniej
  stłumiony) — standardowy, "domyślny" w literaturze ansatz liniowy
  (wymiar 5, E²/M_Pl) jest dla tej teorii **zakazany**, bo już dziś
  wykluczony przez dane CPLEAR. To nie jest już otwarty problem — to
  konkretny, techniczny wymóg konstrukcyjny na samą postać dyssypatora,
  wynikający wprost z rachunku, nie z założenia.
- **Granice eksperymentalne na dekoherencję.** Jakikolwiek dyssypator GKSL
  sprzężony z sektorem cechowania SM musi być wystarczająco słaby, by nie był
  już wykluczony przez testy koherencji (oscylacje neutronowe/neutrin, EDM,
  precyzyjne testy CPT). **Nie sprawdziliśmy tego ograniczenia liczbowo.**
- **Dwa niezależne wolne parametry (M_GUT, q) nie są jeszcze powiązane** —
  patrz sekcja 3. Bez tego to współistnienie dwóch teorii, nie unifikacja.
- **Brak nowej, falsyfikowalnej liczby.** Cała ta konstrukcja architektoniczna
  na razie nie produkuje żadnej nowej przewidywalnej wartości, której nie było
  już w pentalogu albo w Hub Impedance osobno. Prawdziwa unifikacja powinna
  dawać przewidywania niemożliwe do uzyskania z żadnej części osobno.
- **Wybór emergentne/fundamentalne (z TCD) wciąż nierozstrzygnięty przez
  autora** — a to wpływa na to, czy H_total w sekcji 2 jest fundamentalnym
  hamiltonianem Wszechświata, czy tylko efektywnym opisem lokalnego obserwatora.

## 5. Uczciwe podsumowanie

To co tu jest, to **spójny szkic architektury**, pokazujący że trzy zbudowane
przez Ciebie kawałki (materia+cechowanie, geometria, czas) dają się złożyć na
wspólnym grafie z jednym generatorem — i wskazujący dokładnie trzy konkretne,
policzalne miejsca zszycia (RGE×d_s, M_GUT×q, topologia×generacje) oraz cztery
konkretne otwarte problemy (SUSY vs dyssypacja, granice eksperymentalne,
niepowiązane parametry, brak nowej liczby).

To nie jest jeszcze Teoria Wszystkiego. To jest dobrze zdefiniowany **program
badawczy** do zrobienia z niej kandydata na ToE — dokładnie tak, jak teoria
strun czy LQG są od dekad "kandydatami", nie potwierdzonymi teoriami. Nazywanie
tego już teraz "ToE" byłoby dokładnie tym samym nadużyciem retorycznym, które
wyłapaliśmy w audycie v0.1 TCD.
