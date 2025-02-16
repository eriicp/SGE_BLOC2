import connect

def delete_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_delete = '''
    DELETE FROM clientes
    WHERE dirección_cliente = 'Ronda de Sant Antoni 92'
    '''

    cursor.execute(sql_delete)
    conn.commit()

    conn.close()
    cursor.close()
    return {"Delete successfully"}