import re
from salvador_extractor import salvador_extractor
import pandas as pd

deals = {}

with open("../data/teste_rapido_linear/1306.txt") as f:
    gazette = f.read()

pattern = r'(DISPENSA DE LICITAÇÃO [\w\W]*? DATA DO ATO: [0-9/]+)'
        
text = gazette
match = re.findall(pattern, text,  )

df = pd.DataFrame()
for i in match:
    try:
        deal = salvador_extractor.gazetteDeal(i)
        deal.get_process()
        print(deal.process)
        deal.get_company()
        print(deal.company)
        deal.get_company_id()
        print(deal.company_id)
        deal.get_object()
        print(deal.object)
        deal.get_date()
        deal_dict = deal.__dict__
        del deal_dict['filetext']
        df = df.append(deal_dict,ignore_index=True )
    except Exception as e: print(e)

df.to_csv("temp.csv")