import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



st.set_page_config(
        
	layout = 'wide',
        
	initial_sidebar_state = 'collapsed' 
)
im1,im2,im3,im4,im5=st.columns(5)

with im3:
	st.image("gape.png", width=400)

tab1, tab2, tab3, tab4 = st.tabs(["Inflação","Emprego", "Renda", "Desigualdade"])
tab1.subheader("Inflação - 2020 a 2024")
tab2.subheader("Emprego - 2001 a 2018")
tab3.subheader("Renda - 2012 a 2023")
tab4.subheader("Desigualdade - 2012 a 2023")

criac_emp=pd.read_excel('dados_dashboard.xlsx', sheet_name="Criacao_Empreg__Formais_MA", skiprows=1)
inf_mens=pd.read_excel('dados_dashboard.xlsx', sheet_name="Inflação_Mensal_Slz", skiprows=1)
rend_hab=pd.read_excel('dados_dashboard.xlsx', sheet_name="Rend_hab_medio_MA", skiprows=2)
desoc=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desocupacao_Tx_Comb__MA", skiprows=1)
desig=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desigualdade")

with tab1:
    fig13 = go.Figure()
    fig13.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Inflação Mensal - Slz (%)"], name="Inflação Mensal - São Luís (%)"))
    fig13.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Habitação"], name="Habitação"))
    fig13.update_layout(
    title="Inflação Mensal - Slz (%) x Inflação na Habitação",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig13.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig13.add_hline(y=5, line_dash="dash", line_color="blue")
    #fig13.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.plotly_chart(fig13)
    st.write("Comentários sobre o gráfico 13")

    fig14 = go.Figure()
    fig14.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Transportes"], name="Transportes"))
    fig14.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Saúde e cuidados pessoais"], name="Saúde e cuidados pessoais"))
    fig14.update_layout(
    title="Transportes x Saúde e cuidados pessoais",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig14.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig14.add_hline(y=5, line_dash="dash", line_color="blue")
    #fig13.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.plotly_chart(fig14)
    st.write("Comentários sobre o gráfico 14")





with tab2:
    #Primeiro grafico 
    fig = px.line(criac_emp, x='Ano', y="Taxa de Criação de Empregos (JC)- %")
    fig.update_layout(
    title="Taxa de Criação de Empregos (JC)- %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	  
    fig.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig.add_hline(y=5, line_dash="dash", line_color="blue")
    fig.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Segundo grafico
    fig2 = px.line(criac_emp, x='Ano', y="Taxa de Destruição de Empregos (JD)- %")
    fig2.update_layout(
    title="Taxa de Destruição de Empregos (JD)- %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig2.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig2.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig2.add_hline(y=5, line_dash="dash", line_color="blue")
    fig2.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Terceiro grafico
    fig3 = px.line(criac_emp, x='Ano', y="Taxa de Variação Líquida de Empregos (NEG)- %")
    fig3.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG)- %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig3.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig3.add_hline(y=5, line_dash="dash", line_color="blue")
    fig3.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Quarto Gráfico
    fig4 = px.line(criac_emp, x='Ano', y="Extrativa Mineral - NEG")
    fig4.update_layout(
    title="Extrativa Mineral - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig4.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig4.add_hline(y=5, line_dash="dash", line_color="blue")
    fig4.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Quinto Gráfico
    fig5 = px.line(criac_emp, x='Ano', y="Indústria de Transformação - NEG")
    fig5.update_layout(
    title="Indústria de Transformação - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig5.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig5.add_hline(y=5, line_dash="dash", line_color="blue")
    fig5.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    
    #Sexto Gráfico
    fig6 = px.line(criac_emp, x='Ano', y="Servicos Industriais de Utilidade Pública - NEG")
    fig6.update_layout(
    title="Servicos Industriais de Utilidade Pública - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig6.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig6.add_hline(y=5, line_dash="dash", line_color="blue")
    fig6.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Sétimo grafico
    fig7 = px.line(criac_emp, x='Ano', y="Construção Civil - NEG")
    fig7.update_layout(
    title="Construção Civil - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig7.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig7.add_hline(y=5, line_dash="dash", line_color="blue")
    fig7.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Oitavo gráfico
    fig8 = px.line(criac_emp, x='Ano', y="Comércio - NEG")
    fig8.update_layout(
    title="Comércio - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig8.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig8.add_hline(y=5, line_dash="dash", line_color="blue")
    fig8.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Nono gráfico
    fig9 = px.line(criac_emp, x='Ano', y="Serviços - NEG")
    fig9.update_layout(
    title="Serviços - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig9.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig9.add_hline(y=5, line_dash="dash", line_color="blue")
    fig9.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Decimo gráfico
    fig10 = px.line(criac_emp, x='Ano', y="Administração Pública - NEG")
    fig10.update_layout(
    title="Administração Pública - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig10.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig10.add_hline(y=5, line_dash="dash", line_color="blue")
    fig10.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Décimo primeiro grafico
    fig11 = px.line(criac_emp, x='Ano', y="Agropecuária, Extração Vegetal, Caça e Pesca - NEG")
    fig11.update_layout(
    title="Agropecuária, Extração Vegetal, Caça e Pesca - NEG",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig11.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig11.add_hline(y=5, line_dash="dash", line_color="blue")
    fig11.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))


    fig16 = go.Figure()
    fig16.add_trace(go.Scatter(x=desoc['Trimestre'], y=desoc["Percentual"], name="Taxa de Desemprego Real"))
    fig16.update_layout(
    title="Taxa de Desemprego Real",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig16.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig16.add_hline(y=0.5, line_dash="dash", line_color="blue")
    #fig13.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))



  
    


    a1,a2=st.columns(2)

    
    with a1:
        st.plotly_chart(fig3)
        st.write("Comentários sobre o gráfico 3")
        st.plotly_chart(fig)
        st.write("Comentários sobre o gráfico 1")
        st.plotly_chart(fig2)
        st.write("Comentários sobre o gráfico 2")
        st.plotly_chart(fig4)
        st.write("Comentários sobre o gráfico 4")
        st.plotly_chart(fig5)
        st.write("Comentários sobre o gráfico 5") 
        st.plotly_chart(fig6)
        st.write("Comentários sobre o gráfico 6")   
    with a2:
        
        st.plotly_chart(fig7)
        st.write("Comentários sobre o gráfico 7")
        st.plotly_chart(fig8)
        st.write("Comentários sobre o gráfico 8")   
        st.plotly_chart(fig9)
        st.write("Comentários sobre o gráfico 9")
        st.plotly_chart(fig10)
        st.write("Comentários sobre o gráfico 10")   
        st.plotly_chart(fig11)
        st.write("Comentários sobre o gráfico 11")
    
    st.plotly_chart(fig16)
    st.write("Comentários sobre o gráfico 16.")
    

        
    

with tab3:

    fig12 = px.line(rend_hab, x='Trimestre', y="Rendimento habitual médio real – MA (número índice, 1T2012=100)")
    # Update layout to hide y-axis title
    fig12.update_layout(
    yaxis_title="",  # Hide title for primary y-axis (yaxis)
    )

 
    fig12.update_layout(
        title="   Rendimento Habitual Médio em Número índice (1º Trimestre de 2012=100)",
        font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),
        #margin=dict(l=10, r=10, b=0, t=10, pad=4),
        #paper_bgcolor='rgba(0,0,0,0)',
        #plot_bgcolor='rgba(0,0,0,0.2)',
        legend=dict(x=1, y=1, orientation='h')
    )

    fig12.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig11.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig12.add_hline(y=5, line_dash="dash", line_color="green")
    fig12.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    # Adiciona o traço para o eixo secundário
    fig12.add_trace(
        go.Scatter(
            x=rend_hab["Trimestre"],
            y=rend_hab["Proporção do Rendimento das Mulheres em relação aos Homens"],
            yaxis='y2',  # Especifica o eixo secundário
            name='Proporção do Rendimento das Mulheres em relação aos Homens'
        )
    )
   
    fig12.add_trace(
        go.Scatter(
            x=rend_hab["Trimestre"],
            y=rend_hab["Rendimento habitual médio real – MA (número índice, 1T2012=100)"],
            yaxis='y1',  # Especifica o eixo secundário
            name='Rendimento habitual médio real – MA (número índice, 1T2012=100)',
            
        )
    )


    # Configura o eixo secundário
    fig12.update_layout(
        
        yaxis2=dict(
            overlaying='y',
            side='right',
            title_text=''
        )
    )
    
    st.plotly_chart(fig12)
    st.write("Comentários sobre o gráfico 4")
        



with tab4:
    fig15 = go.Figure()
    fig15.add_trace(go.Scatter(x=desig['Trimestre'], y=desig["Índice GINI da renda domiciliar per capta"], name="Índice GINI da renda domiciliar per capta"))
    fig15.add_trace(go.Scatter(x=desig['Trimestre'], y=desig["GINI média móvel"], name="GINI média móvel"))
    fig15.update_layout(
    title="Índice GINI da renda domiciliar per capta x GINI média móvel",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )
	
    fig15.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])
    fig15.add_hline(y=0.5, line_dash="dash", line_color="blue")
    #fig13.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.plotly_chart(fig15)
    st.write("Comentários sobre o gráfico 15")
