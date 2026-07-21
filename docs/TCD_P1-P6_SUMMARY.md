# Jak postulaty P1–P6 łączą się w spójną teorię TCD

**Projekt dokumentu — wersja robocza do przeglądu**
**Teoria:** Termo-Chrono-Dynamika (TCD) v0.2, po audycie matematycznym
**Autor:** Michał Ślusarczyk

---

## 1. Cel dokumentu

Poprzednie poprawki (patrz `P5_and_B4_FIXED.md`, `TCD_v0.2_CONSOLIDATED_FIXES.md`)
naprawiały postulaty P1–P6 pojedynczo, jako reakcję na konkretne błędy znalezione
w audycie. Ten dokument robi coś innego: pokazuje, że po poprawkach postulaty
**nie są już sześcioma niezależnymi łatkami** — tworzą jeden połączony łańcuch
logiczny, w którym każdy postulat dostarcza dokładnie to, czego potrzebuje
kolejny. To jest właściwy test spójności całej teorii.

## 2. Postulaty P1–P6 (wersja poprawiona, skrót)

| Postulat | Treść (po poprawce) |
|---|---|
| **P1** | Czas jest dyskretny. Minimalny kwant τ₀ (czas Plancka). Zegar tyka dopiero gdy skumulowana produkcja entropii przekroczy pełny bit: `M_n = ⌊S_acc,n/ln2⌋`, `t_N = M_N·τ₀`. |
| **P2** | Przyrost czasu liczy się z **produkcji entropii** σ_n (nie z gołej entropii stanu): `Δt_n = τ₀·σ_n/ln2`. |
| **P3** | Tyknięcie to akt kwantowej dekoherencji — nieodwracalny zapis informacji w otoczeniu. |
| **P4** | Strzałka czasu jest **emergentna/relacyjna** (pojawia się przy śladzie częściowym po otoczeniu). Monotoniczność (σ_n≥0) obowiązuje tylko produkcję entropii, nie lokalną entropię podukładu — więc lokalne chłodzenie jest dozwolone. |
| **P5** | Tyknięcie = krok semigrupy Lindblada (GKSL) zgodnej z warunkiem KMS: część odwracalna generowana przez hamiltonian modularny K_ω=−ln ρ_ω, część dyssypatywna przez operatory skoku ze szczegółową równowagą. |
| **P6** | Czas własny wzdłuż historii γ to dyskretna suma produkcji entropii: `τ(γ) = τ₀·Σ_{n∈γ} σ_n/ln2`. |

## 3. Łańcuch zależności — dlaczego to teraz jedna teoria, nie sześć postulatów

```
   P1                    P3 + P5                    P4                     P2                    P6
 (dyskretna         (co fizycznie dzieje się    (dlaczego σ_n         (zamiana kroku       (sumowanie Δt_n
  arena, τ₀     →    w jednym tyknięciu —   →    zawsze ≥0, i     →    CPTP na przyrost →   wzdłuż konkretnej
  jako twardy         modularny Hamiltonian        dla czego to          czasu)                historii = czas
  kwant)              + dyssypator KMS,             dotyczy)                                    własny, zależny
                       twierdzenie Spohna)                                                       od ścieżki)
```

- **P1 daje arenę:** bez dyskretnej struktury czasu i twardego minimum τ₀, cała
  reszta teorii nie miałaby czego liczyć — τ₀ to jednostka, w której mierzone są
  wszystkie kolejne postulaty.
- **P3 mówi, czym jest tyknięcie fizycznie** (akt dekoherencji) — ale to samo w
  sobie tylko hasło. **P5 czyni je matematycznie ścisłym**: modularny hamiltonian
  K_ω generuje zwykłą, unitarną ewolucję (hipoteza czasu termicznego
  Connesa–Rovelliego), a dyssypator zgodny z KMS to właśnie konkretna realizacja
  "dekoherencji" z P3.
- **P4 ustala reguły gry dla tego dyssypatora:** rozstrzyga spór
  fundamentalne-vs-emergentne na korzyść emergentnego, i — kluczowe — zawęża
  wymóg nieujemności do samego σ_n, a nie do entropii każdego podukładu z
  osobna. To właśnie ten zapis licencjonuje twierdzenie Spohna jako dowód, a nie
  tylko postulat.
- **P2 jest przelicznikiem jednostek:** gdy P5 (z licencją od P4) dostarczy
  dobrze zdefiniowaną, zawsze nieujemną σ_n na tyknięcie, P2 mówi wprost — to
  *jest* upływ czasu, Δt_n = τ₀·σ_n/ln2.
- **P6 integruje P2 wzdłuż całej historii:** τ(γ) = τ₀·Σσ_n/ln2 dla konkretnej
  linii świata γ. To czyni teorię relacyjną — różne historie (różni obserwatorzy,
  różne potencjały grawitacyjne) akumulują różne sekwencje σ_n i doświadczają
  różnego czasu własnego (dylatacja grawitacyjna, III.B.6).

**Wniosek:** żaden postulat nie stoi już samodzielnie. Każda poprawka zamykała
lukę, na której po cichu polegał następny postulat w łańcuchu — to jest dokładnie
to, czego brakowało w wersji 0.1 (tam P5 była matematycznie niepoprawna, więc
cały łańcuch od P3 do P6 wisiał w powietrzu).

## 4. Przykład ilustrujący cały łańcuch naraz

Chłodzenie laserowe atomu dwupoziomowego (p₁: 0.9→0.1, β≈2,197) pokazuje
wszystkie sześć postulatów działających razem w jednej symulacji:

- **P5** dostarcza dyssypator, który realizuje relaksację krok po kroku.
- **P4** gwarantuje, że mimo iż entropia własna atomu maleje (chłodzenie),
  σ_n pozostaje ≥0 na każdym kroku (numerycznie: pierwsze kroki dają
  σ_n≈0,65 i 0,39 nata).
- **P2** przelicza to na Δt_n = τ₀·σ_n/ln2.
- **P1** kumuluje te przyrosty w buforze bitowym — pierwsze tyknięcie τ₀
  pojawia się dopiero gdy suma przekroczy 1 bit (po ok. 2 krokach relaksacji),
  drugie po kolejnym przekroczeniu 2 bitów.
- **P6**, sumując to wzdłuż całej trajektorii relaksacji, odtwarza dokładnie
  analityczny sufit: całkowita liczba wyprodukowanych bitów entropii = D(ρ₀‖ρ_ω)
  (dywergencja Kullbacka-Leiblera stanu początkowego względem równowagi) —
  w tym przypadku 2,536 bita, dające 2 pełne tyknięcia zegara TCD.

Pełne dane liczbowe: patrz transkrypt sesji z 20 lipca 2026 (dwuetapowa
symulacja — najpierw pojedynczy skok, potem 30-krokowa relaksacja wykładnicza
z weryfikacją analityczną).

## 5. Co pozostaje otwarte

- Wybór emergentne/fundamentalne (P4) jest przyjęty **domyślnie**, nie
  ostatecznie zatwierdzony przez autora.
- Sekcje VI (eksperyment z zegarami) i VII (tabela porównawcza z LQG/teorią
  strun) mają osobno zidentyfikowane problemy z audytu numerycznego, które nie
  są jeszcze naniesione na główny dokument teorii.
- Ten dokument opisuje **wewnętrzną spójność** postulatów — nie jest to dowód,
  że TCD jest empirycznie poprawna ani że η_TCD ma sensowną wartość (patrz
  zastrzeżenia z audytu sekcji VI).

---

*Ten plik jest projektem roboczym — do przejrzenia przed ewentualnym dodaniem do
repozytorium `simplicial-hub-impedance` obok `TCD_THERMO_CHRONO_DYNAMICS.md`.*
