import numpy as np

def calculate_mizan_acceleration(r_array, m_bar, A0=5.234951, gamma=-0.138325, K_global=0.978294, M_star=1e10, R_c=1.0, k=1):
    """
    Computes the effective centripetal acceleration field g_mizan(r)
    using the Al-Mizan Al-Mutakamil Relational Framework.
    """
    # Classical baryonic centripetal acceleration proxy
    g_bar = (G_CONSTANT_PROXY * m_bar) / (r_array ** 2)
    
    # Non-local relational scale enhancement kernel
    amplitude_factor = A0 * (m_bar / M_star) ** gamma
    scale_ratio = (r_array / (k * R_c)) ** K_global
    kernel = 1.0 + amplitude_factor * scale_ratio
    
    return g_bar * kernel

if __name__ == "__main__":
    print("==================================================")
    print(" Al-Mizan Al-Mutakamil Computational Cosmology Pipeline ")
    print("==================================================")
    
    # Test evaluation across representative galactocentric radii (kpc)
        r_points = np.linspace(0.5, 30.0, 60)
    
    # Benchmark mass: High-Mass Spiral (e.g., NGC 3198 ~ 3.4e10 M_sun)
    m_baryonic = 3.4e10 
    
    print(f"Executing kinematic calibration for M_bar = {m_baryonic:.2e} M_sun...")
    
    G_CONSTANT_PROXY = 4.30091e-6 # (km/s)^2 * kpc / M_sun
    g_results = calculate_mizan_acceleration(r_points, m_baryonic)
    
    print(f"Simulation successfully evaluated across {len(r_points)} radial points.")
    print(f"Outer disk acceleration g_mizan(30 kpc): {g_results[-1]:.6e} (km/s)^2/kpc")
    print("Pipeline execution completed successfully.")
