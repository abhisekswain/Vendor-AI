# Vendor-AI
Vendor-AI is a webapp designed for vendors and bulk-sellers at e-commerce sites. It enables a vendor or seller at sites like amazon.com or ebay.com to upload a picture of the product they want to sell and automatically curates a product page by filling in the necessary textual information. To develop the app, I chose perfumes as my product category and scraped over 20,000+ perfume images and textual data from basenotes.com. Vendor-AI uses computer vision for image matching and flask for displaying image and textual information.


![alt text](https://github.com/abhisekswain/vendor-ai/blob/master/Vendor-AI_screen_shot.png "Vendor-AI app")

## Motivation
Before embarking on my journey as a data scientist, I was a product manager and had to create product pages for my products. I found the process to be time-consuming and cumbersome. The same sentiment has been echoed product managers I talked to at amazon and ebay, specially those who deal with vendors and bulk sellers. Vendors and bulk sell a large number of products on these sites and have to spend considerable amount of time creating creating a product page for each product. Therefore, I set out to build a simple intuitive UI that accomplished this goal, by allowing the user to upload a picture of the product and curating a product page thus automating the selling process.

 

## Data Collection
I scraped 20,000+ images and text from basenotes.com. An example perfuke is below. For each perfume, I stored relevant information in a mongoDB including:

1. Name
2. Year
3. Gender
4. Availability
5. House
6. About
7. Fragrance notes

![alt text](https://github.com/abhisekswain/vendor-ai/blob/master/sample_page.png)

## Methodology

Vendor-AI works by matching the uploaded images to a databse of images and returning the resultant image and text. The process works as follows: 

1. Create codebook of images where each image in represented by a histogram  

2. Upload query image and compare histogram of query image to histograms in codeboook  

3. Return matched image and text for display on webapp  

## Image codebook creation

Raw pixel data is hard to use for machine learning, and for comparing images in general. I used a technique called SIFT (Scale Invaraint Feature Transformation) to decompose an image into keypoints and descriptors. Keypoints are the same thing as interest points. They are spatial locations, or points in the image that define what is interesting or what stands out in the image. The reason why keypoints are special is because no matter how the image changes... whether the image rotates, shrinks/expands, is translated or is subject to distortion (i.e. a projective transformation or homography), you should be able to find the same keypoints in this modified image when comparing with the original image.

What makes keypoints different between frameworks is the way you describe these keypoints. These are what are known as descriptors. Each keypoint that you detect has an associated descriptor that accompanies it. Some frameworks only do a keypoint detection, while other frameworks are simply a description framework and they don't detect the points. There are also some that do both - they detect and describe the keypoints. SIFT and SURF are examples of frameworks that both detect and describe the keypoints.

For each image in my database, I used k-means clustering to cluster the descriptors for each of the 20,000 scrpaed images. Then a codebook of histograms was created indicating which cluster centers are nearest in terms of Euclidean disatnce to each image.



## Tools Used  
Data Collection/Web Scraping  
  
* Scrapy
* Python

Data Storage  

* PyMongo
* MongoDB
* Json

Modelling/Image Processing  

* OpenCV
* Numpy
* Pandas
* Scikit-learn
* Pickle

Plotting  

 * Matplotlib
 * Seaborn
 
 Web App  
 
 * Flask
 * HTML
 * CSS
 * JavaScript
