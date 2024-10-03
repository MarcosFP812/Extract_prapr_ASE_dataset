from extract import load_json_ASE, load_json_prapr, count_correct, shuffle_json

prapr_12 = "Datasets/prapr_src_patches_1.2"
prapr_20 = "Datasets/prapr_src_patches_2.0"
ASE_ICSE_C = "Datasets/ASE_Patches/Patches_ICSE/Dcorrect"
ASE_ICSE_O = "Datasets/ASE_Patches/Patches_ICSE/Doverfitting"
ASE_other_C = "Datasets/ASE_Patches/Patches_others/Dcorrect"
ASE_other_O = "Datasets/ASE_Patches/Patches_others/Doverfitting"

prapr12_json = "json/prapr12.json"
prapr20_json = "json/prapr20.json"
ASE_json = "json/ASE.json"


load_json_prapr(prapr_12, prapr12_json)
shuffle_json(prapr12_json)
print(f"PraPR1.2.: \n\tNúmero de respuestas correctas: {count_correct(prapr12_json, True)}\n\tNúmero de respuestas incorrectas: {count_correct(prapr12_json, False)}")


load_json_prapr(prapr_20, prapr20_json)
shuffle_json(prapr20_json)
print(f"PraPR2.0.: \n\tNúmero de respuestas correctas: {count_correct(prapr20_json, True)}\n\tNúmero de respuestas incorrectas: {count_correct(prapr20_json, False)}")



load_json_ASE(ASE_other_C, ASE_json, True)
load_json_ASE(ASE_other_O, ASE_json, False)
load_json_ASE(ASE_ICSE_C, ASE_json, True)
load_json_ASE(ASE_ICSE_O, ASE_json, False)
shuffle_json(ASE_json)
print(f"ASE: \n\tNúmero de respuestas correctas: {count_correct(ASE_json, True)}\n\tNúmero de respuestas incorrectas: {count_correct(ASE_json, False)}")


