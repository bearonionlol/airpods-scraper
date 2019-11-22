#!/usr/bin/env python3

# from requests_html import AsyncHTMLSession

# def get_session(url, selector):
#     session = HTMLSession()
#     r = session.get(url)
#     r.html.render()
#     return r.html.find(selector)

# async def get_session(url, model)
#     asession = AsyncHTMLSession()
#     r = await asession.get(url)
#     result = session.run(get_bestbuy, get_frys, get_target)
#     return r.html.search('MWP22AM/A')     ?????????

# from requests_html import AsyncHTMLSession
# asession = AsyncHTMLSession()
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     return r
#
# async def get_frys():
#     r = await asession.get('https://www.frys.com/search?search_type=regular&sqxts=1&isFSK=true&cat=&query_string=airpods+pro&nearbyStoreName=false')
#     return r
#
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101')
#     return r
#
# results = asession.run(get_bestbuy, get_frys, get_target)
#
# for result in results:
#     return result.html.search("MWP22AM/A"))




# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     return r
#
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     return r
#
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101')
#     return r
#
# results = asession.run(get_bestbuy, get_frys, get_target)
#
#
# prices = []
# for result in results:
#     r = result
#     url = r.html.url
#     price = r.html.search('${}')[0]
#     prices.append(url)
#     prices.append(price)
#
# print(prices)




# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     return r
#
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     return r
#
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101')
#     return r
#
# results = asession.run(get_bestbuy, get_frys, get_target)
#
#
# prices = []
# for result in results:
#     r = result
#     url = r.html.url
#     #price = r.html.search('${}')[0]
#     prices.append(url)
#     prices.append(r.text)
#
#     if r.html.find('.priceView-hero-price priceView-customer-price'):
#         print(r.text)
#
#     if r.html.find('.price-details-info'):
#         print(r.text)
#
#     if r.html.find('viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div:nth-child(1) > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF'):
#         print(r.text)
#
# print(prices)


# //*[@id="pricing-price-f5629a79-18fa-4ca8-9b26-d788258e80ff"]/div/div/div[1]/div/div[1]/div[1]/div/div/span[1]/text()[2]
# <div class="priceView-hero-price priceView-customer-price"><span aria-hidden="true">$<!-- -->249.99</span><span class="sr-only">Your price for this item is $<!-- -->249.99</span></div>
#
# < table
#
#
# class ="price-details-table table" >
#viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div:nth-child(1) > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF





# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     return r
#
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     return r
#
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101')
#     return r
#
# results = asession.run(get_bestbuy, get_frys, get_target)
#
#
# prices = []
# for result in results:
#     a = result.html.url
#     b = result.html.search('${}')[0]
#     prices.append(a)
#     prices.append(b)
#
# print(prices)
#
#     # if r.html.find('.priceView-hero-price priceView-customer-price'):
#     #     print(r.text)
#     #
#     # if r.html.find('.price-details-info'):
#     #     print(r.text)
#     #
#     # if r.html.find('viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div:nth-child(1) > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF'):
#     #     print(r.text)



# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     return r
#
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     return r
#
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101')
#     return r
#
# results = asession.run(get_bestbuy, get_frys, get_target)
#
#
# prices = []
# for result in results:
#
#     print(result.html.find(selector, first=True).text)
#     # if r.html.find('.priceView-hero-price priceView-customer-price'):
#     #     print(r.text)
#     #
#     # if r.html.find('.price-details-info'):
#     #     print(r.text)
#     #
#     # if r.html.find('viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div:nth-child(1) > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF'):
#     #     print(r.text)
#
# #bestbuy#pricing-price-f5629a79-18fa-4ca8-9b26-d788258e80ff > div > div > div.pricing-lib-price-7-1943-6.price-view-pb.priceView-layout-large > div > div.price-box.pricing-lib-price-7-1943-6 > div:nth-child(1) > div > div
# #frys#MainContainer > div:nth-child(48) > div.content-wrapper > div > div.content-wrapper-inner > div.row.productMainSection > div.col-sm-8 > div > div > div.col-sm-6.col-md-6.col-lg-5 > div > div:nth-child(2) > div.col-xs-6.col-xs-6-price-details-info > div
# #target#viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div:nth-child(1) > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF



# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     return r
#
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     return r
#
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101')
#     return r
#
# results = asession.run(get_bestbuy, get_frys, get_target)
#
#
# prices = []
# for result in results:
#
#     print(result.html.find(selector, first=True).text)
#     # if r.html.find('.priceView-hero-price priceView-customer-price'):
#     #     print(r.text)
#     #
#     # if r.html.find('.price-details-info'):
#     #     print(r.text)
#     #
#     # if r.html.find('viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div:nth-child(1) > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF'):
#     #     print(r.text)



# from requests_html import HTMLSession
#
# def get_session(url, selector):
#     session = HTMLSession()
#     r = session.get(url)
#     r.html.render()
#     return r.html.find(selector)
#
# def find_price():
#     page = get_session('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659', 'priceView-hero-price priceView-customer-price')
#
#     airpod_price = []
#
#     for items in page:
#         price = items.html.search('$', first=True,)
#         airpod_price.append(price)
#
#     print(airpod_price)



from requests_html import HTMLSession

def get_session(url, selector):
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    return r.html.find(selector)

def find_price():
    page = get_session('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659', 'div.priceView-hero-price priceView-customer-price')


    for items in page:
        price_container = items.html.find('span', first=True,)
        airpod_price = [x.text for x in price_container]

    print(airpod_price)








