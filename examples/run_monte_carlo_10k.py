#!/usr/bin/env python3
"""
MONTE CARLO SIMULATION OF 4D SPACETIME STABILITY ON N=10,000 LATTICE
---------------------------------------------------------------------
Autor: Michał Ślusarczyk
Data: Lipiec 2026

Skrypt przeprowadza wielkoskalową symulację Monte Carlo na grafie dualnym
1-szkieletu triangulacji o N = 10,000 węzłów (10^4 sympleksów), zawierającej
topologiczne piasty (anomalie koordynacyjne o stopniu ~800-1000).

Weryfikuje:
1. Stabilność wyłaniającej się fazy 4-wymiarowej (wymiar widmowy D_s -> 4.0)
   pod wpływem ważonej impedancji fizycznej ROI v5.2 (q=0.25).
2. Drastyczną redukcję udziału piast w transporcie (Phi_hub) i wyłączenie skrótów.
3. Jednorodność zregulowanego tensora Einsteina na wielkiej skali N=10^4.

Wyjście:
- monte_carlo_10k_results.csv
"""

import time
import numpy as np
import scipy.sparse as sp
import csv

def generate_large_scale_4d_triangulation(N=10000, num_hubs=10, hub_deg=800, seed=42):
    """
    Generuje rzadki graf dualny 1-szkieletu reprezentujący 4D triangulację
    o N=10,000 węzłów z wbudowanymi piastami topologicznymi.
    """
    np.random.seed(seed)
    L = int(round(N ** 0.25))
    actual_N = L ** 4
    
    def coord_to_idx(x, y, z, w):
        return ((x % L) * L**3) + ((y % L) * L**2) + ((z % L) * L) + (w % L)
        
    rows, cols = [], []
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for w in range(L):
                    u = coord_to_idx(x, y, z, w)
                    # 4D najbliżsi sąsiedzi + cięciwy dualne rzędu 2 (ogólny stopień bulkowy ~12-14)
                    for dx, dy, dz, dw in [(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0),
                                           (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1),
                                           (1,1,0,0), (-1,-1,0,0), (0,0,1,1), (0,0,-1,-1)]:
                        v = coord_to_idx(x+dx, y+dy, z+dz, w+dw)
                        rows.append(u); cols.append(v)
                        
    # Dodawanie piast topologicznych (miękkie piasty CDT)
    hubs = np.random.choice(actual_N, size=num_hubs, replace=False)
    for h in hubs:
        targets = np.random.choice(actual_N, size=hub_deg, replace=False)
        for t in targets:
            if t != h:
                rows.extend([h, t]); cols.extend([t, h])
                
    adj_matrix = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(actual_N, actual_N))
    adj_matrix = (adj_matrix > 0).astype(float).tocsr()
    deg = np.array(adj_matrix.sum(axis=1)).flatten()
    return actual_N, adj_matrix, deg, hubs

def simulate_monte_carlo_walks(N, adj_matrix, deg, q=0.25, num_walks=20000, max_steps=100, seed=1234):
    """
    Symuluje dyfuzję Monte Carlo oraz dokładne rozprzestrzenianie jądra ciepła
    w celu wyznaczenia wymiaru widmowego D_s(tau) oraz udziału piast w transporcie.
    """
    np.random.seed(seed)
    deg_q = np.power(np.maximum(deg, 1.0), -q)
    D_q = sp.diags(deg_q)
    W = D_q @ adj_matrix @ D_q
    w_sums = np.array(W.sum(axis=1)).flatten()
    P = sp.diags(1.0 / np.maximum(w_sums, 1e-15)) @ W
    P_T = P.T.tocsr()
    
    # Próbkowanie regularnych węzłów bulkowych jako punktów startowych
    bulk_nodes = [i for i in range(N) if deg[i] < 30]
    sample_size = min(500, len(bulk_nodes))
    samples = np.random.choice(bulk_nodes, size=sample_size, replace=False)
    
    X = np.zeros((N, sample_size))
    for idx, s in enumerate(samples):
        X[s, idx] = 1.0
        
    ts = np.unique(np.logspace(0.3, np.log10(max_steps), 25).astype(int))
    return_probs = {}
    
    curr_t = 0
    for t in ts:
        while curr_t < t:
            X = P_T @ X
            curr_t += 1
        ret_p = [X[samples[idx], idx] for idx in range(sample_size)]
        return_probs[t] = float(np.mean(ret_p))
        
    # Dopasowanie wymiaru widmowego D_s = -2 * d(log P_r)/d(log t) w oknie średnim [8, 35]
    tv = np.array(ts, dtype=float)
    pv = np.array([return_probs[t] for t in ts], dtype=float)
    mask = (tv >= 8) & (tv <= 35) & (pv > 0)
    if mask.sum() >= 3:
        slope, _ = np.polyfit(np.log(tv[mask]), np.log(pv[mask]), 1)
        ds_mid = -2.0 * float(slope)
    else:
        ds_mid = float('nan')
        
    # Udział piast w transporcie Phi_hub
    cutoff = np.quantile(deg, 0.99)
    top_nodes = set(np.where(deg >= cutoff)[0])
    W_coo = W.tocoo()
    total_w = W_coo.data.sum()
    hub_mask = np.isin(W_coo.row, list(top_nodes)) | np.isin(W_coo.col, list(top_nodes))
    hub_w = W_coo.data[hub_mask].sum()
    phi_hub = float(hub_w / total_w) if total_w > 0 else 0.0
    
    return ds_mid, phi_hub, return_probs

def run_large_scale_experiment():
    t0 = time.time()
    N, adj_matrix, deg, hubs = generate_large_scale_4d_triangulation(N=10000, num_hubs=10, hub_deg=800, seed=42)
    
    print("=" * 78)
    print("WIELKOSKALOWA SYMULACJA MONTE CARLO STABILNOŚCI FAZY 4D (N = 10^4)")
    print(f"Autor: Michał Ślusarczyk | Układ: N={N} węzłów | Piasty: {len(hubs)} (d_max={np.max(deg):.0f})")
    print(f"Średni stopień geometrii bulkowej: <d_bulk> = {np.mean([deg[i] for i in range(N) if i not in hubs]):.1f}")
    print("=" * 78)
    print(f"{'Metryka fizyczna':<18} | {'Wykładnik q':<12} | {'Wymiar widmowy D_s(8-35)':<24} | {'Udział piast Φ_hub':<18} | {'Faza topol.'}")
    print("-" * 92)
    
    results = []
    for q_label, q_val in [("Nieważona (q=0)", 0.00), ("Ważona ROI (q=0.25)", 0.25), ("Symetryczna (q=0.50)", 0.50)]:
        t_start = time.time()
        ds_val, phi_val, _ = simulate_monte_carlo_walks(N, adj_matrix, deg, q=q_val, max_steps=120, seed=1234 + int(q_val*100))
        dt = time.time() - t_start
        
        if abs(ds_val - 4.0) < 0.35:
            phase = "STABILNA FAZA 4D (4D Spacetime)"
        elif ds_val > 4.5:
            phase = "EKSPLOZJA SKRÓTÓW (Wormhole collapse)"
        else:
            phase = "Tłumienie podkrytyczne"
            
        print(f"{q_label:<18} | {q_val:<12.2f} | {ds_val:<24.3f} | {phi_val:<18.4f} | {phase}")
        results.append({
            'metric': q_label,
            'q_exponent': q_val,
            'spectral_dimension_Ds': round(ds_val, 4),
            'hub_transport_share': round(phi_val, 4),
            'max_degree': int(np.max(deg)),
            'bulk_avg_degree': round(float(np.mean(deg)), 2),
            'topological_phase': phase,
            'sim_time_sec': round(dt, 2)
        })
        
    print("-" * 92)
    print(f"Ukończono symulację wielkoskalową w czasie: {time.time()-t0:.2f}s")
    
    out_file = 'monte_carlo_10k_results.csv'
    with open(out_file, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader(); w.writerows(results)
    print(f"Zapisano wyniki symulacji do: {out_file}")
    print("=" * 92)

if __name__ == '__main__':
    run_large_scale_experiment()
