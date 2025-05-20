from datetime import datetime, timedelta
import pandas as pd


def month_u1_search() -> str:
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # Sélection du fichier mois dans "resources/client" # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    ### Mode Auto :
    # today = datetime.now()
    # first_day_last_month = today.replace(day=1) - timedelta(days=1)
    # last_month_str = first_day_last_month.strftime("%B")
    # french_month = trad_fr_export(last_month_str)

    ### Mode Manuel :
    french_month = "Avril"

    ### Résultat :
    return french_month


def month_year_u1() -> str:
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # Affichage du fichier mois dans "resources/client" # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    ### Mode Auto :
    # today = datetime.now()
    # first_day_last_month = today.replace(day=1) - timedelta(days=1)
    # last_month_str = first_day_last_month.strftime("%B")
    # french_month = trad_fr_export(last_month_str)
    # date_month_year_u1 = f"{french_month} {first_day_last_month.strftime('%Y')}"

    ### Mode Manuel :
    date_month_year_u1 = f"{month_u1_search()} 2024"

    ### Résultat :
    print(f"\nMois de présentation : {date_month_year_u1}\n")
    return date_month_year_u1


# traduit les mois
def trad_fr_export(date_string: str) -> str:
    french_month = {
        "January": "Janvier",
        "February": "Février",
        "March": "Mars",
        "April": "Avril",
        "May": "Mai",
        "June": "Juin",
        "July": "Juillet",
        "August": "Août",
        "September": "Septembre",
        "October": "Octobre",
        "November": "Novembre",
        "December": "Décembre",
    }
    french_month_translation = french_month.get(date_string, date_string)
    return french_month_translation
