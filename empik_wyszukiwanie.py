import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryRgTGFieFuEl7q3GI",
    'x-csrf-token': 'b4989f12-54a3-4ca4-baa3-b7ecbccad951',
    'cookie': 'portal_sticky=portal-2; CSRF=b4989f12-54a3-4ca4-baa3-b7ecbccad951; sna_ab_1=enabled; RefererPromotion=GOOGLE_PLA; SHOPPING_CART=95697552-4944-4783-a265-b2de07e87299; cartBeta=enabled; __cfruid=3491cd49a383d903c28a161a2b0a4380a7d16cb6-1641411132; tabSetAB=sna_ab_1:enabled:1642118400000; reco_Hash=729c83b8-a789-4ad2-94ec-91214f75cbca; JSESSIONID=2145B69CBAB1A70845D2DB78D5E49971.portal-2-1; kot_hash=db4a6583-da1c-4293-b7ac-493b2742d531; cookies_accepted=T; reco_prod_id=p1228961452%2Cp1246799956; reco_temp_prod_id=p1228961452%2Cp1246799956',
}


def get_formdata(product_id):
    return f"------WebKitFormBoundaryRgTGFieFuEl7q3GI\r\nContent-Disposition: form-data; name=\"onlyAvailable\"\r\n\r\nfalse\r\n------WebKitFormBoundaryRgTGFieFuEl7q3GI\r\nContent-Disposition: form-data; name=\"productId\"\r\n\r\n{product_id}\r\n------WebKitFormBoundaryRgTGFieFuEl7q3GI\r\nContent-Disposition: form-data; name=\"query\"\r\n\r\nRacib\r\n------WebKitFormBoundaryRgTGFieFuEl7q3GI--\r\n"


for prId in ['p1246799956', 'p1112920314', 'p1100694939']:
    response = requests.post('https://www.empik.com/product/dostepnosc-w-salonie', headers=headers,
                             data=get_formdata(prId))

    response_text = response.text
    responsejson = json.loads(response_text)

    points = responsejson['deliveryPoints']
    print(points)

    get_necessary_data = lambda x: {'productId': prId,
                                    'name': x['name'],
                                    'availability': x['productAvailabilityStatus'],
                                    'inStore': x['availableInStore'],
                                    'price': x['price']
                                    }
    result = list(
        map(get_necessary_data,
            points))
    print(json.dumps(result, indent=4))
