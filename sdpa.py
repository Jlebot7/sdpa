# Importacion de preferencias y codigos complementarios
# Se usa las librerias de ReportLab y funcion numero a letras (Creditos a sus desarrolladores respectivos)

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from numero_letras import numero_a_letras, numero_a_moneda
import datetime as dt
from datetime import datetime
from calendar import calendar
import pytz

# Construccion y obtencion de datos primarios

usr = str(input("Nombre del digitador\n"))
nConsecutivo = str(input("Numero de Pagaré\n"))
doc = SimpleDocTemplate(r"C:\PDFGen\%s\PG%s .pdf"  % (usr, nConsecutivo), pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

# Configuracion de matriz de datos

Story = []

# Obtencion de datos del usuario

nCliente = str(input("Nombre del cliente\n"))
nDocumento = str(input("Numero de documento de identidad\n"))
nEmpresa = str(input("Empresa del cliente\n"))
vCifras = int(input("Valor del pagaré\n"))
vlCifras = numero_a_letras(vCifras)
dRegistro = str(input("Día de registro\n"))
mRegistro = str(input("Mes de registro\n"))
mRegd = calendar.month_name(mRegistro)
aRegistro = str(input("Año de registro\n"))
flPago = str(input("Fecha límite de pago\n"))
cRegistro = str(input("Ciudad de registro\n"))

# Elaboración inicial del PDF

estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
estilos.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
estilos.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
texto = "<b>PAGARÉ N° %s A NOMBRE DE NOMBRE EMPRESA </b>Fecha: %s/%s/%s" % (nConsecutivo, dRegistro, mRegistro ,aRegistro)
Story.append(Paragraph(texto, estilos["Center"]))
Story.append(Spacer(1, 12))
texto = "<b>Valor: $%s</b>" % (vCifras)
Story.append(Paragraph(texto, estilos["Right"]))
Story.append(Spacer(1, 12))

# Integracion inicial de datos en el PDF (Por medio de strings)

texto = 'Nosotros %s, mayores de edad domiciliados en la ciudad de %s, identificados con los números de Cédula de Ciudadanía tal cual como aparece al pie de nuestra(s) firma(s) del presente documento, respectivamente, el primero actuando en nombre propio y/o en representación legal de la sociedad (Empresa o persona): %s el segundo y/o tercero firma a nombre propio y/o como deudor solidario con domicilio en la ciudad de %s, por medio por medio del presente título valor declaramos: <b>PRIMERO:</b> Que nos obligamos solidaria e incondicionalmente a pagar a la sociedad <b>NOMBRE EMPRESA</b> con Nit. NUMERO DEL NIT empresa domiciliada en la ciudad de Cúcuta, el dia %s del mes %s del año %s la suma de <b>%s PESOS</b> ($ %s) Moneda Legal Colombiana' % (nCliente, cRegistro, nEmpresa, cRegistro, dRegistro, mRegistro, aRegistro, vlCifras, vCifras)
Story.append(Paragraph(texto, estilos["Justify"]))
texto = '<b>SEGUNDO:</b> En caso de incumplimiento o retardo en la cancelación de la obligación adquirida con <b>NOMBRE EMPRESA</b>. a la fecha de su vencimiento, sin perjuicio de las acciones legales de la persona acreedor, nos obligamos a pagar además sobre el valor de este pagare un interés corriente de acuerdo a la tasa que rija las operaciones bancarias y en caso de mora la tasa de interés será la más alta legal permitida, de conformidad con la certificación que para tal efecto expida la Superintendencia Financiera de acuerdo con lo estipulado en el artículo 884 del Código de Comercio, modificado por la Ley 510 de 1999, artículo 111. <b>TERCERO:</b> Que autorizamos a la Sociedad <b>NOMBRE EMPRESA</b>. para declarar vencido totalmente el plazo y exigir judicialmente la cancelación de lo adeudado, también hacer exigible la deuda y/o el pagare en caso de embargos, acción judicial en nuestra contra, concordato o concurso de acreedores, liquidación obligatoria, quiebra, fallecimiento, inhabilidad o incapacidad de cualquiera de los que suscribimos y formamos el presente pagaré. En caso de hacerse cobro judicial o extrajudicial serán de nuestro cargo los gastos y costos de cobranza, y los honorarios de abogado en que se incurriese. Los deudores renunciamos irrevocablemente a cualquier presentación, reconvención privada o judicial, protesto, denuncia, reclamación, constitución en mora, requerimiento o notificación adicional pública o privada, de cualquier naturaleza. En caso de muerte de uno o de los deudores la persona acreedora queda en derecho de exigir la totalidad del crédito o valor del presente título a uno o cualquiera de sus herederos si necesidad de demandarlos a todos. <b>CUARTO:</b> Que aceptamos desde ahora cualquier cesión, endoso o traspaso que de este título valor hiciere la sociedad <b>NOMBRE EMPRESA</b>. a cualquier persona natural o jurídica, haciendo declaración de que el acreedor queda con el derecho de dirigirse indistintamente contra cualquiera de los obligados por el presente instrumento, sin necesidad de más notificaciones y que la solidaridad subsiste en caso de prórroga, adición o cualquier modificación a lo estipulado. En caso de iniciarse acción judicial la competencia por razón del territorio del incumplimiento de la obligación será a la elección del demandante o tenedor del pagare. <b>QUINTO:</b> Que en el ejercicio de mi o nuestro derecho a la libertad y autodeterminación informática autorizamos en representación, nombre propio y/o codeudor(es), en forma expresa, permanente e irrevocable a la sociedad <b>NOMBRE EMPRESA</b>. o a la persona o entidad que ésta delegue o designe, para representarlo o su cesionario, endosatario o quien ostente en el futuro la calidad de acreedor, previo a la relación contractual y de manera irrevocable, escrita, expresa, suficiente, voluntaria e informada, con la finalidad que la información comercial, crediticia, financiera y de servicios de la cual soy o somos titulares, referida al nacimiento, ejecución y extinción de las obligaciones dineradas (independiente de la naturaleza que les dio origen) a mi comportamiento e historial crediticio, incluida la información positiva y negativa de mis hábitos de pago y aquella que se refiere a la información personal necesaria para el estudio, análisis, y eventual otorgamiento de un crédito o celebración de un contrato, sea en general administrada y en especial: capturada, tratada, procesada, operada, verificada, trasmitida, trasferida, usada, o puesta en circulación y consultada por terceras personas autorizadas por la ley 1266 de 2.008, incluidos los usuarios de la información. Con esto mismos alcances, atributos y finalidad autorizo o autorizamos expresamente para que la información y referencia sea concernida y reportada en la base de datos de <b>DATACREDITO</b> (EXPERIAN COLOMBIA S.A.) y <b>FENALCO</b> (FEDERACION NACIONAL DE COMERCIANTES) de la persona por quien actuamos y representamos, el comportamiento y crédito comercial, hábitos de pago, manejo de créditos y en general, el cumplimiento o incumplimiento de obligaciones pecuniarias con <b>NOMBRE EMPRESA</b>'
Story.append(Paragraph(texto, estilos["Justify"]))
Story.append(Spacer(1, 12))
texto = 'De la misma manera autorizo o autorizamos a <b>FENALCO</b> Y <b>DATACREDITO</b>, como operadores de las bases de datos que tiene una finalidad estrictamente comercial, financiera, crediticia y de servicios, para que procese, opere, administre la información de la cual soy o somos titulares y para que la misma sea transferida y transmitida a usuarios, lo mismo que a otros operadores nacionales o extranjeros que tengan la misma finalidad o una finalidad que comprenda la que tiene <b>FENALCO</b> y <b>DATACREDITO</b>, o sea para que obtengan de cualquier fuente y reporten a cualquier base de datos las informaciones y referencias relativas a la persona por quien actuamos y representamos, el comportamiento y crédito comercial, hábitos de pago, manejo de cuentas corrientes bancarias y en general, el cumplimiento o incumplimiento de obligaciones pecuniarias. <b>SEXTO:</b> Certifico(amos) que los datos personales suministrados por mi o nosotros los firmantes son veraces, completos, exactos, actualizados, reales y comprobables. Por tanto, cualquier error en la información suministrada será de única y exclusiva responsabilidad mía o nuestra, lo que exonera a <b>NOMBRE EMPRESA</b>., <b>FENALCO</b> Y <b>DATACREDITO</b>, de su responsabilidad ante las autoridades judiciales y /o administrativas. <b>SEPTIMO:</b> Los gastos ocasionados por concepto de impuesto de timbre, correrán por cuenta de los deudores. <b>OCTAVO:</b> Expresamente declaramos excusado el protesto del presente pagaré. <b>NOVENO:</b> cualquiera de los firmantes actúa como deudor o deudor solidario, conoce el documento presente y asume la responsabilidad legal. <b>DECIMO:</b> declaro o declaramos que he o hemos leído y comprendido a cabalidad el contenido del presente documento y de la presente autorización y acepto o aceptamos la finalidad en ella descrita y la consecuencias que se derivan de ella. Para constancia, se firma en la ciudad de Cúcuta, a los %s dias del mes %s del año %s' % (dRegistro, mRegistro, aRegistro)
Story.append(Paragraph(texto, estilos["Justify"]))
Story.append(Spacer(1, 12))
texto = 'Firma representante legal: __________________________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Nombre:________________________________ C.C N° __________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Nombre empresa:_________________________________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'NIT:__________________________ Tel:_______________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Dirección:________________________________________________________   ___________'
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))
texto = 'Firma codeudor solidario: ___________________________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Nombre:_________________________________________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'C.C N°:__________________________ Tel:____________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Dirección:________________________________________________________   ___________'
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))
texto = 'Firma codeudor solidario:____________________________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Nombre:_________________________________________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'C.C N°:__________________________ Tel:____________________________'
Story.append(Paragraph(texto, estilos["Normal"]))
texto = 'Dirección:________________________________________________________   ___________'
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))
texto = 'Digitado por %s' % (usr)
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))

# Obtencion final de los datos ingresados en un archivo PDF

doc.build(Story)