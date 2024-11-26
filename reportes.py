import requests
import pandas as pd


def data_3A():
    response = requests.get('https://manifest-emblem-437615-g9.rj.r.appspot.com/items/carrito/comprado/1')


    if response.status_code == 200:
        data = response.json()
        processed_data = [
            {
                "Nombre": item["producto"]["nombre"],
                "Unidades Vendidas": item["unidades"],
                "Recaudado": item["subtotal"]*4000
            }
            for item in data
        ]
        return processed_data
    else:
        return {"error": "No se pudo obtener datos de la API original"}
    
def data_3B():
  response = requests.get("https://store-api-281290752241.us-central1.run.app/api/ventas/get-ventas/estado/completado")

  if response.status_code == 200:
    data = response.json()
    processed_data = []
    print(type(data["ventas"][0]["pedidos"][0]["total"]))
    for venta in data["ventas"]:
      for pedido in venta["pedidos"]:
        new = {
            "Nombre": pedido["producto"],
            "Unidades Vendidas": pedido["cantidad"],
            "Recaudado": pedido["total"]
        }
        processed_data.append(new)
    return processed_data
  else:
      return {"error": "No se pudo obtener datos de la API original"}


def get_data():
    data_a = data_3A()
    data_b = data_3B()    
    if data_a == {"error": "No se pudo obtener datos de la API original"} and data_b == {"error": "No se pudo obtener datos de la API original"}:
        return {"error": "No se pudo obtener datos de ambas APIs"}    
    if data_a == {"error": "No se pudo obtener datos de la API original"}:
        return data_b
    if data_b == {"error": "No se pudo obtener datos de la API original"}:
        return data_a    
    return data_a + data_b


    

def unidades_vendidas():
    data = get_data()
    if data=={"error": "No se pudo obtener datos de la API original"}:
        return data
    else:
        df=pd.DataFrame(data)
        return df.groupby("Nombre", as_index=False)['Unidades Vendidas'].sum().sort_values(by='Unidades Vendidas', ascending=False)

def total_vendido():
    data= get_data()
    if data=={"error": "No se pudo obtener datos de la API original"}:
        return data
    else:
        df=pd.DataFrame(data)      
        return df.groupby("Nombre", as_index=False)['Recaudado'].sum().sort_values(by='Recaudado', ascending=False)
    




