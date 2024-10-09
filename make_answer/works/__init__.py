from typing import Callable

from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.works.CHIP_CDEE import CHIP_CDEE
from make_answer.works.CHIP_CTC import CHIP_CTC
from make_answer.works.CMeEE import CmeEE
from make_answer.works.C_problem import single_c
from make_answer.works.D_problem import single_d
from make_answer.works.IMCS_V2_MRG import IMCS_V2_MRG
from make_answer.works.Med_Treat_score import med_treat
from make_answer.works.SCD import SCD
from make_answer.works.SPD import spd
from make_answer.works.TCM_CHGD_score import tcm_chgd
from make_answer.works.TCM_Clin_score import tcm_clin
from make_answer.works.TCM_DID_Dataset_score import tcm_did
from make_answer.works.TCM_DS_Dataset_score import tcm_ds
from make_answer.works.TCM_FT_score import tcm_ft
from make_answer.works.TCM_LitData_score import tcm_litdata
from make_answer.works.TCM_SRT_score import tcm_srt
from make_answer.works.TCMeEE_score import tcmeee
from make_answer.works.a_problem import single_a
from make_answer.works.b_problem import single_b

question_prompt_dict: dict[str, Callable[[dict, ChatInvoker], dict]] = {
    "A": single_a, "B": single_b, "C": single_c, "D": single_d,
    "2": tcm_ds, "3": tcm_did, "4": tcm_ft, "5": tcm_chgd, "6": med_treat,
    "7": tcm_clin, "8": tcmeee, "9": tcm_litdata, "10": tcm_srt, "11": SCD,
    "12": spd, "13": CHIP_CDEE, "14": CHIP_CTC, "15": CmeEE, "16": IMCS_V2_MRG
}