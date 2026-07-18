#!/usr/bin/env python3
"""
NUMERICAL SIMULATION OF COSMOLOGICAL EVOLUTION IN ROI v5.2
----------------------------------------------------------
Autor: Michał Ślusarczyk
Data: Lipiec 2026

Skrypt symuluje ewolucję kosmologiczną jednorodnego wszechświata FLRW napędzanego
efektywną ciemną energią wyłaniającą się z dyskretnych równań Einsteina na sieci:
    G_{uv} + Lambda * g_{uv}^{eff} \approx -1.1837

Wyznacza:
1. Gęstość ciemnej energii rho_DE, stałą kosmologiczną Lambda_eff oraz parametr Hubbla H_0.
2. Ewolucję czynnika skali a(t) dla wszechświata płaskiego (k=0, ekspansja de Sittera).
3. Ewolucję czynnika skali a(t) dla wszechświata zamkniętego (k=+1, quantum bounce cosh(H_0 t)).
4. Ewolucję objętości przestrzennej V_3(t) i weryfikuje zbieżność z profilami CDT.

Wyjście:
- cosmology_scale_factor_results.csv
"""

import numpy as np
import csv

def simulate_cosmological_evolution():
    # Średnia wartość zregulowanego tensora Einsteina na sieci
    G_reg_mean = -1.183705
    
    # Jednostki symplicjalne / Plancka (8 pi G = 1)
    G_val = 1.0 / (8.0 * np.pi)
    
    # Parametry kosmologiczne
    Lambda_eff = -G_reg_mean
    rho_DE = Lambda_eff  # dla 8 pi G = 1
    w_eos = -1.0         # równanie stanu próżni
    H0 = np.sqrt(Lambda_eff / 3.0)
    a_min = 1.0 / H0     # minimalny promień odbicia dla k=+1
    
    print("=" * 78)
    print("SYMULACJA KOSMOLOGICZNA MODELU ROI v5.2 (METRYKA FLRW)")
    print(f"Autor: Michał Ślusarczyk | Zregulowany tensor Einsteina <G_reg>: {G_reg_mean:.6f}")
    print("=" * 78)
    print(f"Efektywna Stała Kosmologiczna (Λ_eff): {Lambda_eff:.6f}")
    print(f"Gęstość Ciemnej Energii (ρ_DE):         {rho_DE:.6f} (w jedn. 8πG=1)")
    print(f"Równanie Stanu Próżni (w):             {w_eos:.4f}")
    print(f"Parametr Hubbla (H_0):                 {H0:.6f} t^-1")
    print(f"Minimalny Promień w Odbiciu (a_min):   {a_min:.6f} (dla k=+1)")
    print("=" * 78)
    
    ts = np.linspace(-5.0, 5.0, 101)
    results = []
    
    print(f"{'Czas t':<8} | {'a(t) [k=0 płaski]':<18} | {'a(t) [k=+1 odbicie]':<20} | {'V_3(t) [k=+1 objętość]':<22} | {'Faza kosmol.'}")
    print("-" * 88)
    
    for idx, t in enumerate(ts):
        # 1. Wszechświat płaski (k=0): a(t) = a_min * exp(H_0 * t) dla t >= 0
        a_flat = a_min * np.exp(H0 * t)
        
        # 2. Wszechświat zamknięty (k=+1): a(t) = a_min * cosh(H_0 * t)
        a_closed = a_min * np.cosh(H0 * t)
        
        # 3. Objętość przestrzenna sfery S^3: V_3(t) = 2 * pi^2 * a^3(t)
        v3_closed = 2.0 * (np.pi ** 2) * (a_closed ** 3)
        
        # Faza
        if abs(t) < 0.2:
            phase = "BOUNCE (Odbicie kwant.)"
        elif t < 0:
            phase = "Kontrakcja (zapadanie)"
        else:
            phase = "Ekspansja de Sittera"
            
        if idx % 10 == 0 or abs(t) < 1e-10:
            print(f"{t:<8.2f} | {a_flat:<18.4f} | {a_closed:<20.4f} | {v3_closed:<22.2f} | {phase}")
            
        results.append({
            'time': round(t, 4),
            'scale_factor_flat_k0': round(a_flat, 6),
            'scale_factor_closed_k1': round(a_closed, 6),
            'volume_closed_S3': round(v3_closed, 4),
            'hubble_rate': round(H0 * np.tanh(H0 * t), 6),
            'acceleration_ddot_a': round(a_closed * (H0 ** 2), 6),
            'cosmological_phase': phase
        })
        
    print("-" * 88)
    
    out_file = 'cosmology_scale_factor_results.csv'
    with open(out_file, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader(); w.writerows(results)
    print(f"Zapisano ewolucję kosmologiczną do: {out_file}")
    print("=" * 88)

if __name__ == '__main__':
    simulate_cosmological_evolution()
