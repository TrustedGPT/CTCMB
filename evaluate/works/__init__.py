from typing import Callable

from evaluate.works.CHIP_CDEE_score import CHIP_CDEE
from evaluate.works.CHIP_CTC_score import CHIP_CTC
from evaluate.works.CMeEE_score import CmeEE
from evaluate.works.C_problem import single_c
from evaluate.works.D_problem import single_d
from evaluate.works.IMCS_V2_MRG_score import IMCS_V2_MRG
from evaluate.works.Med_Treat_score import med_treat
from evaluate.works.SCD_score import SCD_scoring
from evaluate.works.SPD_score import spd_score
from evaluate.works.TCM_CHGD_score import tcm_chgd
from evaluate.works.TCM_Clin_score import tcm_clin
from evaluate.works.TCM_DID_Dataset_score import tcm_did
from evaluate.works.TCM_DS_Dataset_score import tcm_ds
from evaluate.works.TCM_FT_score import tcm_ft
from evaluate.works.TCM_LitData_score import tcm_litdata
from evaluate.works.TCM_SRT_score import tcm_srt
from evaluate.works.TCMeEE_score import tcmeee
from evaluate.works.a_problem import single_a
from evaluate.works.b_problem import single_b

question_standard_dict: dict[str, Callable[[str, str], dict|float]] = {
    "A": single_a, "B": single_b, "C": single_c, "D": single_d,
    "2": tcm_ds, "3": tcm_did, "4": tcm_ft, "5": tcm_chgd, "6": med_treat,
    "7": tcm_clin, "8": tcmeee, "9": tcm_litdata, "10": tcm_srt, "11": SCD_scoring,
    "12": spd_score, "13": CHIP_CDEE, "14": CHIP_CTC, "15": CmeEE, "16": IMCS_V2_MRG
}