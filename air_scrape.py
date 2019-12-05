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



# from requests_html import HTMLSession
#
# def get_session(url, selector):
#     session = HTMLSession()
#     r = session.get(url)
#     r.html.render()
#     return r.html.find(selector)
#
# def find_price():
#     page = get_session('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659', '#pricing-price-9a260c55-4b03-497f-93c0-c47c9a1d2a4f > div > div > div.pricing-lib-price-7-1943-6.price-view-pb.priceView-layout-large > div > div.price-box.pricing-lib-price-7-1943-6 > div:nth-child(1) > div > div > span:nth-child(1)')
#
#
#     for items in page:
#         price_container = items.find('span', first=True).attrs['aria-hidden']
#         airpod_price = [x.text for x in price_container]
#     print(airpod_price)
#
#
#
# if __name__ == 'find_price':
#
#     find_price()

# from requests_html import HTMLSession
# #
# # session = HTMLSession()
# # r = session.get('https://github.com/')
# # r.html.render()
# #
# #
# # sel = 'body > div.application-main > main > div.py-6.py-sm-8.jumbotron-codelines > div > div > div.col-md-7.text-center.text-md-left > p'
# #
# # print(r.html.find(sel, first=True).text)

















######it worked!!!!######
# from requests_html import HTMLSession
# #
# # session = HTMLSession()
# # r = session.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
# #
# #
# #
# # sel = '<span aria-hidden="true">$<!-- -->249.99</span>'
# #
# # print(r.html.find(sel, first=True).text)

#### IT WORKED!!!!!!!!!#####





# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
#
#
# bestbuy_price = []
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     sel = '<span aria-hidden="true">$<!-- -->249.99</span>'
#     print("The current price for AirPods Pro at Best Buy: " +r.html.find(sel, first=True).text)
#     bestbuy_price.append(r.html.find(sel, first=True).text)
#     return (bestbuy_price)
#
# frys_price = []
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     sel = '<span id="did_price1valuediv" class="net-total net-total-price ">$269.00</span>'
#     print("The current price for AirPods Pro at Fry's: " +r.html.find(sel, first=True).text)
#     frys_price.append(r.html.find(sel, first=True).text)
#     return (frys_price)
#
# target_price = []
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Electronics%2BShopping_Local&adgroup=SC_Electronics&LID=700000001170770pgs&network=g&device=c&location=9027766&ds_rl=1246978&ds_rl=1248099&ds_rl=1246978&gclid=CjwKCAiA8ejuBRAaEiwAn-iJ3tZYPXz9_sFzXa_lRKXQAr7zzTpoo3XoE3k7JX8rpajVo4JUbovfTxoChYEQAvD_BwE&gclsrc=aw.ds')
#     sel = '<div class="h-text-bold style__PriceFontSize-gob4i1-0 eLdTvF" data-test="product-price">$249.99</div>'
#     print("The current price for AirPods Pro at Target: " +r.html.find(sel, first=True).text)
#     target_price.append(r.html.find(sel, first=True).text)
#     return (target_price)
#
#
# result = asession.run(get_bestbuy, get_frys, get_target,)
#
# all_prices = []
# for price in bestbuy_price, frys_price, target_price,:
#     dollar_stripped = price[0].strip('$')
#     print(float(dollar_stripped))
#     for value in float(dollar_stripped):
######GOOD######


# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
#
#
# bestbuy_price = []
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     sel = '<span aria-hidden="true">$<!-- -->249.99</span>'
#     print("The current price for AirPods Pro at Best Buy: " +r.html.find(sel, first=True).text)
#     bestbuy_price.append(r.html.find(sel, first=True).text)
#     bestbuy_price.append("The cheapest pair of AirPods Pro is from Best Buy: ")
#     return (bestbuy_price)
#
# frys_price = []
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     sel = '<span id="did_price1valuediv" class="net-total net-total-price ">$269.00</span>'
#     print("The current price for AirPods Pro at Fry's: " +r.html.find(sel, first=True).text)
#     frys_price.append(r.html.find(sel, first=True).text)
#     frys_price.append("The cheapest pair of AirPods Pro is from Fry's: ")
#     return (frys_price)
#
# target_price = []
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Electronics%2BShopping_Local&adgroup=SC_Electronics&LID=700000001170770pgs&network=g&device=c&location=9027766&ds_rl=1246978&ds_rl=1248099&ds_rl=1246978&gclid=CjwKCAiA8ejuBRAaEiwAn-iJ3tZYPXz9_sFzXa_lRKXQAr7zzTpoo3XoE3k7JX8rpajVo4JUbovfTxoChYEQAvD_BwE&gclsrc=aw.ds')
#     sel = '<div class="h-text-bold style__PriceFontSize-gob4i1-0 eLdTvF" data-test="product-price">$249.99</div>'
#     print("The current price for AirPods Pro at Target: " +r.html.find(sel, first=True).text)
#     target_price.append(r.html.find(sel, first=True).text)
#     target_price.append("The cheapest pair of AirPods Pro is from Target: ")
#     return (target_price)
#
#
# result = asession.run(get_bestbuy, get_frys, get_target,)
#
# cheapest_store = []
# all_prices = []
# for price, name in bestbuy_price, frys_price, target_price,:
#     dollar_stripped = all_prices.append(price[0].strip('$'))
#     # if float(dollar_stripped).min():
#     #     print(name)
#
# print(all_prices.sort())
# print(target_price[1])
# # print("The cheapest pair of AirPods Pro is from " + name + ": $" + all_prices[0])

####fail####




# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
#
#
# bestbuy_price = []
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     sel = '<span aria-hidden="true">$<!-- -->249.99</span>'
#     print("The current price for AirPods Pro at Best Buy: " +r.html.find(sel, first=True).text)
#     bestbuy_price.append(r.html.find(sel, first=True).text)
#     return (bestbuy_price)
#
# frys_price = []
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     sel = '<span id="did_price1valuediv" class="net-total net-total-price ">$269.00</span>'
#     print("The current price for AirPods Pro at Fry's: " +r.html.find(sel, first=True).text)
#     frys_price.append(r.html.find(sel, first=True).text)
#     return (frys_price)
#
# target_price = []
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Electronics%2BShopping_Local&adgroup=SC_Electronics&LID=700000001170770pgs&network=g&device=c&location=9027766&ds_rl=1246978&ds_rl=1248099&ds_rl=1246978&gclid=CjwKCAiA8ejuBRAaEiwAn-iJ3tZYPXz9_sFzXa_lRKXQAr7zzTpoo3XoE3k7JX8rpajVo4JUbovfTxoChYEQAvD_BwE&gclsrc=aw.ds')
#     sel = '<div class="h-text-bold style__PriceFontSize-gob4i1-0 eLdTvF" data-test="product-price">$249.99</div>'
#     print("The current price for AirPods Pro at Target: " +r.html.find(sel, first=True).text)
#     target_price.append(r.html.find(sel, first=True).text)
#     return (target_price)
#
#
# result = asession.run(get_bestbuy, get_frys, get_target,)
#
# all_prices = []
# for price in bestbuy_price, frys_price, target_price,:
#     dollar_stripped = price[0].strip('$')
#     all_prices.append(float(dollar_stripped))
# # print(all_prices)
#
# lowest_price = []
# low = min(all_prices)
# for x in all_prices:
#     if x == low:
#         lowest_price.append(x)
# print(lowest_price)

#####worked...put lowest prices in list...
#####next step is connecting them to the name of the store..use dict??




# from requests_html import AsyncHTMLSession
#
# asession = AsyncHTMLSession()
#
#
# bestbuy_price = []
# a = {}
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     sel = '<span aria-hidden="true">$<!-- -->249.99</span>'
#     print("The current price for AirPods Pro at Best Buy: " +r.html.find(sel, first=True).text)
#     bestbuy_price.append(r.html.find(sel, first=True).text)
#     a["Best Buy"] = r.html.find(sel, first=True).text
#     return (bestbuy_price)
#
# frys_price = []
# b = {}
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     sel = '<span id="did_price1valuediv" class="net-total net-total-price ">$269.00</span>'
#     print("The current price for AirPods Pro at Fry's: " +r.html.find(sel, first=True).text)
#     frys_price.append(r.html.find(sel, first=True).text)
#     b["Fry's"] = r.html.find(sel, first=True).text
#     return (frys_price)
#
# target_price = []
# c = {}
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Electronics%2BShopping_Local&adgroup=SC_Electronics&LID=700000001170770pgs&network=g&device=c&location=9027766&ds_rl=1246978&ds_rl=1248099&ds_rl=1246978&gclid=CjwKCAiA8ejuBRAaEiwAn-iJ3tZYPXz9_sFzXa_lRKXQAr7zzTpoo3XoE3k7JX8rpajVo4JUbovfTxoChYEQAvD_BwE&gclsrc=aw.ds')
#     sel = '<div class="h-text-bold style__PriceFontSize-gob4i1-0 eLdTvF" data-test="product-price">$249.99</div>'
#     print("The current price for AirPods Pro at Target: " +r.html.find(sel, first=True).text)
#     target_price.append(r.html.find(sel, first=True).text)
#     c["Target"] = r.html.find(sel, first=True).text
#     return (target_price)
#
#
# result = asession.run(get_bestbuy, get_frys, get_target,)
#
# print(a)
# print(b)
# print(c)
#
# all_prices = []
# for price in bestbuy_price, frys_price, target_price,:
#     dollar_stripped = price[0].strip('$')
#     all_prices.append(float(dollar_stripped))
# # print(all_prices)
#
# lowest_price = []
# low = min(all_prices)
# for x in all_prices:
#     if x == low:
#         lowest_price.append(x)
# print(lowest_price)
#
# lowest_price_dict = {}

########WORKED 11/25#######


# from requests_html import AsyncHTMLSession
# import re
#
# asession = AsyncHTMLSession()
#
#
# bestbuy_price = []
# a = {}
# async def get_bestbuy():
#     r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
#     sel = 'div.priceView-hero-price.priceView-customer-price span'
#     print("The current price for AirPods Pro at Best Buy: " +r.html.find(sel, first=True).text)
#     bestbuy_price.append(r.html.find(sel, first=True).text)
#     a["Best Buy"] = r.html.find(sel, first=True).text
#     return (bestbuy_price)
#
# frys_price = []
# b = {}
# async def get_frys():
#     r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
#     sel = 'span#did_price1valuediv.net-total.net-total-price'
#     print("The current price for AirPods Pro at Fry's: " +r.html.find(sel, first=True).text)
#     frys_price.append(r.html.find(sel, first=True).text)
#     b["Fry's"] = r.html.find(sel, first=True).text
#     return (frys_price)
#
# target_price = []
# c = {}
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Electronics%2BShopping_Local&adgroup=SC_Electronics&LID=700000001170770pgs&network=g&device=c&location=9027766&ds_rl=1246978&ds_rl=1248099&ds_rl=1246978&gclid=CjwKCAiA8ejuBRAaEiwAn-iJ3tZYPXz9_sFzXa_lRKXQAr7zzTpoo3XoE3k7JX8rpajVo4JUbovfTxoChYEQAvD_BwE&gclsrc=aw.ds')
#     sel = 'div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF[data-test="product-price"'
#     print("The current price for AirPods Pro at Target: " +r.html.find(sel, first=True,).text)
#     target_price.append(r.html.find(sel, first=True).text)
#     c["Target"] = r.html.find(sel, first=True).text
#     return (target_price)
#
# result = asession.run(get_bestbuy, get_frys, get_target,)
#
# print(a)
# print(b)
# print(c)
# <div class="h-text-bold style__PriceFontSize-gob4i1-0 eLdTvF" data-test="product-price">$249.99</div># values = text.values()
# for x in text.values():
#     pattern = re.sub("[^\d\.]", "", text)
# print (pattern)
##"[^\d\.]"  regex says "anything that isn't a number or a decimal point"

# d = {**a, **b, **c}
# for k, v in d.items():
#     v.lstrip()
#     print ("key: {}, value: {}".format(k, v))



#
# for value in a.values(),:
#      dollar_stripped = value.str.strip('$')
#      all_prices = float(dollar_stripped)
#
#      print(dollar_stripped)

######## all_prices = []
# for price in bestbuy_price, frys_price, target_price,:
#     dollar_stripped = price[0].strip('$')
#     all_prices.append(float(dollar_stripped))
# # print(all_prices)
#
# lowest_price = []
# low = min(all_prices)
# for x in all_prices:
#     if x == low:
#         lowest_price.append(x)
# print(lowest_price)
#
######### lowest_price_dict = {}

# d = {**a, **b, **c}
# for value in d.values():
#     dollar_stripped = value.strip('$')
#     all_prices = float(dollar_stripped)
#
#     print(dollar_stripped)
#
#
#
# for key in d.keys():
#     print(key)
#
# lowest_price = []
# low = min(all_prices)
# for x in all_prices:
#     if x == low:
#         lowest_price.append(x)
# print(lowest_price)

#######changed CSS except Target########




from requests_html import AsyncHTMLSession
import re

asession = AsyncHTMLSession()


bestbuy_price = []
a = {}
async def get_bestbuy():
    r = await asession.get('https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659')
    sel = 'div.priceView-hero-price.priceView-customer-price span'
    print("The current price for AirPods Pro at Best Buy: " +r.html.find(sel, first=True).text)
    bestbuy_price.append(r.html.find(sel, first=True).text)
    a["Best Buy"] = r.html.find(sel, first=True).text
    return (bestbuy_price)

frys_price = []
b = {}
async def get_frys():
    r = await asession.get('https://www.frys.com/product/9956186?site=sr:SEARCH:MAIN_RSLT_PG')
    sel = 'span#did_price1valuediv.net-total.net-total-price'
    print("The current price for AirPods Pro at Fry's: " +r.html.find(sel, first=True).text)
    frys_price.append(r.html.find(sel, first=True).text)
    b["Fry's"] = r.html.find(sel, first=True).text
    return (frys_price)

# target_price = []
# c = {}
# async def get_target():
#     r = await asession.get('https://www.target.com/p/apple-airpods-pro/-/A-54191101?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Electronics%2BShopping_Local&adgroup=SC_Electronics&LID=700000001170770pgs&network=g&device=c&location=9027766&ds_rl=1246978&ds_rl=1248099&ds_rl=1246978&gclid=CjwKCAiA8ejuBRAaEiwAn-iJ3tZYPXz9_sFzXa_lRKXQAr7zzTpoo3XoE3k7JX8rpajVo4JUbovfTxoChYEQAvD_BwE&gclsrc=aw.ds')
#     sel = 'div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF[data-test="product-price"'
#     print("The current price for AirPods Pro at Target: " +r.html.find(sel, first=True,).text)
#     target_price.append(r.html.find(sel, first=True).text)
#     c["Target"] = r.html.find(sel, first=True).text
#     return (target_price)

result = asession.run(get_bestbuy, get_frys,)

print(a)
print(b)

# <div class="h-text-bold style__PriceFontSize-gob4i1-0 eLdTvF" data-test="product-price">$249.99</div># values = text.values()
# for x in text.values():
#     pattern = re.sub("[^\d\.]", "", text)
# print (pattern)
# #"[^\d\.]"  regex says "anything that isn't a number or a decimal point"

#d = {**a, **b}
# for k, v in d.items():
#     v.lstrip()
#     print ("key: {}, value: {}".format(k, v))
#
#
#
#
# for value in a.values(),:
#      dollar_stripped = value.str.strip('$')
#      all_prices = float(dollar_stripped)
#
#      print(dollar_stripped)

all_prices = []
for price in bestbuy_price, frys_price,:
    dollar_stripped = price[0].strip('$')
    all_prices.append(float(dollar_stripped))
# print(all_prices)



# lowest_price = []
# low = min(all_prices)
# for x in all_prices:
#     if x == low:
#         lowest_price.append(str(x))
#         # d = {**a, **b}
#         # print([k for k, v in d.items() if v in x])
# print(lowest_price)
#
# d = {**a, **b}
# print([k for k, v in d.items() if v in lowest_price])


def lowest_price():
    lowest_price = []
    low = min(all_prices)
    for x in all_prices:
        if x == low:
            lowest_price.append(str(x))
    return (lowest_price)

my_list = lowest_price()
d = {**a, **b}
print([k for k, v in d.items() if v in my_list])

### can't access corresponding key for value











