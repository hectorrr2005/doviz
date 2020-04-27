import apikey as api
from evds import evdsAPI

evds = evdsAPI(api.apikey)

#evds.get_data(['TP.DK.USD.A.YTL', 'TP.DK.USD.S.YTL', 'TP.DK.USD.A.EF.YTL', 'TP.DK.USD.S.EF.YTL', 
#               'TP.DK.EUR.A.YTL', 'TP.DK.EUR.S.YTL', 'TP.DK.EUR.A.EF.YTL', 'TP.DK.EUR.S.EF.YTL'], startdate='01-01-2020', enddate='27-04-2020')

#for data in evds.data:
#    print("Tarih: {} USD ALIŞ: {} USD SATIŞ: {} USD EFEKTİF ALIŞ: {} USD EFEKTİF SATIŞ: {} EUR ALIŞ: {} EUR SATIŞ: {} EUR EFEKTİF ALIŞ: {} EUR EFEKTİF SATIŞ: {}".format(data['Tarih'], data['TP_DK_USD_A_YTL'], data['TP_DK_USD_S_YTL'], data['TP_DK_USD_A_EF_YTL'], data['TP_DK_USD_S_EF_YTL'], data['TP_DK_EUR_A_YTL'], data['TP_DK_EUR_S_YTL'], data['TP_DK_EUR_A_EF_YTL'], data['TP_DK_EUR_S_EF_YTL']))

pd = evds.get_series('bie_dkdovytl')

print(pd['SERIE_NAME'].to_string())

#dovizkurlari = pd.to_dict()
#print("KUR KODU: {} KUR ADI: {}".format(dovizkurlari['SERIE_CODE'][1], dovizkurlari['SERIE_NAME'][1]))
