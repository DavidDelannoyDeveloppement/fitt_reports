from pathlib import Path
from abc import ABC, abstractmethod
from data.sorting import month_u1_search, month_year_u1
from data.display import (
    display_conso_reelle,
    display_conso_reelle_elec,
    display_conso_reelle_gaz,
    display_modele_predictif,
    display_modele_predictif_elec,
    display_modele_predictif_gaz,
    display_performance_contrat_kwh,
    display_performance_contrat_kwh_elec,
    display_performance_contrat_kwh_gaz,
    display_performance_contrat_percent_elec,
    display_performance_contrat_percent_gaz,
    display_performance_contrat_percent,
    display_name_machine,
    display_gain_perte,
    display_gain_perte_elec,
    display_gain_perte_gaz,
    display_conso_reelle_year,
    display_conso_reelle_year_elec,
    display_conso_reelle_year_gaz,
    display_modele_predictif_year,
    display_modele_predictif_year_elec,
    display_modele_predictif_year_gaz,
    display_performance_contrat_kwh_year,
    display_performance_contrat_kwh_year_elec,
    display_performance_contrat_kwh_year_gaz,
    display_performance_contrat_percent_year,
    display_performance_contrat_percent_year_elec,
    display_performance_contrat_percent_year_gaz,
    display_gain_perte_year,
    display_gain_perte_year_elec,
    display_gain_perte_year_gaz,
    display_circuit,
    display_temps_fonctionnement,
    display_nombre_demarrage,
    display_ratio_demarrage,
    display_puissances_moyennes_fonctionnement_chaud,
    display_puissances_moyennes_fonctionnement_froid,
    display_puissance_electrique_machine,
    display_eco_surconso,
    display_eco_surconso_elec,
    display_eco_surconso_gaz,
    display_eco_surconso_year,
    display_eco_surconso_year_elec,
    display_eco_surconso_year_gaz,
    display_engagement_contract,
    display_engagement_contract_elec,
    display_engagement_contract_gaz,
    display_conforme,
    display_conforme_elec,
    display_conforme_gaz,
    display_conforme_year,
    display_conforme_year_elec,
    display_conforme_year_gaz,
    display_conforme_color, 
    display_conforme_color_elec, 
    display_conforme_color_gaz, 
    display_conforme_color_year,
    display_conforme_color_year_elec,
    display_conforme_color_year_gaz
)
from data.exports import arrow_display_month, arrow_display_year, valid_ratio, valid_ratio_min, valid_ratio_alvend, valid_ratio_thelia
from data.imports import import_graphic, import_len_circuit


class Page(ABC):
    def __init__(self, df) -> None:
        self._df = df
        self._periode_client_m_y = month_year_u1()
        self._periode_client_m = month_u1_search()
        self._periode_client_y = self._periode_client_m_y[-4:]

    # path_graphics_client = Path(f"./../resources/{name_client}/client/{month_client}/graphics/")
    # path_graphics_fitt = Path(f"./../resources/{name_client}/fitt/{month_client}/graphics/")

    @property
    def template(self) -> str:
        return Path(self.template_file).read_text()

    @abstractmethod
    def get_params(self) -> dict:
        params = {}
        return params

    def format(self) -> str:
        params = self.get_params()
        return self.template.format(**params)


class FrontPage(Page):
    # template_file = "templates/template_presentation.md"

    def __init__(self, df, name_client) -> None:
        super().__init__(df)
        self._name_client = name_client
        self.template_file = f"templates/{name_client}/template_presentation.html"
        # self._path_logo_client = Path(f"./../resources/{name_client}/logo/{name_client}.png")

    def get_params(self) -> dict:
        params = {}
        # params["logo_client"] = Path(f"./../resources/{self._name_client}/logo/{self._name_client}.png")
        params["logo_client"] = Path(
            f"./../../resources/{self._name_client}/logo/{self._name_client}.png"
        )
        params["logo_thelia"] = Path(
            f"./../../resources/{self._name_client}/logo/thelia.png"
        )
        params["nom_machine"] = display_name_machine(self._df)
        params["periode_client"] = self._periode_client_m_y
        params["name_client"] = self._name_client
        return params


class ClientMachinePage(Page):
    def __init__(self, df, name_client) -> None:
        super().__init__(df)
        self._name_client = name_client
        self.template_file = f"templates/{name_client}/template_client_machine.html"

    def get_params(self) -> str:
        params = {}
        params["nom_machine"] = display_name_machine(self._df)
        params["name_client"] = self._name_client
        params["periode_client"] = self._periode_client_m_y

        ########################################################################
        ########################      CPE MENSUEL      #########################
        ########################################################################
        params["consommation_reelle"] = display_conso_reelle(self._df)
        params["modele_predictif"] = display_modele_predictif(self._df)
        params["performance_contrat_kwh"] = display_performance_contrat_kwh(self._df)
        params["gain_perte"] = display_gain_perte(self._df)
        params["performance_contrat_percent"] = display_performance_contrat_percent(
            self._df
        )
        params["arrow_month"] = arrow_display_month(self._df, self._name_client)
        params["engagement_contract"] = display_engagement_contract(self._df)
        params["conforme"] = display_conforme(self._df)
        params["conforme_color"] = display_conforme_color(self._df)
        params["superposition_predictif_reelle"] = import_graphic(
            self._name_client,
            self._periode_client_m,
            "1-superposition_predictif_reelle",
        )
        params["eco_surconso"] = display_eco_surconso(self._df)

        ########################################################################
        ########################        CPE ANNUEL       #######################
        ########################################################################
        params["periode_client_year"] = self._periode_client_y
        params["consommation_reelle_year"] = display_conso_reelle_year(self._df)
        params["modele_predictif_year"] = display_modele_predictif_year(self._df)
        params["performance_contrat_kwh_year"] = display_performance_contrat_kwh_year(self._df)
        params["performance_contrat_percent_year"] = display_performance_contrat_percent_year(self._df)
        params["gain_perte_year"] = display_gain_perte_year(self._df)
        params["arrow_year"] = arrow_display_year(self._df, self._name_client)
        params["engagement_contract"] = display_engagement_contract(self._df)
        params["conforme_year"] = display_conforme_year(self._df)
        params["conforme_color_year"] = display_conforme_color_year(self._df)
        params["superposition_predictif_reelle_year"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year",)
        params["eco_surconso_year"] = display_eco_surconso_year(self._df)

        # Page Index

        ########################################################################
        #########################      Maquette     ##############################
        ########################################################################
        if self._name_client == "maquette":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        #####################      Maquette FiTT     ###########################
        ########################################################################
        if self._name_client == "maquette_fitt":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )




        ########################################################################
        ####################      ALVEND Stockage     ##########################
        ########################################################################
        elif self._name_client == "alvend_stockage":
            params["temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures"
            )
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "4-mode_fonctionnement"
            )
            params["taux_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "5-taux_compression_3_circuits"
            )
            params["sante_circuit_1"] = import_graphic(
                self._name_client, self._periode_client_m, "6-sante_circuit_1"
            )
            params["sante_circuit_2"] = import_graphic(
                self._name_client, self._periode_client_m, "7-sante_circuit_2"
            )
            params["sante_circuit_3"] = import_graphic(
                self._name_client, self._periode_client_m, "8-sante_circuit_3"
            )
            params["intensite_compresseurs"] = import_graphic(
                self._name_client, self._periode_client_m, "9-intensite_compresseurs"
            )

            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/10-demarrage_temps_circuit/demarrage_temps_circuit.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_{i}"] = valid_ratio_alvend(
                    path_data_temps_fonctionnement, index, self._name_client
                )

            params["optimisation_energetique"] = import_graphic(
                self._name_client, self._periode_client_m, "11-optimisation_energetique"
            )
            params["cop_3_circuits"] = import_graphic(
                self._name_client, self._periode_client_m, "12-cop_3_circuits"
            )
            params["eer_3_circuits"] = import_graphic(
                self._name_client, self._periode_client_m, "13-eer_3_circuits"
            )
            params["rendement_compresseur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-rendement_compresseur"
            )
            params["cop_eer_moyens"] = import_graphic(
                self._name_client, self._periode_client_m, "15-cop_eer_moyens"
            )
            # params["puissance_machine_a"] = import_graphic(self._name_client, self._periode_client_m, "puissance_machine_a")
            # params["puissance_machine_b"] = import_graphic(self._name_client, self._periode_client_m, "puissance_machine_b")
            # params["puissance_machine_c"] = import_graphic(self._name_client, self._periode_client_m, "puissance_machine_c")
            # params["puissance_electrique_consommee"] = import_graphic(self._name_client, self._periode_client_m, "puissance_electrique_consommee")

            path_data_puissances_moyennes_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/16-puissances_moyennes_fonctionnment_circuit/par_circuit.csv"
            )
            path_data_puissance_electrique_machine = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/16-puissances_moyennes_fonctionnment_circuit/puissance_electrique_machine.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Puissance_froid_{i}"
                ] = display_puissances_moyennes_fonctionnement_froid(
                    path_data_puissances_moyennes_fonctionnement, index
                )
                params[
                    f"Puissance_chaud_{i}"
                ] = display_puissances_moyennes_fonctionnement_chaud(
                    path_data_puissances_moyennes_fonctionnement, index
                )
            params[
                "puissance_electrique_machine"
            ] = display_puissance_electrique_machine(
                path_data_puissance_electrique_machine
            )

        ########################################################################
        #################      ALVEND conditionnement     ######################
        ########################################################################
        elif self._name_client == "alvend_conditionnement":
            params["temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures"
            )
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "4-mode_fonctionnement"
            )
            params["taux_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "5-taux_compression_4_circuits"
            )
            params["sante_circuit_1"] = import_graphic(
                self._name_client, self._periode_client_m, "6-sante_circuit_1"
            )
            params["sante_circuit_2"] = import_graphic(
                self._name_client, self._periode_client_m, "7-sante_circuit_2"
            )
            params["sante_circuit_3"] = import_graphic(
                self._name_client, self._periode_client_m, "8-sante_circuit_3"
            )
            params["sante_circuit_4"] = import_graphic(
                self._name_client, self._periode_client_m, "9-sante_circuit_4"
            )
            params["intensite_compresseurs"] = import_graphic(
                self._name_client, self._periode_client_m, "10-intensite_compresseurs"
            )

            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/11-demarrage_temps_circuit/demarrage_temps_circuit.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_{i}"] = valid_ratio_alvend(
                    path_data_temps_fonctionnement, index, self._name_client
                )

            params["optimisation_energetique"] = import_graphic(
                self._name_client, self._periode_client_m, "12-optimisation_energetique"
            )
            params["cop_4_circuits"] = import_graphic(
                self._name_client, self._periode_client_m, "13-cop_4_circuits"
            )
            params["eer_4_circuits"] = import_graphic(
                self._name_client, self._periode_client_m, "14-eer_4_circuits"
            )
            params["rendement_compresseur"] = import_graphic(
                self._name_client, self._periode_client_m, "15-rendement_compresseur"
            )
            params["cop_eer_moyens"] = import_graphic(
                self._name_client, self._periode_client_m, "16-cop_eer_moyens"
            )
            # params["puissance_machine_a"] = import_graphic(self._name_client, self._periode_client_m, "puissance_machine_a")
            # params["puissance_machine_b"] = import_graphic(self._name_client, self._periode_client_m, "puissance_machine_b")
            # params["puissance_machine_c"] = import_graphic(self._name_client, self._periode_client_m, "puissance_machine_c")
            # params["puissance_electrique_consommee"] = import_graphic(self._name_client, self._periode_client_m, "puissance_electrique_consommee")

            path_data_puissances_moyennes_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/17-puissances_moyennes_fonctionnment_circuit/par_circuit.csv"
            )
            path_data_puissance_electrique_machine = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/17-puissances_moyennes_fonctionnment_circuit/puissance_electrique_machine.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Puissance_froid_{i}"
                ] = display_puissances_moyennes_fonctionnement_froid(
                    path_data_puissances_moyennes_fonctionnement, index
                )
                params[
                    f"Puissance_chaud_{i}"
                ] = display_puissances_moyennes_fonctionnement_chaud(
                    path_data_puissances_moyennes_fonctionnement, index
                )
            params[
                "puissance_electrique_machine"
            ] = display_puissance_electrique_machine(
                path_data_puissance_electrique_machine
            )


        ########################################################################
        ##################    ITM_Gouvieux "Ancien"  ###########################
        ########################################################################
        elif self._name_client == "ITM_Gouvieux_ancien":
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process"
            )
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation"
            )
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement"
            )
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression"
            )
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            # params["Rendement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "12-Rendement"
            # )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ##################       ITM_Gouvieux "Séparé"      ####################
        ########################################################################
        elif self._name_client == "ITM_Gouvieux":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ################      ITM_Doullens "Ancien"     #######################
        ########################################################################
        elif self._name_client == "ITM_Doullens_ancien":
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process"
            )
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation"
            )
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement"
            )
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression"
            )
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["Rendement"] = import_graphic(
                self._name_client, self._periode_client_m, "12-Rendement"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ##################       ITM_Doullens "Séparé"      ####################
        ########################################################################
        elif self._name_client == "ITM_Doullens":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ###############     ITM_Pont_à_Marcq "Ancien"      #####################
        ########################################################################
        elif self._name_client == "ITM_Pont_à_Marcq_ancien":
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process"
            )
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation"
            )
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement"
            )
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression"
            )
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["Rendement"] = import_graphic(
                self._name_client, self._periode_client_m, "12-Rendement"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ##############       ITM_Pont_à_Marcq "Séparé"      ####################
        ########################################################################
        elif self._name_client == "ITM_Pont_à_Marcq":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            # params["Rendement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "12-Rendement"
            # )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ##################      ITM_Lambersart "Séparé"     ####################
        ########################################################################
        elif self._name_client == "ITM_Lambersart":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        #################      ITM_Le_Quesnoy "Ancien"     #####################
        ########################################################################
        elif self._name_client == "ITM_Le_Quesnoy_ancien":
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process"
            )
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation"
            )
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement"
            )
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression"
            )
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["Rendement"] = import_graphic(
                self._name_client, self._periode_client_m, "12-Rendement"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        ##################       ITM_Le Quesnoy "Séparé"      ##################
        ########################################################################
        elif self._name_client == "ITM_Le_Quesnoy":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            # params["conforme_color"] = display_conforme_color(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )


        ########################################################################
        #####################    Leclerc_Noeux_les_Mines    ####################
        ########################################################################
        elif self._name_client == "Leclerc_Noeux_les_Mines":
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process"
            )
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation"
            )
            params["mode_fonctionnement_CO2"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement_CO2"
            )
            params["taux_de_compression_CO2"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression_CO2"
            )
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur_CO2/demarrage_temps_compresseur_CO2.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures_CO2"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures_CO2"
            )


            params["mode_fonctionnement_RoofTop"] = import_graphic(
                self._name_client, self._periode_client_m, "10-mode_fonctionnement_RoofTop"
            )
            params["taux_de_compression_RoofTop"] = import_graphic(
                self._name_client, self._periode_client_m, "11-taux_de_compression_RoofTop"
            )
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "12-sous_refroidissement_RoofTop"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/13-demarrage_temps_compresseur_RoofTop/demarrage_temps_compresseur_RoofTop.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures_RoofTop"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures_CO2"
            )






            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "14-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "15-EER"
            )
            params["Rendement"] = import_graphic(
                self._name_client, self._periode_client_m, "16-Rendement"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "17-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "18-puissances_recup_chaleur"
            )


        ########################################################################
        ##################          Quercy_Guilmot          ####################
        ########################################################################
        elif self._name_client == "Quercy_Guilmot":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["Rendement"] = import_graphic(
                self._name_client, self._periode_client_m, "12-Rendement"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )

        

        ########################################################################
        ##################      ITM_Montigny "Séparé"     ####################
        ########################################################################
        elif self._name_client == "ITM_Montigny":


            ############   CPE MENSUEL / ANNUEL - ÉLEC / GAZ   #################
            params["eco_surconso_elec"] = display_eco_surconso_elec(self._df)
            params["eco_surconso_gaz"] = display_eco_surconso_gaz(self._df)
            params["consommation_reelle_elec"] = display_conso_reelle_elec(self._df)
            params["consommation_reelle_gaz"] = display_conso_reelle_gaz(self._df)
            params["modele_predictif_elec"] = display_modele_predictif_elec(self._df)
            params["modele_predictif_gaz"] = display_modele_predictif_gaz(self._df)
            params["performance_contrat_kwh_elec"] = display_performance_contrat_kwh_elec(self._df)
            params["performance_contrat_kwh_gaz"] = display_performance_contrat_kwh_gaz(self._df)
            params["performance_contrat_percent_elec"] = display_performance_contrat_percent_elec(self._df)
            params["performance_contrat_percent_gaz"] = display_performance_contrat_percent_gaz(self._df)
            params["engagement_contract_elec"] = display_engagement_contract_elec(self._df)
            params["engagement_contract_gaz"] = display_engagement_contract_gaz(self._df)
            params["conforme_elec"] = display_conforme_elec(self._df)
            params["conforme_color_elec"] = display_conforme_color_elec(self._df)
            params["conforme_color_gaz"] = display_conforme_color_gaz(self._df)
            params["conforme_gaz"] = display_conforme_gaz(self._df)
            params["gain_perte_elec"] = display_gain_perte_elec(self._df)
            params["gain_perte_gaz"] = display_gain_perte_gaz(self._df)

            params["superposition_predictif_reelle_elec"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_elec",)
            params["superposition_predictif_reelle_gaz"] = import_graphic(self._name_client,self._periode_client_m,"1-superposition_predictif_reelle_gaz",)
            params["superposition_predictif_reelle_year_elec"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_elec",)
            params["superposition_predictif_reelle_year_gaz"] = import_graphic(self._name_client,self._periode_client_m,"2-superposition_predictif_reelle_year_gaz",)

            params["consommation_reelle_year_elec"] = display_conso_reelle_year_elec(self._df)
            params["consommation_reelle_year_gaz"] = display_conso_reelle_year_gaz(self._df)
            params["modele_predictif_year_elec"] = display_modele_predictif_year_elec(self._df)
            params["modele_predictif_year_gaz"] = display_modele_predictif_year_gaz(self._df)
            params["performance_contrat_kwh_year_elec"] = display_performance_contrat_kwh_year_elec(self._df)
            params["performance_contrat_kwh_year_gaz"] = display_performance_contrat_kwh_year_gaz(self._df)
            params["performance_contrat_percent_year_elec"] = display_performance_contrat_percent_year_elec(self._df)
            params["performance_contrat_percent_year_gaz"] = display_performance_contrat_percent_year_gaz(self._df)
            params["gain_perte_year_elec"] = display_gain_perte_year_elec(self._df)
            params["gain_perte_year_gaz"] = display_gain_perte_year_gaz(self._df)
            params["conforme_year_elec"] = display_conforme_year_elec(self._df)
            params["conforme_year_gaz"] = display_conforme_year_gaz(self._df)
            params["conforme_color_year_elec"] = display_conforme_color_year_elec(self._df)
            params["conforme_color_year_gaz"] = display_conforme_color_year_gaz(self._df)
            params["eco_surconso_year_elec"] = display_eco_surconso_year_elec(self._df)
            params["eco_surconso_year_gaz"] = display_eco_surconso_year_gaz(self._df)


            ##########   ANALYSE OPÉRATIONNELLE & PERFORMANCES   ###############
            params["temperatures_process"] = import_graphic(
                self._name_client, self._periode_client_m, "3-temperatures_process")
            params["temperatures_opt"] = import_graphic(
                self._name_client, self._periode_client_m, "4-temperatures_optimisation")
            params["mode_fonctionnement"] = import_graphic(
                self._name_client, self._periode_client_m, "5-mode_fonctionnement")
            params["taux_de_compression"] = import_graphic(
                self._name_client, self._periode_client_m, "6-taux_de_compression")
            # params["sous_refroidissement"] = import_graphic(
            #     self._name_client, self._periode_client_m, "7-sous_refroidissement"
            # )
            path_data_temps_fonctionnement = Path(
                f"./../resources/{self._name_client}/client/{self._periode_client_m}/graphics/8-demarrage_temps_compresseur/demarrage_temps_compresseur.csv"
            )
            len_circuit = import_len_circuit(path_data_temps_fonctionnement)
            for i in range(len_circuit):
                index = i
                params[
                    f"Circuit_{i}"
                ] = display_circuit(path_data_temps_fonctionnement, index)
                params[
                    f"Temps_de_fonctionnement_total_{i}"
                ] = display_temps_fonctionnement(path_data_temps_fonctionnement, index)
                params[f"Nombre_de_démarrage_{i}"] = display_nombre_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"Ratio_démarrages_par_heure_{i}"] = display_ratio_demarrage(
                    path_data_temps_fonctionnement, index
                )
                params[f"valid_ratio_min_{i}"] = valid_ratio_thelia(
                    path_data_temps_fonctionnement, index, self._name_client
                )
            params["delta_temperatures"] = import_graphic(
                self._name_client, self._periode_client_m, "9-delta_temperatures"
            )
            params["COP"] = import_graphic(
                self._name_client, self._periode_client_m, "10-COP"
            )
            params["EER"] = import_graphic(
                self._name_client, self._periode_client_m, "11-EER"
            )
            params["Rendement"] = import_graphic(
                self._name_client, self._periode_client_m, "12-Rendement"
            )
            params["taux_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "13-taux_recup_chaleur"
            )
            params["puissances_recup_chaleur"] = import_graphic(
                self._name_client, self._periode_client_m, "14-puissances_recup_chaleur"
            )




        ###################################
        #########      ......      ########
        ###################################
        # elif

        else:
            raise "Client inconnu"
        return params


class FittOverviewPage(Page):
    template_file = "templates/template_fitt.md"

    def __init__(self, df) -> None:
        super().__init__(df)

    def get_params(self) -> str:
        params = {}
        params["presentation"] = ""
        return params


class FittMachinePage(Page):
    template_file = "templates/template_fitt_machine.md"

    def __init__(self, df, name_machine) -> None:
        super().__init__(df)
        self._name_machine = name_machine

    def get_params(self) -> str:
        params = {}
        params["periode_debut_fitt"] = self._df.index[-7].strftime("%d-%m-%Y")
        params["periode_fin_fitt"] = self._df.index[-1].strftime("%d-%m-%Y")
        params["nom_machine"] = self._name_machine
        params["consommation_reelle_week"] = sum_week_consommation(
            self._df, self._consommation_machine_name_column, self._name_machine
        )
        params["modele_predictif_week"] = sum_week_prediction(
            self._df, self._prediction_machine_name_column, self._name_machine
        )
        params["performance_contrat_kwh_week"] = contract_performance_kwh_week(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["performance_contrat_%_week"] = contract_performance_percent_week(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["arrow_week"] = arrow_display_week(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["superposition_predictif_reelle_week"] = superposition_week(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["periode_debut_fitt_week_u4"] = self._df.index[0].strftime("%d-%m-%Y")
        params["consommation_reelle_week_u4"] = sum_week_u4_consommation(
            self._df, self._consommation_machine_name_column, self._name_machine
        )
        params["modele_predictif_week_u4"] = sum_week_u4_prediction(
            self._df, self._prediction_machine_name_column, self._name_machine
        )
        params["performance_contrat_kwh_week_u4"] = contract_performance_kwh_week_u4(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["performance_contrat_%_week_u4"] = contract_performance_percent_week_u4(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["arrow_week_u4"] = arrow_display_week_u4(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        params["superposition_predictif_reelle_week_u4"] = superposition_week_u4(
            self._df,
            self._consommation_machine_name_column,
            self._prediction_machine_name_column,
            self._name_machine,
        )
        return params


class IndexPage(Page):
    def __init__(self, df, name_client) -> None:
        super().__init__(df)
        self._name_client = name_client
        self.template_file = f"templates/{name_client}/template_index.html"

    def get_params(self) -> str:
        params = {}
        params["nom_machine"] = display_name_machine(self._df)
        params["name_client"] = self._name_client
        params["periode_client"] = self._periode_client_m_y
        return params
