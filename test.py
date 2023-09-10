from jinja2 import Environment
from jinja2 import FileSystemLoader
import pdfkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'


def gen_table(description):
    html = ""
    for desc in description:
        html = html + "<tr>"
        if(desc[0] == "Titulo"):html = html + "<td><b><i>"+str(desc[1])+"</i></b></td><td>"+str(desc[2])+"</td>"
        if(desc[0] == "Subtitulo"):html = html + "<td><b><i>"+str(desc[1])+"</i></b></td><td>"+str(desc[2])+"</td>"
        if(desc[0] == "Texto normal"):html = html + "<td>"+str(desc[1])+"</td><td>"+str(desc[2])+" €</td>"
        if(desc[0] == "Nota"):html = html + "<td>"+str(desc[1])+"</td><td>"+str(desc[2])+"</td>"
        html = html + "</tr>"

    return html

def create_pdf(template_vars):
    
    env = Environment(loader=FileSystemLoader('.'))
    # template = env.get_template('budget_A4.html')
    template = env.get_template('invoice_A4.html')
    if(type(template_vars['desc']) == list): template_vars['desc'] = gen_table(template_vars['desc'])
    html_out = template.render(template_vars)
    # path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
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
                ['Titulo','Titulo de prueba',''],
                ['Subtitulo','Subtitulo de prueba',''],
                ['Texto normal','Texto normal',200],
                ['Texto normal','Texto normal 2',200],
                ['Titulo','TEsto es otro titulo',''],
                ['Texto normal','Texto normal4',200],
            ], 
            'subtotal':'123445',
            'iva':21,
            'invoice_total':'123000,23456'}
    
    create_pdf(info)