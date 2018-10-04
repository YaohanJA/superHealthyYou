# SuperHealthyYou

Python Project for Group One
Nowadays, suffered from fast-speed life and heavy pressure, many people eat disorderly. Some of them already noticed the importance of healthy diet and regular exercise. However, not all of them have enough time to prepare the healthy meal, or do sports. Also, some people suffered from sports anxiety.

### Prerequisites
install python 3.7  
install PyCharm  
install Selenium Package in PyCharm  
get the appropriate chromedriver for your environment  
install numpy  
install pandas  
install time  
install os  
install bs4  
install literal_eval  
install json  
install requests  

### Installing

1. Install Python 3.7  
   * Click [download Python 3.7](https://www.jetbrains.com/pycharm/) to download the Python 3.7 to your file.  
   * After the installing package has been downloaded, install it as guided.  
2. Install PyCharm  
   * Click [download Pycharm](https://www.python.org/downloads/) to download the PyCharm to your computer.  
   * After the installing package has been downloaded, install it as guided.  

## Data Sources

Source 1 [NutriStrategy](https://www.nutristrategy.com/activitylist.htm)  
Source 2 [MyFoodBuddy](http://www.myfoodbuddy.com/foodCalorieTable.htm)  
Source 3 [NutritionValue](https://www.nutritionvalue.org/)  
Source 4 [Food2Fork](https://www.food2fork.com/about/api)  

### How to run the Program

1. run the first scrapers "ScrapeNutriValueData.py", it may take a lot of time since there are thousands of links. To make things easier, you can directly use our downloaded file "newLinks.csv".

2. run the second scraper "DownloadNutriData.py", this scraper will download the csvs whose links are in the "newLinks.csv", which is scrapped by the first scraper.

3. run the third scraper "ScrapeMyFoodBuddyData.py", this scraper will scrape the data from the source "myfoodbuddy.com".

4. run the forth scraper "ScrapeNutriStrategyData.py", it will get the sports data from the given website.

5. run the fifth scraper "ScrapeFood2Fork.py", you need go to Souce 4 website and sign up to get an api key, thus, you can get the recipes. For your convinience, you can directly use the cleaned data file "FoodRecipe.csv".

6. run the main program "SuperHealthyYou.py", it will invoke all files to get your body information and recomend several recipes to you.


## Authors

* **Xu Sheng ** -- [Github](https://github.com/FanaticKyo)
* **Hsuan Ouyang   ** -- [Github](https://github.com/hsuan531)
* **Yaohan Jiang   ** -- [Github](https://github.com/YaohanJA)
* **Xiao Shan    ** -- [Github](https://github.com/katesxiao)
* **Shin-yu Wu     ** -- [Github](https://github.com/ai559031)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Things to update

