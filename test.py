import jinja2
import pdfkit
import json

def crea_pdf(template_path,info):
    template_name = template_path.split('/')[-1]
    template_path = template_path.replace(template_name,'')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

    template = env.get_template(template_name)

    html = template.render(info)
    print(html)
    options = {
        'margin-top':'0.05in',
        'margin-left':'0.05in',
        'margin-right':'0.05in',
        'margin-bottom':'0.05in',
        'envoding':'UTF-8'
    }
    
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    out_path = "D:\\CODES\\BudgetInvoiceApp2.0\\out.pdf"

    pdfkit.from_string(html,out_path,configuration=config)

if __name__ == "__main__":
    template_path = "D:/CODES/BudgetInvoiceApp2.0/template.html"

    data = json.load(open('res/data/json/presupuesto/presupuesto_23001.json'))
    print(data)
    crea_pdf(template_path,data)