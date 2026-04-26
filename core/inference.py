from data.rules import rules
from data.penyakit import penyakit_list

def forward_chaining(selected_gejala):
    """
    Fungsi untuk melakukan inferensi menggunakan metode Forward Chaining.
    Mencocokkan semua gejala yang dipilih (selected_gejala) dengan rules.
    """
    detected_diseases = []
    
    for rule in rules:
        for p_kode, gejala_syarat in rule.items():
            if all(g in selected_gejala for g in gejala_syarat):
                for p in penyakit_list:
                    if p['kode'] == p_kode:
                        if p not in detected_diseases:
                            detected_diseases.append(p)
                        break
                        
    return detected_diseases
