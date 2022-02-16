import os
import cx_Oracle
from datetime import date 

class OracleUtility:

    ora_hostname = os.environ['API_ORACLE_HOSTNAME']
    ora_username = os.environ['API_ORACLE_USERNAME']
    ora_password = os.environ['API_ORACLE_PASSWORD']
    oh = "/app/oracle/product/19.3.0"
    os.environ["ORACLE_HOME"] = oh
    os.environ["PATH"] = oh+os.pathsep+os.environ["PATH"]
    os.environ["NLS_LANG"] = "ITALIAN_ITALY.WE8ISO8859P15"
    airflow_username = os.environ['API_AIRFLOW_USERNAME']
    airflow_password = os.environ['API_AIRFLOW_PASSWORD']

    @staticmethod
    def GetConnection():
        try:
            conn = cx_Oracle.connect(OracleUtility.ora_username, OracleUtility.ora_password, OracleUtility.ora_hostname, encoding="UTF-8")
        except Exception as e:
            return 'Exception: ' + str(e)
        return conn
    
    @staticmethod
    def ExecuteQuery(sql,param=None,res="dict"):
        """Execute a Query into database, you can specify the return value

        Parameters
        ----------
        sql : str
            Query string
        param: int
            order number
        res: str
            store code
        
        Returns
        -------
        dict:
            Default - return a dictionary
        res:    
            return a string value
        int:
            return a int value
        """
        if res == "dict" and param != None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql,param)
                column_names = [col[0] for col in cursor.description]
                data_dict = [dict(zip(column_names, row))
                            for row in cursor.fetchall()]
            except Exception as e:
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return data_dict
        elif res == "dict" and param == None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql)
                column_names = [col[0] for col in cursor.description]
                data_dict = [dict(zip(column_names, row))
                            for row in cursor.fetchone()]
            except Exception as e:
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return data_dict
        elif res == "array" and param == None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql)
                column_names = [col[0] for col in cursor.description]
                data_dict = [dict(zip(column_names, row))
                            for row in cursor.fetchall()]
            except Exception as e:
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return data_dict
        elif res == "str" and param != None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql,param)
                column_names = [col[0] for col in cursor.description]
                data_dict = [dict(zip(column_names, row))
                            for row in cursor.fetchall()]
                res = data_dict[0]["RES"]
            except Exception as e:
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return res
        elif res == "str" and param == None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql)
                column_names = [col[0] for col in cursor.description]
                data_dict = [dict(zip(column_names, row))
                            for row in cursor.fetchall()]
                res = data_dict[0]["RES"]
            except Exception as e:
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return res
        elif res == "int" and param == None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql)
                res = cursor.rowcount
                conn.commit()
            except Exception as e:
                conn.rollback()
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return res
        elif res == "int" and param != None:
            try:
                conn = OracleUtility.GetConnection()
                cursor = conn.cursor()
                cursor.execute(sql, param)
                res = cursor.rowcount
                conn.commit()
            except cx_Oracle.DatabaseError as e:
                conn.rollback()
                error, = e.args                
                if error.code == 1:
                    return 'Exception: Codice commessa già presente. Utilizzare un nuovo codice.'
                return 'Exception: ' + str(e)
            except Exception as e:
                return 'Exception: ' + str(e)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            return res
        else:
            return "Invalid return type !"