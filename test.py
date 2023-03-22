from jinja2 import Environment
from jinja2 import FileSystemLoader
import pdfkit

def gen_table(description):
    html = ""
    for desc in description:
        html = html + "<tr>"
        for cell in desc:
            html = html + "<td>"+str(cell)+"</td>"
        html = html + "</tr>"
    
    return html

def create_pdf(template_vars):
    
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('budget_A4.html')
    if(type(template_vars['desc']) == list): template_vars['desc'] = gen_table(template_vars['desc'])
    html_out = template.render(template_vars)
    #path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    #config = configuration(wkhtmltopdf=path_wkhtmltopdf)
    options = {
        "enable-local-file-access": "",
        "encoding":"UTF-8"
    }

    file_content = pdfkit.from_string(
        html_out,
        'out.pdf',
        css='styles/invoice.css',
        options=options
    )

    return file_content


if __name__ == '__main__':

    info = {'doc_number':23001,
            'actual_date':'21/03/2023',
            'client_name':'Dickinson Bedoya Perez',
            'nif':'55607446R',
            'address':'Plaza Jacint Verdaguer 10, 3 - 1',
            'desc':[
                ['Esto es una descripcion de prueba',700],
                ['Esto es una descripcion de prueba 2',600]
            ], 
            'subtotal':'123445',
            'iva':21,
            'invoice_total':'123000,23456'}
    
    create_pdf(info)