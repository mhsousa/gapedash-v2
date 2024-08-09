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
desoc=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desocupacao_Tx_Comb__MA", skiprows=2)
desig=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desigualdade")

with tab1:
    ...
with tab2:
    #Primeiro grafico
    fig = px.line(criac_emp, x='Ano', y="Taxa de Criação de Empregos (JC)- %")
    fig.update_layout(
    title="Taxa de Criação de Empregos (JC)- %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    #paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0.2)',
    legend=dict(x=0, y=1, orientation='h')
    )

    fig.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    #fig.update_yaxes(title_text="Taxa de Criação de Empregos (%)", showgrid=True, gridcolor='LightBlue', range=[0, 10])

    fig.add_hline(y=5, line_dash="dash", line_color="green", annotation_text="Meta")
    fig.update_traces(mode='lines+markers', marker=dict(size=12, color='DarkSlateGrey'))


    fig2 = px.line(criac_emp, x='Ano', y="Taxa de Destruição de Empregos (JD)- %")
    fig2.update_layout(
            title="Taxa de Destruição de Empregos (JD)- %"
      
        )

    fig3 = px.line(criac_emp, x='Ano', y="Taxa de Variação Líquida de Empregos (NEG)- %")
    fig3.update_layout(
            title="Taxa de Variação Líquida de Empregos (NEG)- %"
        )

    fig4 = px.line(criac_emp, x='Ano', y="Extrativa Mineral - NEG")
    fig4.update_layout(
            title="Extrativa Mineral - NEG"
        )

    fig5 = px.line(criac_emp, x='Ano', y="Indústria de Transformação - NEG")
    fig5.update_layout(
            title="Indústria de Transformação - NEG"
        )
    fig6 = px.line(criac_emp, x='Ano', y="Servicos Industriais de Utilidade Pública - NEG")
    fig6.update_layout(
            title="Servicos Industriais de Utilidade Pública - NEG"
        )
    fig7 = px.line(criac_emp, x='Ano', y="Construção Civil - NEG")
    fig7.update_layout(
            title="Construção Civil - NEG"
        )
    fig8 = px.line(criac_emp, x='Ano', y="Comércio - NEG")
    fig8.update_layout(
            title="Comércio - NEG"
        )
    fig9 = px.line(criac_emp, x='Ano', y="Serviços - NEG")
    fig9.update_layout(
            title="Serviços - NEG"
        )
    fig10 = px.line(criac_emp, x='Ano', y="Administração Pública - NEG")
    fig10.update_layout(
            title="Administração Pública - NEG"
        )
    fig11 = px.line(criac_emp, x='Ano', y="Agropecuária, Extração Vegetal, Caça e Pesca - NEG")
    fig11.update_layout(
            title="Agropecuária, Extração Vegetal, Caça e Pesca - NEG"
        )

  
    


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
    

        
    

with tab3:
    st.write("Renda")


with tab4:
    st.write("Desigualdade")
