# Termo-Chrono-Dynamika (TCD) — v0.2 (po audycie)

**Autor:** Michał Ślusarczyk
**Wersja:** 0.2 — poprawiona po niezależnym audycie matematycznym
**Status:** Propozycja teoretyczna, wciąż do dalszej formalizacji

> *"Czas nie płynie — czas się nalicza. Każde tyknięcie to akt produkcji
> entropii."*

Ta notatka to skorygowana wersja rdzenia formalizmu TCD — teorii, w której
czas jest emergentną miarą dyskretnej produkcji entropii, a nie zewnętrznym
parametrem. Jest osobnym, powiązanym wątkiem badawczym względem głównego
tematu tego repozytorium (Simplicial Hub Impedance / CDT) — tym co łączy oba
projekty to wspólne podłoże: dyskretna, przyczynowa struktura czasoprzestrzeni
zamiast gładkiej rozmaitości różniczkowej.

Wersja 0.1 (szkic koncepcyjny) zawierała błąd matematyczny w kluczowym kroku
"dyskretyzacji" przepływu modularnego Tomity–Takesakiego oraz kilka dalszych
niespójności wykrytych w niezależnym audycie. Ten dokument zawiera już
**poprawioną** wersję — diagnozę błędu i naprawę dla każdego problemu.

---

## 1. Diagnoza błędu w wersji 0.1 (Δ w przepływie modularnym)

Oryginalna propozycja "dyskretyzowała" ciągły przepływ modularny zastępując
wykładnik urojony wykładnikiem rzeczywistym:

$$
\sigma_t^{\omega}(A) = \Delta_\omega^{it} A \Delta_\omega^{-it} \quad\text{(poprawne, ciągłe)}
\qquad\longrightarrow\qquad
\sigma_n^{\omega}(A) = \Delta_\omega^{n} A \Delta_\omega^{-n} \quad\text{(błędne, "dyskretne")}
$$

To niepoprawne z dwóch niezależnych powodów:

1. **Twierdzenie Tomity–Takesakiego gwarantuje, że σ_t^ω jest automorfizmem
   algebry von Neumanna 𝒜 wyłącznie dla wykładnika urojonego** (t rzeczywiste).
   Dla wykładnika rzeczywistego (n), `Δⁿ A Δ⁻ⁿ` w ogólności **nie należy do 𝒜** —
   to nie "nieunitarny automorfizm", tylko wyrażenie poza dziedziną, w której
   cokolwiek jest zdefiniowane.
2. Nawet pomijając (1): przepływ modularny dla t rzeczywistego jest **unitarny**,
   a ewolucja unitarna **zachowuje entropię von Neumanna dokładnie** (ΔS ≡ 0).
   Żadna reparametryzacja samego przepływu modularnego — ciągła czy dyskretna —
   może z definicji wyprodukować entropię. Produkcja entropii wymaga osobnego,
   jawnie dyssypatywnego składnika.

## 2. Naprawa — Modularny Hamiltonian + dyssypator zgodny z KMS

Niech układ ma skończenie-wymiarową przestrzeń Hilberta ℋ, a stan termiczny ω
będzie stanem Gibbsa `ρ_ω = e^{-βH}/Z`. **Hamiltonian modularny**:

$$
K_\omega = -\ln \rho_\omega = \beta H + (\ln Z)\,\mathbb{1} \;\propto\; \beta H
$$

Ciągły przepływ modularny redukuje się do zwykłej **unitarnej** ewolucji
Heisenberga w przeskalowanym czasie — dokładnie hipoteza czasu termicznego
Connesa–Rovelliego ("czas modularny = czas fizyczny razy β"):

$$
\sigma_t^{\omega}(A) = \rho_\omega^{\,it}\, A\, \rho_\omega^{-it} = e^{\,i\beta H t}\, A\, e^{-i\beta H t}
$$

Automorfizm 𝒜 dla każdego t ∈ ℝ, bez wyjątków. Tyknięcie zegara TCD **nie jest**
samym przepływem modularnym — jest **generatorem Lindblada (GKSL) zgodnym z
warunkiem KMS**, gdzie K_ω daje część odwracalną, a osobny dyssypator daje
produkcję entropii:

$$
\boxed{\;
\mathcal{L}(\rho) = -i[H,\rho] + \sum_k \gamma_k \Big( L_k \rho L_k^\dagger - \tfrac{1}{2}\{L_k^\dagger L_k, \rho\}\Big)
\;}
$$

z operatorami skoku spełniającymi **szczegółową równowagę KMS** (Davies 1974;
Alicki 1976): `γ_{i→j} / γ_{j→i} = e^{-β(E_i - E_j)}`. Tyknięcie n → n+1 to jeden
krok tej semigrupy na interwale τ₀: `ρ_{n+1} = e^{\tau_0 \mathcal{L}}(ρ_n)`.

**Dlaczego to działa:** `e^{\tau_0 \mathcal{L}}` jest z konstrukcji CPTP
(twierdzenie GKSL) — w przeciwieństwie do `Δⁿ A Δ⁻ⁿ`. Granica γ→0 odtwarza
dokładnie poprawny przepływ modularny — teoria ma sensowną granicę "wyłączonej
dyssypacji".

## 3. Rygorystyczny dowód monotoniczności entropii (twierdzenie Spohna)

Zamiast błędnego odwołania do nierówności Peierlsa–Bogoliubova z wersji 0.1,
właściwym narzędziem jest **twierdzenie Spohna (1978)**: dla semigrupy GKSL
zgodnej ze szczegółową równowagą względem stanu stacjonarnego ρ_ω, względna
entropia kwantowa `D(ρ_t‖ρ_ω)` jest monotonicznie nierosnąca. Podstawiając
`ln ρ_ω = -βH - ln Z`:

$$
\sigma_n \;=\; \Delta S_{\text{vN},n} - \beta\, \Delta\langle H \rangle_n \;\geq\; 0
$$

To jest rygorystyczna, mikroskopowo wyprowadzona II zasada termodynamiki
(relacja typu Clausiusa dS ≥ β dQ), **udowodniona**, nie postulowana.

## 4. Dlaczego produkcja entropii σ_n, a nie entropia stanu ΔS_vN

Entropia von Neumanna S_vN(ρ) jest **funkcją stanu**. Licząc czas z gołego
ΔS_vN(state), całkowity upływ czasu zależałby wyłącznie od stanu początkowego
i końcowego, nie od historii — co niszczy ideę "czasu jako funkcjonału historii"
i nie odtwarza niczego w stylu paradoksu bliźniąt (dwie różne trajektorie
łączące ten sam ρ₀ z tym samym ρ_N dawałyby identyczny czas własny).

Dlatego czas liczymy z **produkcji entropii** σ_n (p. 3), a nie z ΔS_vN samej
w sobie — σ_n zależy od tego, jaki konkretnie dyssypator/sprzężenie z otoczeniem
zadziałało w danym kroku, więc różne historie prowadzące do tego samego stanu
końcowego produkują różne σ_n i różny czas własny. Zależność od ścieżki jest
odzyskana:

$$
\Delta t_n = \tau_0 \cdot \frac{\sigma_n}{\ln 2}, \qquad
\tau(\gamma) = \tau_0 \sum_{n \in \gamma} \frac{\sigma_n}{\ln 2}
$$

## 5. Dalsze poprawki z audytu

| Problem | Poprawka |
|---|---|
| τ₀ jako twarde minimum niespójne z ciągłą entropią | Kwantyzacja: `M_n = ⌊S_acc,n/ln2⌋`, bufor podprogowy — zegar tyka dopiero po przekroczeniu pełnego bitu |
| Zakaz ΔS<0 zabraniałby chłodzenia/lodówek dla podukładów | Monotoniczność obowiązuje tylko dla σ_n (zawsze ≥0), nie dla lokalnego ΔS_vN — podukład może się ochładzać, jeśli ciepło oddane do otoczenia to kompensuje |
| Ciągła całka ∫_γ dS koliduje z dyskretnym zbiorem przyczynowym | Zamieniona na sumę dyskretną Σ_n σ_n/ln2 |
| Nazwa "Chain Rule dla entropii" była myląca (to suma teleskopowa, nie reguła łańcuchowa z teorii informacji) | Przemianowane na "Addytywność produkcji entropii" |
| Sprzeczność: strzałka czasu "fundamentalna" (P4) vs wyprowadzenie przez ślad częściowy, czyli emergentne (III.A.3) | Rozstrzygnięte na korzyść ujęcia **emergentnego/relacyjnego** (zgodnego z Connes–Rovelli i Page–Wootters, już cytowanymi w teorii) — do zatwierdzenia przez autora; alternatywa "czas fundamentalny" wymagałaby odrzucenia globalnej unitarności Wszechświata (znacznie większa przebudowa) |

## Referencje (dodatkowe względem v0.1)

- Davies E.B. (1974). *Markovian master equations.* Commun. Math. Phys. 39, 91.
- Alicki R. (1976). *On the detailed balance condition for non-hamiltonian systems.* Rep. Math. Phys. 10, 249.
- Spohn H. (1978). *Entropy production for quantum dynamical semigroups.* J. Math. Phys. 19, 1227.
- Gorini V., Kossakowski A., Sudarshan E.C.G. (1976). *Completely positive dynamical semigroups of N-level systems.* J. Math. Phys. 17, 821.
- Lindblad G. (1976). *On the generators of quantum dynamical semigroups.* Commun. Math. Phys. 48, 119.
