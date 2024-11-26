from reportes import get_data, unidades_vendidas, total_vendido
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="templates")

@app.route('/reportes', defaults={'report_type': None})
@app.route('/reportes/<report_type>')
def reportes(report_type):
    table_data = None
    title = "Selecciona un reporte"
    if report_type == "datos":
        table_data = pd.DataFrame(get_data()).to_html(classes='table table-striped', index=False)
        title = "Todos los Datos"
    elif report_type == "unidades":
        table_data = unidades_vendidas().to_html(classes='table table-striped', index=False)
        title = "Reporte de Unidades"
    elif report_type == "total":
        table_data = total_vendido().to_html(classes='table table-striped', index=False)
        title = "Reporte Total Vendido"    
    return render_template('reportes.html', table_data=table_data, title=title)


if __name__ == '__main__':
    app.run(debug=True)





