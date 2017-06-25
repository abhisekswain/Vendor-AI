# Vendor-AI
Vendor-AI is a webapp designed for vendors and bulk-sellers at e-commerce sites. It enables a vendor or seller at sites like amazon.com or ebay.com to upload a picture of the product they want to sell and automatically curates a product page by filling in the necessary textual information. To develop the app, I chose perfumes as my product category and scraped over 20,000 perfume images and textual data from basenotes.com. Vendor-AI uses computer vision for image matching and flask for displaying image and textual information.


![alt text](https://github.com/abhisekswain/vendor-ai/blob/master/Vendor-AI_screen_shot.png "Vendor-AI app")

## Motivation
Before embarking on my journey as a data scientist, I was a product manager and had to create product pages for my products. I found the process to be time-consuming and cumbersome. The same sentiment has been echoed by product managers I talked to at amazon and ebay, specially those who deal with vendors and bulk sellers. Vendors and bulk sellers sell a large number of products on these sites and have to spend considerable amount of time creating creating a product page for each product. Therefore, I set out to build a simple intuitive UI that accomplished this goal, by allowing the user to upload a picture of the product and curating a product page thus automating the selling process.

 

## Data Collection
I scraped 20,000+ images and text from basenotes.com. An example perfume page is shown below. For each perfume, I stored relevant information in a mongoDB including:

1. Name
2. Year
3. Gender
4. Availability
5. House
6. About
7. Fragrance notes

![alt text](https://github.com/abhisekswain/vendor-ai/blob/master/sample_page.png)

## Methodology

Vendor-AI works by matching the uploaded image to a databse of images and returning the resultant image and text. The process works as follows: 

1. Create codebook of images where each image in represented by a histogram  

2. Upload query image and compare histogram of query image to histograms in codebook  

3. Return matched image and text for display on webapp  

## Image codebook creation

Raw pixel data is hard to use for machine learning, and for comparing images in general. I used a technique called SIFT (Scale Invaraint Feature Transformation) to decompose an image into keypoints and descriptors. Keypoints are the same thing as interest points. They are spatial locations, or points in the image that define what is interesting or what stands out in the image. The reason why keypoints are special is because no matter how the image changes... whether the image rotates, shrinks/expands, is translated or is subject to distortion (i.e. a projective transformation or homography), you should be able to find the same keypoints in this modified image when comparing with the original image.

What makes keypoints different between frameworks is the way you describe these keypoints. These are what are known as descriptors. Each keypoint that you detect has an associated descriptor that accompanies it. Some frameworks only do a keypoint detection, while other frameworks are simply a description framework and they don't detect the points. There are also some that do both - they detect and describe the keypoints. SIFT and SURF are examples of frameworks that both detect and describe the keypoints.

For each image in my database, I used k-means clustering to cluster the descriptors for each of the 20,000 scraped images. Then a codebook of histograms was created indicating which cluster centers are nearest in terms of Euclidean distance to each image.

## Content based image retrieval  

Content-based image retrieval (CBIR) deals with the problem of retrieving visually similar images from a (large) database of images.For high-level queries, like finding matching images, it is not feasible to do a full comparison (for example using feature matching) between a query image and all images in the database. It would simply take too much time to return any results if the database is large. Thus, we use the image codebook and calculate the chi-squared distance between the queiried image histogram and the image codebook histograms. The top 200 matches were filtered out and to obtain the most accurate results, I matched individual descriptors to get the final result.

## Results and conclusion

I tested my matching algorithm with 30 perfume bottle images taken from a  cell phone and was able to get accurate matches for 21. The algorithm finds is unable to match pictures of bottles that are transparent and have no distinct shape. The model was then saved, and all unlabelled, text for the matching image was piped through it. A Flask webapp was built to display the product page.

An example video of the working app is below. Click on the image to check it out!

[![Vendor_AI Demo](https://i9.ytimg.com/vi/0VuWM9HelWo/3.jpg?sqp=CJSqwMoF&rs=AOn4CLDXa6XG-ySCYkxadjAg1BpNcEyH8A&time=1498420795543)](https://youtu.be/0VuWM9HelWo)


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
