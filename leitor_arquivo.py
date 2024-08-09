import pandas as pd
criac_emp=pd.read_excel('dados_dashboard.xlsx', sheet_name="Criacao_Empreg__Formais_MA", skiprows=1)
inf_mens=pd.read_excel('dados_dashboard.xlsx', sheet_name="Inflação_Mensal_Slz", skiprows=1)
rend_hab=pd.read_excel('dados_dashboard.xlsx', sheet_name="Rend_hab_medio_MA", skiprows=2)
desoc=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desocupacao_Tx_Comb__MA", skiprows=2)
desig=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desigualdade")

print(criac_emp)
#print(inf_mens)
#print(rend_hab)
#print(desoc)
#print(desig)
