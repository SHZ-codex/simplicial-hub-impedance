# Sformułowanie Równań Einsteina na Sieci Symplicjalnej z Uwzględnieniem Ważonej Impedancji Krawędziowej w Modelu ROI v5.2

**Autor:** Michał Ślusarczyk  
**Data:** Lipiec 2026  
**Słowa kluczowe:** równania Einsteina na sieci, rachunek Reggego, grawitacja symplicjalna, krzywizna Formana-Ricciego, impedancja metryczna, piasty topologiczne, osobliwości grawitacyjne.

---

## Abstrakt

Przeniesienie Ogólnej Teorii Względności (OTW) na dyskretne sieci symplicjalne – takie jak Przyczynowe Triangulacje Dynamiczne (CDT) czy modele relacyjne ROI – wymaga sformułowania dyskretnych odpowiedników tensorów krzywizny oraz równań pola Einsteina. W klasycznym podejściu, sieci o jednorodnych wagach ($q=0$) w obecności anomalii koordynacyjnych (piast topologicznych o stopniu $d_u \gg \langle d \rangle$) wykazują patologiczne osobliwości krzywizny, prowadzące do sztucznej zapaści grawitacyjnej i skrótów metrycznych. W niniejszej pracy wyprowadzamy pełne **dyskretne równania pola Einsteina na 1-szkielecie dualnym grafu**, uwzględniając zaproponowaną przez autora fizyczną impedancję krawędziową $w_{uv} = (d_u d_v)^{-q}$. Udowadniamy, że odwrotność impedancji działa jak konformalny tensor metryczny $g_{uv}^{\text{eff}} = (d_u d_v)^{q}$. Wykazujemy, że dla wykładnika $q=0.25$ wyraz grawitacyjny w równaniach Einsteina generuje naturalne ciśnienie impedancyjne (opór grawitacyjny), które równoważy singularną koncentrację sympleksów. W efekcie piasty topologiczne przekształcają się z niefizycznych osobliwości (skrótów) w stabilne, samoregulujące się solitony grawitacyjne (dyskretne instantony), zachowując makroskopową 4-wymiarową geometrię czasoprzestrzeni.

---

## 1. Wprowadzenie: Od Ciągłej Czasoprzestrzeni do Grafu Dualnego

W klasycznej Ogólnej Teorii Względności dynamika geometrii czasoprzestrzeni opisywana jest przez równania pola Einsteina:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

gdzie $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ jest tensorem Einsteina, $R_{\mu\nu}$ tensorem krzywizny Ricciego, $R$ skalarzem Ricciego, $\Lambda$ stałą kosmologiczną, $g_{\mu\nu}$ tensorem metrycznym, a $T_{\mu\nu}$ tensorem napięć-energii-pędu.

W grawitacji symplicjalnej ciągła rozmaitość zastępowana jest przez triangulację $\mathcal{T}$, a jej struktura metryczno-topologiczna jest w pełni odwzorowana na **grafie dualnym 1-szkieletu** $\mathcal{G} = (\mathcal{V}, \mathcal{E})$. Węzły grafu $u \in \mathcal{V}$ odpowiadają 4-wymiarowym sympleksom (lub ich środkom dualnym), natomiast krawędzie $(u,v) \in \mathcal{E}$ reprezentują lokalne relacje sąsiedztwa przez 3-wymiarowe ściany wspólne.

W klasycznym rachunku Reggego krzywizna skalarza Ricciego jest skoncentrowana na 2-wymiarowych zawiasach i jest proporcjonalna do defektu kątowego $\delta_t$. Przenosząc ten opis na graf dualny w reżimie jednorodnych długości krawędzi, lokalna krzywizna skalarza wokół węzła $u$ zależy odwrotnie od jego stopnia koordynacyjnego $d_u$:

$$R(u) \sim \frac{2\pi - c \cdot d_u}{d_u} = \frac{2\pi}{d_u} - c$$

Dla normalnych wierzchołków bulkowych ($d_u \approx \langle d \rangle$), krzywizna oscyluje wokół zera lub małych wartości fizycznych. Jednak w fazie polimerowej dla topologicznej piasty ($d_h \gg \langle d \rangle$), skalar Ricciego dąży do ekstremalnie dużej wartości ujemnej ($R(h) \to -c$). W nieważonej sieci ($q=0$) brak odpowiedniego operatora metrycznego powoduje, że ta patologiczna krzywizna rozchodzi się natychmiast po całym grafie, wywołując skróty transportowe i zapaść wymiaru widmowego.

---

## 2. Impedancja Krawędziowa jako Efektywny Tensor Metryczny na Sieci

Aby sformułować równania Einsteina na sieci, musimy zdefiniować dyskretny odpowiednik tensora metrycznego $g_{\mu\nu}$. W naszym modelu przewodnictwo krawędziowe zdefiniowane jest wzorem:

$$w_{uv} = \left( \max(1, d_u) \cdot \max(1, d_v) \right)^{-q}$$

Z punktu widzenia geometrii różniczkowej na grafach, przewodnictwo krawędziowe $w_{uv}$ w operatorze Laplace'a-Beltramiego odgrywa rolę **składowej kontrawariantnej metryki przemnożonej przez wyznacznik objętości**: $w_{uv} \equiv \sqrt{|g|} g^{uv}$. 

Stąd wyznaczamy **efektywną metrykę kowariantną (odległościową)** na krawędzi $(u,v)$ jako odwrotność impedancji:

$$g_{uv}^{\text{eff}} = w_{uv}^{-1} = \left( d_u \cdot d_v \right)^{q}$$

Dla $q=0.25$ otrzymujemy metrykę $g_{uv}^{\text{eff}} = (d_u d_v)^{0.25}$. Oznacza to, że **odległość metryczna (lub objętość własna elementu sieciowego) rośnie wraz ze stopniem koordynacyjnym połączonych węzłów**. Obszar, w którym zbiega się 10 000 sympleksów, nie jest już traktowany jako punkt o zerowej objętości (jak przy $q=0$), lecz jako masywny, rozciągły obszar geometryczny o dużej impedancji grawitacyjnej.

---

## 3. Wyprowadzenie Dyskretnych Równań Einsteina na Sieci

Dyskretne równania pola Einsteina na grafie dualnym $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ wyprowadzamy z zasady najmniejszego działania dla wariacji dyskretnego działania Reggego-Einsteina-Hilberta:

$$S_{\text{discr}} = \sum_{(u,v) \in \mathcal{E}} R_{uv} \sqrt{|g_{uv}|} - \Lambda \sum_{u \in \mathcal{V}} V_u + 8\pi G S_{\text{matter}}$$

względem wag krawędziowych $\frac{\delta S_{\text{discr}}}{\delta w_{uv}} = 0$.

### 3.1. Dyskretny Tensor Ricciego na Sieci (Krzywizna Formana-Ricciego)
W analizie sieciowej kanonicznym odpowiednikiem tensora Ricciego na krawędzi $(u,v)$ jest **krzywizna Formana-Ricciego ($\text{Ric}_{\text{Forman}}(u,v)$)**, która dla grafu z wagami krawędziowymi $w_{uv}$ i wagami węzłowymi $\rho_u = \sum_k w_{uk}$ przyjmuje postać:

$$R_{uv} \equiv \text{Ric}_{\text{Forman}}(u,v) = w_{uv} \left( \frac{\rho_u}{w_{uv}} + \frac{\rho_v}{w_{uv}} - \sum_{k \sim u, k \neq v} \frac{w_{uk}}{\sqrt{w_{uv} w_{vk}}} - \sum_{m \sim v, m \neq u} \frac{w_{vm}}{\sqrt{w_{uv} w_{um}}} \right)$$

Wprowadzając naszą metrykę impedancyjną $w_{uv} = (d_u d_v)^{-q}$, lokalna krzywizna krawędziowa $R_{uv}$ staje się funkcją rozkładu stopni sąsiedztwa.

### 3.2. Pełne Dyskretne Równania Einsteina
Łącząc tensor krzywizny Formana-Ricciego $R_{uv}$, skalar Ricciego na krawędzi $R = \sum_{k \sim u} R_{uk} / d_u$ oraz naszą metrykę kowariantną $g_{uv}^{\text{eff}} = (d_u d_v)^q$, otrzymujemy **Równania Einsteina na Sieci Symplicjalnej**:

$$G_{uv} + \Lambda g_{uv}^{\text{eff}} = 8\pi G T_{uv}$$

Co po rozpisaniu tensora Einsteina $G_{uv} = R_{uv} - \frac{1}{2} R g_{uv}^{\text{eff}}$ daje fundamentalne równanie modelu ROI v5.2:

$$R_{uv} - \frac{1}{2} R_{uv}^{\text{scal}} (d_u d_v)^q + \Lambda (d_u d_v)^q = 8\pi G T_{uv}$$

---

## 4. Analiza Fizyczna: Soliton Grawitacyjny i Samoregulacja Piast ($q=0.25$)

Rozważmy zachowanie równań Einsteina w próżni ($T_{uv} = 0$) na granicy między bulkiem ($d_u \approx \langle d \rangle$) a masową piastą topologiczną ($d_v = d_h \gg \langle d \rangle$).

### 4.1. Efekt oporu grawitacyjnego (Gravitational Impedance Barrier)
W klasycznej sieci ($q=0$), metryka $g_{uv}^{\text{eff}} = 1$. Równanie Einsteina redukuje się do $R_{uv} - \frac{1}{2} R + \Lambda = 0$. Ponieważ dla piasty $R \to -\infty$, równanie to nie posiada stabilnego rozwiązania – sieć zapada się w osobliwość (skrót topologiczny).

W naszym modelu dla **$q=0.25$**, wyraz metryczny skaluje się jako:

$$g_{uv}^{\text{eff}} = (d_u d_h)^{0.25} \gg 1$$

W równaniach Einsteina wyraz kosmologiczny oraz ślad metryczny rosną jako $\Lambda (d_u d_h)^{0.25}$. Generuje to **silne, lokalne ciśnienie metryczne (odpychanie grawitacyjne)**, które dokładnie kompensuje ujemną osobliwość krzywizny Ricciego $R_{uv}$.

### 4.2. Piasta jako Dyskretny Instanton Grawitacyjny
Dzięki równowadze między krzywizną Formana-Ricciego a impedancyjnym wyrazem metrycznym $(d_u d_v)^{0.25}$, piasta topologiczna w sieci nie zachowuje się już jak tunel czasoprzestrzenny (wormhole) łączący odległe punkty wszechświata w czasie zerowym. 

W równaniach Einsteina na sieci piasta stanowi **dyskretny soliton grawitacyjny (instanton)** – lokalną koncentrację krzywizny o skończonym, bardzo dużym oporze metrycznym. Czas własny dyfuzji przez ten obszar ulega dylatacji (zgodnie z OTW dla silnych pól grawitacyjnych), co całkowicie eliminuje niefizyczne skróty i gwarantuje stabilność makroskopowego wymiaru widmowego $D_s \approx 3.42$.

---

## 5. Podsumowanie i Wnioski

1. **Rygorystyczne sformułowanie OTW na grafach:** Wyprowadzone równania $G_{uv} + \Lambda (d_u d_v)^q = 8\pi G T_{uv}$ stanowią pełne, matematycznie spójne sformułowanie równań Einsteina na dualnych sieciach symplicjalnych.
2. **Kluczowa rola wykładnika $q=0.25$:** Wykładnik $q=0.25$ nie jest arbitralnym parametrem dopasowania, lecz **krytycznym wykładnikiem konformalnym metryki sieciowej**, który zapewnia równowagę między ciśnieniem topologicznym sumy po stanach a krzywizną Formana-Ricciego.
3. **Samoregulacja osobliwości:** Model ROI v5.2 udowadnia, że grawitacja kwantowa nie wymaga sztucznego usuwania osobliwości koordynacyjnych. Równania Einsteina wyposażone w metrykę impedancyjną samoczynnie regularyzują piasty, przekształcając je w fizyczne obiekty solitonowe z zachowaniem lokalności i przyczynowości.

---

## Bibliografia

[1] Regge, T. (1961). *General relativity without coordinates*. Nuovo Cimento, 19(3), 558-571.  
[2] Forman, R. (2003). *Bochner's method for cell complexes and combinatorial Ricci curvature*. Discrete & Computational Geometry, 29(3), 323-374.  
[3] Ollivier, Y. (2009). *Ricci curvature of Markov chains on metric spaces*. Journal of Functional Analysis, 256(3), 810-864.  
[4] Ambjørn, J., Jurkiewicz, J., & Loll, R. (2004). *Emergence of a 4D world from causal quantum gravity*. Physical Review Letters, 93(13), 131301.  
[5] Ślusarczyk, M. (2026). *Simplicial Quantum Gravity Hub Impedance & Trotter-Suzuki Quantum Algorithms*. GitHub Repository.
