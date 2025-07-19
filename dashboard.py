import streamlit as st
import streamlit.pyplot as plt

# Título do app
st.set_page_config(page_title="Dashboard de Riscos Operacionais com IA", layout="wide")
st.title("📊 Dashboard de Riscos Operacionais com IA")

# Seção 1: Distribuição de Riscos por Severidade
st.header("1. Distribuição de Riscos por Severidade")
labels = ['Baixo', 'Médio', 'Alto', 'Crítico']
sizes = [12, 25, 8, 5]
colors = ['#8BC34A', '#FFC107', '#FF5722', '#B71C1C']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax1.axis('equal')
st.pyplot(fig1)

# Seção 2: Evolução Temporal de Incidentes
st.header("2. Evolução Temporal de Incidentes")
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul']
incidentes = [3, 5, 4, 6, 8, 7, 9]
fig2, ax2 = plt.subplots()
ax2.plot(meses, incidentes, marker='o', color='blue')
ax2.set_ylabel("Número de Incidentes")
ax2.set_xlabel("Mês")
ax2.set_title("Incidentes ao longo do tempo")
st.pyplot(fig2)

# Seção 3: Acurácia dos Modelos de IA
st.header("3. Acurácia dos Modelos de IA")
modelos = ['modelo_v1.pkl', 'modelo_v2.pkl', 'modelo_final.pkl']
acuracias = [0.72, 0.84, 0.91]
fig3, ax3 = plt.subplots()
ax3.bar(modelos, acuracias, color='#4CAF50')
ax3.set_ylim(0, 1)
ax3.set_ylabel("Acurácia")
ax3.set_title("Comparativo de Modelos de IA")
st.pyplot(fig3)

# Seção 4: Fontes de Dados Mais Utilizadas
st.header("4. Fontes de Dados Mais Utilizadas")
fontes = ['Logs de Sistema', 'Planilhas Excel', 'APIs Internas', 'Relatórios PDF']
quantidades = [35, 22, 18, 12]
fig4, ax4 = plt.subplots()
ax4.barh(fontes, quantidades, color='#2196F3')
ax4.set_xlabel("Quantidade de Ingestões")
ax4.set_title("Fontes de Dados Mais Utilizadas")
st.pyplot(fig4)
