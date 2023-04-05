import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


@st.cache_data
def cargar_datos(filas):
    data = pd.read_csv(Ruta_archivo, nrows= filas, sep = ',')
    return data

@st.cache_data
def filtros(variable_busqueda,busqueda):
    df_filtrado2 = df[df[variable_busqueda] == busqueda]
    return df_filtrado2

st.title('RETO DEL MÓDULO CINCO - EMPLOYEES')
st.header('Caracteristicas de los empleados de distintas unidades de negocio de distintas ciudades')
st.subheader('El objetivo es brindar una forma simple y didactica para analizar a los empleados de distintas ciudades.')

Ruta_archivo = ('C:/Users/ecrim/Downloads/Employees.csv')
df = cargar_datos(500)
st.text(('Existen ' + str(df.shape[0])  +' registros en total.'))

st.sidebar.subheader('Opciones a escoger')
# Mostrar el df
if st.sidebar.checkbox('Mostrar/Ocultar el DataFrame original'):
    st.subheader('Registros')
    #st.text(('Existen ' + str(df.shape[0])  +' registros en total.'))
    st.write(df)

# Mostrar el estadisticas y tipo de dato
if st.sidebar.checkbox('Estadisticas generales del comportamiento de las variables'):
    st.subheader('Tipo de datos')
    st.write(df.describe())
    st.write(df.dtypes)


# Filtro por ciudad y unidad
if st.sidebar.checkbox('Mostrar/Ocultar los empleados por ciudad'):
    st.sidebar.subheader('Empleados por ciudad')
    ciudades = df['Hometown'].unique()
    seleccion_ciudad = st.sidebar.selectbox('Seleccione la ciudad',    ciudades)
    df_filtrado3 = filtros('Hometown',seleccion_ciudad)
    df_filtrado3 = df_filtrado3['Employee_ID']
    st.text(('Existen ' + str(df_filtrado3.shape[0])  +' empleados en la ciudad de ' + str(seleccion_ciudad)))
    st.write(df_filtrado3)

elif st.checkbox('Mostrar/Ocultar los empleados por unidad'):
    st.subheader('Empleados por unidad')
    ciudades = df['Unit'].unique()
    seleccion_ciudad = st.selectbox('Seleccione la unidad',    ciudades)
    df_filtrado3 = filtros('Unit',seleccion_ciudad)
    #df_filtrado3 = df_filtrado3['Employee_ID']
    st.text(('Existen ' + str(df_filtrado3.shape[0])  +' empleados en la ciudad de ' + str(seleccion_ciudad)))
    st.write(df_filtrado3)


# Graficas
st.sidebar.subheader('Selección de gráficas')
opcion_grafica = st.sidebar.selectbox('Seleccione la variable de seleccion',    ('-', 'Edad', 'Unidad', 'Deserción','Edad vs Deserción','Tiempo de servicio vs Deserción (lineplot)','Tiempo de servicio vs Deserción (scatterplot)'))
if opcion_grafica == 'Edad':
    fig, ax = plt.subplots()
    ax.hist(df['Age'],bins = df['Age'].nunique(),color = 'red')
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    st.pyplot(fig)

elif opcion_grafica == 'Unidad':
    fig, ax = plt.subplots()
    ax.hist(df['Unit'],color = 'green')
    plt.xlabel("Unidad")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif opcion_grafica == 'Deserción':
    desercion_table = df.pivot_table(index = 'Hometown',
                                     values = 'Attrition_rate',
                                     aggfunc= 'mean')
    desercion_table['Attrition_rate'] = desercion_table['Attrition_rate']*100
    fig, ax = plt.subplots()
    ax.plot(desercion_table['Attrition_rate'],color = 'blue')
    plt.xlabel("Ciudad")
    plt.ylabel("Indice de desercion")
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif opcion_grafica == 'Edad vs Deserción':
    desercion_table = df.pivot_table(index = 'Age',
                                     values = 'Attrition_rate',
                                     aggfunc= 'mean')
    desercion_table['Attrition_rate'] = desercion_table['Attrition_rate']*100
    fig, ax = plt.subplots()
    ax.plot(desercion_table['Attrition_rate'],color = 'orange')
    plt.xlabel("Edad")
    plt.ylabel("Indice de desercion")
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif opcion_grafica == 'Tiempo de servicio vs Deserción (lineplot)':
    desercion_table = df.pivot_table(index = 'Time_of_service',
                                     values = 'Attrition_rate',
                                     aggfunc= 'mean')
    desercion_table['Attrition_rate'] = desercion_table['Attrition_rate']*100
    fig, ax = plt.subplots()
    ax.plot(desercion_table['Attrition_rate'],color = 'purple')
    plt.xlabel("Tiempo de servicio (Años)")
    plt.ylabel("Indice de deserción")
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif opcion_grafica == 'Tiempo de servicio vs Deserción (scatterplot)':
    fig, ax = plt.subplots()
    plt.scatter(x = df['Time_of_service'], y = df['Attrition_rate'],color = 'purple')
    plt.xlabel("Tiempo de servicio (Años)")
    plt.ylabel("Indice de desercion")
    plt.xticks(rotation=90)
    st.pyplot(fig)    
    








# Filtro por nivel educativo
st.sidebar.subheader('Filtrado por selección')
option = st.sidebar.selectbox('Nivel educativo',    ('-', '1', '2','3','4','5'))
if option != '-':
    option = int(option)
    df_filtrado = df[df['Education_Level'] == option]
    st.subheader('DataFrame filtrado por nivel educativo')
    st.text(('Existen ' + str(df_filtrado.shape[0])  +' registros con nivel educativo ' + str(option)))
    st.write(df_filtrado)




# Filtro por busqueda

st.sidebar.subheader('Filtrado por busqueda')
option2 = st.sidebar.selectbox('Variable de busqueda',    ('-', 'Employee_ID', 'Hometown','Unit'))
if option2 == 'Employee_ID':
    empleado = st.sidebar.text_input(' ¿Cual es el Employee_ID?')
    df_filtrado2 = filtros('Employee_ID',empleado)
    st.text(('Existen ' + str(df_filtrado2.shape[0])  +' registros para el empleado ' + str(empleado)))
    st.write(df_filtrado2)

elif option2 == 'Hometown':
    ciudad = st.sidebar.text_input(' ¿Cual es la ciudad?')
    df_filtrado2 = filtros('Hometown',ciudad)
    st.text(('Existen ' + str(df_filtrado2.shape[0])  +' registros para la ciudad ' + str(ciudad)))
    st.write(df_filtrado2)

elif option2 == 'Unit':
    unidad = st.sidebar.text_input(' ¿Cual es la unidad?')
    df_filtrado2 = filtros('Unit',unidad)
    st.text(('Existen ' + str(df_filtrado2.shape[0])  +' registros que pertenecen a la unidad ' + str(unidad)))
    st.write(df_filtrado2)






# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = df[df[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data) 