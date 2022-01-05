# Route Planner for Urban Rail Transit System

A web application inspired by the [*Delhi Metro Rail Information*](https://delhimetrorail.info/) website. 

This is what it does: give it a source and destination station, and it will produce the shortest path between them, outlining the stations where you would be required to change lines. Pretty neat, isn't it? A pretty strenuous, long-winded (but elaborate) excuse to just apply Dijkstra's algorithm, we'd say. (Sadly, it currently uses Breadth-First Search instead, as Dijkstra's would only make sense when shortest path would be defined on a parameter such as distance, or time taken, for which we need to input a lot of corresponding data. Right now, shortest path simply means 'the path containing the least number of stations in between'.)

The metro network we use is a subset of the Delhi metro network.

The webapp is now live, check it out [*here*](https://routeplanner.pythonanywhere.com)!

### **Here's a quick glance! :eyes:**

![Find Route page](https://github.com/stephenvincent27/route-planner/blob/master/img/Find%20Route%20page.png)

![Find Route Result page](https://github.com/stephenvincent27/route-planner/blob/master/img/Find%20Route%20Result%20page.png)

![List Of Stations page](https://github.com/stephenvincent27/route-planner/blob/master/img/List%20Of%20Stations%20page.png)

![About page](https://github.com/stephenvincent27/route-planner/blob/master/img/About%20page.png)
