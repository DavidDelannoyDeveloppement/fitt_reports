from pages import (
    FrontPage,
    FittOverviewPage,
    # ClientOverviewPage,
    ClientMachinePage,
    FittMachinePage,
    IndexPage,
)
from pathlib import Path
import pandas as pd


##########################################
############## Rapport Client ############
##########################################
def generate_report_client(
    df_client: pd.DataFrame, name_client: str, len_machines: int, period_report: str
) -> None:
    report = FrontPage(df_client, name_client).format()
    # report += ClientOverviewPage(df_client).format()

    for i in range(len_machines):
        report += ClientMachinePage(df_client, name_client).format()

    report += IndexPage(df_client, name_client).format()

    Path(f"./../creations/{name_client}_reports/{name_client}.html").write_text(report)
    print(
        "# # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    )
    print(
        "# # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    )
    print(
        "# # # # # # # # #                     # # # # # # # # #"
    )
    print(
        "# # # # #                                     # # # # #"
    )
    print(
        "# #                                                 # #"
    )
    print(
        f"       Rapport {name_client} - {period_report} généré        "
    )
    print(
        "# #                                                 # #"
    )
    print(
        "# # # # #                                     # # # # #"
    )
    print(
        "# # # # # # # # #                     # # # # # # # # #"
    )
    print(
        "# # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    )
    print(
        "# # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    )
    


##########################################
############### Rapport FiTT #############
##########################################
def generate_report_fitt(
    df_fitt: pd.DataFrame, name_client: str, len_machines: int
) -> None:
    report = FrontPage(df_fitt, name_client).format()
    report += FittOverviewPage(df_fitt).format()

    for i in len_machines:
        report += FittMachinePage(df_fitt, name_client).format()

    report += IndexPage(df_fitt, name_client).format()

    Path(f"./../creations/reports_created/rapport_fitt{name_client}.md").write_text(
        report
    )
    print(
        "########################################################################################"
    )
    print(
        "#####################           Rapport FiTT seul généré           #####################"
    )
    print(
        "########################################################################################"
    )


##########################################
############# Rapport Combiné ############
##########################################
def generate_report_combined(
    df_client: pd.DataFrame, df_fitt: pd.DataFrame, name_client: str, len_machines
) -> None:
    report = FrontPage(df_client, df_fitt, name_client).format()
    # report += ClientOverviewPage(df_client).format()
    report += FittOverviewPage(df_fitt).format()

    for i in len_machines:
        report += ClientMachinePage(df_client, name_client).format()
        report += FittMachinePage(df_fitt, name_client).format()

    report += IndexPage(df_client, name_client).format()

    Path("./../creations/reports_created/rapport.md").write_text(report)
    print(
        "########################################################################################"
    )
    print(
        "#######################          Rapport Combiné généré           ######################"
    )
    print(
        "########################################################################################"
    )
