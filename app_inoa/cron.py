from django_cron import CronJobBase, Schedule
from .models import Item, QuotedPrice
import yfinance as yf
from django.core.mail import send_mail

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app_inoa.my_cron_job'

    def do(self):
        itens_monitorado = Item.objects.all()
        string = ' '.join(str(item.nome) for item in itens_monitorado)
        tickers = yf.Tickers(string)

        for item in itens_monitorado:
            data = tickers.tickers[item.nome].history(period="1d")
    
            if not item.is_expired():
                continue            

            quoted_price = QuotedPrice (
                item = item,
                open = data['Open'][0],
                high = data['High'][0],
                low = data['Low'][0],
                close = data['Close'][0],
                volume = float(data['Volume'][0]),
                dividends = float(data['Dividends'][0]),
                stock_splits = float(data['Stock Splits'][0]),
                #capital_gains = float(data['Capital Gains'][0])
            )
            quoted_price.save()

            quoted_price.close < item.lower_limit
            send_mail("Assunto", "Alerta de negocioação, venda",'inoainvest@inoa.com.br', ['adeliacristinecs@gmail.com'])
            email = ('Olá, to no e-mail')

            quoted_price.close < item.upper_limit
            send_mail("Assunto", "Alerta de negocioação, compra",'inoainvest@inoa.com.br', ['adeliacristinecs@gmail.com'])
            email = ('Olá, to no e-mail')
        
            
              olem hrgo mtyu epnz


 

    