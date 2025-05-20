import pandas as pd
from pathlib import Path


def import_data(data_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(data_csv)
    return df


def machines_list(infos_csv: Path) -> int:
    df = pd.read_csv(infos_csv)
    len_machine = df["Nombre machines"].iloc[0]
    return len_machine


def import_graphic(name_client: str, periode_client_m: str, graphic_name: str) -> Path:
    path_verif = Path(
        f"./../resources/{name_client}/client/{periode_client_m}/graphics/{graphic_name}/Capture.png"
    )

    path = Path(
        f"../../resources/{name_client}/client/{periode_client_m}/graphics/{graphic_name}/Capture.png"
    )

    if path_verif.exists():
        return path
    else:
        print(
            "########################################################################################"
        )
        print(
            "########################################################################################"
        )
        print(
            "################                 !!! Attention !!!                       ###############"
        )
        print(
            f"################          Le graphique - {graphic_name}          ###############"
        )
        print(
            "################         n'a pas été importé ou mal orthographié         ###############"
        )
        print(
            "########################################################################################"
        )
        print(
            "########################################################################################"
        )


def import_len_circuit(data_csv: Path) -> int:
    df = pd.read_csv(data_csv)
    len_circuit = len(df["Circuit"])
    return len_circuit
