import pandas as pd
from pathlib import Path
from data.imports import import_data
from data.display import (
    display_performance_contrat_percent,
    display_performance_contrat_percent_year,
)


#############################################################
################ Affichage flèches bilan ####################
#############################################################
def arrow_display_month(df: pd.DataFrame, name_client: str) -> Path:
    diff_perf_str = display_performance_contrat_percent(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return Path(f"./../../creations/{name_client}_reports/images/green_arrow.png")
    else:
        return Path(f"./../../creations/{name_client}_reports/images/red_arrow.png")


def arrow_display_year(df: pd.DataFrame, name_client: str) -> Path:
    diff_perf_str = display_performance_contrat_percent_year(df)
    diff_perf = float(diff_perf_str.replace(",", "."))
    if diff_perf >= 0:
        return Path(f"./../../creations/{name_client}_reports/images/green_arrow.png")
    else:
        return Path(f"./../../creations/{name_client}_reports/images/red_arrow.png")


#############################################################
############## Affichage Validation ratio ###################
#############################################################
def valid_ratio(path_df: Path, i: int, name_client: str) -> Path:
    df = import_data(path_df)
    ratio_demarrage = df["Ratio démarrages par heure"].iloc[i]
    seuil = 3.5
    if ratio_demarrage <= seuil:
        return Path(f"./../../creations/{name_client}_reports/images/green_valid.png")
    else:
        return Path(f"./../../creations/{name_client}_reports/images/red_valid.png")


def valid_ratio_min(path_df: Path, i: int, name_client: str) -> Path:
    df = import_data(path_df)
    ratio_demarrage = df["Ratio démarrages par heure"].iloc[i]
    seuil = 5
    if ratio_demarrage < seuil:
        return Path(f"./../../creations/{name_client}_reports/images/red_valid.png")
    else:
        return Path(f"./../../creations/{name_client}_reports/images/green_valid.png")


def valid_ratio_alvend(path_df: Path, i: int, name_client: str) -> Path:
    df = import_data(path_df)
    ratio_demarrage = df["Ratio démarrages par heure"].iloc[i]
    seuil = 5
    if ratio_demarrage >= seuil:
        return Path(f"./../../creations/{name_client}_reports/images/green_valid.png")
    # elif ratio_demarrage == 0:
    #     return Path(f"./../../creations/{name_client}_reports/images/blanc.png")
    else:
        return Path(f"./../../creations/{name_client}_reports/images/blanc.png")


def valid_ratio_thelia(path_df: Path, i: int, name_client: str) -> Path:
    df = import_data(path_df)
    ratio_demarrage = df["Ratio démarrages par heure"].iloc[i]
    seuil = 5
    if ratio_demarrage >= seuil:
        return Path(f"./../../creations/{name_client}_reports/images/green_valid.png")
    # elif ratio_demarrage == 0:
    #     return Path(f"./../../creations/{name_client}_reports/images/blanc.png")
    else:
        return Path(f"./../../creations/{name_client}_reports/images/blanc.png")


# def arrow_display_year(df: pd.DataFrame) -> Path:
#     diff_perf = contract_performance_kwh_year(df, consommation_machine_name_column, prediction_machine_name_column, name_machine)
#     if diff_perf >= 0:
#         return Path(f"../../resources/images/green_arrow_xs.png")
#     else:
#         return Path(f"../../resources/images/red_arrow_xs.png")


# def arrow_display_week(df: pd.DataFrame) -> Path:
#     diff_perf = contract_performance_kwh_week(df, consommation_machine_name_column, prediction_machine_name_column, name_machine)
#     if diff_perf >= 0:
#         return Path(f"../../resources/images/green_arrow_xs.png")
#     else:
#         return Path(f"../../resources/images/red_arrow_xs.png")


# def arrow_display_week_u4(df: pd.DataFrame) -> Path:
#     diff_perf = contract_performance_kwh_week_u4(df, consommation_machine_name_column, prediction_machine_name_column, name_machine)
#     if diff_perf >= 0:
#         return Path(f"../../resources/images/green_arrow_xs.png")
#     else:
#         return Path(f"../../resources/images/red_arrow_xs.png")
