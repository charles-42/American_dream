
import pandas as pd
import sqlalchemy
import mysql.connector

from conf.conf import mysql_pseudo, mysql_mdp


# After dowloading my csv and xlsx files, I read them with pandas
df = pd.read_excel(r"/home/apprenant/PycharmProjects/American_dream/Data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx", skiprows=3)
df2 = pd.read_csv(r"/home/apprenant/PycharmProjects/American_dream/Data/01_raw/DataAnalyst.csv")

# I create a connexion with mysql server thanks to mysql connector
mysql_username = mysql_pseudo
mysql_password = mysql_mdp
database_name = 'american_dream_db'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.
                                               format(mysql_username, mysql_password, database_name), pool_recycle=1, pool_timeout=57600).connect()

# I  transpose the table in mysql
df.to_sql(con=database_connection, name='survey_1', if_exists='replace')
df2.to_sql(con=database_connection, name='survey_2', if_exists='replace')
database_connection.close()
