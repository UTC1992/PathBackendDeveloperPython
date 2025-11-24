import pyodbc
import pandas as pd

# -----------------------------------------------------------
# 1. CONFIGURACIÓN DE LA CONEXIÓN (AJUSTAR ESTOS VALORES)
# -----------------------------------------------------------
DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = 'vacacionesnetbyserver.database.windows.net'
DATABASE = 'siGESTHProd'
USERNAME = 'vacaciones'
PASSWORD = 'p88HmEwbfrX9iB7'

CONNECTION_STRING = (
    f'DRIVER={DRIVER};'
    f'SERVER={SERVER};'
    f'PORT=1433;'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
    f'Encrypt=no;'
    f'TrustServerCertificate=no;'
    f'Connection Timeout=30;'
)

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
    # 2. Conexión y Ejecución
    with pyodbc.connect(CONNECTION_STRING) as cnxn:
        # Cargar los resultados directamente en un DataFrame de Pandas
        df = pd.read_sql(SQL_QUERY, cnxn)

        # 3. Creación del Archivo
        # Exportar a CSV (muy común para reportes)
        df.to_csv('reporte_vacaciones_calculadas.csv', index=False, encoding='utf-8')

        # Si quieres exportar a Excel
        # df.to_excel('reporte_vacaciones_calculadas.xlsx', index=False)

        print("✅ ¡Datos obtenidos y archivo 'reporte_vacaciones_calculadas.csv' creado con éxito!")

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"❌ Error al conectar o ejecutar SQL: {sqlstate}")
    print(ex)