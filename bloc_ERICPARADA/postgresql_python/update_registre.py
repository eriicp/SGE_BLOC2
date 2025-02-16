import connect
def update_reg():
    conn = connect.connection_db()
    cursor =conn.cursor()
    sql_update ='''
    UPDATE clientes
    SET teléfono_cliente=000000000
    WHERE dirección_cliente = 'Carrer de Balmes 127'
    '''

    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}