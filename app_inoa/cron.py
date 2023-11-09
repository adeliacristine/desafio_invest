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
            data = tickers.tickers[item.nome].history(period="1m")
    
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
                stock_splits = float(data['Stock Splits'][0])
            )
            quoted_price.save()

            if quoted_price.close < item.lower_limit:
                subject = "Alerta de negociação! {}".format(quoted_price.item)
                message = f"Olá, Seu ativo {quoted_price.item} atingiu um valor menor que o limite inferior do túnel de preço. Sugerimos que é um bom momento para COMPRA."
                from_email = 'inoainvest@inoa.com.br'
                recipient_list = ['dellycris.ufrrj@gmail.com']
    
                send_mail(subject, message, from_email, recipient_list)

            if quoted_price.close < item.upper_limit:
                subject = "Alerta de negociação! {}".format(quoted_price.item)
                
                message = f"Olá, Seu ativo {quoted_price.item} atingiu um valor maior que o limite superior do túnel de preço, sugerimos assim que é bom momento para VENDA."
                from_email = 'inoainvest@inoa.com.br'
                recipient_list = ['dellycris.ufrrj@gmail.com']
            