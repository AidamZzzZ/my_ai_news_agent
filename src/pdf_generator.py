from fpdf import FPDF

def remove_non_latin1(text):
    return text.encode('latin-1', 'ignore').decode('latin-1')

def create_pdf(summarizer_news, file_name="./output/noticias_tecnologia.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=16)
    pdf.cell(200, 10, txt="Resumen de noticias de Tecnologia", ln=True, align='C')
    pdf.ln(5)

    for summarizer in summarizer_news:
        title_summarizer = remove_non_latin1(summarizer['titulo'])
        content_summarizer = remove_non_latin1(summarizer['resumen'])
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 10, txt=title_summarizer)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, txt=content_summarizer)
        pdf.cell(0, 10, "Visit article.", ln=1, link=summarizer["url"])
        pdf.ln(5)

    pdf.output(file_name)