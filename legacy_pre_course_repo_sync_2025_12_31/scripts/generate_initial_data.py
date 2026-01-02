from phs564_ci.datasets.synthetic import (
    generate_l01_data, 
    generate_l02_data, 
    generate_l03_data,
    generate_l04_data,
    generate_l05_data,
    generate_l06_data,
    generate_l07_data,
    generate_l08_l09_data,
    generate_l10_data,
    generate_l11_data,
    generate_l12_survival_data
)
import os

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    
    generate_l01_data().to_csv("data/l01_potential_outcomes.csv", index=False)
    generate_l02_data().to_csv("data/l02_ideal_rct.csv", index=False)
    generate_l03_data().to_csv("data/l03_observational.csv", index=False)
    generate_l04_data().to_csv("data/l04_effect_modification.csv", index=False)
    generate_l05_data().to_csv("data/l05_collider_bias.csv", index=False)
    generate_l06_data().to_csv("data/l06_confounding.csv", index=False)
    generate_l07_data().to_csv("data/l07_selection_bias.csv", index=False)
    generate_l08_l09_data().to_csv("data/l08_l09_parametric.csv", index=False)
    generate_l10_data().to_csv("data/l10_iv.csv", index=False)
    generate_l11_data().to_csv("data/l11_ipw.csv", index=False)
    generate_l12_survival_data().to_csv("data/l12_survival.csv", index=False)
    
    print("Generated all data files (L01-L12)")
