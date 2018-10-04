# SuperHealthyYou
Python Project for Group One
Nowadays, suffered from fast-speed life and heavy pressure, many people eat disorderly. Some of them already noticed the importance of healthy diet and regular exercise. However, not all of them have enough time to prepare the healthy meal, or do sports. Also, some people suffered from sports anxiety.

### Prerequisites

install python 3.7  
install PyCharm  
install Selenium Package in PyCharm

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Data Sources

Source 1 [NutriStrategy](https://www.nutristrategy.com/activitylist.htm)  -using scraping to obtain the data  
Source 2 [MyFoodBuddy](http://www.myfoodbuddy.com/foodCalorieTable.htm)  -using scraping to obtain the data  
Source 3 [NutritionValue](https://www.nutritionvalue.org/)  -using scraping to obtain the data  
Source 4 [Food2Fork](https://www.food2fork.com/about/api)  -using API to obtain the data  


## Logic
As for the diet part, we take the user weight, height, age, and sex as inputs, and in our data warehouse, we match the users’ inputs with the amount of calories and nutrition they need to take under specific body situation. Also, considering that some sports people maintain regular exercise, we also provide users a place to enter the amount of exercises they have already done in that particular day, and this amount of exercise will be translated into a calorie amount in our program using data source one. Therefore, at the end, we can return a precise amount of nutrition a user needs to take in that day.					

As for the second part of our program, we pass the amount of calories needed to data source two and three. After getting user input in keywords of what they want to eat, we search for their favorites, and return a bundle of foods matching the calories and nutrition amount they need to take. In this bundle, we specifically include the keyword food they choose at the beginning.					
There is also a parallel process in the second part. When we get the user input in the food type, we also pass the information to data source four, which will provide user with links of receipts they might be interested in.					

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
