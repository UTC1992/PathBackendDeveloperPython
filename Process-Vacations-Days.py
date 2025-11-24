import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from ShowConsolePagination import paginar_ansi

# -----------------------------------------------------------
# 1. CONFIGURACIÓN DE LA CONEXIÓN (AJUSTAR ESTOS VALORES)
# -----------------------------------------------------------
DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = 'vacacionesnetbyserver.database.windows.net'
DATABASE = 'siGESTHProd'
USERNAME = 'vacaciones'
PASSWORD = 'p88HmEwbfrX9iB7'

# Crear URL de conexión para SQLAlchemy
connection_url = URL.create(
    "mssql+pyodbc",
    username=USERNAME,
    password=PASSWORD,
    host=SERVER,
    port=1433,
    database=DATABASE,
    query={
        "driver": DRIVER,
        "Encrypt": "no",
        "TrustServerCertificate": "no",
        "Connection Timeout": "30"
    }
)

# Crear engine de SQLAlchemy
engine = create_engine(connection_url)

# Tu consulta SQL (usando la lógica final de cálculo de antigüedad)
SQL_QUERY = """
            select
                siu.CODIGO_USR,
                siu.NOMBRES_USR,
                siu.APELLIDOS_USR,
                sic.FECHA_INI_CON,
                sic.FECHA_FIN_CON,
                sitc.TIC_NOMBRE_TIPO_CONTRATO,
                sitc.TIC_GANA_VACACIONES as Tiene_Vacaciones,
                ------------------------------------------------------
                -- COLUMNAS BASADAS EN REGISTROS DE LA DB (GN_DIAS_GANADOS)
                ------------------------------------------------------
                COUNT(gndg.CODIGO_USR) AS Dias_Registrados,
                ------------------------------------------------------
                -- COLUMNAS BASADAS EN CÁLCULO DE ANTIGÜEDAD
                ------------------------------------------------------
                -- 1. Antigüedad en Meses Completos Reales
                CAST(
                        DATEDIFF(
                            month,
                                sic.FECHA_INI_CON,
                                IIF(
                                        sic.FECHA_FIN_CON IS NULL OR sic.FECHA_FIN_CON >= GETDATE(),
                                        GETDATE(),
                                        sic.FECHA_FIN_CON
                                )
                        )
                            -
                        IIF(DAY(sic.FECHA_INI_CON) > DAY(GETDATE()), 1, 0)
                    AS INT) AS Meses_Total

            from SI_USUARIO siu
                     inner join SI_CONTRATO sic on siu.CODIGO_USR = sic.CODIGO_USR_CON
                     inner join GN_DIAS_GANADOS gndg on sic.CODIGO_CON = gndg.CODIGO_CON
                     inner join SI_TIPO_CONTRATO sitc on sic.TIPO_CON = sitc.TIC_CODIGO_TIPO_CONTRATO
-- where sitc.TIC_GANA_VACACIONES = 'S'
            group by
                siu.CODIGO_USR,
                siu.NOMBRES_USR,
                siu.APELLIDOS_USR,
                sic.FECHA_INI_CON,
                sic.FECHA_FIN_CON,
                sitc.TIC_NOMBRE_TIPO_CONTRATO,
                sitc.TIC_GANA_VACACIONES
            order by siu.NOMBRES_USR;

            """

try:
    # 2. Conexión y Ejecución con SQLAlchemy
    df = pd.read_sql(SQL_QUERY, engine)

    df_with_problems = df[df["Dias_Registrados"] != df["Meses_Total"]]
    if not df_with_problems.empty:
        paginar_ansi(df_with_problems, filas_por_pagina=10)
    else:
        print("No hay registros con problemas")

    # 3. Creación del Archivo
    # Exportar a CSV (muy común para reportes)
    df.to_csv('reporte_vacaciones_calculadas.csv', index=False, encoding='utf-8')

    # Si quieres exportar a Excel
    # df.to_excel('reporte_vacaciones_calculadas.xlsx', index=False)

    print("✅ ¡Datos obtenidos y archivo 'reporte_vacaciones_calculadas.csv' creado con éxito!")

except Exception as ex:
    print(f"❌ Error al conectar o ejecutar SQL: {ex}")


