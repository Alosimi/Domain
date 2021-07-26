import time
import requests
from colorama import init ,Fore
email = open('list.txt','r')
init()
def los():
    while True:
        p = email.readline().split("\n")[0]
        x = p.split('@gmail.com')[0]
        url = f"https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=79895&rt=j"
        pauload={
           'continue': 'https://mail.google.com/mail',
           'flowEntry': 'SignUp',
           'flowName': 'GlifWebSignIn',
           'hl': 'ar',
           'service': 'mail',
           'dsh': 'S-1090057145:1627240276218060',
           'f.req': f'["AEThLlx4EPxG3IhoPg9oJf82soNVm9c-tfFNK0DIfakdfJ42QakII8NZ4bzJ0T0JwJeW4JzBf8vFY_4-fW2RSkEHBu4Sj7rE2FDmJwVXukKWEGwMhH9DEDjhhaJvuD30oxYR6tSB29wa7uaf0NsccykUtpOyQZuwajLC0SRU1N3jFqriLfZAMli2adw1DiDefJqk42jgI7sxMwmLAl_raRFptuJgro32hw","","",{x},true]',
           'at': 'AFoagUU5DxFJ6xvLgkyRm9BtTMRcyy7ycw:1627240291270',
           'azt': 'AFoagUW_oILaqpGm404J0sBe_p2ztxo0JQ:1627240291270',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"SA",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"a166a511-b4fd-4499-b353-f5c619867039",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false,1,""]',
            'gmscoreversion': 'undefined'
    }
        heads={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-length': '1336',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cookie': 'LSOLH=_SVI_Ch9NNU5sNU91SVNRZ1VvRHpXTm1laFFKR3loc2VhbXhjEIze2c3U7_ACGAMiP01BRURIZl9xbGt5dmowUHBwbWNoOE8zTVNKbnBEaFo5WGtvNV81UF9HNlA4d3hVTXZZbE1mdm4tcVlMdHRjMA_:27038644:c8f3; SEARCH_SAMESITE=CgQI5JIB; ACCOUNT_CHOOSER=AFx_qI4o6z2mmeACUlyA8XIt9KxdwqT-7mSDO_z1PyVtQ_rvY7Mg37ALWQTLMcSNtTqjgWxybWjz1xmrPrIMCwaF7xf9zweUOhpRI6XNWDuQATF3C7l4lvsGJhkFFFga9-AAABANZiBQLlzeKbte_4uLjwp5Ae808PvJVAslPnvolxCzeBOvQhkCbcCECxvZHzLxkx6k4bxk; SMSV=ADHTe-CfMvv2CnSOfFLef76U3XzrTF8ZEzZOy4360F3DnhM3Mq7kd2P24ZLO3zsJeFSLkk_gFhu5l_xlgxJxB92WMJVrM-Dm2HqCWKGXs0XTvmnz5ZO9Xt0; SID=_wceGkSMacN2qe9HD86SYJGpIL7N9PBZkOYsHmGFz1Hov4pcRvL6ThXssEjzEAF1ZmsqFQ.; __Secure-1PSID=_wceGkSMacN2qe9HD86SYJGpIL7N9PBZkOYsHmGFz1Hov4pcBYuIdwAYCjbBvHWIfIg6sA.; __Secure-3PSID=_wceGkSMacN2qe9HD86SYJGpIL7N9PBZkOYsHmGFz1Hov4pcMcK3i3sALe28ZdK-Q6xvlg.; __Host-1PLSID=doritos|o.myaccount.google.com|s.SA|s.blogger|s.youtube:_wceGnUTxv-IK__zI0lT-yXjsBmvd1S3pGWY0xxjlZr2j5N7L2m6ifsYONCjatQ0IRQn5g.; HSID=A4aULV6kB8ZT_AArm; SSID=A7R-csWgPXjmazgAh; APISID=48Jzf4UBL2-FLVR_/A2sVxILjOJBtJZ7jC; SAPISID=1VD5K0NO_BDW0S5f/AqYV7ZvaY-BxvjFdM; __Secure-1PAPISID=1VD5K0NO_BDW0S5f/AqYV7ZvaY-BxvjFdM; __Secure-3PAPISID=1VD5K0NO_BDW0S5f/AqYV7ZvaY-BxvjFdM; OGPC=19022591-1:; LSID=doritos|o.chat.google.com|o.mail.google.com|o.myaccount.google.com|s.SA|s.blogger|s.youtube:_wceGnUTxv-IK__zI0lT-yXjsBmvd1S3pGWY0xxjlZr2j5N7oCZXKe7elwDcI6EMPIU4eA.; __Host-3PLSID=doritos|o.chat.google.com|o.mail.google.com|o.myaccount.google.com|s.SA|s.blogger|s.youtube:_wceGnUTxv-IK__zI0lT-yXjsBmvd1S3pGWY0xxjlZr2j5N7mtUNXHbTsxo2tTY2-gFBvw.; NID=219=21cvEux9IUst0duinE5VuyNPU9SLGbeV-IpWaMPHZ6yvcWvjzQUryXpou4LMR_qbHujrJlqLakYI98qcnctyypVj6m6X0ysqnPuR3kjVwZazlAdn-H3iQwcwhjtL3NvWCemLNmDgZIuj0jiGDuqAI5R8Bz7CaOOo7uS4LL25edkjUMUSRVWb7bImAJM-z9uxKJuQiY_8vJCm5Vv_AAqJTdMX368q5X2ZgxICPpK4A3MFpHpIZTBVXD4lsnhWon5GZrslu3mK8hMnw-edqUvfRH29LoAmfCA; 1P_JAR=2021-07-25-19; __Host-GAPS=1:sZw3iNe0oQ1Ye9cc9mzm1j5wOSuSaxOwehhMGi-8-FX-5otJOM8fnFW_wGwOOCfwAT2YwYx51WVFQcu2tPtm7QdBLqcgxA:91arbBoM8Pn3HNjG; SIDCC=AJi4QfFbuw1Hv5XLL2UPnXrNonsYdiJ0AFLswZPqOEls87-yie8maXXaLP3iVA1NpxwkSh1GbZI; __Secure-3PSIDCC=AJi4QfHxmI9pQ-f2no7svL6e3HjwsCI2E4gdSKDQwCoOU5R02NJAKypEYKOz9634isJgMhU69g',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=ar&dsh=S-1090057145%3A1627240276218060&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=a166a511-b4fd-4499-b353-f5c619867039,signin_mode=all_accounts,signout_mode=show_confirmation',
            'x-client-data': 'CI22yQEIpLbJAQjEtskBCKmdygEI64zLAQjQmssBCIyeywEIoKDLAQit8ssBCNzyywEI8PLLAQiP9MsBCLT4ywEI7PjLAQie+csBCPH5ywEIsPrLAQjC+8sBGLryywEYkPXLAQ==',
            'x-same-domain': '1',
    }
        r = requests.post(url,data=pauload,headers=heads).text
        if '"gf.wuar",2,' in r:
           print(f'{Fore.RED}Not-available>>>{x}')
           save4 = open("Email Not-available.txt", 'a')
           save4.write(x + '\n')
        elif '"gf.wuar",1,' in r:
           print(f'{Fore.GREEN}Email available>>{x}')
           save3= open("Gmail available.txt", 'a')
           save3.write(x+ '\n')
        elif '"gf.wuar",3,' in r:
            print(f"{Fore.RED}Too Short>>>{x}")
        else:
         print(r)
         los()
def Yahoo():
 while True:
        p =email.readline().split("\n")[0]
        x = p.split('@yahoo.com')[0]
        url = f'https://login.yahoo.com/account/module/create?validateField={x}'
        data = {
            'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Riyadh","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6647)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1920","h":"1080"},"availableResolution":{"w":"1040","h":"1920"},"ts":{"serve":1626485643460,"render":1626485643606}}',
            'specId': 'yidreg',
            'cacheStored': '',
            'crumb': 'rew4cJTw15T',
            'acrumb': 'zyopNCt1',
            'done': 'https://mail.yahoo.com/d',
            'googleIdToken': '',
            'authCode': '',
            'attrSetIndex': '0',
            'specData': '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|ZoDO1OLXcOI8GEzU0PznCw==|GpM+Y/D7inmNpgIXxUVoiw==',
            'tos0': 'oath_freereg|xa|en-JO',
            'firstName': 'fdgg',
            'lastName': 'dfgdfg',
            'yid': x,
            'password': '',
            'shortCountryCode': 'AF',
            'phone': '129748741874',
            'mm': '3',
            'dd': '5',
            'yyyy': '4',
            'freeformGender': '',
            'signup': '',
        }
        headf = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '16933',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'APID=UPf19e6da5-c08f-11eb-9d0a-0626b1a58a08; B=6fm0vvhgb4m9s&b=3&s=po; A1=d=AQABBDxZsmACENCrlgVsuYjht-D5Sfwf2GcFEgEBBAG_8GDPYaqqb2UB_eMAAAcIPFmyYPwf2Gc&S=AQAAAoTltpf-r39ONb2vgLfB1pw; A3=d=AQABBDxZsmACENCrlgVsuYjht-D5Sfwf2GcFEgEBBAG_8GDPYaqqb2UB_eMAAAcIPFmyYPwf2Gc&S=AQAAAoTltpf-r39ONb2vgLfB1pw; GUC=AQEBBAFg8L9hz0IgIASk; A1S=d=AQABBDxZsmACENCrlgVsuYjht-D5Sfwf2GcFEgEBBAG_8GDPYaqqb2UB_eMAAAcIPFmyYPwf2Gc&S=AQAAAoTltpf-r39ONb2vgLfB1pw&j=WORLD; cmp=t=1626484429&j=0; APIDTS=1626485372; AS=v=1&s=zyopNCt1&d=A60f38492|hYrAGXb.2TqvlyJ1_srlqmG.s6HrHK73Jzw90TYmGJmWKNGONgIzPcmynfYGXsAMuzgYyAmF.XIQfugwAL0JazlorLTPcIVRozFEd.vqdC42Xpd4uZnOzcyBaZjFrpWkk2aHTQ1LXsmRmAicRVZSbH0eT7dRGqpjVfLOdI_FxHhzitByEDurvbtS_3X8zDlxxEl8KBRKCEaCdqS0UkpW3783OvKFTmG0kqIzUA_gSIWGLB9Lq_wn52zESHeMPR.b27SsxRikko.67TFNrDRSI9XWWe069U73EL5NZq9iS4fXHk9Yy0f0.gSZIByFwjJCg5TWxrQRR56rHkmWueIKOAo9ozwEh3O.MIdMKIF4DUy4I2HG9H94E9o5soLG8VYSaSTU_zZfesBu_0aybgdXSVXqxWLN9kbyweoXzAJcGMxDbBr8dSVLZP_WmDQL2L1kyCmVHkiNmCHAQhQ2Dxf19X7o12p._18EVeOOKYbudeQySNTnnrBavGjcjnh5mJvbAclxPo3VeVSWJvX_ZHPyihfSbe2EdKEN5V5OVUj.6__PsA_4sbiGmAjy2H0xlVeT1pzq85Yv2bJNdMjj5aiTDbBBo5wN5mf7f2YEOh_E9IuBavPT31pNewbfZTzdZTyMc7C75DHU380ByROrgWq_ooxiNfOdqnWQXEJivGFKpJFVeu_OyDHXuNfpRMcdHIInoCAFTWb10gC8GNbTQVm1KFJct84EICogH_EbkfjmbJ03FXd72alGRHKNG0DrMg4i7JKcLf8RjtcdC._V.Lt1ovbGQD56H3JxBzBQ0TJn1Hgx6TayEuqDle3pPiFMuPAclS2S0g8ZTjHT2YFP7NLXNOgxo7Uw0OsQXYQEjyG_gyHvQMgXS_Q5d24PY2J0hmLD2p8rOy5k9WAI4iVyCGA7.jcyGKrPJiQ5HoUDjw--~A|D60f38475|Cvj5NL_.2Tr7ZMl9_Zswmy.qdGDj_ZeM4P792dojUPg92dLgezbW7PlygiFM2MfXTtpyYkSzlwDxCuJRbFAuhSTX21CD_nJIsTXVVoLHVZJClHPffk5vfLx3cT9APhjFQ6gAX5gOO2dJr4gINYEJDNn02OS9k3B0sZ0KNx_itwn3O4hGLADLuTb7E96rDQdgNhWVMVqG5knFjri5d9TYUNi.FEcrw9AXpHU0CDfSd3QaRf9jGriELtzwizaQHrWKTKPDUDy_VuMiJwZnl7l1XXV5SVaImT3jRbDAnBTqJL60MDrA0jGoQ6A3tSo35Tdb2ulG01sRsAi94LYwzKEtUQKahg1Rh0gO4Bp9hWdFYYilI6wCJ1BMRDQMNZn4GeNlBpzAdrsOljXgE05OKJcWnVFgv9xfDBzZichIJ_ToHvY2RrYD4i1q224JS2cAllUUPoc_VA0h3IH7J18UKz2pTOD9U75jcgu2I7mBfbfajXQRZVytPwtgVeLRZwOkvkwMtQkJEKi.352z7x3zN_gRb5cDXu9tpFmHd_P_KXayhW_48LrqIoUKsdjSccvCKuQLIbAbspp5v.bzRyQzVgYRKX9DEZ2Rm.HcJc86DDaCnrieOqxNHCZCaZYkyFudvDclzhML3hWDs_5T9vyQff9cOQHh_.uvJZ9BLwf9QoPgC5HOpKlTbbuWewA8WGGdAvgBXVsiF.8IZoL8GxKlezbvT.0mtvYaMkCACu3sHuGCpcClKwehixA_uOtdLlsKKlxPHTmy7KrFq2quful_E7F.i37CnqKFl7enApLcESRr_wc3ImaU9sAdvC65dL276RLD9gFB.HZ7vUsrmQzejDvuoqXV0kYRRFaMeQ_bYmPznkYTwdJWcTWFIQVbv4WtjFQcZhMRmysFUsAnRqW8eD8ShsG77Vvpq6l6BL8GJEM-~A',
            'Host': 'login.yahoo.com',
            'Origin': 'https://login.yahoo.com',
            'Referer': 'https://login.yahoo.com/account/create?specId=usernamereg&.intl=us&intl=xa&.lang=en-US&src=ym&activity=mail-direct&pspid=159600001&.done=https%3A%2F%2Fmail.yahoo.com%2Fd&done=https%3A%2F%2Fmail.yahoo.com%2Fd&context=reg',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        r = requests.post(url, data=data, headers=headf).text
        if '"IDENTIFIER_EXISTS"' in r:
            print(f'{Fore.RED}[+] Email Unavailable : {x}@yahoo.com')
        elif f'{Fore.RED}"LENGTH_TOO_SHORT"' in r:
            print(f'{Fore.RED}[+] Too Short : {x}@yahoo.com')
        elif '"IDENTIFIER_NOT_AVAILABLE"' in r:
            print(f'{Fore.RED}[+] Email Unavailable : {x}@yahoo.com')
        elif '"RESERVED_WORD_PRESENT"' in r:
            print(f"{Fore.RED}[+] already exists : {x}@yahoo.com")
        else:
         c = print(f'{Fore.GREEN}[+] Email available : {x}@yahoo.com')
         save = open("Yahoo available.txt",'a')
         save.write(x+"@yahoo.com"+'\n')
         Yahoo()
def vv():
    while True:
        p = email.readline().split("\n")[0]
        url = 'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress='+p+'&_=1627196218419'
        pays={
            'hm': '0',
            'emailAddress': p,
            '_': '1627196218419'
        }
        headq={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': 'mkt=en-US; MUID=cbc2617711cf4c49a342b5452121a655; logonLatency=LGN01=637627846125002497; fptctx2=taBcrIH61PuCVH7eNCyH0K%252fD9DJ44Cptuv0RyrXgXCsf5eqGykXHrvtMeCasGvEY0VPTjbfX6vQyrW9lD7u2Bk8z%252fATjuDoATKylORHdcgkLmzNsMjikWIqWROFr%252bcBcvJMfKH%252f%252bz4XdJ8UiCZXU%252bMQnPWW2T0tAB0IpAKSIGJeV27Cqo%252fNjZ7AsjsmJ8ZA5GYBzGwyE3tT87%252f6%252foHSEY7U%252b%252bD9OQFjqpPcQs%252bwDbwwgtrXtJ%252fFLvZ5aumtwAHbp6GFSfu2RhZvglvD3G3ZqUp%252fyKpSQSIAHies6L9Et%252f8A%253d; xid=22ae7334-5c88-4206-9815-6a88247164d5&&RD00155D99954E&249; wla42=; E=P:eo3uhzZP2Yg=:sC8ZsELJLGFDEiYX0i7Lfc03G28a/vKshNEpPpk60AU=:F; xidseq=4; mkt1=ar-SA; amsc=szKu18nwF1HdY5wu5vdWgmYEYrPVpJXWNnRDrDGY1OOZT1untMUwMOu6IeqkEOreMUq66PDfuLdV02EkP7trzG4FFpsW0ML0B1CzyFIhE5JJ4lzylZdib2gLbN11sbKN5oTzjgfw5h5GBrR21BnSLiYAdo1iL9XJNX6XpwN+hmUHNIF8UXGZN3gaDieabsyEI+jOXmXKvbBpJjms32aC00CUwB7yJTjfng1WkCvyup/LXcGkxynf7Wv8J1Gn1cMU8/OkqC1eNH5L6a2n83kRwyYQe7fKOUY1XOQ2lHwpmQtO+w8R4wFWmOp0kbLHGr+p3JrEqVYoYeI9K6OkMwYkSA==:2:3c',
            'referer': 'https://odc.officeapps.live.com/odc/emailhrd',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            'x-correlationid': '2f473501-322d-4179-98fd-0e8d46556aa5',
            'x-requested-with': 'XMLHttpRequest'
        }
        r = requests.post(url,data=pays,headers=headq).text
        if 'Neither' in r:
            print(f'{Fore.GREEN}Email available>>{p}')
            save1 = open("Hotmail available.txt", 'a')
            save1.write(p+'\n')
        elif 'MSAccount' in r:
            print(f'{Fore.RED}Email Not-available>>{p}')
            save2 = open("Hotmail Not-available.txt", 'a')
            save2.write(p+'\n')
        else:
         print(r)
         vv()
print(f"""{Fore.WHITE}

██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║███████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║╚════██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                  
        {Fore.WHITE}"Hello Wellcome To Checker Domains v1 Coded by Alosimi - insta :@lord.hellx - Discord : RealSos#6666                                                                
""")
time.sleep(2)
indx = input(f'[1]'+' Yahoo'+'\n' +f'[2]'+ ' Gmail'+'\n' +f'[3]' +' Outlook and Hotmail'+'\n' +f'[+] Enter Number (1-2-3) : ')
if indx == "1":
    Yahoo()
elif indx == "2":
    los()
elif indx =='3':
    vv()