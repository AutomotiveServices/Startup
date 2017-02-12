# Startup
Current plan:<br />
Step 1: Get a list of websites/webpages(preferably) which includes the service coupons of the automobile center in either text or image format. This will be performed using the yellow pages API.<br />

Current progress: Given a webpage currently we can extract the coupons page of that is present in the webpage. For example:
Given ---> http://www.firestonecompleteautocare.com/offers/:
Output:urls_out:
1:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-renu-1702
2:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-lof2-1701
3:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-coolant-1701
4:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-transforceat-50d-fcac-feb1-28
5:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-bulb-1702
6:http://www.firestonecompleteautocare.com/offers
7:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-alignment-1702
8:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-battery-1701
9:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-fuel-1701
10:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-winterforce-60d-feb1-28
11:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-lof-1702
12:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-fr710-10p-fcac-feb1-28
13:http://www.firestonecompleteautocare.com/offers/
14:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-ccp-1701
15:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-brakes-1702
16:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-blizzak-70d-fcac-feb1-28
17:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-destination-50d-fcac-feb1-28
18:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-presidentsdaysavings100500
19:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-valtour-25p-fcac-feb3-28
20:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-code-1701
21:http://www.firestonecompleteautocare.com/offers/offer-detail/fcac-invclear-fcac-feb1-28

Description: Given the above url we get all the discount pages from that webpage as shown above

Step 2: Crawl these webpages and find out the services offered<br />
        - We may have to find the services web page from the website or we just have record of the webpage which has the services       page(later saves us a bunch o time)<br />
        - We categorize the service page to be in the form of photos or text<br /> ----->(To do: Now that we have the list of coupon urls which mostly has images, we need to read this using the Google vision API and read the images) Ravi does this sound right to you?
        - After categorization we extract the features which could be prices, coupons, rebates. (We need to deicde on the list of features)<br />
        - The above extracted features need to be put in a csv file which the app will use<br />
Step 3: The app reads the csv file and shows the captured information based on place, state, etc(more info can be added to the classification part here that is place, state and more based on the data we gather)<br /> --->(Should we show all coupon codes 


Current status: We have done a part of step 1 where we can extract the coupon webpages given a webpage. We will need urls for this however which will be extracted from the yelp api(correct me if I am wrong).

To do items:
Bharat: 
- Read information in the coupon images
- Come up with some kind of a classification of coupons such as: tires, windows, alignment, misc, etc

Ravi: 
- Get the right urls to read from?

Heather & Pranay:
- Get an idea on how to generate revenue out of this
- What is a good way to market this?


Please continue adding detailed approaches when performing the tasks and keep updating this so that we are in sync<br />
