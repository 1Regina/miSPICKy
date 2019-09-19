#%%
# pip install google_images_download
# importing google_images_download module 
# from google_images_download import google_images_download  


# creating object 
response = google_images_download.googleimagesdownload()  
  
search_queries = ['disorganized room'] 

# update limit 
def downloadimages(query): 
    arguments = {"keywords": query,"format": "jpg", "limit":350,"print_urls": True, "size": "medium", "aspect_ratio": "panoramic", 
                "chromedriver": "chromedriver.exe" } 
    try: 
        response.download(arguments) 
        
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                        "format": "jpg", 
                        "limit":350, 
                        "print_urls":True,  
                        "size": "medium",
                        "chromedriver": "chromedriver.exe" } # add chromedriver argument
                        
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print() 

#%%
