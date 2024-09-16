import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



st.set_page_config(
        
	layout = 'wide',
        
	initial_sidebar_state = 'collapsed' 
)
im1,im2,im3,im4,im5, im6, im7, im8, im9=st.columns(9)


#with im4:
#	st.image("gape.png", width=400)

st.markdown("""
  <style>

	.stTabs {
	        font-family: Candara;
	    }
	 .stApp div.stTab  {
  		font-family:Candara}
        white-space: pre-wrap;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
  		font-family:Candara
  		
    }

	

</style>""",
    unsafe_allow_html=True
)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inflação","Emprego", "Renda", "Desigualdade", "• Dados de Referência"])

#tab1.subheader("Inflação")
#tab2.subheader("Emprego")
#tab3.subheader("Renda")
#tab4.subheader("Desigualdade")

criac_emp=pd.read_excel('dados_dashboard.xlsx', sheet_name="Criacao_Empreg__Formais_MA", skiprows=1)
inf_mens=pd.read_excel('dados_dashboard.xlsx', sheet_name="Inflação_Mensal_Slz", skiprows=1)
rend_hab=pd.read_excel('dados_dashboard.xlsx', sheet_name="Rend_hab_medio_MA", skiprows=2)
desoc=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desocupacao_Tx_Comb__MA", skiprows=1)
desig=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desigualdade")
rend_e_des=pd.read_excel('dados_dashboard.xlsx', sheet_name="Renda e Des")

def add_hline_with_annotation(fig, y_value, text, line_color='red', line_dash='dash', line_width=2,
                              annotation_position='top' , pos=0):
    """
    Adiciona uma linha horizontal com uma anotação acima dela em um gráfico Plotly.

    Args:
        fig: Objeto Figure do Plotly.
        y_value: Valor y da linha horizontal.
        text: Texto da anotação.
        line_color: Cor da linha (default: 'red').
        line_dash: Estilo da linha (default: 'dash').
        line_width: Espessura da linha (default: 2).
        annotation_position: Posição da anotação ('top' ou 'bottom').

    Returns:
        O objeto Figure com a linha horizontal e a anotação adicionadas.
    """

    fig.add_hline(y=y_value, line_color=line_color, line_dash=line_dash, line_width=line_width)

    fig.add_annotation(
        x=0.0,  # Centralizado no eixo x
        y=y_value+pos,
        xref="paper",
        yref="y",
        text=text,
        showarrow=False,
        font=dict(size=10, color="black")
    )

    return fig

with tab1:
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	 <br>&emsp;&emsp;Os indicadores sobre inflação, medidos pelo <b>IPCA (Índice de Preços ao Consumidor Amplo)</b> são, de maneira geral, uma aproximação ao custo de vida em São Luís. Além desse indicador tradicional, apurado pelo IBGE, calculamos o impacto dos principais grupos de despesas das famílias sobre a inflação mensal. Dessa forma, é possível apurar e acompanhar como as despesas com habitação, transporte, alimentação e cuidados pessoais afetam o nível agregado de preços na nossa cidade. </p>
	

 
	""", unsafe_allow_html=True)
    #Gráfico 13
    fig13 = go.Figure()
    fig13.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Inflação Mensal - Slz (%)"], name="Inflação Mensal (IPCA em %) de São Luís - MA."))
    fig13.update_yaxes(tickformat=".2f")
    fig13.update_layout(
    title="Inflação Mensal (IPCA em %) de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig13.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig13.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig13.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig13,y_value=inf_mens["Inflação Mensal - Slz (%)"].mean(),text="%.3f" % round(inf_mens["Inflação Mensal - Slz (%)"].mean(),3), line_color="blue", pos=0.2)
    st.divider()
    st.plotly_chart(fig13,config={'modeBarButtonsToRemove': ['toImage', 'zoom2d', 'select2d', 'lasso2d', 'autoScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian', 'toggleSpikes', 'resetScale2d', 'pan2d', 'zoomIn2d', 'zoomOut2d', 'editTrace', 'annotationEdit', 'eye', 'modeBar', 'select', 'lasso']})
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br> &emsp;&emsp;A <b>inflação mensal</b> é calculada pelo IBGE (Instituto Brasileiro de Geografia e Estatística) por meio do Índice Nacional de Preços ao Consumidor Amplo – IPCA e reflete uma aproximação ao custo de vida mensal da cidade de São Luís, por meio da variação de preços dos grupos de despesas relacionados a alimentação e bebidas, habitação, artigos de residência, vestuário, transportes, saúde e cuidados pessoais, despesas pessoais, educação e comunicação. A curva tracejada azul indica a média da inflação para São Luís, considerando toda a série temporal neste gráfico, iniciada em janeiro de 2020.
	</p>
	""", unsafe_allow_html=True)

    #Gráfico 15
    fig15 = go.Figure()
    fig15.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Habitação"], name="Habitação"))
    fig15.update_yaxes(tickformat=".2f")
    fig15.update_layout(
    title="Impacto das despesas com a Habitação na Inflação (em p.p.) de São Luís - MA .",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig15.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig15.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig15,y_value=inf_mens["Habitação"].mean(),text=str(round(inf_mens["Habitação"].mean(),3)), line_color="blue",pos=0.1)
    fig15.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.divider()
    st.plotly_chart(fig15)

    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>&emsp;&emsp;O <b>impacto das despesas de habitação na inflação</b> em São Luís, mede o quanto dos gastos relacionados à habitação, como aluguel, reparos e reformas, taxa de água e esgoto, artigos de limpeza, combustíveis, energia, etc. impactaram diretamente a inflação do mês. Assim, por exemplo, se o impacto da despesa de habitação, em fevereiro de 2024, foi de 0,26 p.p. (pontos percentuais) e a inflação do mês foi de 1,03%, isso significa que 25% da inflação de fevereiro de 2024 foi puxada pelos gastos relativos a habitação ou, de outra maneira, que da inflação de fevereiro desse ano (1,03%), 0,26 p.p. foi relativo às despesas com habitação. A curva tracejada azul indica a média do impacto, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados do IBGE.
	</p>
	""", unsafe_allow_html=True)
   

    #Gráfico 14
    fig14 = go.Figure()
    fig14.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Saúde e cuidados pessoais"], name="Saúde e cuidados pessoais"))
    fig14.update_yaxes(tickformat=".2f")
    fig14.update_layout(
    title="Impacto das despesas com Saúde e Cuidados Pessoais na Inflação (em p.p.) de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig14.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig14.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig14.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    add_hline_with_annotation(fig14,y_value=inf_mens["Saúde e cuidados pessoais"].mean(),text=str(round(inf_mens["Saúde e cuidados pessoais"].mean(),3)), line_color="blue",pos=0.05)
    st.divider()
    st.plotly_chart(fig14)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>&emsp;&emsp;O <b>impacto das despesas com saúde e cuidados pessoais na inflação</b> em São Luís, mede o quanto dos gastos com cuidados pessoais, como produtos farmacêuticos, analgésicos, antigripais, antibióticos, vitaminas, óculos de grau, planos de saúde, serviços médicos, dentistas, exames, produtos de higiene pessoal, etc. impactaram diretamente a inflação do mês. Assim, por exemplo, se o impacto dos gastos com cuidados pessoais, em dezembro de 2022, foi de 0,35 p.p. (pontos percentuais) e a inflação do mês foi de 0,77%, isso significa que 45,45% da inflação de dezembro desse ano foi puxada pelos gastos relativos aos cuidados pessoais ou, de outra maneira, que da inflação de dezembro de 2022 (0,77%), 0,35 p.p. foi relativo às despesas com cuidados pessoais. A curva tracejada azul indica a média do impacto, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados do IBGE.
    </p>
	""", unsafe_allow_html=True)
   

    #Gráfico 16
    fig16 = go.Figure()
    fig16.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Transportes"], name="Transportes"))
    fig16.update_yaxes(tickformat=".2f")
    fig16.update_layout(
    title="Impacto das despesas com Transporte na Inflação  (em p.p.) de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig16.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig16.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig16.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    add_hline_with_annotation(fig16,y_value=inf_mens["Transportes"].mean(),text=str(round(inf_mens["Transportes"].mean(),3)), line_color="blue",pos=0.15)    
    st.divider()
    st.plotly_chart(fig16)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br> &emsp;&emsp;O <b>impacto das despesas de transporte na inflação</b> em São Luís, mede o quanto dos gastos relacionados aos transportes, como ônibus urbano, táxi, passagem aérea, transporte por aplicativo, automóvel novo, emplacamento e licença, seguros, pneus, gasolina, diesel, estacionamento, etc. impactaram diretamente a inflação do mês. Assim, por exemplo, se o impacto da despesa de transporte, em fevereiro de 2024, foi de 0,30 p.p. (pontos percentuais) e a inflação do mês foi de 1,03%, isso significa que 29,12% da inflação de fevereiro de 2024 foi puxada pelos gastos relativos aos transportes ou, de outra maneira, que da inflação de fevereiro (1,03%), 0,30 p.p. foi relativo às despesas com transportes. A curva tracejada azul indica a média do impacto, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados do IBGE.
    </p>
	""", unsafe_allow_html=True)

    fig19 = go.Figure()
    fig19.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Alimentação e bebidas"], name="Alimentação e Bebidas"))
    fig19.update_yaxes(tickformat=".2f")
    fig19.update_layout(
    title="Impacto das despesas com Alimentação e Bebidas na Inflação (em p.p.) de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig19.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig19.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig19.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    add_hline_with_annotation(fig19,y_value=inf_mens["Alimentação e bebidas"].mean(),text=str(round(inf_mens["Alimentação e bebidas"].mean(),3)), line_color="blue",pos=0.15)    
    st.divider()
    st.plotly_chart(fig19)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br> &emsp;&emsp;O <b>impacto das despesas com Alimentação e Bebidas na inflação</b> em São Luís, mede o quanto dos gastos com alimentação no domicílio, como cereais, leguminosas, feijão, arroz, farinha, milho, frutas, carnes, aves e ovos, bebidas e infusões, enlatados e conservas, tubérculos, etc., bem como os gastos com alimentação fora do domicílio, como refeições, lanches, cafezinhos, cervejas, sorvetes, vinhos, doces, refrigerantes e etc. impactaram diretamente a inflação do mês. Assim, por exemplo, se o impacto dos gastos com alimentação e bebidas, em fevereiro de 2024, foi de 0,15 p.p. (pontos percentuais) e a inflação do mês foi de 1,03%, isso significa que 14,5% da inflação de fevereiro de 2024 foi puxada pelos gastos relativos à alimentação dos ludovicenses, ou, de outra maneira, que da inflação de fevereiro desse ano (1,03%), 0,15 p.p. foi relativo às despesas com alimentação e bebidas. A curva tracejada azul indica a média do impacto, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados do IBGE.
	</p>
	""", unsafe_allow_html=True)
 





with tab2:
    #Primeiro grafico 
    fig = px.line(criac_emp, x='Ano', y="Taxa de Criação de Empregos (JC)- %")
    fig.update_yaxes(tickformat=".2f")
    fig.update_layout(
    title="Taxa Bruta de Criação de Empregos (JC) no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))  
    fig.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig.update_yaxes(title_text="")
    add_hline_with_annotation(fig,y_value=criac_emp["Taxa de Criação de Empregos (JC)- %"].mean(),text=str(round(criac_emp["Taxa de Criação de Empregos (JC)- %"].mean(),3)), line_color="blue", pos=1)
    fig.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Segundo grafico
    fig2 = px.line(criac_emp, x='Ano', y="Taxa de Destruição de Empregos (JD)- %")
    fig2.update_yaxes(tickformat=".2f")
    fig2.update_layout(
    title="Taxa Bruta de Destruição de Empregos (JD) no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig2.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig2.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig2.update_yaxes(title_text="")
    add_hline_with_annotation(fig2,y_value=criac_emp["Taxa de Destruição de Empregos (JD)- %"].mean(),text=str(round(criac_emp["Taxa de Destruição de Empregos (JD)- %"].mean(),3)), line_color="blue", pos=1)
    fig2.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Terceiro grafico
    fig3 = px.line(criac_emp, x='Ano', y="Taxa de Variação Líquida de Empregos (NEG)- %")
    fig3.update_yaxes(tickformat=".2f")
    fig3.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig3.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig3.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig3.update_yaxes(title_text="")
    add_hline_with_annotation(fig3,y_value=criac_emp["Taxa de Variação Líquida de Empregos (NEG)- %"].mean(),text=str(round(criac_emp["Taxa de Variação Líquida de Empregos (NEG)- %"].mean(),3)), line_color="blue", pos=2)
    fig3.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Quarto Gráfico
    fig4 = px.line(criac_emp, x='Ano', y="Extrativa Mineral - NEG")
    fig4.update_yaxes(tickformat=".2f")
    fig4.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor da Indústria Extrativa Mineral  no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig4.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig4.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig4.update_yaxes(title_text="")
    add_hline_with_annotation(fig4,y_value=criac_emp["Extrativa Mineral - NEG"].mean(),text=str(round(criac_emp["Extrativa Mineral - NEG"].mean(),3)), line_color="blue", pos=0.007)
    fig4.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Quinto Gráfico
    fig5 = px.line(criac_emp, x='Ano', y="Indústria de Transformação - NEG")
    fig5.update_yaxes(tickformat=".2f")
    fig5.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor da Indústria de Transformação no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig5.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig5.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig5.update_yaxes(title_text="")
    add_hline_with_annotation(fig5,y_value=criac_emp["Indústria de Transformação - NEG"].mean(),text="%.3f" % round(criac_emp["Indústria de Transformação - NEG"].mean(),3), line_color="blue", pos=0.1)
    fig5.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    
    #Sexto Gráfico
    fig6 = px.line(criac_emp, x='Ano', y="Servicos Industriais de Utilidade Pública - NEG")
    fig6.update_yaxes(tickformat=".2f")
    fig6.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor da Indústria de Servicos Industriais de Utilidade Pública no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig6.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig6.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig6.update_yaxes(title_text="")
    add_hline_with_annotation(fig6,y_value=criac_emp["Servicos Industriais de Utilidade Pública - NEG"].mean(),text=str(round(criac_emp["Servicos Industriais de Utilidade Pública - NEG"].mean(),3)), line_color="blue", pos=0.07)
    fig6.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Sétimo grafico
    fig7 = px.line(criac_emp, x='Ano', y="Construção Civil - NEG")
    fig7.update_yaxes(tickformat=".2f")
    fig7.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor da Indústria de Construção Civil no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig7.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig7.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig7.update_yaxes(title_text="")
    add_hline_with_annotation(fig7,y_value=criac_emp["Construção Civil - NEG"].mean(),text=str(round(criac_emp["Construção Civil - NEG"].mean(),3)), line_color="blue", pos=0.2)
    fig7.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Oitavo gráfico
    fig8 = px.line(criac_emp, x='Ano', y="Comércio - NEG")
    fig8.update_yaxes(tickformat=".2f")
    fig8.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Comércio no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig8.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig8.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig8.update_yaxes(title_text="")
    add_hline_with_annotation(fig8,y_value=criac_emp["Comércio - NEG"].mean(),text=str(round(criac_emp["Comércio - NEG"].mean(),3)), line_color="blue", pos=0.2)
    fig8.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Nono gráfico
    fig9 = px.line(criac_emp, x='Ano', y="Serviços - NEG")
    fig9.update_yaxes(tickformat=".2f")
    fig9.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Serviços no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig9.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig9.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig9.update_yaxes(title_text="")
    add_hline_with_annotation(fig9,y_value=criac_emp["Serviços - NEG"].mean(),text=str(round(criac_emp["Serviços - NEG"].mean(),3)), line_color="blue", pos=1)
    fig9.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Decimo gráfico
    fig10 = px.line(criac_emp, x='Ano', y="Administração Pública - NEG")
    fig10.update_yaxes(tickformat=".2f")
    fig10.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Administração Pública - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig10.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig10.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig10.update_yaxes(title_text="")
    add_hline_with_annotation(fig10,y_value=criac_emp["Administração Pública - NEG"].mean(),text=str(round(criac_emp["Administração Pública - NEG"].mean(),3)), line_color="blue", pos=1)
    fig10.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Décimo primeiro grafico
    fig11 = px.line(criac_emp, x='Ano', y="Agropecuária, Extração Vegetal, Caça e Pesca - NEG")
    fig11.update_yaxes(tickformat=".2f")
    fig11.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Agropecuária, Extração Vegetal, Caça e Pesca no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig11.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig11.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig11.update_yaxes(title_text="")
    add_hline_with_annotation(fig11,y_value=criac_emp["Agropecuária, Extração Vegetal, Caça e Pesca - NEG"].mean(),text=str(round(criac_emp["Agropecuária, Extração Vegetal, Caça e Pesca - NEG"].mean(),3)), line_color="blue", pos=0.15)
    fig11.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))


    fig16 = go.Figure()
    fig16.add_trace(go.Scatter(x=desoc['Trimestre'], y=desoc["Percentual"], name="Taxa de Desemprego Real"))
    fig16.update_yaxes(tickformat=".2f")
    fig16.update_layout(
    title="Taxa de Desemprego Real no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig16.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig16.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig16.update_yaxes(title_text="")
    add_hline_with_annotation(fig16,y_value=desoc["Percentual"].mean(),text=str(round(desoc["Percentual"].mean(),3)), line_color="blue", pos=1)
    fig16.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
   
    st.markdown("""
    <p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
    <br>&emsp;&emsp;A maioria dos indicadores de empregos apresentados aqui se refere à <b>demanda de empregos das empresas</b> no Maranhão, aferida anualmente. Há indicadores que apuram a <b>taxa bruta de criação</b> de postos de trabalho, bem como a <b>taxa bruta de destruição</b> de postos de trabalho. Por consequência, apuramos, também, a <b>taxa de variação líquida de empregos</b> criados ou destruídos (diferença entre o número de postos de trabalhos criados e destruídos). Os indicadores se referem ao nível agregado da demanda por empregos das empresas no Maranhão. Há, ainda, o indicador da variação líquida da demanda por empregos das firmas para os principais setores da atividade econômica do Estado. Ao final, disponibilizamos o índice que permite o acompanhamento da “Taxa de Desemprego Real” do Estado.
		</p>
	""", unsafe_allow_html=True)
    st.divider()
    
    st.plotly_chart(fig3)
    st.markdown("""
	     <p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	      <b>Nota Técnica</b>:<br><br>&emsp;&emsp;Os indicadores de emprego descritos aqui se referem à demanda das empresas por <b>empregos formais</b> e são definidos a partir de três fluxos: os fluxos de criação bruta de emprego (JC – da sigla em inglês para <i>job creation</i>), que exprimem os novos postos de trabalho criados pelas firmas; os fluxos de destruição bruta de emprego (JD – da sigla em inglês para <i>job destruction</i>), que exprimem os postos de trabalho fechados pelas empresas; e a variação líquida de empregos (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de -8,46 em 2016 no Maranhão significa que, neste ano, o Estado teve destruição líquida de postos de trabalho de 8,46% em relação à média do estoque (E) de empregos do ano atual e o anterior (E=Et+Et-1/2); o que significa que o número de postos de trabalho fechados foi superior ao de postos de trabalho criados. A curva tracejada azul indica a taxa média da variação líquida de postos de trabalhos, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis e John Haltiwanger em Handbook of Labor Economics</i>, <b>1999</b>. </p>""", unsafe_allow_html=True)

    st.plotly_chart(fig)
    st.markdown("""
	    <p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	    <b>Nota Técnica</b>:<br><br>&emsp;&emsp;O indicador mede os fluxos de criação bruta de emprego formal (JC – da sigla em inglês para <i>job creation) </i>, que exprimem os novos postos de trabalho criados pelas firmas, sem considerar os postos fechados ou destruídos pelas empresas, do ponto de vista agregado. Por exemplo, a JC de 11,42% em 2018, no Maranhão, significa que o Estado, neste ano, criou 11,42% postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), o que significa que o número bruto de postos de trabalho criados foi superior ao de postos de trabalho fechados. A curva tracejada azul indica a taxa média da criação bruta de empregos formais, considerando toda a série temporal. O cálculo para aferição é feito pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows </i> proposta por <i>Steven J. Davis e John Haltiwanger em Handbook of Labor Economics</i>, <b>1999</b>.
     
	    </p>
	    """, unsafe_allow_html=True)
            
    st.plotly_chart(fig2)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>&emsp;&emsp;O indicador mede os fluxos de destruição bruta de emprego formal (JD – da sigla em inglês para<i> job destruction</i>), que exprimem os novos postos de trabalho fechados pelas firmas, sem considerar os postos criados pelas empresas, do ponto de vista agregado. Por exemplo, a JD de 10,95% em 2018, no Maranhão, significa que o Estado, neste ano, destruiu 10,95% postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), o que significa que o número bruto de postos de trabalho destruídos, para esse ano, foi superior ao de postos de trabalho criados. A curva tracejada azul indica a taxa média da destruição bruta de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis e John Haltiwanger </i>em <i>Handbook of Labor Economics, </i> <b>1999</b>.</p>
 
	""", unsafe_allow_html=True)
    st.plotly_chart(fig4)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor da indústria extrativa mineral, (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 0,06% em 2013 significa que o setor, neste ano, criou 0,06% postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor da indústria extrativa mineral criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -0,09 do ano de 2015, revela o contrário: que o setor destruiu mais portos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis</i> e <i>John Haltiwanger</i> em <i>Handbook of Labor Economics</i>, <b>1999</b>.
	</p>
	""", unsafe_allow_html=True)
    st.plotly_chart(fig5)
    st.markdown("""
              <p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	      <b>Nota Técnica</b>:<br><br>
       &emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor da indústria de transformação, (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 0,82% em 2010 significa que o setor, nesse ano, criou 0,82% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -1,08 do ano de 2017, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i> Steven J. Davis</i>  e <i>John Haltiwanger</i>  em <i> Handbook of Labor Economics</i>, <b>1999</b>.
	   </p>
	     """, unsafe_allow_html=True)
    st.plotly_chart(fig6)
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>&emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor da indústria de serviços industriais de utilidade pública (SIUP) (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 0,15% em 2008 significa que o setor, nesse ano, criou 0,15% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -0,01% do ano de 2018, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows </i>proposta por <i>Steven J. Davi</i>s e <i>John Haltiwanger</i> em <i>Handbook of Labor Economics</i>, <b>1999</b>.
	 </p>
	""", unsafe_allow_html=True)  
    st.plotly_chart(fig7)
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para net <i>employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor da indústria de construção civil (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 2,64% em 2008 significa que o setor, nesse ano, criou 2,64% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -1,12% do ano de 2018, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis</i> e <i>John Haltiwanger em Handbook of Labor Economics</i>, <b>1999</b>.
	 </p>
 
	""", unsafe_allow_html=True)  
    st.plotly_chart(fig8)
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor do comércio (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 2,85% em 2010 significa que o setor, nesse ano, criou 2,85% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor do comércio criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -1,13% do ano de 2018, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis e John Haltiwanger</i> em <i>Handbook of Labor Economics</i>, <b>1999</b>.
	</p>
	""", unsafe_allow_html=True)  
    st.plotly_chart(fig9)
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>&emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor de serviços (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 3,68% em 2011 significa que o setor, nesse ano, criou 3,68% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor de serviços criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -2,75% do ano de 2018, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davi</i> s e <i>John Haltiwanger em Handbook of Labor Economics, </i>  <b>1999</b>.
	 </p>
	""", unsafe_allow_html=True)  
    st.plotly_chart(fig10)
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor da administração pública (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 11,90% em 2006 significa que o setor, nesse ano, criou 11,90% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor da administração pública criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -16,65% do ano de 2017, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis</i> e <i>John Haltiwanger em Handbook of Labor Economics</i>, <b>1999</b>.
	</p>
 
	""", unsafe_allow_html=True)  
    st.plotly_chart(fig11)
    st.markdown("""<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;O indicador mede a variação líquida de empregos formais (NEG – da sigla em inglês para <i>net employment growth</i>), que reflete a taxa da variação líquida dos postos de trabalho criados ou destruídos pelas firmas do setor da agropecuária, extração vegetal, caça e pesca (ou seja, representa a diferença entre os postos de trabalho criados e destruídos, resultando numa criação ou destruição líquida de postos de trabalho). Por exemplo, a NEG de 0,46% em 2003 significa que o setor, nesse ano, criou 0,46% de postos de trabalho a mais em relação à média do estoque (E) de empregos do ano em tela e o anterior (E=Et+Et-1/2), já descontados os postos que esse mesmo setor fechou; o que significa que o setor da agropecuária, extração vegetal, caça e pesca criou mais empregos do que destruiu, nesse ano. Por outro lado, a NEG de -0,41% do ano de 2018, revela o contrário: que o setor destruiu mais postos de trabalho do que criou. A curva tracejada azul indica a taxa média da variação líquida de empregos formais, considerando toda a série temporal. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base na metodologia <i>Gross Job Flows</i> proposta por <i>Steven J. Davis</i> e <i>John Haltiwanger</i> em <i>Handbook of Labor Economics</i>, <b>1999</b>.
	</p>
	""", unsafe_allow_html=True)  
    st.divider()
    st.plotly_chart(fig16)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;A <b>taxa de desemprego real</b> para o Maranhão refere-se à taxa combinada de desocupação e da força de trabalho potencial. A primeira é a relação entre o número de desocupados e a força de trabalho, a segunda é definida como o conjunto de pessoas de 14 anos ou mais de idade que não estavam ocupadas nem desocupadas, mas que possuíam potencial de comporem a força de trabalho. Assim, o indicador é a calculado como a razão entre os desocupados + força de trabalho potencial e a força de trabalho no Maranhão. A taxa é calculada pelo IBGE (Instituto Brasileiro de Geografia e Estatística) e esteve muito presente nas estatísticas por ocasião da crise do COVID-19, quando a usual taxa de desocupação deixou de refletir as dinâmicas do mercado de trabalho em função das medidas de restrição social, implementadas à época. Por refletir com mais acurácia a situação de desemprego da força de trabalho, utilizamos aqui como taxa real de desemprego. A curva tracejada azul indica a média da taxa de desemprego, considerando toda a série temporal.
	</p>
	""", unsafe_allow_html=True)
    

        
    

with tab3:
    st.markdown("""
    <p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	<br>&emsp;&emsp;Nesta aba, apresentamos dois indicadores: a <b>evolução do rendimento médio real habitual da estrutura de ocupação</b> do Maranhão, que permite o acompanhamento, trimestral, da evolução do aumento da remuneração média real comparado ao primeiro trimestre de 2012; e a <b>evolução da proporção da remuneração média real</b> dos trabalhadores com nível superior em relação ao que possuem nível médio, que permite o acompanhamento anual da distância entre trabalhadores com perfis educacionais distintos, em termos de renda, no setor formal da economia maranhense.
	</p>
	""", unsafe_allow_html=True)

    fig12 = px.line(rend_hab, x='Trimestre', y="Rendimento habitual médio real – MA (número índice, 1T2012=100)")
    fig12.update_yaxes(tickformat=".2f")
    fig12.update_layout(yaxis_title="",)
    fig12.update_layout(title="Evolução do Rendimento Médio Real Habitual em Número Índice (1º Trimestre de 2012=100)", font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),legend=dict(x=0, y=1, orientation='h'))
    fig12.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig12,y_value=rend_hab["Rendimento habitual médio real – MA (número índice, 1T2012=100)"].mean(),text=str(round(rend_hab["Rendimento habitual médio real – MA (número índice, 1T2012=100)"].mean(),3)), line_color="blue", pos=2)
    fig12.update_layout(yaxis_range=[90,130])
    fig12.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig12.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig12.update_layout( 
        yaxis2=dict(
            overlaying='y',
            side='right',
            title_text=''))
    st.divider()
    st.plotly_chart(fig12)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;''>
	   <b>Nota Técnica</b>: <br><br>
    &emsp;&emsp;O <b>rendimento médio real</b> habitualmente recebido refere-se à remuneração recebida por todos os trabalhos feitos pelas pessoas ocupadas de 14 anos ou mais no Maranhão, em termos reais, ou seja, considerando a evolução do poder de compra (descontando a inflação). Transformou-se o valor do rendimento em um número índice com base no primeiro trimestre de 2012 para poder visualizar a evolução do aumento real do rendimento ao longo do tempo. Por exemplo, o índice do 1T2023 (primeiro trimestre de 2023) igual a 124,61, sugere que o rendimento do maranhense, no primeiro trimestre de 2023, era, em termos reais, 24,61% maior do que no primeiro trimestre de 2012. Por outro lado, o índice do 2T2014 (segundo trimestre de 2014) igual a 96,16, significa dizer que o rendimento do maranhense, no segundo trimestre de 2014, era 3,84% (100 – 96,16) menor que o verificado no primeiro trimestre de 2012. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos dados do IBGE.
	</p>
	""", unsafe_allow_html=True)


    fig17 = px.line(rend_hab, x='Trimestre', y="Proporção do Rendimento das Mulheres em relação aos Homens")
    fig17.update_yaxes(tickformat=".2f")
    fig17.update_layout(yaxis_title="",)
    fig17.update_layout(title="Evolução da proporção do Rendimento Médio Real das Mulheres em relação ao dos Homens no Maranhão.", font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),legend=dict(x=0, y=1, orientation='h'))
    fig17.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig17,y_value=rend_hab["Proporção do Rendimento das Mulheres em relação aos Homens"].mean(),text=str(round(rend_hab['Proporção do Rendimento das Mulheres em relação aos Homens'].mean(),3)), line_color="blue", pos=0.02)
    fig17.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig17.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig17.update_layout( 
        yaxis2=dict(
            overlaying='y',
            side='right',
            title_text=''))
    

    fig24 = px.line(rend_e_des, x='Ano', y="S/M")
    fig24.update_yaxes(tickformat=".2f")
    fig24.update_layout(yaxis_title="",)
    fig24.update_layout(title="Proporção da Remuneração Média Real dos Trabalhadores com Ensino Superior em relação aos que possuem Ensino Médio – Setor Formal (MA)", font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),legend=dict(x=0, y=1, orientation='h'))
    fig24.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig24,y_value=rend_e_des["S/M"].mean(),text=str(round(rend_e_des['S/M'].mean(),3)), line_color="blue", pos=1)
    fig24.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig24.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig24.update_layout( 
        yaxis2=dict(
            overlaying='y',
            side='right',
            title_text=''))
    st.divider()
    st.plotly_chart(fig24)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;''>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;A proporção mede a <b>evolução da remuneração média real dos trabalhadores do setor formal da economia maranhense</b>, com instrução de nível superior, em relação aos trabalhadores que possuíam instrução de nível médio, desse mesmo setor. Por exemplo, em 2002 a proporção de 5,69 sugere que os trabalhadores do setor formal que possuíam nível superior ganhavam, em média, 5,69 vezes a mais que os trabalhadores que detinham apenas o nível médio de instrução, nesse mesmo setor. Já, em 2019, a proporção de 2,89 sugere que os trabalhadores com nível superior ganhavam, em média, cerca de 2,89 vezes a mais que os trabalhos de nível médio de instrução. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos dados do Ministério do Trabalho e Emprego. 
    </p>
	""", unsafe_allow_html=True)
        



with tab4:
    st.markdown("""
    <p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	<br>&emsp;&emsp;Nesta aba, monitoramos a desigualdade de renda no Estado do Maranhão por meio do índice de Gini e da distância no rendimento entre homens e mulheres. No primeiro caso, há dois indicadores: o primeiro índice monitora, trimestralmente, a evolução da desigualdade de renda domiciliar per capta, considerando <b>toda a estrutura da ocupação</b> no Maranhão; o segundo indicador monitora a desigualdade de renda individual no mercado de <b>trabalho formal</b>  do Estado. No segundo caso, também há dois indicadores: o primeiro índice monitora a evolução anual da remuneração média real das mulheres em relação aos homens no <b>mercado formal</b>  da economia maranhense; e o segundo índice acompanha, trimestralmente, a proporção do rendimento médio real das mulheres em relação ao dos homens, <b> considerando toda a estrutura de ocupação</b>  do estado.
	</p>""", unsafe_allow_html=True)
    fig15 = go.Figure()
    fig15.add_trace(go.Scatter(x=desig['Trimestre'], y=desig["Índice GINI da renda domiciliar per capta"], name="Índice GINI da renda domiciliar per capta"))
    fig15.update_yaxes(tickformat=".2f")
    fig15.update_layout(
    title="Desigualdade de Renda no Maranhão (Índice GINI da renda domiciliar per-capta por trimestre)",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=0, orientation='h'))	
    fig15.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig15.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig15,y_value=desig["Índice GINI da renda domiciliar per capta"].mean(),text=str(round(desig["Índice GINI da renda domiciliar per capta"].mean(),3)), line_color="blue", pos=0.01)
    fig15.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.divider()
    st.plotly_chart(fig15)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;''>
	   <b>Nota Técnica</b>:<br><br>
    &emsp;&emsp;O <b>índice de desigualdade de renda do Maranhão</b> acompanha, trimestralmente, a concentração de renda no Estado e, portanto, mede a distância ou a diferença entre os que ganham mais e os que ganham menos. O indicador usado é o índice de Gini. Esse coeficiente assume valores que variam entre 0 e 1 e significa que os valores próximos a 0 representam que a estrutura da sociedade está próxima de uma igualdade em termos de renda. Já para valores próximos de 1, essa sociedade está próxima da desigualdade absoluta. Portanto, quanto mais próximo de 0, maior é a igualdade e quanto mais próximo de 1, maior é a desigualdade. Geralmente, o indicador é considerado elevado quando assume valores a partir de 0,45. Particularmente para o Maranhão, o índice foi calculado considerando o rendimento domiciliar per capta, que representa a relação entre o total dos rendimentos domiciliares nominais e o total dos moradores. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados da PNADC-Anual do IBGE.	</p>
	""", unsafe_allow_html=True)


    fig18 = go.Figure()
    fig18.add_trace(go.Scatter(x=desig['Trimestre'], y=desig["GINI média móvel"], name="GINI média móvel"))
    fig18.update_yaxes(tickformat=".2f")
    fig18.update_layout(
    title="Desigualdade de Renda no Maranhão (Índice GINI - Média Móvel, MM=3T)",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=0, orientation='h'))
    fig18.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig18.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig18,y_value=desig["GINI média móvel"].mean(),text=str(round(desig["GINI média móvel"].mean(),3)), line_color="blue", pos=0.01)
    fig18.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.divider()
    st.plotly_chart(fig18)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
       &emsp;&emsp;O indicador é o mesmo do gráfico anterior, apenas tratado com uma média móvel para suavizar a curva e permitir uma melhor visualização da trajetória e tendência da concentração de renda no Estado.
    	</p>
	""", unsafe_allow_html=True)
    #Gráfico 22
    fig22 = go.Figure()
    fig22.add_trace(go.Scatter(x=rend_e_des['Ano'], y=rend_e_des["F/M"], name="Proporção da Remuneração Real Média das Mulheres em relação a dos Homens - Setor Formal da Economia Maranhense"))
    fig22.update_yaxes(tickformat=".2f")
    fig22.update_layout(
    title="Proporção da Remuneração Real Média das Mulheres em relação a dos Homens - Setor Formal da Economia Maranhense",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=0, orientation='h'))
    fig22.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig22.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig22,y_value=rend_e_des["F/M"].mean(),text=str(round(rend_e_des["F/M"].mean(),3)), line_color="blue", pos=0.01)
    fig22.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.divider()
    st.plotly_chart(fig22)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
		&emsp;&emsp;A proporção mede a <b>evolução da remuneração média real das mulheres que trabalham no setor formal da economia maranhense em relação a dos homens</b>. Portanto, a proporção não inclui os trabalhadores informais do Estado, que representam a grande maioria da ocupação. O indicador reflete a distância entre mulheres e homens, do ponto de vista da renda. Por exemplo, a proporção de 0,96 em 2011 sugere que as mulheres, ocupadas no setor formal da economia, ganhavam 96% da remuneração média real dos homens. Já, a proporção de 0,78 em 2000 aponta que essas mesmas mulheres ganhavam 78% da remuneração média dos homens ocupados no setor formal, nesse ano. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados do Ministério do Trabalho e Emprego.
     </p>
	""", unsafe_allow_html=True)

    #Gráfico 23
    fig23 = go.Figure()
    fig23.add_trace(go.Scatter(x=rend_e_des['Ano'], y=rend_e_des["GINI"], name="Desigualdade – Índice de GINI da remuneração média do Setor Formal da Economia – MA"))
    fig23.update_yaxes(tickformat=".2f")
    fig23.update_layout(
    title="Desigualdade – Índice de GINI da remuneração média do Setor Formal da Economia – MA",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=0, orientation='h'))
    fig23.update_layout(title_font=dict( family="Candara",size=18, color="black"))
    fig23.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig23,y_value=rend_e_des["GINI"].mean(),text=str(round(rend_e_des["GINI"].mean(),3)), line_color="blue", pos=0.01)
    fig23.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.divider()
    st.plotly_chart(fig23)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;''>
	   <b>Nota Técnica</b>:<br><br>
    <br>&emsp;&emsp;O <b>índice de desigualdade do setor formal da economia do Maranhão</b> acompanha, anualmente, a concentração de renda no Estado nos setores de ocupação formal. Portanto, ao contrário do primeiro gráfico de desigualdade, não se está considerando toda a ocupação, mas apenas a desigualdade entre os trabalhadores formais, individualmente. O indicador usado é o índice de Gini. Esse coeficiente assume valores que variam entre 0 e 1 e significa que os valores próximos a 0 representam que a estrutura da sociedade está próxima de uma igualdade em termos de renda. Já para valores próximos de 1, essa sociedade está próxima da desigualdade absoluta. Portanto, quanto mais próximo de 0, maior é a igualdade e quanto mais próximo de 1, maior é a desigualdade. Geralmente, o indicador é considerado elevado quando assume valores a partir de 0,45. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos microdados do Ministério do Trabalho e Emprego.
	</p>
	""", unsafe_allow_html=True)

    st.divider()
    st.plotly_chart(fig17)
    st.markdown("""
	<p style='font-family: Candara, sans-serif; font-size: 16px;text-align: justify;'>
	   <b>Nota Técnica</b>:<br><br>
   	 &emsp;&emsp;A proporção mede a evolução do <b>rendimento médio real habitual das mulheres ocupadas em relação ao dos homens ocupados no Maranhão</b>. Portanto a proporção diz respeito a todos os rendimentos provenientes de toda as ocupações (formal e informal) e reflete a distância entre mulheres e homens, do ponto de vista da renda. Por exemplo, a proporção de 0,94 no 2T2017 (segundo trimestre de 2017) sugere que as mulheres ocupadas ganhavam, nesse período, 94% da remuneração média real dos homens. Já, a proporção de 0,87 no 2T2023 (segundo trimestre de 2023) aponta que essas mesmas mulheres ganhavam 87% da remuneração média dos homens ocupados nesse trimestre. A aferição é feita pelo GAPE – Grupo de Análise da Política Econômica do PPGDSE – Programa de Pós-Graduação em Desenvolvimento Socioeconômico, da UFMA, com base nos dados do IBGE.	
    </p>
	""", unsafe_allow_html=True)
with tab5:
    criac_emp2=criac_emp
    criac_emp2["Ano"]=criac_emp2["Ano"].astype(str)
    st.markdown("""<h4 style="font-family: Candara;">Taxa de Criação e de Destruição  de Empregos por Setor.</h4>""", unsafe_allow_html=True)
    st.write("")
    st.dataframe(criac_emp)
    st.divider()
    st.markdown("""<h4 style="font-family: Candara;">Impacto (p.p.) dos preços de grupos de produtos e serviços sobre a inflação mensal - Slz.</h4>""", unsafe_allow_html=True)
    st.write("")
    st.dataframe(inf_mens)
    st.divider()
    st.markdown("""<h4 style="font-family: Candara;">Rendimento habitual médio real e Proporção do Rendimento das Mulheres – MA.</h4>""", unsafe_allow_html=True)
    st.write("")
    st.dataframe(rend_hab)
    st.divider()
    st.markdown("""<h4 style="font-family: Candara;">Taxa de Desemprego Real</h4>""", unsafe_allow_html=True)
    st.write("")
    st.dataframe(desoc)
    st.divider()
    st.markdown("""<h4 style="font-family: Candara;">Índice GINI da renda domiciliar per capita e Gini Média Móvel.</h4>""", unsafe_allow_html=True)
    st.write("")
    st.dataframe(desig)
