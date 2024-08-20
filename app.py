import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



st.set_page_config(
        
	layout = 'wide',
        
	initial_sidebar_state = 'collapsed' 
)
im1,im2,im3,im4,im5, im6, im7, im8, im9=st.columns(9)

with im4:
	st.image("gape.png", width=400)

tab1, tab2, tab3, tab4 = st.tabs(["Inflação","Emprego", "Renda", "Desigualdade"])
tab1.subheader("Inflação - Período compreendido entre 2020 a 2024")
tab2.subheader("Emprego - Período compreendido entre 2001 a 2018")
tab3.subheader("Renda - Período compreendido entre 2012 a 2023")
tab4.subheader("Desigualdade - Período compreendido entre 2012 a 2023")

criac_emp=pd.read_excel('dados_dashboard.xlsx', sheet_name="Criacao_Empreg__Formais_MA", skiprows=1)
inf_mens=pd.read_excel('dados_dashboard.xlsx', sheet_name="Inflação_Mensal_Slz", skiprows=1)
rend_hab=pd.read_excel('dados_dashboard.xlsx', sheet_name="Rend_hab_medio_MA", skiprows=2)
desoc=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desocupacao_Tx_Comb__MA", skiprows=1)
desig=pd.read_excel('dados_dashboard.xlsx', sheet_name="Desigualdade")

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
    #Gráfico 13
    fig13 = go.Figure()
    fig13.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Inflação Mensal - Slz (%)"], name="Inflação Mensal - São Luís (%)"))
    fig13.update_yaxes(tickformat=".2f")
    fig13.update_layout(
    title="Inflação Mensal em São Luís (IPCA) - MA",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig13.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig13.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig13,y_value=inf_mens["Inflação Mensal - Slz (%)"].median(),text="%.3f" % round(inf_mens["Inflação Mensal - Slz (%)"].median(),3), line_color="blue", pos=0.2)

    st.plotly_chart(fig13)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 13</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)

    #Gráfico 15
    fig15 = go.Figure()
    fig15.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Habitação"], name="Habitação"))
    fig15.update_yaxes(tickformat=".2f")
    fig15.update_layout(
    title="Impacto das despesas com a Habitação na Inflação de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig15.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig15,y_value=inf_mens["Habitação"].median(),text=str(round(inf_mens["Habitação"].median(),3)), line_color="blue",pos=0.1)
    fig15.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.plotly_chart(fig15)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 15</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)
    

    #Gráfico 14
    fig14 = go.Figure()
    fig14.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Saúde e cuidados pessoais"], name="Saúde e cuidados pessoais"))
    fig14.update_yaxes(tickformat=".2f")
    fig14.update_layout(
    title="Impacto das despesas com Saúde e Cuidados Pessoais na Inflação de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig14.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig14.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    add_hline_with_annotation(fig14,y_value=inf_mens["Habitação"].median(),text=str(round(inf_mens["Habitação"].median(),3)), line_color="blue",pos=0.05)
    st.plotly_chart(fig14)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 14</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)
    

    #Gráfico 16
    fig16 = go.Figure()
    fig16.add_trace(go.Scatter(x=inf_mens['Mês'], y=inf_mens["Transportes"], name="Transportes"))
    fig16.update_yaxes(tickformat=".2f")
    fig16.update_layout(
    title="Impacto das despesas com Transporte na Inflação de São Luís - MA.",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig16.update_xaxes(title_text="Mês", showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig16.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    add_hline_with_annotation(fig16,y_value=inf_mens["Habitação"].median(),text=str(round(inf_mens["Habitação"].median(),3)), line_color="blue",pos=0.15)    
    st.plotly_chart(fig16)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 16</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)
 





with tab2:
    #Primeiro grafico 
    fig = px.line(criac_emp, x='Ano', y="Taxa de Criação de Empregos (JC)- %")
    fig.update_yaxes(tickformat=".2f")
    fig.update_layout(
    title="Taxa Bruta de Criação de Empregos (JC) em São Luís - MA - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))  
    fig.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig,y_value=criac_emp["Taxa de Criação de Empregos (JC)- %"].median(),text=str(round(criac_emp["Taxa de Criação de Empregos (JC)- %"].median(),3)), line_color="blue", pos=1)
    fig.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Segundo grafico
    fig2 = px.line(criac_emp, x='Ano', y="Taxa de Destruição de Empregos (JD)- %")
    fig2.update_yaxes(tickformat=".2f")
    fig2.update_layout(
    title="Taxa Bruta de Destruição de Empregos (JD) no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig2.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig2,y_value=criac_emp["Taxa de Destruição de Empregos (JD)- %"].median(),text=str(round(criac_emp["Taxa de Destruição de Empregos (JD)- %"].median(),3)), line_color="blue", pos=1)
    fig2.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Terceiro grafico
    fig3 = px.line(criac_emp, x='Ano', y="Taxa de Variação Líquida de Empregos (NEG)- %")
    fig3.update_yaxes(tickformat=".2f")
    fig3.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig3.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig3,y_value=criac_emp["Taxa de Variação Líquida de Empregos (NEG)- %"].median(),text=str(round(criac_emp["Taxa de Variação Líquida de Empregos (NEG)- %"].median(),3)), line_color="blue", pos=2)
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
    add_hline_with_annotation(fig4,y_value=criac_emp["Extrativa Mineral - NEG"].median(),text=str(round(criac_emp["Extrativa Mineral - NEG"].median(),3)), line_color="blue", pos=0.007)
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
    add_hline_with_annotation(fig5,y_value=criac_emp["Indústria de Transformação - NEG"].median(),text="%.3f" % round(criac_emp["Indústria de Transformação - NEG"].median(),3), line_color="blue", pos=0.1)
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
    add_hline_with_annotation(fig6,y_value=criac_emp["Servicos Industriais de Utilidade Pública - NEG"].median(),text=str(round(criac_emp["Servicos Industriais de Utilidade Pública - NEG"].median(),3)), line_color="blue", pos=0.07)
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
    add_hline_with_annotation(fig7,y_value=criac_emp["Construção Civil - NEG"].median(),text=str(round(criac_emp["Construção Civil - NEG"].median(),3)), line_color="blue", pos=0.2)
    fig7.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Oitavo gráfico
    fig8 = px.line(criac_emp, x='Ano', y="Comércio - NEG")
    fig8.update_yaxes(tickformat=".2f")
    fig8.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Comércio no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig8.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig8,y_value=criac_emp["Comércio - NEG"].median(),text=str(round(criac_emp["Comércio - NEG"].median(),3)), line_color="blue", pos=0.2)
    fig8.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))

    #Nono gráfico
    fig9 = px.line(criac_emp, x='Ano', y="Serviços - NEG")
    fig9.update_yaxes(tickformat=".2f")
    fig9.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Serviços no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig9.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig9,y_value=criac_emp["Serviços - NEG"].median(),text=str(round(criac_emp["Serviços - NEG"].median(),3)), line_color="blue", pos=1)
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
    add_hline_with_annotation(fig10,y_value=criac_emp["Administração Pública - NEG"].median(),text=str(round(criac_emp["Administração Pública - NEG"].median(),3)), line_color="blue", pos=1)
    fig10.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    
    #Décimo primeiro grafico
    fig11 = px.line(criac_emp, x='Ano', y="Agropecuária, Extração Vegetal, Caça e Pesca - NEG")
    fig11.update_yaxes(tickformat=".2f")
    fig11.update_layout(
    title="Taxa de Variação Líquida de Empregos (NEG) do Setor de Agropecuária, Extração Vegetal, Caça e Pesca no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig11.update_xaxes(title_text="Ano", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig11,y_value=criac_emp["Agropecuária, Extração Vegetal, Caça e Pesca - NEG"].median(),text=str(round(criac_emp["Agropecuária, Extração Vegetal, Caça e Pesca - NEG"].median(),3)), line_color="blue", pos=0.15)
    fig11.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))


    fig16 = go.Figure()
    fig16.add_trace(go.Scatter(x=desoc['Trimestre'], y=desoc["Percentual"], name="Taxa de Desemprego Real"))
    fig16.update_yaxes(tickformat=".2f")
    fig16.update_layout(
    title="Taxa de Desemprego Real no Maranhão - %",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=1, orientation='h'))
    fig16.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig16,y_value=desoc["Percentual"].median(),text=str(round(desoc["Percentual"].median(),3)), line_color="blue", pos=1)
    fig16.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
   


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
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 16</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)
    

        
    

with tab3:

    fig12 = px.line(rend_hab, x='Trimestre', y="Rendimento habitual médio real – MA (número índice, 1T2012=100)")
    fig12.update_yaxes(tickformat=".2f")
    fig12.update_layout(yaxis_title="",)
    fig12.update_layout(title="Evolução do Rendimento Real Habitual Médio em Número índice (1º Trimestre de 2012=100)", font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),legend=dict(x=0, y=1, orientation='h'))
    fig12.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig12,y_value=rend_hab["Rendimento habitual médio real – MA (número índice, 1T2012=100)"].median(),text=str(round(rend_hab["Rendimento habitual médio real – MA (número índice, 1T2012=100)"].median(),3)), line_color="blue", pos=2)
    fig12.update_layout(yaxis_range=[90,130])
    fig12.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig12.update_layout( 
        yaxis2=dict(
            overlaying='y',
            side='right',
            title_text=''))
    st.plotly_chart(fig12)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 12</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)


    fig17 = px.line(rend_hab, x='Trimestre', y="Proporção do Rendimento das Mulheres em relação aos Homens")
    fig17.update_yaxes(tickformat=".2f")
    fig17.update_layout(yaxis_title="",)
    fig17.update_layout(title="Evoluçao da proporção do Rendimento das Mulheres em relação ao rendimento real médio dos Homens no Maranhão.", font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),legend=dict(x=0, y=1, orientation='h'))
    fig17.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig17,y_value=rend_hab["Proporção do Rendimento das Mulheres em relação aos Homens"].median(),text=str(round(rend_hab['Proporção do Rendimento das Mulheres em relação aos Homens'].median(),3)), line_color="blue", pos=0.02)
    fig17.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    fig17.update_layout( 
        yaxis2=dict(
            overlaying='y',
            side='right',
            title_text=''))
    st.plotly_chart(fig17)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 17</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)
        



with tab4:
    fig15 = go.Figure()
    fig15.add_trace(go.Scatter(x=desig['Trimestre'], y=desig["Índice GINI da renda domiciliar per capta"], name="Índice GINI da renda domiciliar per capta"))
    fig15.update_yaxes(tickformat=".2f")
    fig15.update_layout(
    title="Desigualdade de Renda no Maranhão (Índice GINI da renda domiciliar per-capta por trimestre)",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=0, orientation='h'))	
    fig15.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig15,y_value=desig["Índice GINI da renda domiciliar per capta"].median(),text=str(round(desig["Índice GINI da renda domiciliar per capta"].median(),3)), line_color="blue", pos=0.01)
    fig15.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.plotly_chart(fig15)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 15</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)


    fig18 = go.Figure()
    fig18.add_trace(go.Scatter(x=desig['Trimestre'], y=desig["GINI média móvel"], name="GINI média móvel"))
    fig18.update_yaxes(tickformat=".2f")
    fig18.update_layout(
    title="Desigualdade de Renda no Maranhão (Índice GINI - Média Móvel, MM=3T)",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    legend=dict(x=0, y=0, orientation='h'))
    fig18.update_xaxes(title_text="Trimestre", showgrid=True, gridwidth=1, gridcolor='LightPink')
    add_hline_with_annotation(fig18,y_value=desig["GINI média móvel"].median(),text=str(round(desig["GINI média móvel"].median(),3)), line_color="blue", pos=0.01)
    fig18.update_traces(mode='lines+markers', marker=dict(size=7, color='DarkSlateGrey'))
    st.plotly_chart(fig18)
    st.markdown("""
	<p style='font-family: Arial, sans-serif; font-size: 16px;'>
	   <b>Comentários sobre o gráfico 18</b>: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, velit et malesuada euismod, risus massa convallis dui, ac bibendum libero eros non nisi. Aliquam erat volutpat. Mauris eros augue, eleifend suscipit quam non, faucibus lacinia erat. Nulla a mollis dolor. Vivamus ultricies, neque eget hendrerit congue, turpis sem condimentum libero, et pretium ipsum nibh quis ex. Curabitur sollicitudin, nisi ac ornare mollis, nibh mi ullamcorper urna, vel aliquet ipsum felis eu metus. Nam sollicitudin magna vitae est aliquet, feugiat lobortis nulla vehicula. Sed aliquet vulputate ex, et lobortis metus auctor in. Duis consequat mi eu ligula semper, eu fermentum augue luctus. Nullam sed finibus eros. Cras nec aliquam orci. Sed ante libero, tempus vel pretium vitae, rutrum et lacus. Donec vitae urna malesuada odio commodo molestie. Praesent varius elit urna, ac aliquam nulla tempus id.
	</p>
	""", unsafe_allow_html=True)
