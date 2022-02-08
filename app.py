import streamlit as st
import pandas as pd
import time
st.set_page_config(page_title="Fii")
st.header('Visão Geral')


#load DF
df = pd.read_excel('excel_formatado.xlsx')
df=df.drop(columns=['Unnamed: 0'])
df = df.replace('<NA>','0', regex=True)

#st.dataframe(df)


# 'preco_atual_em_RS',
#  'liquidez_diaria',
#  'dividendo_em_RS',
#  'dividendo_yield_em_percent',
#  'dividendo_acumulado_3m_em_percent',
#  'dividendo_acumulado_6m_em_percent',
#  'dividendo_acumulado_12m_em_percent',
#  'dividendo_media_3m_em_percent',
#  'dividendo_media_6m_em_percent',
#  'dividendo_media_12m_em_percent',
#  'dividendo_ano_em_percent',
#  'variacao_preco_em_percent',
#  'rentabilidade_periodo_ultimo_mes_em_percent',
#  'rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_percent',
#  'patrimonio_liquido_em_RS',
#  'vpa_em_RS',
#  'pvpa',
#  'dividendo_patrimonial_em_percent',
#  'variacao_patrimonial_em_RS',
#  'rentabilidade_patrimonio_no_periodo_ultimo_mes_em_percent',
#  'rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_percent',
#  'vacancia_fisica_em_percent',
#  'vacancia_financeira_em_percent',
#  'quantidade_ativos,

preco_atual_em_R = df['preco_atual_em_RS'].unique().tolist()
liquidez_diaria = df['liquidez_diaria'].unique().tolist()
dividendo_em_R  = df['dividendo_em_RS'].unique().tolist()
dividendo_yield_em_  = df['dividendo_yield_em_percent'].unique().tolist()
dividendo_acumulado_3m_em_  = df['dividendo_acumulado_3m_em_percent'].unique().tolist()
dividendo_acumulado_6m_em_  = df['dividendo_acumulado_6m_em_percent'].unique().tolist()
dividendo_acumulado_12m_em_  = df['dividendo_acumulado_12m_em_percent'].unique().tolist()
dividendo_media_3m_em_  = df['dividendo_media_3m_em_percent'].unique().tolist()
dividendo_media_6m_em_  = df['dividendo_media_6m_em_percent'].unique().tolist()
dividendo_media_12m_em_  = df['dividendo_media_12m_em_percent'].unique().tolist()
dividendo_ano_em_  = df['dividendo_ano_em_percent'].unique().tolist()
variacao_preco_em_  = df['variacao_preco_em_percent'].unique().tolist()
rentabilidade_periodo_ultimo_mes_em_  = df['rentabilidade_periodo_ultimo_mes_em_percent'].unique().tolist()
rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_  = df['rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_percent'].unique().tolist()
patrimonio_liquido_em_R  = df['patrimonio_liquido_em_RS'].unique().tolist()
vpa_em_R  = df['vpa_em_RS'].unique().tolist()
pvpa = df['pvpa'].unique().tolist()
dividendo_patrimonial_em_  = df['dividendo_patrimonial_em_percent'].unique().tolist()
variacao_patrimonial_em_R  = df['variacao_patrimonial_em_RS'].unique().tolist()
rentabilidade_patrimonio_no_periodo_ultimo_mes_em_  = df['rentabilidade_patrimonio_no_periodo_ultimo_mes_em_percent'].unique().tolist()
rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_  = df['rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_percent'].unique().tolist()
vacancia_fisica_em_  = df['vacancia_fisica_em_percent'].unique().tolist()
vacancia_financeira_em_  = df['vacancia_financeira_em_percent'].unique().tolist()
quantidade_ativos  = df['quantidade_ativos,'].unique().tolist()

# select_preco_atual_em_R = st.slider('preco_atual_em_R',min_value=min(preco_atual_em_R), max_value=max(preco_atual_em_R), value=(min(preco_atual_em_R),max(preco_atual_em_R)))
# select_liquidez_diaria = st.slider('liquidez_diaria',min_value=min(liquidez_diaria), max_value=max(liquidez_diaria), value=(min(liquidez_diaria),max(liquidez_diaria)))
# select_dividendo_em_R = st.slider('dividendo_em_R',min_value=min(dividendo_em_R), max_value=max(dividendo_em_R), value=(min(dividendo_em_R),max(dividendo_em_R)))
# select_dividendo_yield_em_ = st.slider('dividendo_yield_em_',min_value=min(dividendo_yield_em_), max_value=max(dividendo_yield_em_), value=(min(dividendo_yield_em_),max(dividendo_yield_em_)))
# select_dividendo_media_12m_em_ = st.slider('dividendo_media_12m_em_',min_value=min(dividendo_media_12m_em_), max_value=max(dividendo_media_12m_em_), value=(min(dividendo_media_12m_em_),max(dividendo_media_12m_em_)))
# select_dividendo_ano_em_ = st.slider('dividendo_ano_em_',min_value=min(dividendo_ano_em_), max_value=max(dividendo_ano_em_), value=(min(dividendo_ano_em_),max(dividendo_ano_em_)))
# select_variacao_preco_em_ = st.slider('variacao_preco_em_',min_value=min(variacao_preco_em_), max_value=max(variacao_preco_em_), value=(min(variacao_preco_em_),max(variacao_preco_em_)))
# select_rentabilidade_periodo_ultimo_mes_em_ = st.slider('rentabilidade_periodo_ultimo_mes_em_',min_value=min(rentabilidade_periodo_ultimo_mes_em_), max_value=max(rentabilidade_periodo_ultimo_mes_em_), value=(min(rentabilidade_periodo_ultimo_mes_em_),max(rentabilidade_periodo_ultimo_mes_em_)))

#select_dividendo_acumulado_3m_em_ = st.slider('dividendo_acumulado_3m_em_',min_value=min(dividendo_acumulado_3m_em_), max_value=max(dividendo_acumulado_3m_em_), value=(min(dividendo_acumulado_3m_em_),max(dividendo_acumulado_3m_em_)))
#select_dividendo_acumulado_6m_em_ = st.slider('dividendo_acumulado_6m_em_',min_value=min(dividendo_acumulado_6m_em_), max_value=max(dividendo_acumulado_6m_em_), value=(min(dividendo_acumulado_6m_em_),max(dividendo_acumulado_6m_em_)))
#select_dividendo_acumulado_12m_em_ = st.slider('dividendo_acumulado_12m_em_',min_value=min(dividendo_acumulado_12m_em_), max_value=max(dividendo_acumulado_12m_em_), value=(min(dividendo_acumulado_12m_em_),max(dividendo_acumulado_12m_em_)))
#select_dividendo_media_3m_em_ = st.slider('dividendo_media_3m_em_',min_value=min(dividendo_media_3m_em_), max_value=max(dividendo_media_3m_em_), value=(min(dividendo_media_3m_em_),max(dividendo_media_3m_em_)))
#select_dividendo_media_6m_em_ = st.slider('dividendo_media_6m_em_',min_value=min(dividendo_media_6m_em_), max_value=max(dividendo_media_6m_em_), value=(min(dividendo_media_6m_em_),max(dividendo_media_6m_em_)))
#select_rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_ = st.slider('rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_',min_value=min(rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_), max_value=max(rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_), value=(min(rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_),max(rentabilidade_acumulada_inicio_ano_ate_ultimo_mes_em_)))
#select_patrimonio_liquido_em_R = st.slider('patrimonio_liquido_em_R',min_value=min(patrimonio_liquido_em_R), max_value=max(patrimonio_liquido_em_R), value=(min(patrimonio_liquido_em_R),max(patrimonio_liquido_em_R)))

# select_vpa_em_R = st.slider('vpa_em_R',min_value=min(vpa_em_R), max_value=max(vpa_em_R), value=(min(vpa_em_R),max(vpa_em_R)))
# select_pvpa = st.slider('pvpa',min_value=min(pvpa), max_value=max(pvpa), value=(min(pvpa),max(pvpa)))
# select_dividendo_patrimonial_em_ = st.slider('dividendo_patrimonial_em_',min_value=min(dividendo_patrimonial_em_), max_value=max(dividendo_patrimonial_em_), value=(min(dividendo_patrimonial_em_),max(dividendo_patrimonial_em_)))
# select_variacao_patrimonial_em_R = st.slider('variacao_patrimonial_em_R',min_value=min(variacao_patrimonial_em_R), max_value=max(variacao_patrimonial_em_R), value=(min(variacao_patrimonial_em_R),max(variacao_patrimonial_em_R)))
# select_rentabilidade_patrimonio_no_periodo_ultimo_mes_em_ = st.slider('rentabilidade_patrimonio_no_periodo_ultimo_mes_em_',min_value=min(rentabilidade_patrimonio_no_periodo_ultimo_mes_em_), max_value=max(rentabilidade_patrimonio_no_periodo_ultimo_mes_em_), value=(min(rentabilidade_patrimonio_no_periodo_ultimo_mes_em_),max(rentabilidade_patrimonio_no_periodo_ultimo_mes_em_)))
# select_rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_ = st.slider('rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_',min_value=min(rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_), max_value=max(rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_), value=(min(rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_),max(rentabilidade_patrimonio_acumulada_inicio_ano_ate_ultimo_mes_em_)))
# select_vacancia_fisica_em_ = st.slider('vacancia_fisica_em_',min_value=min(vacancia_fisica_em_), max_value=max(vacancia_fisica_em_), value=(min(vacancia_fisica_em_),max(vacancia_fisica_em_)))
# select_vacancia_financeira_em_ = st.slider('vacancia_financeira_em_',min_value=min(vacancia_financeira_em_), max_value=max(vacancia_financeira_em_), value=(min(vacancia_financeira_em_),max(vacancia_financeira_em_)))
# select_quantidade_ativos = st.slider('quantidade_ativos',min_value=min(quantidade_ativos), max_value=max(quantidade_ativos), value=(min(quantidade_ativos),max(quantidade_ativos)))


st.sidebar.header('Filtros')

# select_cod_fundo = st.sidebar.multiselect(
#     'Selectione um Fundo específico',
#     options=df['cod_fundo'].unique(),
    
# )
select_setor = st.sidebar.multiselect(
    'Selectione o Filtro',
    options=df['setor'].unique(),
    
)

select_preco_atual_em_R = st.sidebar.slider(
    'Preço',
    min_value=min(preco_atual_em_R),
    max_value=max(preco_atual_em_R),
    value=(min(preco_atual_em_R),max(preco_atual_em_R))
)
select_liquidez_diaria = st.sidebar.slider(
    'Liquidez diária',
    min_value=min(liquidez_diaria),
    max_value= max(liquidez_diaria),#max(liquidez_diaria),
    value=(min(liquidez_diaria),max(liquidez_diaria))
)
select_dividendo_em_R = st.sidebar.slider(
    'Dividendo em R$',
    min_value=min(dividendo_em_R),
    max_value=max(dividendo_em_R),#max(liquidez_diaria),
    value=(min(dividendo_em_R),max(dividendo_em_R))
)
select_dividendo_yield_em_ = st.sidebar.slider(
    'Dividendo em %',
    min_value=min(dividendo_yield_em_),
    max_value=max(dividendo_yield_em_),#max(liquidez_diaria),
    value=(min(dividendo_yield_em_),max(dividendo_yield_em_))
)
select_dividendo_ano_em_ = st.sidebar.slider(
    'Dividendo no Ano',
    min_value=min(dividendo_ano_em_),
    max_value=max(dividendo_ano_em_),
    value=(min(dividendo_ano_em_),max(dividendo_ano_em_))
)
# select_vpa_em_R = st.sidebar.slider(
#     'VPA em R$',
#     min_value=min(vpa_em_R),
#     max_value=max(vpa_em_R),
#     value=(min(vpa_em_R),max(vpa_em_R))
# )
select_pvpa = st.sidebar.slider(
    'p/vpa',
    min_value=min(pvpa),
    max_value=max(pvpa),
    value=(min(pvpa),max(pvpa))
)
print('--------')
print(select_pvpa)
print('-----Aqui----')
if len(select_setor) == 0:
    select_setor = ['URPR11']
print(len(select_setor))
print(select_setor)
#print(preco_atual_em_R[1])
#print(preco_atual_em_R(1))


#df = df[df['cod_fundo'].isin(select_cod_fundo)]

df_selection = df.query(
    """
        setor==@select_setor
    """
)


df_selection2= df_selection.where(
    
    (df_selection['preco_atual_em_RS']>=select_preco_atual_em_R[0]) & (df_selection['preco_atual_em_RS']<=select_preco_atual_em_R[1]) &
    (df_selection['dividendo_em_RS'] >= select_dividendo_em_R[0]) & (df_selection['dividendo_em_RS'] <= select_dividendo_em_R[1]) &
    (df_selection['dividendo_yield_em_percent']>=select_dividendo_yield_em_[0]) & (df_selection['dividendo_yield_em_percent']<=select_dividendo_yield_em_[1]) &
    (df_selection['dividendo_ano_em_percent']>=select_dividendo_ano_em_[0]) & (df_selection['dividendo_ano_em_percent']<=select_dividendo_ano_em_[1]) &
    #(df_selection['vpa_em_RS']>=vpa_em_R[0]) & (df_selection['vpa_em_RS']<=vpa_em_R[1])
    (df_selection['pvpa']>=select_pvpa[0]) & (df_selection['pvpa']<=select_pvpa[1])
                                       
                                    )

                        



st.header(len(df_selection2.dropna()))
st.dataframe(df_selection2.dropna())
