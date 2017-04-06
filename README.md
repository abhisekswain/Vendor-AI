# Vendor-AI
Vendor-AI is a webapp designed for vendors and bulk-sellers at e-commerce sites. It enables a vendor or seller at sites like amazon.com or ebay.com to upload a picture of the product they want to sell and automatically curates a product page by filling in the necessary textual information. To develop the app, I chose perfumes as my product category and scraped over 20,000+ perfume images and textual data from basenotes.com. Vendor-AI uses computer vision for image matching and flask for displaying image and textual information.


![alt text](https://github.com/abhisekswain/vendor-ai/blob/master/Vendor-AI_screen_shot.png)

## Motivation
Before embarking on my journey into data science, I was a product manager and had to create product page for my products. I found the process to be time-consuming and cumbersome. The same sentiment has been echoed my Product Manager I talked to at amazon and ebay, specially those who deal with vendors and bulk sellers. Creating product page for 

## Data Collection
I scraped 10,000 articles from PR Newswire. An example article is below. For each article, I stored relevant information in a mongoDB including:

1. Headline
2. Time
3. Date
4. Location
5. Images
6. Body Text
