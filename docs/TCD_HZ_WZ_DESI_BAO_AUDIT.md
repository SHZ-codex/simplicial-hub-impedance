# TCD / ROI: wyprowadzenie H(z), w(z) i audyt dopasowania DESI/BAO

**Data:** 28 października 2026  
**Status:** audyt częściowy; brak uprawnionego dopasowania do rzeczywistych danych DESI/BAO.

## 1. Co rzeczywiście wynika z grafu

Repozytorium raportuje dla `q=0.25`:

\[
\langle \mathcal G_{reg}\rangle=-1.183705
\]

w jednostkach symplicjalnych, przy założeniu \(8\pi G=1\). Z przyjętej identyfikacji:

\[
\Lambda_{eff}=-\langle\mathcal G_{reg}\rangle=1.183705,
\qquad
H_* = \sqrt{\Lambda_{eff}/3}=0.628147\;t_{lat}^{-1}.
\]

Dla próżni i płaskiej geometrii:

\[
H_{graph}(t)=H_*,\qquad a(t)=a_0e^{H_*t},
\qquad w_{graph}=-1.
\]

Dla zamkniętego rozwiązania bounce używanego w repo:

\[
a(t)=H_*^{-1}\cosh(H_*t),
\qquad
H(t)=\frac{\dot a}{a}=H_*\tanh(H_*t).
\]

To jest model czystej próżni de Sittera w jednostkach grafu. Nie jest jeszcze obserwacyjnym \(H(z)\).

## 2. Dlaczego nie ma jeszcze fizycznego H(z)

Aby przejść od wyniku grafowego do danych kosmologicznych, potrzebne są trzy niezdefiniowane mapowania:

1. **Skala czasu:** \(t_{phys}=A_t t_{lat}\). Wtedy \(H_{0,phys}=0.628147/A_t\). Repo nie wyprowadza \(A_t\), więc fizyczne \(H_0\) nie jest predykcją.
2. **Skala długości / normalizacja \(a\):** potrzebna do obliczenia odległości komowalnej \(D_M(z)\).
3. **Sektor materii i promieniowania:** sam graf próżni daje \(w=-1\), ale nie daje \(\Omega_m\), \(\Omega_r\), \(\Omega_k\) ani \(r_d\) (skali dźwięku BAO).

Jeśli doda się standardowy sektor materii jako zewnętrzne założenie, otrzymuje się jedynie fenomenologiczny model:

\[
H(z)=H_0\sqrt{\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_k(1+z)^2+\Omega_{DE}},
\]

z \(w(z)=-1\) i \(\Omega_{DE}=1-\Omega_m-\Omega_r-\Omega_k\). To nie jest jeszcze wyprowadzenie z grafu.

## 3. Audyt istniejącego „dopasowania DESI/Pantheon+”

Plik `data/experimental_cosmology_fit.csv` ma 25 punktów w regularnej siatce:

\[
z=0.02,0.0858,\ldots,1.60,
\]

z identycznym błędem \(\sigma_\mu=0.07\) mag. Skrypt `examples/run_experimental_confirmation.py` pokazuje, że punkty są generowane lokalnie:

- `z_obs = np.linspace(0.02, 1.60, 25)`;
- odległości są tworzone przybliżonym wzorem, a nie całką z opublikowanego \(H(z)\);
- do wartości dodawany jest losowy szum `np.random.normal`;
- nie ma importu, identyfikatorów ani macierzy kowariancji DESI/Pantheon+.

Wniosek: ten plik **nie jest rzeczywistym zbiorem DESI/BAO** i wcześniejsze stwierdzenie o obserwacyjnym potwierdzeniu ROI było zbyt mocne.

### Reprodukowalny test

Dopasowanie czystego de Sittera do tych syntetycznych punktów, z wolnym \(H_0\) i offsetem modułu odległości, daje w przybliżeniu:

| Model | Wynik | \(\chi^2\) | \(\chi^2/\mathrm{dof}\) |
|---|---:|---:|---:|
| Czysty de Sitter, \(H(z)=H_0\) | \(H_0\approx60.93\), offset \(\approx0.922\) | 1716.4 | 74.63 |
| Płaski model \(\Lambda\)CDM, \(H_0,\Omega_m\), offset wolne | \(H_0\approx65.32\), \(\Omega_m\approx0\), offset \(\approx0.434\) | 341.9 | 15.54 |

Te wartości nie są dopasowaniem do danych obserwacyjnych. Pokazują tylko, że zapisany plik i używany wzór nie stanowią wiarygodnej walidacji kosmologicznej.

## 4. Co trzeba zrobić, aby wykonać prawdziwy fit DESI/BAO

Należy dodać do repo:

1. oficjalną tabelę DESI BAO z wersją release, redshiftami, obserwablami i pełną macierzą kowariancji;
2. definicję obserwabli: \(D_M/r_d\), \(D_H/r_d=c/[H(z)r_d]\), ewentualnie \(D_V/r_d\);
3. niezależny model grafowy dla \(\Omega_m(z)\), \(\Omega_r(z)\), \(r_d\) i mapowania \(t_{lat}\to t_{phys}\);
4. funkcję \(\chi^2=\Delta^T C^{-1}\Delta\), bez dopasowywania danych syntetycznych;
5. test zależności od rozmiaru grafu, realizacji Monte Carlo i wartości \(q\);
6. porównanie z płaskim \(\Lambda\)CDM oraz modelem ewoluującej ciemnej energii.

## Werdykt

Z obecnego repo można wyprowadzić:

\[
\Lambda_{eff}=1.183705,
\quad H_*=0.628147\,t_{lat}^{-1},
\quad w=-1
\]

dla idealizowanego sektora próżniowego. Nie można jeszcze wyprowadzić fizycznego \(H(z)\) ani wykonać prawidłowego dopasowania DESI/BAO, ponieważ brakuje kalibracji jednostek, sektora materii/radiacji, skali BAO i rzeczywistych danych z kowariancją.
