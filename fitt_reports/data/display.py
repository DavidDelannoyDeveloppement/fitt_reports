import pandas as pd
from pathlib import Path
from data.imports import import_data


#############################################################
######################## CPE MOIS ###########################
#############################################################


def display_conso_reelle(df: pd.DataFrame) -> str:
    conso_reelle = df["consommation_reelle"].iloc[0]
    conso_reelle_str = str(conso_reelle)
    return conso_reelle_str.replace(".", ",")

def display_conso_reelle_elec(df: pd.DataFrame) -> str:
    conso_reelle = df["consommation_reelle_elec"].iloc[0]
    conso_reelle_str = str(conso_reelle)
    return conso_reelle_str.replace(".", ",")

def display_conso_reelle_gaz(df: pd.DataFrame) -> str:
    conso_reelle = df["consommation_reelle_gaz"].iloc[0]
    conso_reelle_str = str(conso_reelle)
    return conso_reelle_str.replace(".", ",")


def display_modele_predictif(df: pd.DataFrame) -> str:
    modele_predictif = df["modele_predictif"].iloc[0]
    modele_predictif_str = str(modele_predictif)
    return modele_predictif_str.replace(".", ",")

def display_modele_predictif_elec(df: pd.DataFrame) -> str:
    modele_predictif = df["modele_predictif_elec"].iloc[0]
    modele_predictif_str = str(modele_predictif)
    return modele_predictif_str.replace(".", ",")

def display_modele_predictif_gaz(df: pd.DataFrame) -> str:
    modele_predictif = df["modele_predictif_gaz"].iloc[0]
    modele_predictif_str = str(modele_predictif)
    return modele_predictif_str.replace(".", ",")


def display_performance_contrat_kwh(df: pd.DataFrame) -> str:
    performance_contrat_kwh = df["performance_contrat_kwh"].iloc[0]
    performance_contrat_kwh_str = str(performance_contrat_kwh)
    return performance_contrat_kwh_str.replace(".", ",")

def display_performance_contrat_kwh_elec(df: pd.DataFrame) -> str:
    performance_contrat_kwh = df["performance_contrat_kwh_elec"].iloc[0]
    performance_contrat_kwh_str = str(performance_contrat_kwh)
    return performance_contrat_kwh_str.replace(".", ",")

def display_performance_contrat_kwh_gaz(df: pd.DataFrame) -> str:
    performance_contrat_kwh = df["performance_contrat_kwh_gaz"].iloc[0]
    performance_contrat_kwh_str = str(performance_contrat_kwh)
    return performance_contrat_kwh_str.replace(".", ",")


def display_performance_contrat_percent(df: pd.DataFrame) -> str:
    performance_contrat_percent = df["performance_contrat_percent"].iloc[0]
    performance_contrat_percent_str = str(performance_contrat_percent)
    return performance_contrat_percent_str.replace(".", ",")

def display_performance_contrat_percent_elec(df: pd.DataFrame) -> str:
    performance_contrat_percent = df["performance_contrat_percent_elec"].iloc[0]
    performance_contrat_percent_str = str(performance_contrat_percent)
    return performance_contrat_percent_str.replace(".", ",")

def display_performance_contrat_percent_gaz(df: pd.DataFrame) -> str:
    performance_contrat_percent = df["performance_contrat_percent_gaz"].iloc[0]
    performance_contrat_percent_str = str(performance_contrat_percent)
    return performance_contrat_percent_str.replace(".", ",")


def display_performance_contrat_percent_float(df: pd.DataFrame) -> float:
    performance_contrat_percent = df["performance_contrat_percent"].iloc[0]
    return performance_contrat_percent

def display_performance_contrat_percent_float_elec(df: pd.DataFrame) -> float:
    performance_contrat_percent = df["performance_contrat_percent_elec"].iloc[0]
    return performance_contrat_percent

def display_performance_contrat_percent_float_gaz(df: pd.DataFrame) -> float:
    performance_contrat_percent = df["performance_contrat_percent_gaz"].iloc[0]
    return performance_contrat_percent


def display_name_machine(df: pd.DataFrame) -> str:
    name_machine = df["nom_machine"].iloc[0]
    return name_machine


def display_engagement_contract(df: pd.DataFrame) -> str:
    engagement_contract = df["engagement"].iloc[0]
    engagement_contract_int = int(engagement_contract)
    return engagement_contract_int

def display_engagement_contract_elec(df: pd.DataFrame) -> str:
    engagement_contract = df["engagement_elec"].iloc[0]
    engagement_contract_int = int(engagement_contract)
    return engagement_contract_int

def display_engagement_contract_gaz(df: pd.DataFrame) -> str:
    engagement_contract = df["engagement_gaz"].iloc[0]
    engagement_contract_int = int(engagement_contract)
    return engagement_contract_int


#############################################################
################## Affichage gain/perte #####################


def display_gain_perte(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "un Gain"
    else:
        return "une Perte"
    
def display_gain_perte_elec(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_elec(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "un Gain"
    else:
        return "une Perte"
    
def display_gain_perte_gaz(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_gaz(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "un Gain"
    else:
        return "une Perte"


#############################################################
########### Affichage économie/surconsommation ##############


def display_eco_surconso(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "d'Économie"
    else:
        return "de Surconsommation"

def display_eco_surconso_elec(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_elec(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "d'Économie"
    else:
        return "de Surconsommation"

def display_eco_surconso_gaz(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_gaz(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "d'Économie"
    else:
        return "de Surconsommation"


#############################################################
##########   Affichage conforme/non conforme   ##############


def display_conforme(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract(df)
    performance = display_performance_contrat_percent_float(df)
    if performance >= engagement:
        return "Conforme"
    else:
        return "Non conforme"
    
def display_conforme_elec(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_elec(df)
    performance = display_performance_contrat_percent_float_elec(df)
    if performance >= engagement:
        return "Conforme"
    else:
        return "Non conforme"
    
def display_conforme_gaz(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_gaz(df)
    performance = display_performance_contrat_percent_float_gaz(df)
    if performance >= engagement:
        return "Conforme"
    else:
        return "Non conforme"


def display_conforme_color(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract(df)
    performance = display_performance_contrat_percent_float(df)
    if performance >= engagement:
        print("vert")
        return "#00a250"
    else:
        print("rouge")
        return "#be097f"
    
def display_conforme_color_elec(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_elec(df)
    performance = display_performance_contrat_percent_float_elec(df)
    if performance >= engagement:
        return "#00a250"
    else:
        return "#be097f"
    
def display_conforme_color_gaz(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_gaz(df)
    performance = display_performance_contrat_percent_float_gaz(df)
    if performance >= engagement:
        return "#00a250"
    else:
        return "#be097f"


#############################################################
######################## CPE ANNEE ##########################
#############################################################
def display_conso_reelle_year(df: pd.DataFrame) -> str:
    conso_reelle = df["consommation_reelle_year"].iloc[0]
    conso_reelle_str = str(conso_reelle)
    return conso_reelle_str.replace(".", ",")

def display_conso_reelle_year_elec(df: pd.DataFrame) -> str:
    conso_reelle = df["consommation_reelle_year_elec"].iloc[0]
    conso_reelle_str = str(conso_reelle)
    return conso_reelle_str.replace(".", ",")

def display_conso_reelle_year_gaz(df: pd.DataFrame) -> str:
    conso_reelle = df["consommation_reelle_year_gaz"].iloc[0]
    conso_reelle_str = str(conso_reelle)
    return conso_reelle_str.replace(".", ",")


def display_modele_predictif_year(df: pd.DataFrame) -> str:
    modele_predictif = df["modele_predictif_year"].iloc[0]
    modele_predictif_str = str(modele_predictif)
    return modele_predictif_str.replace(".", ",")

def display_modele_predictif_year_elec(df: pd.DataFrame) -> str:
    modele_predictif = df["modele_predictif_year_elec"].iloc[0]
    modele_predictif_str = str(modele_predictif)
    return modele_predictif_str.replace(".", ",")

def display_modele_predictif_year_gaz(df: pd.DataFrame) -> str:
    modele_predictif = df["modele_predictif_year_gaz"].iloc[0]
    modele_predictif_str = str(modele_predictif)
    return modele_predictif_str.replace(".", ",")


def display_performance_contrat_kwh_year(df: pd.DataFrame) -> str:
    performance_contrat_kwh = df["performance_contrat_kwh_year"].iloc[0]
    performance_contrat_kwh_str = str(performance_contrat_kwh)
    return performance_contrat_kwh_str.replace(".", ",")

def display_performance_contrat_kwh_year_elec(df: pd.DataFrame) -> str:
    performance_contrat_kwh = df["performance_contrat_kwh_year_elec"].iloc[0]
    performance_contrat_kwh_str = str(performance_contrat_kwh)
    return performance_contrat_kwh_str.replace(".", ",")

def display_performance_contrat_kwh_year_gaz(df: pd.DataFrame) -> str:
    performance_contrat_kwh = df["performance_contrat_kwh_year_gaz"].iloc[0]
    performance_contrat_kwh_str = str(performance_contrat_kwh)
    return performance_contrat_kwh_str.replace(".", ",")


def display_performance_contrat_percent_year(df: pd.DataFrame) -> str:
    performance_contrat_percent = df["performance_contrat_percent_year"].iloc[0]
    performance_contrat_percent_str = str(performance_contrat_percent)
    return performance_contrat_percent_str.replace(".", ",")

def display_performance_contrat_percent_year_elec(df: pd.DataFrame) -> str:
    performance_contrat_percent = df["performance_contrat_percent_year_elec"].iloc[0]
    performance_contrat_percent_str = str(performance_contrat_percent)
    return performance_contrat_percent_str.replace(".", ",")

def display_performance_contrat_percent_year_gaz(df: pd.DataFrame) -> str:
    performance_contrat_percent = df["performance_contrat_percent_year_gaz"].iloc[0]
    performance_contrat_percent_str = str(performance_contrat_percent)
    return performance_contrat_percent_str.replace(".", ",")


def display_performance_contrat_percent_year_float(df: pd.DataFrame) -> float:
    performance_contrat_percent = df["performance_contrat_percent_year"].iloc[0]
    return performance_contrat_percent

def display_performance_contrat_percent_year_float_elec(df: pd.DataFrame) -> float:
    performance_contrat_percent = df["performance_contrat_percent_year_elec"].iloc[0]
    return performance_contrat_percent

def display_performance_contrat_percent_year_float_gaz(df: pd.DataFrame) -> float:
    performance_contrat_percent = df["performance_contrat_percent_year_gaz"].iloc[0]
    return performance_contrat_percent


#############################################################
################## Affichage gain/perte #####################


def display_gain_perte_year(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_year(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "un Gain"
    else:
        return "une Perte"
    
def display_gain_perte_year_elec(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_year_elec(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "un Gain"
    else:
        return "une Perte"
    
def display_gain_perte_year_gaz(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_year_gaz(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "un Gain"
    else:
        return "une Perte"


#############################################################
########### Affichage économie/surconsommation ##############


def display_eco_surconso_year(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_year(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "d'Économie"
    else:
        return "de Surconsommation"
    
def display_eco_surconso_year_elec(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_year_elec(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "d'Économie"
    else:
        return "de Surconsommation"
    
def display_eco_surconso_year_gaz(df: pd.DataFrame) -> str:
    diff_perf_str = display_performance_contrat_percent_year_gaz(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return "d'Économie"
    else:
        return "de Surconsommation"


#############################################################
##########   Affichage conforme/non conforme   ##############


def display_conforme_year(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract(df)
    performance = display_performance_contrat_percent_year_float(df)
    if performance >= engagement:
        return "Conforme"
    else:
        return "Non conforme"
    
def display_conforme_year_elec(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_elec(df)
    performance = display_performance_contrat_percent_year_float_elec(df)
    if performance >= engagement:
        return "Conforme"
    else:
        return "Non conforme"
    
def display_conforme_year_gaz(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_gaz(df)
    performance = display_performance_contrat_percent_year_float_gaz(df)
    if performance >= engagement:
        return "Conforme"
    else:
        return "Non conforme"
    


def display_conforme_color_year(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract(df)
    performance = display_performance_contrat_percent_year_float(df)
    if performance >= engagement:
        print("vert")
        return "#00a250"
    else:
        print("rouge")
        return "#be097f"
    
def display_conforme_color_year_elec(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_elec(df)
    performance = display_performance_contrat_percent_year_float_elec(df)
    if performance >= engagement:
        return "#00a250"
    else:
        return "#be097f"
    
def display_conforme_color_year_gaz(df: pd.DataFrame) -> str:
    engagement = display_engagement_contract_gaz(df)
    performance = display_performance_contrat_percent_year_float_gaz(df)
    if performance >= engagement:
        return "#00a250"
    else:
        return "#be097f"


#############################################################
############    Démarrage et temps des circuits    ##########
#############################################################
def display_circuit(path_df: Path, i: int) -> str:
    df = import_data(path_df)
    circuit = df["Circuit"].iloc[i]
    return circuit  


def display_temps_fonctionnement(path_df: Path, i: int) -> str:
    df = import_data(path_df)
    temps_fonctionnement = df["Temps de fonctionnement total"].iloc[i]
    temps_fonctionnement_str = str(temps_fonctionnement)
    return temps_fonctionnement_str.replace(".", ",")


def display_nombre_demarrage(path_df: Path, i: int) -> str:
    df = import_data(path_df)
    nombre_demarrage = df["Nombre de démarrage"].iloc[i]
    nombre_demarrage_str = str(nombre_demarrage)
    return nombre_demarrage_str.replace(".", ",")


def display_ratio_demarrage(path_df: Path, i: int) -> str:
    df = import_data(path_df)
    ratio_demarrage = df["Ratio démarrages par heure"].iloc[i]
    radio_demarrage_str = str(ratio_demarrage)
    return radio_demarrage_str.replace(".", ",")


#############################################################
######    Puissances moyennes fonctionnement circuit   ######
#############################################################
def display_puissances_moyennes_fonctionnement_froid(path_df: Path, i: int) -> str:
    df = import_data(path_df)
    puissances_moyenne_fonctionnement_froid = df["Puissance_froid"].iloc[i]
    puissances_moyenne_fonctionnement_froid_str = str(
        puissances_moyenne_fonctionnement_froid
    )
    return puissances_moyenne_fonctionnement_froid_str.replace(".", ",")


def display_puissances_moyennes_fonctionnement_chaud(path_df: Path, i: int) -> str:
    df = import_data(path_df)
    puissances_moyenne_fonctionnement_chaud = df["Puissance_chaud"].iloc[i]
    puissances_moyenne_fonctionnement_chaud_str = str(
        puissances_moyenne_fonctionnement_chaud
    )
    return puissances_moyenne_fonctionnement_chaud_str.replace(".", ",")


def display_puissance_electrique_machine(path_df: Path) -> str:
    df = import_data(path_df)
    puissance_electrique_machine = df["Puissance électrique machine"].iloc[0]
    puissance_electrique_machine_str = str(puissance_electrique_machine)
    return puissance_electrique_machine_str.replace(".", ",")
