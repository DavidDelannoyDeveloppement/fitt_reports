import typer
from pathlib import Path
from data.sorting import month_u1_search, month_year_u1
from data.imports import import_data, machines_list
from report import (
    generate_report_client,
    generate_report_fitt,
    generate_report_combined,
)


def main(name_client: str, report_type: str):
    # recherche le mois précédent pour rapport client
    month_client = month_u1_search()
    month_client_name = month_year_u1()
    # chemins permettant d'aller chercher les infos du mois
    path_data_client = Path(
        f"./../resources/{name_client}/client/{month_client}/data_cpe.csv"
    )
    path_data_fitt = Path(f"./../resources/{name_client}/fitt/{month_client}/data.csv")
    path_infos_client = Path(f"./../resources/{name_client}/infos.csv")
    # path_logo_client = Path(f"./../resources/{name_client}/logo/")
    # path_graphics_client = Path(
    #     f"./../resources/{name_client}/client/{month_client}/graphics/"
    # )
    # path_graphics_fitt = Path(
    #     f"./../resources/{name_client}/fitt/{month_client}/graphics/"
    # )

    if report_type == "client":
        df_client = import_data(path_data_client)
        len_machines = machines_list(path_infos_client)
        generate_report_client(df_client, name_client, len_machines, month_client_name)

    elif report_type == "fitt":
        df_fitt = import_data(path_data_fitt)
        len_machines = machines_list(path_infos_client)
        generate_report_fitt(df_fitt, name_client, len_machines)

    elif report_type == "combined":
        df_client = import_data(path_data_client)
        df_fitt = import_data(path_data_fitt)
        len_machines = machines_list(path_infos_client)
        generate_report_combined(df_client, df_fitt, name_client, len_machines)

    else:
        print("Erreur de saisie")

    # choix type rapport : client ou fitt
    # nom du client → accès au répertoire d'image du client
    # avec le today → donne les dates en rapport pour client et fitt et donne accès au bon mois client pour éviter les erreurs.

    #  typer = poetry run python3 -m main nom_du_client type_de_rapport
    # → débloque accès répertoire resources/nom_du_client/logo...... et le today crée le fichier client_mois.html
    # possibilité de vérifier les dates éditées et les dates copiées/collées
    return


if __name__ == "__main__":
    typer.run(main)
